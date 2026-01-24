def handle_generate_interactive(params_to_handle: list[dict]) -> dict:
    '''
    Questa funzione prende in input un array di dictionary
    I dictionary presenti nell'array sono cosi formati:

    ```
    {
        'property_name': 'property_name_val',
        'property_label': 'property_label_val', # Questo e' il valore che verra' fatto vedere all'utente.
        'property_type': str | int | float # etc...,
        'property_is_optional': True, # Questo specifica se il valore deve per forza essere passato o meno.
        'property_allowed_vals': [], # Questo e' un valore opzionale. Nel caso in cui sia valorizzato
                                     # solamente i valori presenti saranno accettati come validi
                                     # nel momento in cui verra eseguito il controllo sull'input.
        'property_ask_for_val_msg': '', # Questo e' il messaggio con il quale si chiede all'utente di inserire il valore.
    }
    ```
    '''
    # TODO: include value check on all parts of the list 
    
    return_dict = {}
    for param in params_to_handle:
        ask_for_val_msg = param.get('property_ask_for_val_msg',f"Please insert value for: '{param.get('property_label', '')}':")
        value = input(ask_for_val_msg)
        if param.get('property_allowed_vals', []):
            if value not in param['property_allowed_vals']:
                print("value not between allowed values.")

        return_dict[param['property_name']] = value

    return return_dict
