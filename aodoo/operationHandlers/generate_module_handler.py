import os
import sys

MAIN_INIT_FILE_CONTENTS = '''from . import models
from . import wizards
'''

MANIFEST_FILE_CONTENTS = """{{
	'name': '{module_name}',
	'version': '0.1',
	'depends': ['base'],
	'author': '{author}',
	'application': {is_application},
	'data': ['security/ir.model.access.csv'],
}}
"""

BASE_MODEL_FILE_CONTENTS = f'''from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)
'''

SECURITY_FILE_CONTENTS = 'id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink\n'

def handle_generate_module(name, is_application):

	assert name != False, "Did not pass the module name!"

	assert os.path.isdir(module_name) == False, "Module with same name already exists!"
	
	module_name = re.sub(r'(?<!^)(?=[A-Z])', '_', name.replace(' ', '_')).lower()
	
	print(f"Generating new {'application' if is_application else 'module'}: {module_name}")

	module_path = os.path.join(os.getcwd(), module_name)
	print(f"[1] Creating {'Application' if is_application else 'Module'} directory")
	os.mkdir(module_path)

	print(f"[2] Creating {'Application' if is_application else 'Module'} internal directories")
	os.mkdir(os.path.join(module_path, 'models'))
	os.mkdir(os.path.join(module_path, 'views'))
	os.mkdir(os.path.join(module_path, 'security'))
	os.mkdir(os.path.join(module_path, 'wizards'))

	print("[3] Creating __init__.py, __manifest__.py and __init__.py in models/ and wizards/")
	
	with open(module_path + '/__init__.py', 'w') as init_file:
		init_file.write(MAIN_INIT_FILE_CONTENTS)

	with open(module_path + '/__manifest__.py', 'w') as manifest_file:
		manifest_file.write(MANIFEST_FILE_CONTENTS.format(
			module_name=module_name.replace('_', ' ').title(), 
			author=os.getlogin(), 
			is_application=is_application)
		)

	with open(module_path + '/models/__init__.py', 'w') as models_init:
		models_init.write(f"from . import {module_name.replace(' ', '_')}\n")

	with open(module_path + f"/models/{module_name.replace(' ', '_')}.py", 'w') as models_base_file:
		models_base_file.write(f"""from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)
"""
		)

	print("[4] Creating ir.model.access.csv file in security/ folder")

	with open(module_path + f'/security/ir.model.access.csv', 'w') as security_file:
		security_file.write(SECURITY_FILE_CONTENTS)
