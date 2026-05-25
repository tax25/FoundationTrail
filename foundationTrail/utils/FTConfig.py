from os.path import expanduser, isfile
from tomllib import load as load_toml
from typing import override

FT_CONFIG_FILE_PATH = '~/.config/FoundationTrail/config.toml'
CONFIGURATION_LABEL = 'configuration'
OPTIONS_LABEL = 'options'

ERR_ODOO_CONF_PATH_NON_EXISTENT = "The path specified for the Odoo configuration file ('{path}') is *non* existent."
ERR_ODOO_CONF_FILE_NOT_VALID = 'The contents of the configuration file specified make up for an invalid configuration.'

class OdooConfPathNonExistentError(BaseException):
    pass

class OdooConfFileNotValid(BaseException):
    pass

class FTConfig:
    conf_odoo_conf_path: str = ''
    conf_odoo_conf: OdooConf

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
            self.conf_odoo_conf = OdooConf(tmp_odoo_conf_path)

    @override
    def __str__(self) -> str:
        str_to_return = f"""
            {{
                conf_odoo_conf_path = {self.conf_odoo_conf_path}
            }}
        """

        return str_to_return

class OdooConf:
    addon_paths: list[str]

    def __init__(self, conf_path: str):
        if not isfile(conf_path):
            raise OdooConfPathNonExistentError(ERR_ODOO_CONF_PATH_NON_EXISTENT.format(path=conf_path))

        with open(conf_path, 'rb') as conf_file:
            conf_values = load_toml(conf_file)
            if OPTIONS_LABEL not in conf_values:
                raise OdooConfFileNotValid(ERR_ODOO_CONF_FILE_NOT_VALID)

            addons_path: str = conf_values['options'].get('addons_path', '') # pyright: ignore[reportAny]
            addons_paths: list[str] = addons_path.split(',')

            self.addon_paths = addons_paths
