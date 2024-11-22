import odoorpc
from app.core.config import settings

class OdooClient:
    def __init__(self):
        self.url = settings.ODOO_URL  
        self.port = settings.ODOO_PORT  
        self.db_name = settings.ODOO_DB  
        self.username = settings.ODOO_USERNAME 
        self.password = settings.ODOO_PASSWORD 

        self.odoo = odoorpc.ODOO(self.url, port=self.port)
        self.odoo.login(self.db_name, self.username, self.password)

    def get_env(self):
        return self.odoo.env

def connect_odoo() -> OdooClient:
    client = OdooClient()
    return client.get_env()