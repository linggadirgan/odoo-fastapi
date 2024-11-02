import xmlrpc.client
from app.core.config import settings

class OdooClient:
    def __init__(self):
        self.url = settings.ODOO_URL
        self.db = settings.ODOO_DB
        self.username = settings.ODOO_USERNAME
        self.password = settings.ODOO_PASSWORD
        self.common = xmlrpc.client.ServerProxy(f'{self.url}/xmlrpc/2/common')
        self.models = xmlrpc.client.ServerProxy(f'{self.url}/xmlrpc/2/object')

        self.uid = self.common.authenticate(self.db, self.username, self.password, {})

    def get_records(self, model, fields, domain):
        return self.models.execute_kw(
            self.db, self.uid, self.password,
            model, 'search_read',
            [domain], {'fields': fields}
        )
