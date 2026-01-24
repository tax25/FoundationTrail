import os
import json
import platform

def _get_end_directory():

	match platform.system():
		case 'Darwin':
			return f'/Users/{os.getlogin()}'
		case 'Linux':
			return '/home'

MANIFEST_FILENAME = '__manifest__.py'
END_DIRECTORY = _get_end_directory()

SECURITY_FILE_HEADER = 'id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink\n'
SECURITY_FILE_CONTENTS = "\n{line_id},{line_name},{model_id},{group_id},{perm_read},{perm_write},{perm_create},{perm_unlink}\n"

GENERATE_SECURITY_PARAMETERS = [
    {
        'property_name': 'security_file_name',
        'property_type': str,
        'property_is_optional': True,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': "Please specify the file name you'd like the security configuration to be saved in"
    },
    {
        'property_name': 'line_id',
        'property_type': str,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the line id for this security configuration'
    },
    {
        'property_name': 'line_name',
        'property_type': str,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the line name for this security configuration'
    },
    {
        'property_name': 'model_id',
        'property_type': str,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the model id for this security configuration'
    },
    {
        'property_name': 'group_id',
        'property_type': str,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the group id for this security configuration'
    },
    {
        'property_name': 'perm_read',
        'property_type': bool,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the read permissions for this security configuration'
    },
    {
        'property_name': 'perm_write',
        'property_type': bool,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the write permissions for this security configuration'
    },
    {
        'property_name': 'perm_create',
        'property_type': bool,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the create permissions for this security configuration'
    },
    {
        'property_name': 'perm_unlink',
        'property_type': bool,
        'property_is_optional': False,
        'property_allowed_vals': None,
        'property_ask_for_val_msg': 'Please specify the unlink permissions for this security configuration'
    },
]

def handle_generate_security(
	security_file_name: str,
	line_id: str,
	line_name: str,
	model_id: str,
	group_id: str,
	perm_read: bool,
	perm_write: bool,
	perm_create: bool,
	perm_unlink: bool,
) -> None:
	# NOTE: `file_name` is used in the `__manifest__.py`.
	file_name = f"security/{security_file_name if security_file_name else 'ir.model.access.csv'}"
	file_name_and_path = ''

	if 'security' in os.getcwd():
		file_name_and_path = os.getcwd() + '/' + security_file_name.replace('.csv', '') + '.csv'
	elif os.path.exists(os.getcwd() + '/security'):
		file_name_and_path = os.getcwd() + f"/security/{security_file_name if security_file_name else 'ir.model.access.csv'}"
	elif os.path.exists(os.getcwd() + '/../security'):
		file_name_and_path = os.getcwd() + f"/../security/{security_file_name if security_file_name else 'ir.model.access.csv'}"
	else:
		print(f"Cannot find /security directory so creating the file in the current directory ({os.getcwd()})")
		file_name = security_file_name if security_file_name else 'ir.model.access.csv'

	if os.path.isfile(file_name_and_path):
		with open(file_name_and_path, 'a') as new_security_file:
			new_security_file.write(
				SECURITY_FILE_CONTENTS.format(
					line_id=line_id,
					line_name=line_name,
					model_id=f"model_{model_id.replace('model_', '')}",
					group_id=group_id if group_id else '',
					perm_read=int(perm_read),
					perm_write=int(perm_write),
					perm_create=int(perm_create),
					perm_unlink=int(perm_unlink),
				)
			)

	else:
		with open(file_name_and_path, 'w') as existing_security_file:
			existing_security_file.write(SECURITY_FILE_HEADER)
			existing_security_file.write(
				SECURITY_FILE_CONTENTS.format(
					line_id=line_id,
					line_name=line_name,
					model_id=f"model_{model_id.replace('model_', '')}",
					group_id=group_id,
					perm_read=int(perm_read),
					perm_write=int(perm_write),
					perm_create=int(perm_create),
					perm_unlink=int(perm_unlink),
				)
			)

	manifest_file_path = ''
	if not os.path.isfile(MANIFEST_FILENAME):
		os.chdir('..')
		while True:
			if not os.path.isfile(MANIFEST_FILENAME):
				os.chdir('..')
			else:
				manifest_file_path = os.path.abspath(os.curdir)
				break
			if os.path.abspath(os.curdir) == END_DIRECTORY:
				print(f"ERROR: {MANIFEST_FILENAME} file not found! Security file generated, but not added to the {MANIFEST_FILENAME}.")
				return

	with open(
		manifest_file_path + f'/{MANIFEST_FILENAME}' if manifest_file_path else MANIFEST_FILENAME,
		 'r+'
		) as manifest:
		manifest_content = manifest.read()

		if not manifest_content or manifest_content[0] != '{':
			raise Exception(f"ERROR: {MANIFEST_FILENAME} is empty or not valid!")

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

		print(f"Security file created and added to the {MANIFEST_FILENAME} file as {security_file_name}")
