from os.path import expanduser, isfile
from tomllib import load as load_toml
from typing import override
# from re import search as regex_search


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
    addon_paths: list[str] = []
    
    def __init__(self, conf_path: str):
        if not isfile(conf_path):
            raise OdooConfPathNonExistentError(ERR_ODOO_CONF_PATH_NON_EXISTENT.format(path=conf_path))
        
        with open(conf_path, 'r') as conf_file:
            for config_line in conf_file:

                if config_line.startswith(';') or       \
                        config_line.startswith('\n') or \
                        config_line.startswith('['):
                    # If we enter this if statement, it means that the line is either:
                    # 1. a comment
                    # 2. blank
                    # 3. a section specifier (which we don't handle at the moment)
                    continue
                
                if not '=' in config_line and not config_line.startswith('['):
                    raise OdooConfFileNotValid(ERR_ODOO_CONF_FILE_NOT_VALID)

                config_line_name, config_line_value = config_line.split('=')
                
                self._process_config_line_val(config_line_name.strip(), config_line_value)
                
    def _process_config_line_val(self, line_name: str, line_val: str) -> None:
        match line_name:
            case 'addon_paths':
                # NOTE: should we check if the directories exist?
                tmp = line_val.replace('\n', '').split(',')
                for index, path in enumerate(tmp):
                    tmp[index] = path.strip()

                self.addon_paths = tmp

            case _:
                # TODO: handle the case in which the line_name is not recognized
                # (print a warning?)
                pass


if __name__ == '__main__':
    my_config: FTConfig = FTConfig()
    print(my_config.conf_odoo_conf.addon_paths)
