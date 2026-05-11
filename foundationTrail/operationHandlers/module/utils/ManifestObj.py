from typing import override

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
            depends: list[str] | None = None,
            author: str = '',
            application: bool = False,
            description: str = '',
            category: str = '',
            data: list[str] | None = None 
    ):
        self.name = name
        self.version = version
        self.depends = depends if depends else []
        self.author = author
        self.application = application
        self.description = description
        self.category = category
        self.data = data if data else []
    
    @override
    def __str__(self):
        return (
            "{\n"                                                   +
                    f"\t'name': \"{self.name}\",\n"                 +
                    f"\t'version': \"{self.version}\",\n"           +
                    f"\t'depends': \"{self.depends}\",\n"           +
                    f"\t'author': \"{self.author}\",\n"             +
                    f"\t'application': {self.application},\n"       +
                    f"\t'description': \"{self.description}\",\n"   +
                    f"\t'category': \"{self.category}\",\n"         +
            "}\n"
        )


