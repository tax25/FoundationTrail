from dataclasses import dataclass

@dataclass
class InteractiveProp:
    prop_name: str
    prop_type: type
    is_optional: bool
    allowed_vals: list[str]
    query_msg: str
