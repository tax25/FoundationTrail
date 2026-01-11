def send_help() -> None:

    print("""
Hey! It looks like you need help!

FoundationTrail usage:

-> First flag: `-g` (or `--generate`)
    This does nothing other than tell `foundationTrail` that you want to *generate* something.
    
-> Second flag: `-M` (or `--module`), `-m` (or `--model`), `-v` (or `--view`), `-s` (or `--security`) 
    This flag specifies which *type* of resource you want to generate

=> To get more information of the usage of the singular second flags, please use:
`foundationTrail --explain {secondFlag}` or `foundationTrail -e {secondFlag}`.
-> Where `secondFlag` is the flag you want clarifications about.
    """)

def explain_module_generation() -> None:
    print("""
Looks like you need help with the generation of a module!

So, the available flags are:
* -n  | --name => allows you to specify the name of the module to be created.
* -a  | --app => allows you to specify that the module to be created is an application - sets the `app` attribute in the `__manifest__.py` file to `True`.
* -d  | --deps => allows you to specify one or more dependencies for the module. They have to be specified separated by commas, no spaces!
* -A  | --author => allows you to specify who is the author of the module. If not set, `foundationTrail` automatically takes your login username.
* -mv | --m-version => allows you to specify the version of the module.
* -D  | --description => allows you to specify the description of the module.
* -c  | --category => allows you to specify the category of the module.

All these flags mainly just change what is written in the `__manifest__.py` file.
    """)

def explain_model_generation() -> None:
    print("This part of the application still has to be developed!")

def explain_view_generation() -> None:
    print("This part of the application still has to be developed!")

def explain_security_generation() -> None:
    print("This part of the application still has to be developed!")