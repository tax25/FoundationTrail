from os.path import expanduser, isfile
from tomllib import load as load_toml
from typing import override

FT_CONFIG_FILE_PATH = '~/.config/FoundationTrail/config.toml'
CONFIGURATION_LABEL = 'configuration'

ERR_ODOO_CONF_PATH_NON_EXISTENT = "The path specified for the Odoo configuration file ('{path}') is *non* existent."

class OdooConfPathNonExistentError(BaseException):
    pass

class FTConfig:
    conf_odoo_conf_path: str = ''

    def __init__(self):
        configuration_file_path = expanduser(FT_CONFIG_FILE_PATH)
        # NOTE: if not isfile(...) => user has not created the configuration file in the 
        # expected path (or has not created a configuration file at all), thus we skip.
        if not isfile(configuration_file_path):
            return

        with open(configuration_file_path, 'rb') as toml_config:
            toml_values = load_toml(toml_config)

            if CONFIGURATION_LABEL not in toml_values:
                return

            tmp_odoo_conf_path: str = toml_values['configuration'].get('odoo-conf-path', '') # pyright: ignore[reportAny]
            if not isfile(tmp_odoo_conf_path):
                raise OdooConfPathNonExistentError(ERR_ODOO_CONF_PATH_NON_EXISTENT.format(path=tmp_odoo_conf_path))

            self.conf_odoo_conf_path = tmp_odoo_conf_path

    @override
    def __str__(self) -> str:
        str_to_return = f"""
            {{
                conf_odoo_conf_path = {self.conf_odoo_conf_path}
            }}
        """

        return str_to_return

