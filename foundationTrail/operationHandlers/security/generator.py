import os
import json
import platform

from foundationTrail.operationHandlers.security.constants import (
        MANIFEST_FILE_NAME_TMPLT,
        MANIFEST_FILENAME,
        SECURITY_FILE_HEADER,
        SECURITY_FILE_CONTENTS,

        INFO_SECURITY_FILE_CREATED,

        ERR_SEC_FILE_NOT_FOUND,
        ERR_MANIFEST_FILE_NOT_FOUND,
        ERR_MANIFEST_EMPTY_OR_NOT_VALID,
)

def _get_end_directory():
    match platform.system():
        case 'Darwin':
            return f'/Users/{os.getlogin()}'
        case 'Linux':
            return f'/home/{os.getlogin()}'
        case _:
            return 'lmao'

def handle_generate_security(
    security_file_name: str,
    line_id: str,
    line_name: str,
    model_id: str,
	group_id: str,
	perm_read: int,
	perm_write: int,
	perm_create: int,
	perm_unlink: int,
):
    manifest_file_name = MANIFEST_FILE_NAME_TMPLT.format(
        name=security_file_name
    )

    file_name_and_path = ''
    if 'security' in os.getcwd():
        file_name_and_path = f'{os.getcwd()}/{security_file_name}.csv'
    elif os.path.exists(f'{os.getcwd()}/security'):
        file_name_and_path = f'{os.getcwd()}/security/{security_file_name}.csv'
    elif os.path.exists(f'{os.getcwd()}/../security') and os.path.isfile(f'{os.getcwd()}/../security/{security_file_name}.csv'):
        file_name_and_path = f'{os.getcwd()}/../security/{security_file_name}.csv'
    else:
        print(ERR_SEC_FILE_NOT_FOUND.format(currentWD=os.getcwd()))
        file_name_and_path = security_file_name

    has_to_create_sec_file = os.path.isfile(file_name_and_path)
    
    with open(file_name_and_path, 'w' if has_to_create_sec_file else 'a') as security_file:
        if has_to_create_sec_file:
            _ = security_file.write(SECURITY_FILE_HEADER)
            _ = security_file.write(
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
    
    manifest_file_path = '.'
    if not os.path.isfile(MANIFEST_FILENAME):
        os.chdir('..')
        while True:
            if not os.path.isfile(MANIFEST_FILENAME):
                os.chdir('..')
            else:
                manifest_file_path = os.path.abspath(os.curdir)
                break
            if os.path.abspath(os.curdir) == _get_end_directory():
                print(
                    ERR_MANIFEST_FILE_NOT_FOUND.format(
                        manifest_file=MANIFEST_FILENAME
                    )
                )
                return
    
    with open(f'{manifest_file_path}/{MANIFEST_FILENAME}', 'r+') as manifest_file:
        manifest_content = manifest_file.read()
        if not manifest_content or manifest_content[0] != '{':
            raise Exception(ERR_MANIFEST_EMPTY_OR_NOT_VALID)
    
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

        manifest_dict['data'].append(manifest_file_name)

        _ = manifest_file.seek(0)

        _ = manifest_file.write(json.dumps(manifest_dict, indent=4).replace('true', 'True').replace('false', 'False'))

        manifest_file.truncate()

        print(INFO_SECURITY_FILE_CREATED)
