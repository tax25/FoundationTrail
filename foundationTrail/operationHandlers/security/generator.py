from os import getcwd, curdir, getlogin, chdir
from os.path import (
    abspath as absolute_path,
    exists as path_exists,
    isfile
)

import platform

from foundationTrail.utils.ManifestUtils import Manifest, ManifestContentNotValid

from foundationTrail.operationHandlers.security.constants import (
        SECURITY_FILE_NAME_FOR_MANIFEST_TMPLT,
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
            return f'/Users/{getlogin()}'
        case 'Linux':
            return f'/home/{getlogin()}'
        case _:
            return '/'

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
    security_file_name_for_manifest = SECURITY_FILE_NAME_FOR_MANIFEST_TMPLT.format(
        name=security_file_name.replace('.csv', '')
    )

    file_name_and_path = ''
    if 'security' in getcwd():
        file_name_and_path = f'{getcwd()}/{security_file_name}.csv'
    elif path_exists(f'{getcwd()}/security'):
        file_name_and_path = f'{getcwd()}/security/{security_file_name}.csv'
    elif path_exists(f'{getcwd()}/../security') and isfile(f'{getcwd()}/../security/{security_file_name}.csv'):
        file_name_and_path = f'{getcwd()}/../security/{security_file_name}.csv'
    else:
        print(ERR_SEC_FILE_NOT_FOUND.format(currentWD=getcwd()))
        file_name_and_path = security_file_name

    sec_file_exists = isfile(file_name_and_path)

    with open(file_name_and_path, 'a' if sec_file_exists else 'w') as security_file:
        if not sec_file_exists:
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
    if not isfile(MANIFEST_FILENAME):
        chdir('..')
        while True:
            if not isfile(MANIFEST_FILENAME):
                chdir('..')
            else:
                manifest_file_path = absolute_path(curdir)
                break
            if absolute_path(curdir) == _get_end_directory():
                print(
                    ERR_MANIFEST_FILE_NOT_FOUND.format(
                        manifest_file=MANIFEST_FILENAME
                    )
                )
                return
    else:
        manifest_file_path = absolute_path(curdir)

    try:
        manifest_obj = Manifest(manifest_path=f'{manifest_file_path}/{MANIFEST_FILENAME}')
    except ManifestContentNotValid:
        print(ERR_MANIFEST_EMPTY_OR_NOT_VALID)
        return
    
    if security_file_name_for_manifest not in manifest_obj.data:
        manifest_obj.data.append(security_file_name_for_manifest)

        with open(f'{manifest_file_path}/{MANIFEST_FILENAME}', 'r+') as manifest_file:
            _ = manifest_file.seek(0)

            _ = manifest_file.write(manifest_obj.fn_manifest_to_pretty_string())

            _ = manifest_file.truncate()

    print(INFO_SECURITY_FILE_CREATED)
