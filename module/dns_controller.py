from .dns_handler import DnsHandler

class DnsController:
    
    def __init__(self, args):
        
        self.args = args
        self.dns_handler = DnsHandler()
            
    def reset_dns(self):
        self.dns_handler.reset_dns()
    
    def force_save_conf(self):
        self.dns_handler.force_save_conf()
    
    def set_custom_conf(self, config_path: str):
        self.dns_handler.set_custom_conf(config_path)
    
    def set_default_conf(self):
        self.dns_handler.set_default_conf()
    
    def check_dummy(self):
        self.dns_handler.check_dummy()
    
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