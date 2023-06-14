'''
copyright: Copyright (C) 2015-2022, Wazuh Inc.

           Created by Wazuh, Inc. <info@wazuh.com>.

           This program is free software; you can redistribute it and/or modify it under the terms of GPLv2

type: integration

brief: The 'wazuh-analysisd' daemon receives the log messages and compares them to the rules.
       It then creates an alert when a log message matches an applicable rule.
       Specifically, these tests will verify if the 'wazuh-analysisd' daemon generates valid
       alerts from Windows registry-related 'syscheck' events.

components:
    - analysisd

suite: all_syscheckd_configurations

targets:
    - manager

daemons:
    - wazuh-analysisd
    - wazuh-db

os_platform:
    - linux

os_version:
    - Arch Linux
    - Amazon Linux 2
    - Amazon Linux 1
    - CentOS 8
    - CentOS 7
    - Debian Buster
    - Red Hat 8
    - Ubuntu Focal
    - Ubuntu Bionic

references:
    - https://documentation.wazuh.com/current/user-manual/reference/daemons/wazuh-analysisd.html

tags:
    - events
'''
import pytest

from pathlib import Path

from wazuh_testing.constants.daemons import WAZUH_DB_DAEMON, ANALYSISD_DAEMON
from wazuh_testing.constants.paths.sockets import ANALYSISD_QUEUE_SOCKET_PATH
from wazuh_testing.modules.analysisd import utils, ANALYSISD_DEBUG_CONFIG
from wazuh_testing.tools import mitm
from wazuh_testing.utils import configuration

from . import TEST_CASES_PATH

pytestmark = [pytest.mark.linux, pytest.mark.tier(level=2), pytest.mark.server]

# Configuration and cases data.
test_cases_path = Path(TEST_CASES_PATH, 'cases_syscheck_registry_events_win32.yaml')

# Test configurations.
_, test_metadata, test_cases_ids = configuration.get_test_cases_data(test_cases_path)

# Test internal options.
local_internal_options = ANALYSISD_DEBUG_CONFIG

# Test variables.
receiver_sockets_params = [(ANALYSISD_QUEUE_SOCKET_PATH, 'AF_UNIX', 'UDP')]

mitm_analysisd = mitm.ManInTheMiddle(address=ANALYSISD_QUEUE_SOCKET_PATH, family='AF_UNIX', connection_protocol='UDP')
monitored_sockets_params = [(WAZUH_DB_DAEMON, None, None), (ANALYSISD_DAEMON, mitm_analysisd, True)]

receiver_sockets, monitored_sockets = None, None  # Set in the fixtures

events_dict = {}
analysisd_regex_keyword = r'(.*)syscheck:(.+)$'
analysisd_injections_per_second = 200


# Test function.
@pytest.mark.parametrize('test_metadata', test_metadata, ids=test_cases_ids)
def test_validate_all_win32_registry_alerts(test_metadata, configure_local_internal_options, truncate_monitored_files_module,
                                            configure_sockets_environment, connect_to_sockets, wait_for_analysisd_startup,
                                            generate_events_syscheck, read_alerts_syscheck):
    '''
    description: Check if the alerts generated by the 'wazuh-analysisd' daemon from Windows registry-related
                 'syscheck' events are valid. The 'validate_analysis_alert_complex' function checks if
                 an 'analysisd' alert is properly formatted in reference to its 'syscheck' event.

    wazuh_min_version: 4.2.0

    tier: 2

    parameters:
        - test_metadata:
            type: dict
            brief: Test case metadata.
        - configure_local_internal_options:
            type: fixture
            brief: Configure the Wazuh local internal options.
        - truncate_monitored_files_module:
            type: fixture
            brief: Truncate all the log files and json alerts files before and after the test execution.
        - configure_sockets_environment:
            type: fixture
            brief: Configure environment for sockets and MITM.
        - connect_to_sockets:
            type: fixture
            brief: Module scope version of 'connect_to_sockets' fixture.
        - wait_for_analysisd_startup:
            type: fixture
            brief: Wait until the 'wazuh-analysisd' has begun and the 'alerts.json' file is created.
        - generate_events_syscheck:
            type: fixture
            brief: Read the specified yaml and generate every event using the input from every test case.
        - read_alerts_syscheck:
            type: fixture
            brief: Read the alerts from the JSON file. Return single alerts.

    assertions:
        - Verify that the alerts generated are consistent with the events received.

    input_description: Different test cases that are contained in an external
                       YAML file (syscheck_registry_events_win32.yaml)
                       that includes 'syscheck' events data and the expected output.

    inputs:
        - 20254 test cases distributed among 'syscheck' events of type 'added', 'modified', and 'deleted'.

    expected_output:
        - Multiple messages (alert logs) corresponding to each test case,
          located in the external input data file.

    tags:
        - alerts
        - man_in_the_middle
        - wdb_socket
    '''
    alert = next(read_alerts_syscheck)
    path = alert['syscheck']['path']
    mode = alert['syscheck']['event'].title()

    try:
        value_name = alert['syscheck']['value_name']
        path += '\\' + value_name
    except KeyError:
        pass

    utils.validate_analysis_alert_syscheck(alert, events_dict[path][mode], schema='win32')
