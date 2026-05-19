class InteractiveProp:
    prop_name: str
    prop_type: type
    is_optional: bool
    allowed_vals: list[str]
    query_msg: str
    
    def __init__(self,
        name: str = '',
        specified_type: type = str,
        optional: bool = False,
        allowed_vals: list[str] | None = None,
        msg: str = ""
    ):
        self.prop_name = name
        self.prop_type = specified_type
        self.is_optional = optional
        self.allowed_vals = allowed_vals if allowed_vals else []
        self.query_msg = msg
