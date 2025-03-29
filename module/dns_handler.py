# from service import DNSService
import json
import os
import shutil
import logging
logger = logging.getLogger(os.getenv('APP_LOG_NAME'))

class DnsHandler:
    
    def __init__(self):
        
        self.DEFAULT_CONF:dict = {
            'shecan': {
                'nameserver1': '178.22.122.100',
                'nameserver2': '185.51.200.2'
            }
        }
        
        # Env variables
        self.DEFAULT_DNS_CONF_FILE_PATH = os.getenv('DUMMY_DEFAULT_DNS_CONF_FILE_PATH')    # By default it is located at /etc/resolv.conf
        self.SYSTEM_RESOLV_CONF_FILE_PATH = os.getenv('DUMMY_SYSTEM_DNS_CONF_FILE_PATH')    # By default it is located at /etc/dummy-dns/default.conf
        self.DNS_SERVER_CONFIG_PATH = os.getenv('DUMMY_DNS_SERVERS_CONFIG_PATH')       # By default it is located at /etc/dummy-dns/config.json
        
        self.dns_servers_config:dict = None # It will be initialized when needs 
        
    # Reset resolv.conf file into system default
    def reset_dns(self) -> None:    
        shutil.copy(self.DEFAULT_DNS_CONF_FILE_PATH, self.SYSTEM_RESOLV_CONF_FILE_PATH)
    
    # Save resolv.conf file as default conf file in /etc/dummy-dns  
    def force_save_conf(self) -> None:        
        shutil.copy(self.SYSTEM_RESOLV_CONF_FILE_PATH, self.DEFAULT_DNS_CONF_FILE_PATH)

            
    # Set given custom configuration with --config-file option
    def set_custom_conf(self, config_path: str) -> None:
        
        nameserver1, nameserver2 = self._load_config_json(config_path) # read nameservers from given json file
        
        with open(self.DNS_SERVER_CONFIG_PATH, 'r') as file:
            self.dns_servers_config:dict = json.load(file)
            file.close()
        
        value = input('[INPUT] Do you want to add this configuration to global config.json?(y/n)')
        if value.lower() == 'y':
            name = input('[INPUT] Set name for your DNS server:')
            self._append_dns_server(
                {
                    'nameserver1': nameserver1,
                    'nameserver2': nameserver2
                },
                name
            )
        
        self._set_dns(nameserver1, nameserver2)

    # Set default configuration
    def set_default_conf(self) -> None:
        self._set_dns(
            self.DEFAULT_CONF['shecan']['nameserver1'],
            self.DEFAULT_CONF['shecan']['nameserver2']
        )
    
    # Read /etc/resolv.conf file
    def _load_resolv_conf(self) -> list[str]:
        
        with open(self.SYSTEM_RESOLV_CONF_FILE_PATH, 'r') as file:
            content = file.readlines()
            file.close()
            return content

    # Write /etc/resolv.conf file
    def _write_resolv_conf(self, content: list[str]) -> None:

        with open(self.SYSTEM_RESOLV_CONF_FILE_PATH, 'w') as file:
            file.writelines(content)
            file.close()

    # Load configuration file (/etc/dummy-dns/config.json) that contains DNS server addresses
    def _load_config_json(self, path: str) -> tuple:
        
        with open(path, 'r') as file:
            data = json.load(file)
            file.close()
            
            return data['nameserver1'], data['nameserver2']
    
    # Write configs on /etc/dummy-dns/config.json
    def _write_config_json(self):
        
        json.dump(self.dns_servers_config, open(self.DNS_SERVER_CONFIG_PATH, 'w')) # write on config.json
    
    # Checking dummy-dns is set your DNS configurations or not
    def check_dummy(self):
        with open(self.SYSTEM_RESOLV_CONF_FILE_PATH, 'r') as file:
            first_line = file.readline(-1)
            if 'dummy' in first_line:
                logger.info('Dummy is active.')
            else:
                logger.info('Dummy is not active.')
    
    # Algorithm of setting DNS
    def _set_dns(self, nameserver1:str, nameserver2:str):
        
        resolv_file_content = self._load_resolv_conf()
            
        for line_number, line in enumerate(resolv_file_content):
            
            if 'nameserver' in line:
                if '#' in line and 'dummy' in resolv_file_content[0]:
                    resolv_file_content[line_number + 1] = f'nameserver {nameserver1}\n'
                    resolv_file_content[line_number + 2] = f'nameserver {nameserver2}\n'
                
                else:
                    resolv_file_content[line_number] = f'# {line}nameserver {nameserver1}\nnameserver {nameserver2}\n'                
                
                break
            
            
        if not 'dummy' in resolv_file_content[0]:
            resolv_file_content.insert(0, '# dummy is running\n')

        self._write_resolv_conf(resolv_file_content)

    # Select saved DNS configration and server addresses from /etc/dummy-dns/config.json
    def select_saved_server(self, name: str) -> None:
                
        with open(self.DNS_SERVER_CONFIG_PATH, 'r') as file:
            self.dns_servers_config:dict = json.load(file)
            file.close()
        
        if not name in self.dns_servers_config.keys():
            raise ValueError(f'No DNS configuration found for {name}.')
        
        nameserver1 = self.dns_servers_config[name]['nameserver1']
        nameserver2 = self.dns_servers_config[name]['nameserver2']
        self._set_dns(nameserver1, nameserver2)

    # Add server configuration to /etc/dummy-dns/config.json file
    def _append_dns_server(self, config:dict, name: str) -> None:
        
        self.dns_servers_config[name] = config
        self._write_config_json()
        logger.info(f'{name} DNS server added successfully.')
    
    