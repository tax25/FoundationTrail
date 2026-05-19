GENERATE_VIEW_PARAMETERS = [
    {
        'property_name': 'view_name',
        'property_type': str,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the name for the view to be generated'
    },
    {
        'property_name': 'model',
        'property_type': str,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the model that the view to be created will refer to'
    },
    {
        'property_name': 'inherit_id',
        'property_type': str,
        'property_is_optional': True,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the view this view will be inheriting from'
    },
    {
        'property_name': 'is_for_wizard',
        'property_type': bool,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Is this view for a wizard?'
    },
]
