from platform import system
from os import getcwd, chdir, getlogin, curdir
from os.path import (
    abspath as absolute_path,
    exists as path_exists,
    isfile,
)

from foundationTrail.utils.ManifestUtils import Manifest, ManifestContentNotValid
from foundationTrail.operationHandlers.view.constants import (
    INHERIT_ID_TMPLT,
    VIEW_FILE_TMPLT,
    MANIFEST_FILENAME,
    
    INFO_VIEW_FILE_CREATED,

    ERR_VIEW_DIRECTORY_NOT_FOUND,
    ERR_MANIFEST_FILE_NOT_FOUND,
    ERR_MANIFEST_VALUE_NOT_VALID
)

def _get_end_directory():

    match system():
        case 'Darwin':
            return f'/Users/{getlogin()}'
        case 'Linux':
            return '/home'
        case _:
            raise Exception("unknown system")

def handle_generate_view(
    view_name: str,
    model: str,
    inherit_id: str,
    is_for_wizard: bool
):
    
    view_directory = 'views' if not is_for_wizard else 'wizards'
    
    view_file_name = f'{view_name}.xml'
    
    # NOTE: `file_name_and_dir` used in __manifest__.py
    file_name_and_dir = \
            f"{view_directory}/{view_name}.xml"

    file_name_and_path = ''

    if view_directory in getcwd():
        file_name_and_path = getcwd() + '/' + view_file_name 
    elif path_exists(getcwd() + '/' + view_directory):
        file_name_and_path = getcwd() + '/' + file_name_and_dir
    elif path_exists(getcwd() + '/../' + view_file_name):
        file_name_and_path = getcwd() + '/../' + file_name_and_dir 
    else:
        print(ERR_VIEW_DIRECTORY_NOT_FOUND.format(
                view_directory=view_directory,
                current_directory=getcwd()
            )
        )
        file_name_and_dir = view_file_name
        file_name_and_path = getcwd() + '/' + view_file_name
    
    with open(file_name_and_path, 'w') as view_file:
        _ = view_file.write(
            VIEW_FILE_TMPLT.format(
                view_name=view_name,
                name=view_name.replace('_', '.'),
                model=model.replace('_', '.'),
                inherit_id_string=INHERIT_ID_TMPLT.format(
                    inherited_view=inherit_id if inherit_id else ''
                )
            )
        )
    
    manifest_file_path = ''
    if not isfile(MANIFEST_FILENAME):
        chdir('..')
        while True:
            if not isfile(MANIFEST_FILENAME):
                chdir('..')
            else:
                manifest_file_path = absolute_path(curdir) + '/' + MANIFEST_FILENAME
                break 

            if absolute_path(curdir) == _get_end_directory():
                print(ERR_MANIFEST_FILE_NOT_FOUND.format(view_generation_dir=file_name_and_dir))
                return
    else:
        manifest_file_path = absolute_path(curdir) + '/' + MANIFEST_FILENAME
    
    try:
        manifest_obj = Manifest(manifest_path=manifest_file_path)
    except ManifestContentNotValid:
        print(ERR_MANIFEST_VALUE_NOT_VALID)
        return

    if file_name_and_dir not in manifest_obj.data:
        manifest_obj.data.append(file_name_and_dir)

    with open(manifest_file_path, 'w') as manifest_file:
        _ = manifest_file.seek(0)

        _ = manifest_file.write(manifest_obj.fn_manifest_to_pretty_string())

        _ = manifest_file.truncate()

        print(INFO_VIEW_FILE_CREATED.format(file_name=file_name_and_dir))


