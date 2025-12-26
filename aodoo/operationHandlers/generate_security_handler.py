import os
import platform

def _get_end_directory():

	match platform.system():
		case 'Darwin':
			return f'/Users/{os.getlogin()}'
		case 'Linux':
			return '/home'

MANIFEST_FILENAME = '__manifest__.py'
END_DIRECTORY = _get_end_directory()

def handle_generate_security(
	security_file_name: str,
	line_id: str,
	model_id: str,
	group_id: str,
	perm_read: bool,
	perm_write: bool,
	perm_create: bool,
	perm_unlink: bool
) -> None:

	# trovare la directory `security`
	# trovare `ir.model.access.csv`
	# eventualmente creare il file
	# aggiungere la nuova linea

	print("handle generate security")

	security_file_name = f"security/{security_file_name if security_file_name else 'ir.model.access.csv'}"
	file_name_and_path = ''

	if 'security' in os.getcwd():
		file_name_and_path = os.getcwd() + '/' + security_file_name.replace('.csv', '') + '.csv'
	elif os.path.exists(os.getcwd() + '/security'):
		file_name_and_path = os.getcwd() + f"/security/{security_file_name if security_file_name else 'ir.model.access.csv'}"
	elif os.path.exists(os.getcwd() + f'/../security'):
		file_name_and_path = os.getcwd() + f"/../security/{security_file_name if security_file_name else 'ir.model.access.csv'}"
	else:
		print(f"Cannot find /security directory so creating the file in the current directory ({os.getcwd()})")
		file_name = security_file_name if security_file_name else 'ir.model.access.csv'


