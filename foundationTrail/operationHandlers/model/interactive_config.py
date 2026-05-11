INTERACTIVE_CONFIG = [
    {
        'property_name': 'name',
        'property_type': str,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify model name'
    },
    {
        'property_name': 'chosen_type',
        'property_type': str,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify model type'
    },
    {
        'property_name': 'is_wizard',
        'property_type': bool,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Is this model for a wizard?'
    },
    {
        'property_name': 'inherit',
        'property_type': str,
        'property_is_optional': True,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the model this new model has to inherit from'
    },
    {
        'property_name': 'file_name',
        'property_type': str,
        'property_is_optional': True,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': "Please specify the file name in which you'd like the module to be created"
    },
    {
        'property_name': 'cli_perms',
        'property_type': str,
        'property_is_optional': True,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the permissions for the model to be created'
    },

]
