import os
import json

MANIFEST_FILENAME = '__manifest__.py'


def handle_generate_view(view_name: str) -> int:
    
    # check if user is in a directory
    if not os.path.exists(os.getcwd() + '/views') and not '/views' in os.getcwd():
        return _handle_eventual_views_dir_creation()
    
    # create file
    file_name_and_path = ''
    if '/views' in os.getcwd():
        file_name_and_path = os.getcwd() + f'/{view_name}.xml'
    else:
        file_name_and_path = os.getcwd() + f'/views/{view_name}.xml'

    with open(file_name_and_path, 'w') as view_file:
        basic_view_file_string = f"""<?xml version="1.0" encoding="utf-8"?>
<odoo>

    <data>

        <record id="{view_name}" model="ir.ui.view"></record>

    </data>

</odoo>
"""
        view_file.write(basic_view_file_string)
    
    # add file to __manifest__.py
    manifest_file_path = ''
    module_name = ''
    if not os.path.isfile(MANIFEST_FILENAME):
        os.chdir('..') 
        while True:
            if not os.path.isfile(MANIFEST_FILENAME):
                os.chdir('..')
            else:
                manifest_file_path = os.path.abspath(os.curdir)
                # taking the last argument as the module name 
                # is the current directory
                module_name = manifest_file_path.split('/')[-1]
                break

            if os.path.abspath(os.curdir) == '/home':
                print("__manifest__.py file not found...")
                break
    else:
        manifest_file_path = os.path.abspath(os.curdir)
        module_name = manifest_file_path.split('/')[-1]

    with open(manifest_file_path + '/__manifest__.py', 'r') as manifest:
        #  print(manifest.read())
        print("valore manifest", type(manifest
                    .read()
                    .replace('\n', '')
                    .replace('\t', '')
                    .replace("'", '"')
                    .replace('false', 'false')
                    .replace('true', 'true')
                    .replace(',}', '}'))
        )
        manifest_str = manifest.read().replace('\n', '').replace('\t', '').replace("'", '"').replace('false', 'false').replace('true', 'true').replace(',}', '}')
        
        stuff = json.loads(manifest_str)

        print(stuff)
    print("View file created and added to the __manifest__.py")


def _handle_eventual_views_dir_creation() -> int: 
    print("The views directory has not been found")




