from os import getcwd
from os.path import exists as path_exists

from foundationTrail.operationHandlers.view.constants import (
    INHERIT_ID_TMPLT,
    VIEW_FILE_TMPLT,
    ERR_VIEW_DIRECTORY_NOT_FOUND
)

def handle_generate_view(
    view_name: str,
    model: str,
    inherit_id: str,
    is_for_wizard: bool
):
    
    view_directory = 'views' if not is_for_wizard else 'wizards'
    
    view_file_name = f'{view_name}.xml'

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
    
    # with open(file_name_and_path, 'w') as view_file:
        
