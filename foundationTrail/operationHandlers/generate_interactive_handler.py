ERROR_TYPE_NOT_COMPATIBLE = 'The value you specified cannot be converted into the needed type.'

def _check_value_is_type(value_to_check, type_to_check_against) -> bool:
    # NOTE: checking if `type_to_check_against` is actually a type
    # and not a random value
    if not isinstance(type_to_check_against, type):
        # TODO: also print on screen some kind of warning to inform that the type was not specified.
        return False 

    if not isinstance(value_to_check, type_to_check_against):
        return False
    
    return True


def handle_generate_interactive(params_to_handle: list[dict]) -> dict:
    '''
    The input of this function is a list of dictionary that are like this:
        [
            {
                'property_name': 'technical_name_of_the_property', # a.k.a the name of the parameter for the function that will be called.
                'property_type': str | int | float, # etc...
                'property_is_optional': True, # can the user avoid giving this value to us?
                'property_allowed_vals': [], # a list of allowed values, to which the user-inserted value will be compared to.
                'property_ask_for_val_msg': '', # the string that will be printed to screen to ask the user for the value.
            }
        ]
    '''

    # TODO: include value check on all parts of the list 

    return_dict = {}
    for param in params_to_handle:
        fallback_string = f"Please insert value for '{param.get('property_label', '')}':"
        ask_for_val_msg = param.get('property_ask_for_val_msg', fallback_string)

        final_msg = '{}{}{}:'.format(
            ask_for_val_msg,
            ' [Optional]' if param['property_is_optional'] else '',
            ' [y/N]' if param['property_type'] is bool else ''
        )

        value = input(final_msg)

        if value != '' and param['property_type'] is not bool and not _check_value_is_type(value, param.get('property_type', str)):
            print(ERROR_TYPE_NOT_COMPATIBLE)

        if param.get('property_allowed_vals', []):
            if value not in param['property_allowed_vals']:
                print("value not between allowed values.")

        if param['property_type'] is not bool:
            return_dict[param['property_name']] = value
        else:
            return_dict[param['property_name']] = True if value in ('y', 'Y') else False

    # print('[DEBUG] return_dict's value: ', return_dict)

    return return_dict
