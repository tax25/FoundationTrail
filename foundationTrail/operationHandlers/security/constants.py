MANIFEST_FILE_NAME_TMPLT = 'security/{name}'

MANIFEST_FILENAME = '__manifest__.py'

SECURITY_FILE_HEADER = 'id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink\n'

SECURITY_FILE_CONTENTS = "\n{line_id},{line_name},{model_id},{group_id},{perm_read},{perm_write},{perm_create},{perm_unlink}\n"

INFO_SECURITY_FILE_CREATED = 'Security file created successfully.'

ERR_SEC_FILE_NOT_FOUND = "Cannot find /security directory, so creating the file in the current directory ({currentWD})."

ERR_MANIFEST_FILE_NOT_FOUND = "ERROR: {manifest_file} file not found! Security file generated, but not added to the {manifest_file}."

ERR_MANIFEST_EMPTY_OR_NOT_VALID = "ERROR: Manifest file empty or not valid!"
