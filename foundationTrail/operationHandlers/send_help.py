def send_help() -> None:
    print("""
Hey! It looks like you need help!

FoundationTrail usage:

-> First flag: `-g` (or `--generate`)
    This does nothing other than tell `foundationTrail` that you want to *generate* something.
    
-> Second flag: `-M` (or `--module`), `-m` (or `--model`), `-v` (or `--view`), `-s` (or `--security`) 
    This flag specifies which *type* of resource you want to generate

=> To get more information of the usage of the singular second flags, please use:
`foundationTrail --explain {secondFlag}` or `foundationTrail -e {secondFlag}` or `foundationTrail -e=-{secondFlag}` or `foundationTrail --explain=-{secondFlag}`.
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
    print("""
Alright, I'll help you with this one!

So, the available flags are:
* -n  | --name => allows you to specify the name of the model to be created. If `--file-name` is *not* specified, it also sets the file name of the model.
* -fn | --file-name => allows you to specify the name of the file you want the model to be saved in.
* -mt | --model-type => allows you to specify the type of the model that you want to create: Model? TransientModel? AbstractModel, and so forth...
* -i  | --inherit => allows you to specify the model(s) that the model that you are creating will be inheriting from. You can specify more than one, just separate them with commas.
* -wz | --wizard => this is just a toggle. If set, the model is created in the `wizards/` directory and added to the `wizards/__init__.py` file. If not, the file will be created in the `models/` directory, and added to the `models/__init__.py` file.
* -mp | --m-perms => allows you to specify the perms with which the model will be created. These are the values that will be set in the `security/ir.model.access.csv` file.
    """)

def explain_view_generation() -> None:
    print("""
FoundationTrail to the rescue!

So, the available flags are:
* -n  | --name => allows you to specify the name of the view (the id) you want to create. If `--file-name` is *not* specified, it also sets the file name of the view.
* -fn | --file-name => allows you to specify the name of the file the view will be saved in.
* -vm | --view-model => allows you to specify which model will the view relate to.
* -iv | --inherit-view => allows you to specify which view should your view inherit from.
    """)

def explain_security_generation() -> None:
    print("""
*walks over* is it you that needs help? Alright.

So, the available flags are:
* -id  | --line-id => allows you to specify the line id of the line that will be inserted in the `security/ir.model.access.file.csv`.
* -ln  | --line-name => allows you to specify the line name of the line that will be inserted in the security file.
* -mid | --model-id => allows you to specify the model id for the security line.
* -gid | --group-id => allows you to specify the group id.
* -pr  | --perm-read => allows you to specify the reading permission. Defaults to 0.
* -pw  | --perm-write => allows you to specify the writing permission. Defaults to 0.
* -pc  | --perm-create => allows you to specify the creating permission. Defaults to 0.
* -pu  | --perm-unlink => allows you to specify the unlink permission. Defaults to 0.
    """)
