import re, os

id_pattern = re.compile(r'^.\d+$') 

API_ID = os.environ.get("API_ID", "28414026")

API_HASH = os.environ.get("API_HASH", "595e101e4009da570ae71cae7060d20f")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "6526902074:AAFFUh9pQ-i4wu9j1KsKNdLiWvIz1APb4fA") 

FORCE_SUB = os.environ.get("FORCE_SUB", "superyoutubedl") 

DB_NAME = os.environ.get("DB_NAME","rename")     

DB_URL = os.environ.get("DB_URL","mongodb+srv://Bikash:Bikashop@bikash.cbkkx4c.mongodb.net/?retryWrites=true&w=majority")
 
FLOOD = int(os.environ.get("FLOOD", "10"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/Rename-Bot-01-15")

ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '').split()]

PORT = os.environ.get("PORT", "8080")
