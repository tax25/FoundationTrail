from typing import override
from os import chdir, curdir
from os.path import isfile, abspath as absolute_path

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
            manifest_filename: str = '__manifest__.py',
            stop_dir: str = '',
            name: str = '',
            version: str = '0.1',
            depends: list[str] | None = None,
            author: str = '',
            application: bool = False,
            description: str = '',
            category: str = '',
            data: list[str] | None = None 
    ):
        self.path: str = self._get_manifest_path(manifest_filename, stop_dir)
        self.name = name
        self.version = version
        self.depends = depends if depends else []
        self.author = author
        self.application = application
        self.description = description
        self.category = category
        self.data = data if data else []
    
    def _get_manifest_path(
            self, 
            manifest_fname: str,
            stop_dir: str
        ) -> str:
        if isfile(manifest_fname):
            return manifest_fname
        
        chdir('..')
        while True:
            if isfile(manifest_fname):
                return absolute_path(curdir)
            if absolute_path(curdir) == stop_dir:
                return ''
    
    @override
    def __str__(self):
        return (
            "{\n"                                                   +
                    f"\t'name': \"{self.name}\",\n"                 +
                    f"\t'version': \"{self.version}\",\n"           +
                    f"\t'depends': {self.depends},\n"               +
                    f"\t'author': \"{self.author}\",\n"             +
                    f"\t'application': {self.application},\n"       +
                    f"\t'description': \"{self.description}\",\n"   +
                    f"\t'category': \"{self.category}\",\n"         +
                    f"\t'data': \"{self.data}\",\n"                 +
            "}\n"
        )


