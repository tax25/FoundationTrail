class Sex(dict):
    def __str__(self):
        value = lambda val: val if type(val) == bool else f"'{val}'" if type(val) == str else str(val)

        initial_str = '{'
        for k, v in self.items():
            initial_str += f"\n\t'{k}': {value(v)},"
        initial_str += '\n}'
        
        return initial_str


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


with open('bullshit.json', 'w') as bullshit:
    MANIFEST_FILE_CONTENTS['name'] = 'aa'
    MANIFEST_FILE_CONTENTS['depends'] = [1, 2, 3]
    MANIFEST_FILE_CONTENTS['author'] = 'tiburzio'
    MANIFEST_FILE_CONTENTS['application'] = True
    MANIFEST_FILE_CONTENTS['description'] = "questa e' una descrizione"
    MANIFEST_FILE_CONTENTS['category'] = "questa e' una categoria"

    bullshit.write(str(Sex(MANIFEST_FILE_CONTENTS)))
