# from service import DNSService
import json
import os 
import sys
import shutil

class DnsHandler:
    
    def __init__(self):
        
        self.DEFAULT_CONF:dict = {
            'shecan': {
                'nameserver1': '178.22.122.100',
                'nameserver2': '185.51.200.2'
            }
        }
        
        self.app_conf_path = os.getenv('DUMMY_DNS_CONFIG_PATH')
        self.system_conf_path = os.getenv('DUMMY_DNS_APP_CONF_PATH')
        self.dns_config_path = os.getenv('DUMMY_DNS_SYSTEM_CONF_PATH')
        
    
    def reset_dns(self) -> None:
        try:
            shutil.copy(self.app_conf_path, self.system_conf_path)
        except Exception as error:
            print(f'Reset process failed ==> Error:{error}')
            
    def force_save_conf(self) -> None:
        try:
            shutil.copy(self.system_conf_path, self.app_conf_path)
        except Exception as error:
            print(f'Save file process failed ==> Error:{error}')
            
    def set_custom_conf(self, config_path: str) -> None:
        nameserver1, nameserver2 = self._load_config_json(config_path)
        self._set_dns(nameserver1, nameserver2)
    
    def set_default_conf(self) -> None:
        self._set_dns(
            self.DEFAULT_CONF['shecan']['nameserver1'],
            self.DEFAULT_CONF['shecan']['nameserver2']
        )
    
    def load_resolv_conf(self) -> list[str]:
        
        with open(self.system_conf_path, 'r') as file:
            content = file.readlines()
            file.close()
            return content

    def write_resolv_conf(self, content: list[str]) -> None:
        
        with open(self.system_conf_path, 'w') as file:
            file.writelines(content)
            file.close()    
    
    def _load_config_json(self, path: str) -> tuple:
        
        with open(path, 'r') as file:
            data = json.load(file)
            file.close()
            
            return data['nameserver1'], data['nameserver2']
        
    def check_dummy(self):
        with open(self.system_conf_path, 'r') as file:
            first_line = file.readline(-1)
            if 'dummy' in first_line:
                print('Dummy is active.')
            else:
                print('Dummy is not active.')
            
            return
    
    def _set_dns(self, nameserver1:str, nameserver2:str):
        
        resolv_file_content = self.load_resolv_conf()
            
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

        self.write_resolv_conf(resolv_file_content)
