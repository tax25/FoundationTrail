GENERATE_MODULE_PARAMETERS = [
    {
        'property_name': 'name',
        'property_type': str,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please insert the module name'
    },
    {
        'property_name': 'is_application',
        'property_type': bool,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Is the module an application?'
    },
    {
        'property_name': 'dependencies',
        'property_type': str,
        'property_is_optional': True,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify any dependencies of the module'
    },
    {
        'property_name': 'author',
        'property_type': str,
        'property_is_optional': True,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the author of the module'
    },
    {
        'property_name': 'version',
        'property_type': str,
        'property_is_optional': True,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the starting version of the module'
    },
    {
        'property_name': 'description',
        'property_type': str,
        'property_is_optional': True,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please insert a description for the module'
    },
    {
        'property_name': 'category',
        'property_type': str,
        'property_is_optional': True,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please insert a category for the module'
    }
]
