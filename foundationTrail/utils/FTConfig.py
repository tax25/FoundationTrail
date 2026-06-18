from os.path import expanduser, isfile
from tomllib import load as load_toml
from typing import override
from re import search as regex_search


FT_CONFIG_FILE_PATH = '~/.config/FoundationTrail/config.toml'
CONFIGURATION_LABEL = 'configuration'
OPTIONS_LABEL = 'options'

ERR_ODOO_CONF_PATH_NON_EXISTENT = "The path specified for the Odoo configuration file ('{path}') is *non* existent."
ERR_ODOO_CONF_FILE_NOT_VALID = 'The contents of the configuration file specified make up for an invalid configuration.'

SECTION_NAME_REGEX = r'^\[([a-zA-Z_-]+)\]$'

class OdooConfPathNonExistentError(BaseException):
    pass

class OdooConfFileNotValid(BaseException):
    pass

class FTConfig:
    # TODO: review naming convention.
    # This already looks confusing.
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
        
        with open(conf_path, 'r') as conf_file:
            config_dict: dict[str, dict[str, str]] = {}
            current_section: str = ""

            for config_line in conf_file:
                
                if config_line.startswith(';'):
                    # Then it means it is a comment, and should **not** be considered.
                    continue
                if config_line.startswith('['):
                    if new_section_name := regex_search(SECTION_NAME_REGEX, config_line.strip()):
                        current_section = new_section_name.group(1)
                        # NOTE: once we get the new section, we go on, as there
                        # are no actual values in this line.
                        continue

                if not '=' in config_line and not config_line.startswith('['):
                    raise OdooConfFileNotValid(ERR_ODOO_CONF_FILE_NOT_VALID)

                config_line_name, config_line_value = config_line.split('=')
                
                if not current_section in config_dict:
                    config_dict[current_section] = {
                        config_line_name.strip(): config_line_value
                    }
                else:
                    config_dict[current_section][config_line_name.strip()] = config_line_value

            print(config_dict) 


if __name__ == '__main__':
    my_config: FTConfig = FTConfig()
