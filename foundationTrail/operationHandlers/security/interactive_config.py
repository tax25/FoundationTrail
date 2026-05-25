GENERATE_SECURITY_PARAMETERS = [
    {
        'property_name': 'security_file_name',
        'property_type': str,
        'property_is_optional': True,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': "Please specify the file name you'd like the security configuration to be saved in"
    },
    {
        'property_name': 'line_id',
        'property_type': str,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the line id for this security configuration'
    },
    {
        'property_name': 'line_name',
        'property_type': str,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the line name for this security configuration'
    },
    {
        'property_name': 'model_id',
        'property_type': str,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the model id for this security configuration'
    },
    {
        'property_name': 'group_id',
        'property_type': str,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the group id for this security configuration'
    },
    {
        'property_name': 'perm_read',
        'property_type': bool,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the read permissions for this security configuration'
    },
    {
        'property_name': 'perm_write',
        'property_type': bool,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the write permissions for this security configuration'
    },
    {
        'property_name': 'perm_create',
        'property_type': bool,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the create permissions for this security configuration'
    },
    {
        'property_name': 'perm_unlink',
        'property_type': bool,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the unlink permissions for this security configuration'
    },
]
