import argparse
from module.dns_controller import DnsController as main
import os

# Define argument parser
parser = argparse.ArgumentParser(
    prog='dummy-dns',
    description="Set your DNS automatically."
)

# Use custom DNS configuration: 
parser.add_argument(
    '-cf',
    "--config-file",
    required=False,
    type=str,
    default='',
    help="Path to custom DNS configuration. The JSON config file shold be have one two keys named `nameserver1` and `nameserver2`.",
)

# Use default DNS configuration:
parser.add_argument(
    '--default', 
    required=False, 
    help="Use default configuration, currently Shekan is supported.",
    action='store_true',
    # type=bool
)

# Reset configuration
parser.add_argument(
    '--reset', 
    required=False, 
    help="Reset your DNS configuration.",
    action='store_true',
    # type=bool
)

# Force reconfigure
parser.add_argument(
    '-fr',
    '--force-reset', 
    help="It re-creates and resets your default DNS configurations.",
    action='store_true',
    # type=bool
)

parser.add_argument(
    '-cd',
    '--check-dummy',
    help='Check dns is affected or not.',
    action='store_true'
)

args = parser.parse_args()


if __name__ == "__main__":

    if os.geteuid() != 0:
        print('Please use sudo before the command.\nexit code 0')
        exit(0)
        
    app = main(args)
    
    app.dns_handler.dns_config_path = './test/dummy/config.json'
    app.dns_handler.app_conf_path = './test/dummy/default_resolv.conf'
    app.dns_handler.system_conf_path = './test/system/resolv.conf'
    
    app.run()
    
    
    