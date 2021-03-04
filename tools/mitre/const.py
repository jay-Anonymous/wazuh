#!/usr/bin/env python
#
# Copyright (C) 2015-2021, Wazuh Inc.
# Created by Wazuh, Inc. <info@wazuh.com>.
# This program is a free software; you can redistribute it and/or modify it under the terms of GPLv2

####### Constants #######

TIME_FORMAT= '%Y-%m-%dT%H:%M:%S.%fZ'

### Table

ID_t= 'id'
VERSION_t= 'version'
NAME_t= 'name'
DESCRIPTION_t= 'description'
CREATED_t= 'created_time'
MODIFIED_t= 'modified_time'
MITRE_VERSION_t= 'mitre_version'
REVOKED_BY_t= 'revoked_by'
DEPRECATED_t= 'deprecated'
MITRE_DETECTION_t= 'mitre_detection'
NETWORK_REQ_t= 'network_requirements'
REMOTE_SUPPORT_t= 'remote_support'
SUBTECHNIQUE_OF_t= 'subtechnique_of'
SOURCE_t= 'source'
DEFENSE_t= 'defense'
PERMISSION_t= 'permission'
IMPACT_t= 'impact'
REQUIREMENT_t= 'requirement'

# Aliases
ALIAS_t='alias'
# Contributors
CONTRIBUTOR_t='contributor'
# Platforms
PLATFORM_t='platform'
# References
SOURCE_t='source'
EXTERNAL_ID_t='external_id'
SOURCE_NAME_t='source_name'
URL_t='url'

### Relationships
DATASOURCE_r= 'DataSource'
DEFENSEBYPASSES_r='DefenseByPasses'
EFFECTIVEPERMISSON_r= 'EffectivePermission'
IMPACT_r= 'Impact'
PERMISSION_r= 'Permission'
SYSTEMREQ_r= 'SystemRequirement'
TECHNIQUES_r= 'techniques'
CONTRIBUTORS_r='Contributor'
PLATFORMS_r='Platform'
REFERENCES_r='Reference'
ALIASES_r='Alias'
GROUPS_r='Groups'
SOFTWARE_r='Software'
MITIGATIONS_r='Mitigation'

### ForeignKey
TECHNIQUE_ID_fk= 'techniques.id'

### Json index

# Global
TYPE_j= 'type'
OBJECT_j= 'objects'
# Groups
INTRUSION_SET_j= 'intrusion-set'
# Mitigations
COURSE_OF_ACTION_j= 'course-of-action'
# Software
MALWARE_j= 'malware'
TOOL_j= 'tool'
# Techniques
ATTACK_PATTERN_j= 'attack-pattern'

ID_j= 'id'
VERSION_j= 'spec_version'
IDENTITY_j= 'identity'
MARKING_DEFINITION_j= 'marking-definition'
DEFINITION_j= 'definition'
STATEMENT_j= 'statement'
NAME_j= 'name'
DESCRIPTION_j= 'description'
CREATED_j= 'created'
MODIFIED_j= 'modified'
MITRE_VERSION_j= 'x_mitre_version'
DEPRECATED_j='x_mitre_deprecated'
MITRE_DETECTION_j= 'x_mitre_detection'
MITRE_NETWOR_REQ_j= 'x_mitre_network_requirements'
MITRE_REMOTE_SUPP_j= 'x_mitre_remote_support'
DATASOURCE_j= 'x_mitre_data_sources'
DEFENSE_BYPASSED_j= 'x_mitre_defense_bypassed'
EFFECTIVE_PERMISSION_j= 'x_mitre_effective_permissions'
IMPACT_TYPE_j= 'x_mitre_impact_type'
PERMISSIONS_REQ_j= 'x_mitre_permissions_required'
SYSTEM_REQ_j= 'x_mitre_system_requirements'

# Aliases
ALIAS_j='x_mitre_aliases'
# Contributors
CONTRIBUTOR_j='x_mitre_contributors'
# Platforms
PLATFORM_j='x_mitre_platforms'
# References
EXTERNAL_REFERENCES_j='external_references'
SOURCE_NAME_j='source_name'
EXTERNAL_ID_j='external_id'
URL_j='url'

# Relationship type
RELATIONSHIP_j= 'relationship'
RELATIONSHIP_TYPE_j= 'relationship_type'
REVOKED_BY_j= 'revoked-by'
SOURCE_REF_j='source_ref'
TARGET_REF_j= 'target_ref'
SUBTECHNIQUE_OF_j= 'subtechnique-of'

