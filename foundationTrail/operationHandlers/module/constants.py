from dataclasses import dataclass
# MISCELLANEOUS

MAIN_INIT_FILE_CONTENTS = \
'from . import models\n'
'from . import wizards\n'

MANIFEST_FILE_CONTENTS = {
    'name': '',
    'version': '0.1',
    'depends': [],
    'author': '',
    'application': False,
    'description': '',
    'category': '',
    'data': ['security/ir.model.access.csv'],
}

class ManifestObj:
    name: str
    version: str
    depends: list[str]
    author: str
    application: bool
    description: str
    category: str
    data: list[str]
    
    def __init__(
            self, 
            name: str = '',
            version: str = '0.1',
            depends: list[str] = [],
            author: str = '',
            application: bool = False,
            description: str = '',
            category: str = '',
            data: list[str] = ''
    ):
        self.name = name
        self.version = version
        self.depends = depends
        self.author = author
        self.application = application
        self.description = description
        self.category = category
        self.data = data
    
    def __str__(self):
        return \
        "{\n"                                                 \
                f"\t'name': '{self.name}',\n"                 \
                f"\t'version': '{self.version}',\n"           \
                f"\t'depends': '{self.depends}',\n"           \
                f"\t'author': '{self.author}',\n"             \
                f"\t'application': {self.application},\n"     \
                f"\t'description': '{self.description}',\n"   \
                f"\t'category': '{self.category}',\n"         \
        "}\n"


BASE_MODEL_FILE_CONTENTS = \
'''from odoo import api, fields, models

import logging
_logger = logging.getLogger(__name__)
'''

SECURITY_FILE_CONTENTS = \
        'id,name,model_id:id,group_id:id,perm_read,perm_write,perm_create,perm_unlink\n'

# INFO

INFO_GENERATING_APPLICATION = "Generating {resource}: {resource_name}..."
