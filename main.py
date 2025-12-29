
import os
import csv
import time
import random
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

import config
import templates

def main():
    # --- 1. LOGIN GOOGLE ---
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', config.SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', config.SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    print(f"✅ LOGIN SUKSES! Siap kirim dari: {config.SENDER_EMAIL_LOG}")
    print("=" * 50)

    # --- 2. KIRIM EMAIL ---
    try:
        with open(config.CSV_FILENAME, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            
            count = 0
            for row in reader:
                try:
                    nama = row['Name']
                    email = row['Email']
                    divisi = row['Division']
                    status = row['Status'].strip().lower()

                    if not email or email == '-' or '@' not in email:
                        print(f"⛔ SKIP: {nama} (Email Invalid)")
                        continue

                    # PILIH TEMPLATE & RAKIT
                    if status == 'selected':
                        print(f"[{count+1}] SELECTED: {nama} -> Hijau")
                        html_body = templates.get_html_selected(nama, divisi)
                        
                        # Parameter gambar footer diganti jadi IMG_LOGO aja
                        message = templates.create_email_object(
                            config.SENDER_EMAIL_LOG, email, config.SUBJECT_EMAIL, 
                            html_body, config.IMG_HEADER, config.IMG_LOGO, config.FILE_KOMITMEN
                        )
                    
                    elif status == 'moved':
                        print(f"[{count+1}] MOVED DIVISION: {nama} -> Biru")
                        # Panggil template biru
                        html_body = templates.get_html_moved(nama, divisi) 
                        # Tetap kirim PDF Komitmen (Karena diterima)
                        message = templates.create_email_object(
                            config.SENDER_EMAIL_LOG, email, config.SUBJECT_EMAIL, 
                            html_body, config.IMG_HEADER, config.IMG_LOGO, config.FILE_KOMITMEN
                        )
                        
                    elif status == 'not selected':
                        print(f"[{count+1}] NOT SELECTED: {nama} -> Pink")
                        html_body = templates.get_html_not_selected(nama)
                        
                        # Sama, pakai IMG_LOGO, tanpa attachment
                        message = templates.create_email_object(
                            config.SENDER_EMAIL_LOG, email, config.SUBJECT_EMAIL, 
                            html_body, config.IMG_HEADER, config.IMG_LOGO, None
                        )
                    else:
                        continue

                    # KIRIM
                    service.users().messages().send(userId="me", body=message).execute()
                    print("   ✅ Terkirim.")
                    count += 1
                    
                    time.sleep(random.randint(5, 10))

                except Exception as e:
                    print(f"❌ ERROR baris ini: {e}")

    except FileNotFoundError:
        print(f"❌ ERROR: File '{config.CSV_FILENAME}' tidak ditemukan!")
    except Exception as e:
        print(f"❌ ERROR UTAMA: {e}")

if __name__ == '__main__':
    main()