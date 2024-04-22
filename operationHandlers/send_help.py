def send_help() :

    print("""
Hi! It looks like you have not passed enough parameters!

## WARNING: this is still a WIP (obviously) and needs updates, will update the help function 
## as i go on with the development

Here are some informations on the generic parameters of Aodoo:
    1. The first parameter you have to pass is the "action". 
       Basically "what do you want to do?": generate something? Other? (not that there are other options at the moment, lol).
       So for now you will just pass "generate" or "g" if you don't want to type too much.

    2. The second parameter is the "detail" of the first one. So you want to generate something: what? A security file, a model, an entire module?
       You can pass the following parameters to the "generate" action:

           * "module" or "m" -> to generate a complete module boilerplate
           * "view" or "v" -> to generate a single view file (and include it in the __manifest__) for a specific model
           * "model" or "M" -> to generate a new model file (and add it in the right __init__)
           * "security" or "s" -> to generate a security file or add the security for a specific model

    """)

