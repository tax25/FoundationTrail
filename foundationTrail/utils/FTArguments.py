from argparse import ArgumentParser
from typing import override

from foundationTrail.utils.FTConfig import FTConfig

class Argument:
    shortForm: str = ''
    longForm: str = ''
    argumentType: type = type
    action: str = ''
    
    def __init__(self,
             short: str, 
             long: str, 
             argType: type = type,
             action: str=''
    ):
        self.shortForm = short
        self.longForm = long
        self.argumentType = argType
        self.action = action


# NOTE:
'''
To be able to use the groups of argparse, this has to be done:
    ```
        parser = argparse.ArgumentParser()
        my_group = parser.add_argument_group('groupName')
        my_group.add_argument(**my_argument)
    ```
'''

ARGUMENTS_DESCR = {
    'Miscellaneous': [
        Argument('-h', '--help', action='store_true'),
        Argument('-V', '--version', action='store_true'),
        Argument('-I', '--interactive', action='store_true'),
        Argument('-e', '--explain', argType=str),
        Argument('-n', '--name', argType=str),
        Argument('-fn', '--filename', argType=str),
    ],
    'Basic Actions': [
        Argument('-g', '--generate', action='store_true'),
    ],
    'Specifics.Modules': [
        Argument('-M', '--module', action='store_true'), 
        Argument('-a', '--app', action='store_true'),
        Argument('-d', '--deps', argType=str),
        Argument('-A', '--author', argType=str),
        Argument('-mv', '--m_version', argType=str),
        Argument('-D', '--description', argType=str),
        Argument('-c', '--category', argType=str),
    ],
    'Specifics.Models': [
        Argument('-m', '--model', action='store_true'), 
        Argument('-mt', '--model_type', argType=str),
        Argument('-i', '--inherit', argType=str),
        Argument('-wz', '--wizard', action='store_true'),
        Argument('-mp', '--m_perms', argType=str)
    ],
    'Specifics.Views': [
        Argument('-v', '--view', action='store_true'),
        Argument('-vm', '--view_model', argType=str),
        Argument('-wv', '--wizard_view', action='store_true'),
        Argument('-iv', '--inherit_view', argType=str),
    ],
    'Specifics.Security': [
        Argument('-s', '--security', action='store_true'),
        Argument('-id', '--line_id', argType=str),
        Argument('-ln', '--line_name', argType=str),
        Argument('-mid', '--model_id', argType=str),
        Argument('-gid', '--group_id', argType=str),
        Argument('-pr', '--perm-read', action='store_true'),
        Argument('-pw', '--perm-write', action='store_true'),
        Argument('-pc', '--perm-create', action='store_true'),
        Argument('-pu', '--perm-unlink', action='store_true'),
    ],
}

class FTArguments:
    help: bool = False
    version: bool = False
    interactive: bool = False
    explain: str = ""
    
    name: str = ""
    filename: str = ""

    generate: bool = False

    module: bool = False
    app: bool = False
    deps: str = ""
    author: str = ""
    m_version: str = ""
    description: str = ""
    category: str = ""

    model: bool = False
    model_type: str = ""
    inherit: str = ""
    wizard: bool = False
    m_perms: str = ""

    view: bool = False
    view_model: str = ""
    wizard_view: bool = False
    inherit_view: str = ""

    security: bool = False
    line_id: str = ""
    line_name: str = ""
    model_id: str = ""
    group_id: str = ""
    perm_read: bool = False
    perm_write: bool = False
    perm_create: bool = False
    perm_unlink: bool = False
    
    _parser: ArgumentParser = ArgumentParser(
        prog='FoundationTrail',
        description='A tool for Odoo developing',
        epilog='Stay the reading of our swan song and epilogue',
        add_help=False
    )
    
    def _fn_get_class_props_list(self) -> list[str]:
        all_props: list[str] = []
        for prop in __class__.__dict__.items():
            if (prop[0].startswith('_') or prop[0].startswith('fn_')):
                continue

            all_props.append(prop[0])

        return all_props
    
    def _fn_flatten_args_descr(self, args_descr: dict[str, list[Argument]]):
        flattened: list[Argument] = []
        for group in args_descr:
            for argument in args_descr[group]:
                flattened.append(argument)
        
        return flattened


    def __init__(self, configurationVals: FTConfig):
        cli_args: list[Argument] = self._fn_flatten_args_descr(ARGUMENTS_DESCR)

        class_props = self._fn_get_class_props_list()
        
        if len(class_props) != len(cli_args):
            print("ERROR: Contents of ARGUMENTS_DESCR and respective class properties do not match!")
            return
        
        for arg in cli_args:
            if arg.action:
                _ = self._parser.add_argument(
                    arg.shortForm,
                    arg.longForm,
                    action=arg.action
                )

            elif arg.argumentType:
                _ = self._parser.add_argument(
                    arg.shortForm,
                    arg.longForm,
                    type=arg.argumentType
                )
            
            else:
                print("ERROR: argument description needs either type or action")
                return
        
        _ = self._parser.parse_args(namespace=self)

    def fn_get_module_props_in_dict(self) -> dict[str, str | bool]:
        return {
            'name': self.name,
            'app': self.app,
            'deps': self.deps,
            'author': self.author,
            'm_version': self.m_version,
            'description': self.description,
            'category': self.category,
        }
    
    def fn_get_model_props_in_dict(self):
        return {
            'name': self.name,
            'model_type': self.model_type,
            'inherit': self.inherit,
            'wizard': self.wizard,
            'filename': self.filename,
            'm_perms': self.m_perms,
        }
    
    def fn_get_security_props_in_dict(self):
        return {
            'security_file_name': self.filename.replace('.csv', '') if self.filename else 'ir.model.access',
            'line_id': self.line_id,
            'line_name': self.line_name,
            'model_id': self.model_id,
            'group_id': self.group_id,
            'perm_read': self.perm_read,
            'perm_write': self.perm_write,
            'perm_create': self.perm_create,
            'perm_unlink': self.perm_unlink,
        }
    
    def fn_get_view_props_in_dict(self):
        return {
            'view_name': self.filename.replace('.xml', '') if self.filename else self.name.replace('.xml', ''),
            'model': self.view_model if self.view_model else '',
            'inherit_id': self.inherit_view,
            'is_for_wizard': self.wizard,
        }

    @override
    def __str__(self):
        str_to_return = f"""
            {{
                version: {self.version},
                interactive: {self.interactive},
                explain: {self.explain},
                name: {self.name},
                filename: {self.filename},
                generate: {self.generate},
                module: {self.module},
                app: {self.app},
                deps: {self.deps},
                author: {self.author},
                m_version: {self.m_version},
                description: {self.description},
                category: {self.category},
                model: {self.model},
                model_type: {self.model_type},
                inherit: {self.inherit},
                wizard: {self.wizard},
                m_perms: {self.m_perms},
                view: {self.view},
                view_model: {self.view_model},
                inherit_view: {self.inherit_view},
                security: {self.security},
                line_id: {self.line_id},
                line_name: {self.line_name},
                model_id: {self.model_id},
                group_id: {self.group_id},
                perm_read: {self.perm_read},
                perm_write: {self.perm_write},
                perm_create: {self.perm_create},
                perm_unlink: {self.perm_unlink},
            }}
        """
    
        return str_to_return
