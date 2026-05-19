from foundationTrail.utils.InteractiveModeUtils import InteractiveProp

MODEL_NAME_MSG = 'Please specify the model name'
MODEL_TYPE_MSG = 'Please specify the model type'
IS_WIZARD_MSG = 'Is this model for a wizard?'
INHERIT_MODEL_MSG = 'Please specify the model this new model has to inherit from'
FILE_NAME_MSG = "Please specify the file name you'd like the model to be created in"
CLI_PERMS_MSG = 'Please specify the permissions for the model to be created'

INTERACTIVE_CONFIG: list[InteractiveProp] = [
    InteractiveProp('name', str, False, None, MODEL_NAME_MSG),
    InteractiveProp('chosen_type', str, False, None, MODEL_TYPE_MSG),
    InteractiveProp('is_wizard', str, False, None, IS_WIZARD_MSG),
    InteractiveProp('inherit', str, True, None, INHERIT_MODEL_MSG),
    InteractiveProp('file_name', str, True, None, FILE_NAME_MSG),
    InteractiveProp('name', str, True, None, CLI_PERMS_MSG), 
]
