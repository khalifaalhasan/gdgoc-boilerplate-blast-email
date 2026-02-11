import os

# --- PATH CONFIGURATION ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, 'assets')
DATA_DIR = os.path.join(BASE_DIR, 'data')

# File Paths
CSV_FILE = os.path.join(DATA_DIR, 'recipients.csv')
CERTIFICATES_DIR = os.path.join(ASSETS_DIR, 'certificates')
HEADER_IMG = os.path.join(ASSETS_DIR, 'header.png')
FOOTER_IMG = os.path.join(ASSETS_DIR, 'footer.png')
TOKEN_PATH = os.path.join(BASE_DIR, 'token.json')
CREDENTIALS_PATH = os.path.join(BASE_DIR, 'credentials.json')

# --- EMAIL CONFIGURATION ---
SENDER_NAME = "GDG on Campus UNSRI"
SENDER_EMAIL = "dscunsri@gmail.com"  # Pastikan sama dengan akun auth
EMAIL_SUBJECT = "Thank you for joining GDGoC UNSRI [Nama Event]! Claim Your Certificate Here. "

# --- GOOGLE API ---
SCOPES = ['https://www.googleapis.com/auth/gmail.send']