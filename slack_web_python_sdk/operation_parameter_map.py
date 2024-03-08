operation_parameter_map = {
    '/admin.usergroups.addChannels-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_ids'
            },
            {
                'name': 'usergroup_id'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.emoji.add-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'token'
            },
            {
                'name': 'url'
            },
        ]
    },
    '/admin.conversations.restrictAccess.addGroup-POST': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'group_id'
            },
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.users.assign-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'channel_ids'
            },
            {
                'name': 'is_restricted'
            },
            {
                'name': 'is_ultra_restricted'
            },
        ]
    },
    '/admin.emoji.addAlias-POST': {
        'parameters': [
            {
                'name': 'alias_for'
            },
            {
                'name': 'name'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/admin.apps.approve-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'app_id'
            },
            {
                'name': 'request_id'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.inviteRequests.approve-POST': {
        'parameters': [
            {
                'name': 'invite_request_id'
            },
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.conversations.archive-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
        ]
    },
    '/admin.usergroups.addTeams-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_ids'
            },
            {
                'name': 'usergroup_id'
            },
            {
                'name': 'auto_provision'
            },
        ]
    },
    '/admin.conversations.convertToPrivate-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
        ]
    },
    '/admin.conversations.create-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'is_private'
            },
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'org_wide'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.teams.create-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_domain'
            },
            {
                'name': 'team_name'
            },
            {
                'name': 'team_description'
            },
            {
                'name': 'team_discoverability'
            },
        ]
    },
    '/admin.conversations.delete-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
        ]
    },
    '/admin.inviteRequests.deny-POST': {
        'parameters': [
            {
                'name': 'invite_request_id'
            },
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.conversations.disconnectShared-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'leaving_team_ids'
            },
        ]
    },
    '/admin.teams.admins.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/admin.conversations.getConversationPrefs-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
        ]
    },
    '/admin.teams.settings.info-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.apps.restricted.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'enterprise_id'
            },
        ]
    },
    '/admin.conversations.getTeams-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/admin.users.session.invalidate-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'session_id'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.conversations.invite-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'user_ids'
            },
        ]
    },
    '/admin.users.invite-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_ids'
            },
            {
                'name': 'email'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'custom_message'
            },
            {
                'name': 'guest_expiration_ts'
            },
            {
                'name': 'is_restricted'
            },
            {
                'name': 'is_ultra_restricted'
            },
            {
                'name': 'real_name'
            },
            {
                'name': 'resend'
            },
        ]
    },
    '/admin.apps.approved.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'enterprise_id'
            },
        ]
    },
    '/admin.apps.requests.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.inviteRequests.approved.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/admin.inviteRequests.denied.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/admin.teams.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/admin.usergroups.listChannels-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'usergroup_id'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'include_num_members'
            },
        ]
    },
    '/admin.emoji.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/admin.conversations.restrictAccess.listGroups-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.conversations.ekm.listOriginalConnectedChannelInfo-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_ids'
            },
            {
                'name': 'team_ids'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/admin.teams.owners.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/admin.inviteRequests.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/admin.users.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/admin.usergroups.removeChannels-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_ids'
            },
            {
                'name': 'usergroup_id'
            },
        ]
    },
    '/admin.emoji.remove-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/admin.conversations.restrictAccess.removeGroup-POST': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'group_id'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/admin.users.remove-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/admin.conversations.rename-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/admin.emoji.rename-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'new_name'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/admin.users.session.reset-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'mobile_only'
            },
            {
                'name': 'web_only'
            },
        ]
    },
    '/admin.apps.restrict-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'app_id'
            },
            {
                'name': 'request_id'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.conversations.search-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_ids'
            },
            {
                'name': 'query'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'search_channel_types'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'sort_dir'
            },
        ]
    },
    '/admin.users.setAdmin-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/admin.conversations.setConversationPrefs-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'prefs'
            },
        ]
    },
    '/admin.teams.settings.setDefaultChannels-POST': {
        'parameters': [
            {
                'name': 'channel_ids'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/admin.teams.settings.setDescription-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'description'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.teams.settings.setDiscoverability-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'discoverability'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.users.setExpiration-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'expiration_ts'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/admin.teams.settings.setIcon-POST': {
        'parameters': [
            {
                'name': 'image_url'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/admin.teams.settings.setName-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'name'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.users.setRegular-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/admin.conversations.setTeams-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'org_channel'
            },
            {
                'name': 'target_team_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.users.setOwner-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/admin.conversations.unarchive-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
        ]
    },
    '/admin.apps.approve-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'app_id'
            },
            {
                'name': 'request_id'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.apps.restrict-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'app_id'
            },
            {
                'name': 'request_id'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.apps.approved.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'enterprise_id'
            },
        ]
    },
    '/admin.apps.requests.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.apps.restricted.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'enterprise_id'
            },
        ]
    },
    '/admin.conversations.archive-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
        ]
    },
    '/admin.conversations.convertToPrivate-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
        ]
    },
    '/admin.conversations.create-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'is_private'
            },
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'org_wide'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.conversations.delete-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
        ]
    },
    '/admin.conversations.disconnectShared-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'leaving_team_ids'
            },
        ]
    },
    '/admin.conversations.getConversationPrefs-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
        ]
    },
    '/admin.conversations.getTeams-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/admin.conversations.invite-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'user_ids'
            },
        ]
    },
    '/admin.conversations.rename-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/admin.conversations.search-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_ids'
            },
            {
                'name': 'query'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'search_channel_types'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'sort_dir'
            },
        ]
    },
    '/admin.conversations.setConversationPrefs-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'prefs'
            },
        ]
    },
    '/admin.conversations.setTeams-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'org_channel'
            },
            {
                'name': 'target_team_ids'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.conversations.unarchive-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
        ]
    },
    '/admin.conversations.ekm.listOriginalConnectedChannelInfo-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_ids'
            },
            {
                'name': 'team_ids'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/admin.conversations.restrictAccess.addGroup-POST': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'group_id'
            },
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.conversations.restrictAccess.listGroups-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_id'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.conversations.restrictAccess.removeGroup-POST': {
        'parameters': [
            {
                'name': 'channel_id'
            },
            {
                'name': 'group_id'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/admin.emoji.add-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'token'
            },
            {
                'name': 'url'
            },
        ]
    },
    '/admin.emoji.addAlias-POST': {
        'parameters': [
            {
                'name': 'alias_for'
            },
            {
                'name': 'name'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/admin.emoji.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/admin.emoji.remove-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/admin.emoji.rename-POST': {
        'parameters': [
            {
                'name': 'name'
            },
            {
                'name': 'new_name'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/admin.inviteRequests.approve-POST': {
        'parameters': [
            {
                'name': 'invite_request_id'
            },
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.inviteRequests.deny-POST': {
        'parameters': [
            {
                'name': 'invite_request_id'
            },
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.inviteRequests.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/admin.inviteRequests.approved.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/admin.inviteRequests.denied.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/admin.teams.create-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_domain'
            },
            {
                'name': 'team_name'
            },
            {
                'name': 'team_description'
            },
            {
                'name': 'team_discoverability'
            },
        ]
    },
    '/admin.teams.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/admin.teams.admins.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/admin.teams.owners.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/admin.teams.settings.info-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.teams.settings.setDefaultChannels-POST': {
        'parameters': [
            {
                'name': 'channel_ids'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/admin.teams.settings.setDescription-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'description'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.teams.settings.setDiscoverability-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'discoverability'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.teams.settings.setIcon-POST': {
        'parameters': [
            {
                'name': 'image_url'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/admin.teams.settings.setName-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'name'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.usergroups.addChannels-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_ids'
            },
            {
                'name': 'usergroup_id'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.usergroups.addTeams-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_ids'
            },
            {
                'name': 'usergroup_id'
            },
            {
                'name': 'auto_provision'
            },
        ]
    },
    '/admin.usergroups.listChannels-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'usergroup_id'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'include_num_members'
            },
        ]
    },
    '/admin.usergroups.removeChannels-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_ids'
            },
            {
                'name': 'usergroup_id'
            },
        ]
    },
    '/admin.users.assign-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'channel_ids'
            },
            {
                'name': 'is_restricted'
            },
            {
                'name': 'is_ultra_restricted'
            },
        ]
    },
    '/admin.users.invite-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel_ids'
            },
            {
                'name': 'email'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'custom_message'
            },
            {
                'name': 'guest_expiration_ts'
            },
            {
                'name': 'is_restricted'
            },
            {
                'name': 'is_ultra_restricted'
            },
            {
                'name': 'real_name'
            },
            {
                'name': 'resend'
            },
        ]
    },
    '/admin.users.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/admin.users.remove-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/admin.users.setAdmin-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/admin.users.setExpiration-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'expiration_ts'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/admin.users.setRegular-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/admin.users.setOwner-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'user_id'
            },
        ]
    },
    '/admin.users.session.invalidate-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'session_id'
            },
            {
                'name': 'team_id'
            },
        ]
    },
    '/admin.users.session.reset-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'mobile_only'
            },
            {
                'name': 'web_only'
            },
        ]
    },
    '/api.test-GET': {
        'parameters': [
            {
                'name': 'error'
            },
            {
                'name': 'foo'
            },
        ]
    },
    '/apps.permissions.request-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'scopes'
            },
            {
                'name': 'trigger_id'
            },
        ]
    },
    '/apps.event.authorizations.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'event_context'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/apps.permissions.scopes.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
        ]
    },
    '/apps.permissions.resources.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/apps.permissions.info-GET': {
        'parameters': [
            {
                'name': 'token'
            },
        ]
    },
    '/apps.permissions.users.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/apps.permissions.users.request-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'scopes'
            },
            {
                'name': 'trigger_id'
            },
            {
                'name': 'user'
            },
        ]
    },
    '/apps.uninstall-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
        ]
    },
    '/apps.event.authorizations.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'event_context'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/apps.permissions.request-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'scopes'
            },
            {
                'name': 'trigger_id'
            },
        ]
    },
    '/apps.permissions.info-GET': {
        'parameters': [
            {
                'name': 'token'
            },
        ]
    },
    '/apps.permissions.resources.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/apps.permissions.scopes.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
        ]
    },
    '/apps.permissions.users.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/apps.permissions.users.request-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'scopes'
            },
            {
                'name': 'trigger_id'
            },
            {
                'name': 'user'
            },
        ]
    },
    '/auth.revoke-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'test'
            },
        ]
    },
    '/auth.test-GET': {
        'parameters': [
            {
                'name': 'token'
            },
        ]
    },
    '/bots.info-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'bot'
            },
        ]
    },
    '/calls.add-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'external_unique_id'
            },
            {
                'name': 'join_url'
            },
            {
                'name': 'title'
            },
            {
                'name': 'created_by'
            },
            {
                'name': 'date_start'
            },
            {
                'name': 'desktop_app_join_url'
            },
            {
                'name': 'external_display_id'
            },
            {
                'name': 'users'
            },
        ]
    },
    '/calls.participants.add-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'id'
            },
            {
                'name': 'users'
            },
        ]
    },
    '/calls.end-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'id'
            },
            {
                'name': 'duration'
            },
        ]
    },
    '/calls.info-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/calls.participants.remove-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'id'
            },
            {
                'name': 'users'
            },
        ]
    },
    '/calls.update-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'id'
            },
            {
                'name': 'title'
            },
            {
                'name': 'desktop_app_join_url'
            },
            {
                'name': 'join_url'
            },
        ]
    },
    '/calls.participants.add-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'id'
            },
            {
                'name': 'users'
            },
        ]
    },
    '/calls.participants.remove-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'id'
            },
            {
                'name': 'users'
            },
        ]
    },
    '/chat.delete-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'as_user'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'ts'
            },
        ]
    },
    '/chat.deleteScheduledMessage-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'scheduled_message_id'
            },
            {
                'name': 'as_user'
            },
        ]
    },
    '/chat.getPermalink-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'message_ts'
            },
        ]
    },
    '/chat.scheduledMessages.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'latest'
            },
            {
                'name': 'oldest'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/chat.meMessage-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'text'
            },
        ]
    },
    '/chat.postEphemeral-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'user'
            },
            {
                'name': 'as_user'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'blocks'
            },
            {
                'name': 'icon_emoji'
            },
            {
                'name': 'icon_url'
            },
            {
                'name': 'link_names'
            },
            {
                'name': 'parse'
            },
            {
                'name': 'text'
            },
            {
                'name': 'thread_ts'
            },
            {
                'name': 'username'
            },
        ]
    },
    '/chat.postMessage-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'as_user'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'blocks'
            },
            {
                'name': 'icon_emoji'
            },
            {
                'name': 'icon_url'
            },
            {
                'name': 'link_names'
            },
            {
                'name': 'mrkdwn'
            },
            {
                'name': 'parse'
            },
            {
                'name': 'reply_broadcast'
            },
            {
                'name': 'text'
            },
            {
                'name': 'thread_ts'
            },
            {
                'name': 'unfurl_links'
            },
            {
                'name': 'unfurl_media'
            },
            {
                'name': 'username'
            },
        ]
    },
    '/chat.scheduleMessage-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'as_user'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'blocks'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'link_names'
            },
            {
                'name': 'parse'
            },
            {
                'name': 'post_at'
            },
            {
                'name': 'reply_broadcast'
            },
            {
                'name': 'text'
            },
            {
                'name': 'thread_ts'
            },
            {
                'name': 'unfurl_links'
            },
            {
                'name': 'unfurl_media'
            },
        ]
    },
    '/chat.unfurl-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'ts'
            },
            {
                'name': 'unfurls'
            },
            {
                'name': 'user_auth_message'
            },
            {
                'name': 'user_auth_required'
            },
            {
                'name': 'user_auth_url'
            },
        ]
    },
    '/chat.update-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'ts'
            },
            {
                'name': 'as_user'
            },
            {
                'name': 'attachments'
            },
            {
                'name': 'blocks'
            },
            {
                'name': 'link_names'
            },
            {
                'name': 'parse'
            },
            {
                'name': 'text'
            },
        ]
    },
    '/chat.scheduledMessages.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'latest'
            },
            {
                'name': 'oldest'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/conversations.archive-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
        ]
    },
    '/conversations.close-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
        ]
    },
    '/conversations.create-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'is_private'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/conversations.history-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'latest'
            },
            {
                'name': 'oldest'
            },
            {
                'name': 'inclusive'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/conversations.info-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'include_locale'
            },
            {
                'name': 'include_num_members'
            },
        ]
    },
    '/conversations.invite-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'users'
            },
        ]
    },
    '/conversations.join-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
        ]
    },
    '/conversations.kick-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'user'
            },
        ]
    },
    '/conversations.leave-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
        ]
    },
    '/conversations.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'exclude_archived'
            },
            {
                'name': 'types'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/conversations.mark-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'ts'
            },
        ]
    },
    '/conversations.members-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/conversations.open-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'return_im'
            },
            {
                'name': 'users'
            },
        ]
    },
    '/conversations.rename-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/conversations.replies-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'ts'
            },
            {
                'name': 'latest'
            },
            {
                'name': 'oldest'
            },
            {
                'name': 'inclusive'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/conversations.setPurpose-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'purpose'
            },
        ]
    },
    '/conversations.setTopic-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'topic'
            },
        ]
    },
    '/conversations.unarchive-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
        ]
    },
    '/dialog.open-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'dialog'
            },
            {
                'name': 'trigger_id'
            },
        ]
    },
    '/dnd.endDnd-POST': {
        'parameters': [
            {
                'name': 'token'
            },
        ]
    },
    '/dnd.endSnooze-POST': {
        'parameters': [
            {
                'name': 'token'
            },
        ]
    },
    '/dnd.info-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'user'
            },
        ]
    },
    '/dnd.setSnooze-POST': {
        'parameters': [
            {
                'name': 'num_minutes'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/dnd.teamInfo-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'users'
            },
        ]
    },
    '/emoji.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
        ]
    },
    '/files.remote.add-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'external_url'
            },
            {
                'name': 'filetype'
            },
            {
                'name': 'indexable_file_contents'
            },
            {
                'name': 'preview_image'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/files.delete-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/files.comments.delete-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'file'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/files.remote.remove-POST': {
        'parameters': [
            {
                'name': 'external_id'
            },
            {
                'name': 'file'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/files.remote.info-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'file'
            },
            {
                'name': 'external_id'
            },
        ]
    },
    '/files.info-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'file'
            },
            {
                'name': 'count'
            },
            {
                'name': 'page'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/files.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'user'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'ts_from'
            },
            {
                'name': 'ts_to'
            },
            {
                'name': 'types'
            },
            {
                'name': 'count'
            },
            {
                'name': 'page'
            },
            {
                'name': 'show_files_hidden_by_limit'
            },
        ]
    },
    '/files.remote.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'ts_from'
            },
            {
                'name': 'ts_to'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/files.revokePublicURL-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/files.remote.share-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'file'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'channels'
            },
        ]
    },
    '/files.sharedPublicURL-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'file'
            },
        ]
    },
    '/files.remote.update-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'external_url'
            },
            {
                'name': 'file'
            },
            {
                'name': 'filetype'
            },
            {
                'name': 'indexable_file_contents'
            },
            {
                'name': 'preview_image'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/files.upload-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'channels'
            },
            {
                'name': 'content'
            },
            {
                'name': 'file'
            },
            {
                'name': 'filename'
            },
            {
                'name': 'filetype'
            },
            {
                'name': 'initial_comment'
            },
            {
                'name': 'thread_ts'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/files.comments.delete-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'file'
            },
            {
                'name': 'id'
            },
        ]
    },
    '/files.remote.add-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'external_url'
            },
            {
                'name': 'filetype'
            },
            {
                'name': 'indexable_file_contents'
            },
            {
                'name': 'preview_image'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/files.remote.remove-POST': {
        'parameters': [
            {
                'name': 'external_id'
            },
            {
                'name': 'file'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/files.remote.info-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'file'
            },
            {
                'name': 'external_id'
            },
        ]
    },
    '/files.remote.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'ts_from'
            },
            {
                'name': 'ts_to'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/files.remote.share-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'file'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'channels'
            },
        ]
    },
    '/files.remote.update-POST': {
        'parameters': [
            {
                'name': 'title'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'external_url'
            },
            {
                'name': 'file'
            },
            {
                'name': 'filetype'
            },
            {
                'name': 'indexable_file_contents'
            },
            {
                'name': 'preview_image'
            },
            {
                'name': 'token'
            },
        ]
    },
    '/migration.exchange-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'users'
            },
            {
                'name': 'team_id'
            },
            {
                'name': 'to_old'
            },
        ]
    },
    '/oauth.access-GET': {
        'parameters': [
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
            {
                'name': 'code'
            },
            {
                'name': 'redirect_uri'
            },
            {
                'name': 'single_channel'
            },
        ]
    },
    '/oauth.v2.access-GET': {
        'parameters': [
            {
                'name': 'code'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
            {
                'name': 'redirect_uri'
            },
        ]
    },
    '/oauth.token-GET': {
        'parameters': [
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
            {
                'name': 'code'
            },
            {
                'name': 'redirect_uri'
            },
            {
                'name': 'single_channel'
            },
        ]
    },
    '/oauth.v2.access-GET': {
        'parameters': [
            {
                'name': 'code'
            },
            {
                'name': 'client_id'
            },
            {
                'name': 'client_secret'
            },
            {
                'name': 'redirect_uri'
            },
        ]
    },
    '/pins.add-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'timestamp'
            },
        ]
    },
    '/pins.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
        ]
    },
    '/pins.remove-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'timestamp'
            },
        ]
    },
    '/reactions.add-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'name'
            },
            {
                'name': 'timestamp'
            },
        ]
    },
    '/reactions.get-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'file'
            },
            {
                'name': 'file_comment'
            },
            {
                'name': 'full'
            },
            {
                'name': 'timestamp'
            },
        ]
    },
    '/reactions.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'user'
            },
            {
                'name': 'full'
            },
            {
                'name': 'count'
            },
            {
                'name': 'page'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/reactions.remove-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'name'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'file'
            },
            {
                'name': 'file_comment'
            },
            {
                'name': 'timestamp'
            },
        ]
    },
    '/reminders.add-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'text'
            },
            {
                'name': 'time'
            },
            {
                'name': 'user'
            },
        ]
    },
    '/reminders.complete-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'reminder'
            },
        ]
    },
    '/reminders.delete-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'reminder'
            },
        ]
    },
    '/reminders.info-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'reminder'
            },
        ]
    },
    '/reminders.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
        ]
    },
    '/rtm.connect-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'batch_presence_aware'
            },
            {
                'name': 'presence_sub'
            },
        ]
    },
    '/search.messages-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'query'
            },
            {
                'name': 'count'
            },
            {
                'name': 'highlight'
            },
            {
                'name': 'page'
            },
            {
                'name': 'sort'
            },
            {
                'name': 'sort_dir'
            },
        ]
    },
    '/stars.add-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'file'
            },
            {
                'name': 'file_comment'
            },
            {
                'name': 'timestamp'
            },
        ]
    },
    '/stars.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'count'
            },
            {
                'name': 'page'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'limit'
            },
        ]
    },
    '/stars.remove-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'channel'
            },
            {
                'name': 'file'
            },
            {
                'name': 'file_comment'
            },
            {
                'name': 'timestamp'
            },
        ]
    },
    '/team.accessLogs-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'before'
            },
            {
                'name': 'count'
            },
            {
                'name': 'page'
            },
        ]
    },
    '/team.billableInfo-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'user'
            },
        ]
    },
    '/team.profile.get-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'visibility'
            },
        ]
    },
    '/team.info-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'team'
            },
        ]
    },
    '/team.integrationLogs-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'app_id'
            },
            {
                'name': 'change_type'
            },
            {
                'name': 'count'
            },
            {
                'name': 'page'
            },
            {
                'name': 'service_id'
            },
            {
                'name': 'user'
            },
        ]
    },
    '/team.profile.get-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'visibility'
            },
        ]
    },
    '/usergroups.create-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'name'
            },
            {
                'name': 'description'
            },
            {
                'name': 'channels'
            },
            {
                'name': 'handle'
            },
            {
                'name': 'include_count'
            },
        ]
    },
    '/usergroups.disable-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'usergroup'
            },
            {
                'name': 'include_count'
            },
        ]
    },
    '/usergroups.enable-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'usergroup'
            },
            {
                'name': 'include_count'
            },
        ]
    },
    '/usergroups.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'include_users'
            },
            {
                'name': 'include_count'
            },
            {
                'name': 'include_disabled'
            },
        ]
    },
    '/usergroups.users.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'usergroup'
            },
            {
                'name': 'include_disabled'
            },
        ]
    },
    '/usergroups.update-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'usergroup'
            },
            {
                'name': 'description'
            },
            {
                'name': 'channels'
            },
            {
                'name': 'handle'
            },
            {
                'name': 'include_count'
            },
            {
                'name': 'name'
            },
        ]
    },
    '/usergroups.users.update-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'usergroup'
            },
            {
                'name': 'users'
            },
            {
                'name': 'include_count'
            },
        ]
    },
    '/usergroups.users.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'usergroup'
            },
            {
                'name': 'include_disabled'
            },
        ]
    },
    '/usergroups.users.update-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'usergroup'
            },
            {
                'name': 'users'
            },
            {
                'name': 'include_count'
            },
        ]
    },
    '/users.conversations-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'user'
            },
            {
                'name': 'types'
            },
            {
                'name': 'exclude_archived'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
        ]
    },
    '/users.deletePhoto-POST': {
        'parameters': [
            {
                'name': 'token'
            },
        ]
    },
    '/users.getPresence-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'user'
            },
        ]
    },
    '/users.profile.get-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'include_labels'
            },
            {
                'name': 'user'
            },
        ]
    },
    '/users.identity-GET': {
        'parameters': [
            {
                'name': 'token'
            },
        ]
    },
    '/users.info-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'include_locale'
            },
            {
                'name': 'user'
            },
        ]
    },
    '/users.list-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'limit'
            },
            {
                'name': 'cursor'
            },
            {
                'name': 'include_locale'
            },
        ]
    },
    '/users.lookupByEmail-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'email'
            },
        ]
    },
    '/users.setActive-POST': {
        'parameters': [
            {
                'name': 'token'
            },
        ]
    },
    '/users.setPhoto-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'crop_w'
            },
            {
                'name': 'crop_x'
            },
            {
                'name': 'crop_y'
            },
            {
                'name': 'image'
            },
        ]
    },
    '/users.setPresence-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'presence'
            },
        ]
    },
    '/users.profile.set-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'name'
            },
            {
                'name': 'profile'
            },
            {
                'name': 'user'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/users.profile.get-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'include_labels'
            },
            {
                'name': 'user'
            },
        ]
    },
    '/users.profile.set-POST': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'name'
            },
            {
                'name': 'profile'
            },
            {
                'name': 'user'
            },
            {
                'name': 'value'
            },
        ]
    },
    '/views.open-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'trigger_id'
            },
            {
                'name': 'view'
            },
        ]
    },
    '/views.publish-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'user_id'
            },
            {
                'name': 'view'
            },
            {
                'name': 'hash'
            },
        ]
    },
    '/views.push-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'trigger_id'
            },
            {
                'name': 'view'
            },
        ]
    },
    '/views.update-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'view_id'
            },
            {
                'name': 'external_id'
            },
            {
                'name': 'view'
            },
            {
                'name': 'hash'
            },
        ]
    },
    '/workflows.stepCompleted-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'workflow_step_execute_id'
            },
            {
                'name': 'outputs'
            },
        ]
    },
    '/workflows.stepFailed-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'workflow_step_execute_id'
            },
            {
                'name': 'error'
            },
        ]
    },
    '/workflows.updateStep-GET': {
        'parameters': [
            {
                'name': 'token'
            },
            {
                'name': 'workflow_step_edit_id'
            },
            {
                'name': 'inputs'
            },
            {
                'name': 'outputs'
            },
            {
                'name': 'step_name'
            },
            {
                'name': 'step_image_url'
            },
        ]
    },
};