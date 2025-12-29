import os
import json
import platform

def _get_end_directory():

    # WARN: this type of check 
    # is *not* optimal.
    # (It could break easily if, for some reason,
    # the user is not using `/home/*` or `/Users/*`)
    match platform.system():

        case 'Darwin':
            return f'/Users/{os.getlogin()}'
        case 'Linux':
            return '/home'


MANIFEST_FILENAME = '__manifest__.py'
END_DIRECTORY = _get_end_directory()

BASIC_VIEW_FILE_STRING = ''
INHERIT_VIEW_FILE_STRING = ''

def handle_generate_view(view_name: str, model: str, inherit_id: str, is_for_wizard: bool):
    # create file
    # `file_name` is used in the `__manifest__.py`
    file_name = f"{'views' if not is_for_wizard else 'wizards'}/{view_name}.xml"
    file_name_and_path = ''
    
    if f"{'views' if not is_for_wizard else 'wizards'}" in os.getcwd():
        file_name_and_path = os.getcwd() + f'/{view_name}.xml'
    elif os.path.exists(os.getcwd() + f"/{'views' if not is_for_wizard else 'wizards'}"):
        file_name_and_path = os.getcwd() + f"/{'views' if not is_for_wizard else 'wizards'}/{view_name}.xml"
    elif os.path.exists(os.getcwd() + f"/../{'views' if not is_for_wizard else 'wizards'}"): # in case the user is in the models directory, for example
        file_name_and_path = os.getcwd() + f'/../{'views' if not is_for_wizard else 'wizards'}/{view_name}.xml'
    else:
        print(f"Cannot find /{'views' if not is_for_wizard else 'wizards'} directory so creating the file in current directory ({os.getcwd()})")
        file_name = f'{view_name}.xml'
        file_name_and_path = os.getcwd() + f'/{view_name}.xml'

    with open(file_name_and_path, 'w') as view_file:
        inherit_id_string = '<field name="inherit_id" ref="{0}"/>'
        basic_view_file_string = f"""<?xml version="1.0" encoding="utf-8"?>
        
<odoo>

    <data>

        <record id="{view_name}" model="ir.ui.view">
            <field name="name">{view_name.replace('_', '.')}</field>
            <field name="model">{model.replace('_', '.') if model is not None else ''}</field>
            {inherit_id_string.format(inherit_id) if inherit_id else ''}
            <field name="arch" type="xml">

            </field>
        </record>

    </data>

</odoo>
"""
        view_file.write(basic_view_file_string)
    
    # add file to __manifest__.py
    manifest_file_path = ''
    # module_name = ''
    if not os.path.isfile(MANIFEST_FILENAME):
        os.chdir('..') 
        while True:
            if not os.path.isfile(MANIFEST_FILENAME):
                os.chdir('..')
            else:
                manifest_file_path = os.path.abspath(os.curdir)
                # taking the last argument as the module name 
                # is the current directory
                # module_name = manifest_file_path.split('/')[-1]
                break

            if os.path.abspath(os.curdir) == END_DIRECTORY :
                print("ERROR: __manifest__.py file not found! View is generated, but not added to __manifest__.py")
                return
    else:
        manifest_file_path = os.path.abspath(os.curdir)
        # module_name = manifest_file_path.split('/')[-1]

    with open(manifest_file_path + '/__manifest__.py', 'r+') as manifest:
        manifest_content = manifest.read()
        
        if not manifest_content or manifest_content[0] != '{':
            # @TODO(handle manifest being empty or at least not valid)
            raise Exception("ERROR: __manifest__.py is empty or not valid")
            
        manifest_dict = json.loads(
            "".join(manifest_content.split())
                .replace('\n', '')
                .replace('\t', '')
                .replace("'", '"')
                .replace('False', 'false')
                .replace('True', 'true')
                .replace(',]', ']')
                .replace(',}', '}')
        )
            
        manifest_dict['data'].append(file_name)
        
        manifest.seek(0)
        
        manifest.write(json.dumps(manifest_dict, indent=4).replace('true', 'True').replace('false', 'False'))
        
        manifest.truncate()
        
        print(f"View file created and added to the __manifest__.py as {file_name}")
        





