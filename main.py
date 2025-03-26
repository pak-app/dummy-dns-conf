# import argparse
# import json
import os 
import sys

# parser = argparse.ArgumentParser(description="Set your Linux DNS automatically.")
# # Use custom DNS configuration: 
# parser.add_argument("--file", required=False, help="Path to custom DNS configuration. The JSON config file shold be have one two keys named `nameserver1` and `nameserver2`.")
# # Use default DNS configuration:
# parser.add_argument('--default', required=False, help="Use default configuration, currently Shekan is supported.")
# Reset configuration
# parser.add_argument('--reset', required=False, help="Reset your DNS configuration.")
# Force reconfigure
# parser.add_argument('--force-reset', required=False, help="It re-creates and resets your default DNS configurations.")
# args = parser.parse_args()

DEFAULT_CONF = {
    'shekan': {
        'nameserver1': '178.22.122.100',
        'nameserver2': '185.51.200.2'
    }
}

def import_config(conf: dict, default_conf_dns: list[str]):
    
    name_server_1 = conf['shekan']['nameserver1']
    name_server_2 = conf['shekan']['nameserver2']
    
    for index, line in enumerate(default_conf_dns):
        
        if 'dummy-dns' in line:
            print('dummy-dns is running.')
            break
            
        if 'nameserver' in line:
            default_conf_dns.insert(index - 1, "# dummy-dns is running\n")
            default_conf_dns[index] = "# " + line
            default_conf_dns.insert(index + 1, f'nameserver {name_server_1}\n')
            default_conf_dns.insert(index + 2, f'nameserver {name_server_2}\n')
            break
    
        
    
    return default_conf_dns

if __name__ == "__main__":
    
    conf = DEFAULT_CONF.copy()
    
    if os.geteuid() != 0:
        print("This script must be run as root. Try using sudo.")
        sys.exit(1)
    
    default_conf_dns = None
    
    with open('./resolv.conf', 'r') as file:
        default_conf_dns = file.readlines()
        file.close()
        
    new_conf = import_config(conf, default_conf_dns)
    
    with open('./resolv.conf', 'w') as file:
        file.writelines(new_conf)
        file.close()
    