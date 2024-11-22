import os
from dotenv import load_dotenv
load_dotenv()

class Settings:
    ODOO_URL = os.getenv("ODOO_URL", "localhost")
    ODOO_PORT = os.getenv("ODOO_PORT", "8069")
    ODOO_DB = os.getenv("ODOO_DB", "your_database")
    ODOO_USERNAME = os.getenv("ODOO_USERNAME", "admin")
    ODOO_PASSWORD = os.getenv("ODOO_PASSWORD", "admin")

settings = Settings()
