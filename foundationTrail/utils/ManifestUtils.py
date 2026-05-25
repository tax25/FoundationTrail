from ast import literal_eval
from typing import override
from os.path import isfile
import json

MANIFEST_BASE_LINE = '\"{manifest_key}\": \"{manifest_key_val}\",\n'
MANIFEST_DIRECT_VALUE_LINE = '\"{manifest_key}\": {manifest_key_val},\n'

DIRECT_VALUE_KEYS = ['depends', 'data', 'demo', 'external_dependencies']

class ManifestPathNotValid(BaseException):
    pass

class ManifestContentNotValid(BaseException):
    pass

class ManifestNameNotValued(BaseException):
    pass

class Manifest:
    name: str
    version: str
    description: str
    author: str
    website: str
    license: str
    category: str
    depends: list[str]
    data: list[str]
    demo: list[str]
    auto_install: bool
    external_dependencies: dict[str, list[str] | dict[str, str]]
    application: bool
    assets: dict[str, list[str]]
    installable: bool
    mantainer: str
    pre_init_hook: str
    post_init_hook: str
    uninstall_hook: str

    _path: str = ''

    def __init__(self,
        name: str = '',
        version: str = '0.1',
        description: str = '',
        author: str = '',
        website: str = '',
        license: str = '',
        category: str = '',
        depends: list[str] | None = None,
        data: list[str] | None = None,
        demo: list[str] | None = None, 
        auto_install: bool = False,
        external_dependencies: dict[str, list[str] | dict[str, str]] | None = None,
        application: bool = False,
        assets: dict[str, list[str]] | None = None,
        installable: bool = True,
        mantainer: str = '',
        pre_init_hook: str = '',
        post_init_hook: str = '',
        uninstall_hook: str = '',
        manifest_path: str = ''
    ):
        # NOTE: `name` is the only required field in the `__manifest__.py` file.
        if not name and not manifest_path:
            raise ManifestNameNotValued("Either value `name` or `manifest_path`")

        if manifest_path:
            self.fn_ingurgitate_manifest_value(manifest_path)
            return

        self.name = name
        self.version = version
        self.description = description
        self.author = author
        self.website = website
        self.license = license 
        self.category = category
        self.depends = depends if depends else []
        self.data = data if data else []
        self.demo = demo if demo else []
        self.auto_install = auto_install
        self.external_dependencies = external_dependencies if external_dependencies else {}
        self.application = application
        self.assets = assets if assets else {} 
        self.installable = installable
        self.mantainer = mantainer
        self.pre_init_hook = pre_init_hook
        self.post_init_hook = post_init_hook
        self.uninstall_hook = uninstall_hook
    
    def fn_ingurgitate_manifest_value(self, manifest_path: str) -> None:
        manifest_file_path = manifest_path if manifest_path else self._path
    
        if not manifest_file_path or not isfile(manifest_file_path):
            raise ManifestPathNotValid(manifest_file_path)
        
        manifest_fd = open(manifest_file_path, 'r')

        manifest_contents = manifest_fd.read()
        
        manifest_fd.close()

        if not manifest_contents or manifest_contents[0] != '{':
            raise ManifestContentNotValid()
        
        manifest_dict = literal_eval(manifest_contents) # pyright: ignore[reportAny]
        
        self.name = manifest_dict['name']
        self.version = manifest_dict.get('version', '0.1') # pyright: ignore[reportAny]
        self.description = manifest_dict.get('description', '') # pyright: ignore[reportAny]
        self.author = manifest_dict.get('author', '') # pyright: ignore[reportAny]
        self.website = manifest_dict.get('website', '') # pyright: ignore[reportAny]
        self.license = manifest_dict.get('license', '') # pyright: ignore[reportAny]
        self.category = manifest_dict.get('category', '') # pyright: ignore[reportAny]
        self.depends =  manifest_dict.get('depends', []) # pyright: ignore[reportAny]
        self.data = manifest_dict.get('data', []) # pyright: ignore[reportAny]
        self.demo = manifest_dict.get('demo', []) # pyright: ignore[reportAny]
        self.auto_install = manifest_dict.get('auto_install', False) # pyright: ignore[reportAny]
        self.external_dependencies = manifest_dict.get('external_dependencies', {})  # pyright: ignore[reportAny]
        self.application = manifest_dict.get('application', False) # pyright: ignore[reportAny]
        self.assets = manifest_dict.get('assets', {})  # pyright: ignore[reportAny]
        self.installable = manifest_dict.get('installable', True) # pyright: ignore[reportAny]
        self.mantainer = manifest_dict.get('mantainer', '') # pyright: ignore[reportAny]
        self.pre_init_hook = manifest_dict.get('pre_init_hook', '') # pyright: ignore[reportAny]
        self.post_init_hook = manifest_dict.get('post_init_hook', '') # pyright: ignore[reportAny]
        self.uninstall_hook = manifest_dict.get('uninstall_hook', '') # pyright: ignore[reportAny]

    def fn_manifest_to_pretty_string(self):
        manifest_dict = {}
        for prop in self.__dict__.items():
            if prop[0].startswith('_') or prop[0].startswith('fn_') or (not prop[1] and not type(prop[1]) == bool): # pyright: ignore[reportAny]
                continue

            manifest_dict[prop[0]] = prop[1]

        return json.dumps(manifest_dict, indent=4).replace('true', 'True').replace('false', 'False')

    @override
    def __str__(self) -> str:
        manifest_string = "{\n"
        
        for prop in self.__dict__.items():
            if prop[0].startswith('_') or prop[0].startswith('fn_') or not prop[1]:
                continue

            if prop[0] in DIRECT_VALUE_KEYS:
                manifest_string += MANIFEST_DIRECT_VALUE_LINE.format(manifest_key=prop[0], manifest_key_val=prop[1]) # pyright: ignore[reportAny]
            else:
                manifest_string += MANIFEST_BASE_LINE.format(manifest_key=prop[0], manifest_key_val=prop[1]) # pyright: ignore[reportAny]

        manifest_string += "}"
        
        return manifest_string

if __name__ == '__main__':
    # NOTE: testing the class
    my_manifest = Manifest(
        name='my_module_name',
        version='0.2',
        description="this is the description",
        author='your author',
        website='https://yourwebsite.com/',
        license='LGPL-3',
        category='this is the category',
        depends=['aa', 'bb'],
        demo=['daa', 'dbb'],
        auto_install=True,
        external_dependencies={
            'python': ['python-ldap'],
            'apt': {
                'python-ldap': 'python3-ldap'
            }
        },
        application=True,
        assets={
            'assets': ['aaa']
        },
        installable=False,
        mantainer='sos',
        pre_init_hook='your_init_hook',
        post_init_hook='your_post_init_hook',
        uninstall_hook='your_uninstall_hook'
    )
    
    print("manifest value: ", my_manifest.fn_manifest_to_pretty_string())
