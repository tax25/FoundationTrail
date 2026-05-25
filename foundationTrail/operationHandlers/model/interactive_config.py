from foundationTrail.utils.InteractiveModeUtils import InteractiveProp

MODEL_NAME_MSG = 'Please specify the model name'
MODEL_TYPE_MSG = 'Please specify the model type'
IS_WIZARD_MSG = 'Is this model for a wizard?'
INHERIT_MODEL_MSG = 'Please specify the model this new model has to inherit from'
FILE_NAME_MSG = \
        "Please specify the file name you'd like the model to be created in"
CLI_PERMS_MSG = 'Please specify the permissions for the model to be created'

INTERACTIVE_CONFIG: list[InteractiveProp] = [
    InteractiveProp('name', str, False, [], MODEL_NAME_MSG),
    InteractiveProp('filename', str, True, [], FILE_NAME_MSG),
    InteractiveProp('model_type', str, False, [], MODEL_TYPE_MSG),
    InteractiveProp('inherit', str, True, [], INHERIT_MODEL_MSG),
    InteractiveProp('wizard', bool, False, [], IS_WIZARD_MSG),
    InteractiveProp('m_perms', str, True, [], CLI_PERMS_MSG), 
]
