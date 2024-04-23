import os
import sys


def handle_generate_module(module_name, is_application):

	print(f"Generating new module: {module_name}")

	module_path = os.path.join(os.getcwd(), module_name.replace(' ', '_'))
	print("[1] Creating Module directory")
	os.mkdir(module_path)

	print("[2] Creating Module directories")
	os.mkdir(os.path.join(module_path, 'models'))
	os.mkdir(os.path.join(module_path, 'views'))
	os.mkdir(os.path.join(module_path, 'security'))
	os.mkdir(os.path.join(module_path, 'wizards'))

	print("[3] Creating __init__.py, __manifest__.py and __init__.py in models and wizards")
	main_init = '''from . import models
from . import wizards
'''
	with open(module_path + '/__init__.py', 'w') as init_file:
		init_file.write(main_init)

	with open(module_path + '/__manifest__.py', 'w') as manifest_file:
		manifest_file.write(f"""{{
	'name': '{module_name.replace('_', ' ')}',
	'version': '0.1',
	'depends': ['base'],
	'author': '{os.getlogin()}',
	'application': {is_application},
	'data': [],
}}
""")

	with open(module_path + '/models/__init__.py', 'w') as models_init:
		models_init.write(f"from . import {module_name.replace(' ', '_')}")

	with open(module_path + f"/models/{module_name.replace(' ', '_')}.py", 'w') as models_base_file:
		models_base_file.write(f"""from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)
"""
		)

	print("[4] Creating ir.model.access.csv file in security/ folder")

	with open(module_path + f'/security/ir.model.access.csv', 'w') as security_file:
		security_file.write("id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink\n")
