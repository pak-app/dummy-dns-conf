import argparse
from module.dns_controller import DnsController as main
import os
from dotenv import load_dotenv
import logging

# Basic logging configuration
logging.basicConfig(
    level=logging.INFO,  # Set the minimum logging level
    format="[%(levelname)s]: %(message)s",  # Log format
)
logger = logging.getLogger(os.getenv('APP_LOG_NAME'))

# Load environment variables
def env_manager() -> None:
    
    load_dotenv('.env') # Load app environment variables
    app_env = os.getenv('APP_ENV') # Load application runtime environment
    
    # Load production environment variables
    if app_env == 'production':
        load_dotenv('.env.production') # prod env

    # Load production environment variables
    elif app_env == 'development':
        load_dotenv('.env.development') # dev env

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
    help="It sets the given servers' addresses in configuration file. The JSON config file shold be have one two keys named `nameserver1` and `nameserver2`.",
)

parser.add_argument(
    '-s',
    '--set',
    type=str,
    default='',
    help="It sets the DNS by given DNS name as input. If you do not give the name it automatically sets the first DNS configuration in /etc/dummy-dns/config.json file."
)

# Unset the DNS
parser.add_argument(
    '--unset', 
    required=False, 
    help="It unsets your DNS configuration.",
    action='store_true',
    # type=bool
)

# Use default DNS configuration:
parser.add_argument(
    '-d',
    '--default', 
    required=False, 
    help="It will use the default DNS servers and currently Shekan DNS is supported.",
    action='store_true',
    # type=bool
)

# Reset configuration
parser.add_argument(
    '--reset', 
    required=False, 
    help="Reset your DNS configuration to system default.",
    action='store_true',
    # type=bool
)

# Force reconfigure
parser.add_argument(
    '-fr',
    '--force-reset', 
    help="It re-creates and resets your default DNS configurations. Be carefull to use this option, It will replace the default DNS setting saved during installation. Use this command when you sure about resolv.conf file is in its default.",
    action='store_true',
    # type=bool
)

# Check is dummy-dns set configuration 
parser.add_argument(
    '-cd',
    '--check-dummy',
    help='Check DNS is affected or not.',
    action='store_true'
)

args = parser.parse_args()


if __name__ == "__main__":

    # Check if you run it as root (sudo ...)
    if os.geteuid() != 0:
        logger.error('Please use sudo before the command. Try with sudo again.')
        
    # Load env variables in production mode
    env_manager()
    
    # Run program
    app = main(args)
    app.run()
    
    
    