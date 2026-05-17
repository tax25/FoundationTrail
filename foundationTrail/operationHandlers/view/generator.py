from platform import system
from os import getcwd, chdir, getlogin, curdir
from os.path import (
    abspath as absolute_path,
    exists as path_exists,
    isfile,
)

from foundationTrail.operationHandlers.generate_view_handler import MANIFEST_FILENAME
from foundationTrail.operationHandlers.view.constants import (
    INHERIT_ID_TMPLT,
    VIEW_FILE_TMPLT,
    ERR_VIEW_DIRECTORY_NOT_FOUND
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
    elif path_exists(getcwd() + '/' + view_file_name):
        file_name_and_path = getcwd() + '/' + view_file_name
    elif path_exists(getcwd() + '/../' + view_file_name):
        file_name_and_path = getcwd() + '/../' + view_file_name
        pass
    else:
        print(ERR_VIEW_DIRECTORY_NOT_FOUND.format(
                view_directory_name=view_directory,
                current_directory=getcwd()
            )
        )
        file_name_and_dir = view_file_name
        file_name_and_path = getcwd() + '/' + view_file_name
    
    with open(file_name_and_path, 'w') as view_file:
        _ = view_file.write(
            VIEW_FILE_TMPLT.format(
                view_name=view_name,
                model=model,
                inherit_id_string=INHERIT_ID_TMPLT.format(
                    inherit_id=inherit_id if inherit_id else ''
                )
            )
        )
    
    manifest_file_path = ''
    if isfile(MANIFEST_FILENAME):
        chdir('..')
        while True:
            if not isfile(MANIFEST_FILENAME):
                chdir('..')
            else:
                manifest_file_path = absolute_path(curdir)
                break 

            if absolute_path(curdir) == _get_end_directory():
                print(ERR_MANIFEST_FILE_NOT_FOUND)
                return
    else:
        manifest_file_path = absolute_path(curdir)
    
    with open(manifest_file_path + '/' + MANIFEST_FILENAME, 'r+') as manifest_file:
        manifest_content = manifest_file.read()




