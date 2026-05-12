from typing import override


class FTArguments:
    help: bool = False
    version: bool = False
    interactive: bool = False
    explain: str = ""

    generate: bool = False

    module: bool = False
    app: bool = False
    deps: str = ""
    author: str = ""
    m_version: str = ""
    description: str = ""
    category: str = ""

    model: bool = False
    model_type: str = ""
    inherit: str = ""
    wizard: bool = False
    m_perms: str = ""

    view: bool = False
    view_model: str = ""
    wizard_view: bool = False
    inherit_view: str = ""

    security: bool = False
    line_id: str = ""
    line_name: str = ""
    model_id: str = ""
    group_id: str = ""
    perm_read: bool = False
    perm_write: bool = False
    perm_create: bool = False
    perm_unlink: bool = False
    
    @override
    def __str__(self):
        str_to_return = f"""
            {{
                version: {self.version},
                interactive: {self.interactive},
                explain: {self.explain},
                generate: {self.generate},
                module: {self.module},
                app: {self.app},
                deps: {self.deps},
                author: {self.author},
                m_version: {self.m_version},
                description: {self.description},
                category: {self.category},
                model: {self.model},
                model_type: {self.model_type},
                inherit: {self.inherit},
                wizard: {self.wizard},
                m_perms: {self.m_perms},
                view: {self.view},
                view_model: {self.view_model},
                inherit_view: {self.inherit_view},
                security: {self.security},
                line_id: {self.line_id},
                line_name: {self.line_name},
                model_id: {self.model_id},
                group_id: {self.group_id},
                perm_read: {self.perm_read},
                perm_write: {self.perm_write},
                perm_create: {self.perm_create},
                perm_unlink: {self.perm_unlink},
            }}
        """
    
        return str_to_return
