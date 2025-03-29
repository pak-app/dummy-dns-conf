from .dns_handler import DnsHandler
import logging
import os
from .exception_handlers import handle_exceptions

logger = logging.getLogger(os.getenv('APP_LOG_NAME'))
class DnsController:
    
    def __init__(self, args):
        
        self.args = args
        self.dns_handler = DnsHandler()
    
    # Reset DNS configuration
    @handle_exceptions(
        successful_message='System DNS is reseted.',
        error_message='Reset system DNS configuration is failed.'
    )
    def reset_dns(self):
        self.dns_handler.reset_dns()
        
    # Save current system DNS configuration for dummy-dns
    @handle_exceptions(
        successful_message='Current system DNS configuration is saved as dummy-dns default system DNS configuration.\nIt is located on /etc/dummy-dns/default.conf',
        error_message='Save current system configuration for dummy-dns.'
    )       
    def force_save_conf(self):
        self.dns_handler.force_save_conf()

    # Set given configuration.     
    @handle_exceptions(
        successful_message='DNS is set successfully.',
        error_message='Faild to set your given DNS. Please check the error and try again.'
    )
    def set_custom_conf(self, config_path: str):
        self.dns_handler.set_custom_conf(config_path)
    
    # Set default DNS configuration on your machine.(Shecan)
    @handle_exceptions(
        successful_message='Default DNS configuration is set successfully.',
        error_message='Faild to set defualt DNS configuration. Please check the error and try again.'
    )
    def set_default_conf(self):
        self.dns_handler.set_default_conf()
    
    # Checking if dummy-dns is set DNS or not
    @handle_exceptions(
        error_message='Faild to check dummy-dns status. Please check the error and try again.\nIt may /etc/resolv.conf file damaged. Please use dummy-dns --reset to reset configuration and set DNS again.'
    )
    def check_dummy(self):
        self.dns_handler.check_dummy()
    
    # Select DNS configuration form /etc/dummy-dns/config.json by its name
    @handle_exceptions(
        successful_message='{name} DNS configuration is set successfully.',
        error_message='Faild to set {name} DNS configuration. Please check the error and try again.'
    )
    def select_saved_server(self, name: str) -> None:
        self.dns_handler.select_saved_server(name)

    
    def run(self):
        
        if self.args.reset or self.args.unset:
            self.reset_dns()
        
        elif self.args.force_reset:
            self.force_save_conf()
        
        elif self.args.default:
            self.set_default_conf()
        
        elif not self.args.config_file == '':
            self.set_custom_conf(self.args.config_file)
        
        elif self.args.check_dummy:
            self.check_dummy()
        
        elif not self.args.set == '':
            self.select_saved_server(self.args.set)