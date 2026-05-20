from argparse import ArgumentParser
from dataclasses import dataclass
from typing import override

from foundationTrail.utils.InteractiveModeUtils import InteractiveProp

@dataclass
class Argument:
    shortForm: str = ''
    longForm: str = ''
    argumentType: type = type
    action: str = ''

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
        Argument('-e', '--explain', argumentType=str),
        Argument('-n', '--name', argumentType=str),
        Argument('-fn', '--filename', argumentType=str),
    ],
    'Basic Actions': [
        Argument('-g', '--generate', action='store_true'),
    ],
    'Specifics.Modules': [
        Argument('-M', '--module', action='store_true'), 
        Argument('-a', '--app', action='store_true'),
        Argument('-d', '--deps', argumentType=str),
        Argument('-A', '--author', argumentType=str),
        Argument('-mv', '--m_version', argumentType=str),
        Argument('-D', '--description', argumentType=str),
        Argument('-c', '--category', argumentType=str),
    ],
    'Specifics.Models': [
        Argument('-m', '--model', action='store_true'), 
        Argument('-mt', '--model_type', argumentType=str),
        Argument('-i', '--inherit', argumentType=str),
        Argument('-wz', '--wizard', action='store_true'),
        Argument('-mp', '--m_perms', argumentType=str)
    ],
    'Specifics.Views': [
        Argument('-v', '--view', action='store_true'),
        Argument('-vm', '--view_model', argumentType=str),
        Argument('-wv', '--wizard_view', action='store_true'),
        Argument('-iv', '--inherit_view', argumentType=str),
    ],
    'Specifics.Security': [
        Argument('-s', '--security', action='store_true'),
        Argument('-id', '--line_id', argumentType=str),
        Argument('-ln', '--line_name', argumentType=str),
        Argument('-mid', '--model_id', argumentType=str),
        Argument('-gid', '--group_id', argumentType=str),
        Argument('-pr', '--perm-read', action='store_true'),
        Argument('-pw', '--perm-write', action='store_true'),
        Argument('-pc', '--perm-create', action='store_true'),
        Argument('-pu', '--perm-unlink', action='store_true'),
    ],
}

class ValueNotAllowedError(BaseException):
    pass

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


    def __init__(self):
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
    
    def fn_args_from_interactive(self, interactive_conf: list[InteractiveProp]):
        for param in interactive_conf:
            query_string = \
                    "{main_query}{optional_specifier}{yes_or_no}: ".format(
                            main_query=param.query_msg,
                            optional_specifier='[Optional]' if param.is_optional else '',
                            yes_or_no='[y/n]' if param.prop_type == bool else ''
                        )

            param_val = input(query_string)
            
            if type(param_val) != param.prop_type:
                raise TypeError()

            if len(param.allowed_vals) > 0 and param_val not in param.allowed_vals:
                raise ValueNotAllowedError(f"{param_val} is not between the allowed values ({param.allowed_vals})")

            setattr(self, param.prop_name, param_val)

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
