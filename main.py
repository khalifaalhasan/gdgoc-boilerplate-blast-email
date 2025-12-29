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
    # ==========================================
    # 1. SETUP OTENTIKASI GOOGLE (LOGIN)
    # ==========================================
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', config.SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', config.SCOPES)
            creds = flow.run_local_server(port=8080)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    
    # Setup Nama Pengirim agar terlihat Profesional
    # Hasil: "GDG on Campus Unsri <dscunsri@gmail.com>"
    SENDER_FULL_NAME = config.SENDER_EMAIL_LOG
    
    print(f"✅ LOGIN SUKSES! Mengirim sebagai: {SENDER_FULL_NAME}")
    print("=" * 60)

    # ==========================================
    # 2. PROSES KIRIM EMAIL
    # ==========================================
    try:
        # Gunakan utf-8-sig untuk handle BOM karakter jika CSV dari Excel
        with open(config.CSV_FILENAME, mode='r', encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            
            count = 0
            for row in reader:
                file_attachment = None # Reset variabel file setiap loop
                try:
                    # --- A. AMBIL DATA DARI CSV ---
                    nama = row.get('Name', '').strip()
                    email = row.get('Email', '').strip()
                    divisi = row.get('Division', '').strip()
                    status = row.get('Status', '').strip().lower()

                    # --- FITUR PINTAR: CARI KOLOM NIM ---
                    # Mencari key apapun yang mengandung kata "nim" (case-insensitive)
                    # Ini solusi untuk mengatasi error KeyError: 'NIM'
                    nim_key = next((k for k in row.keys() if k and 'nim' in k.lower()), None)
                    nim_value = row[nim_key] if nim_key else "-"

                    # Validasi Email
                    if not email or email == '-' or '@' not in email:
                        print(f"⛔ SKIP: {nama} (Email Invalid)")
                        continue

                    # --- B. GENERATE DOCX DINAMIS (SURAT KOMITMEN) ---
                    # Hanya buat file jika peserta lolos (Selected/Moved)
                    if status in ['selected', 'moved']:
                        # 1. Data yang akan direplace ke dalam Word {{...}}
                        context_data = {
                            'nama_lengkap': nama,
                            'nama_divisi': divisi,
                            'nim_peserta': nim_value # Data NIM yang sudah diamankan
                        }
                        
                        # 2. Buat nama file sementara yang unik
                        clean_name = nama.replace(" ", "_")
                        temp_filename = f"Commitment_{clean_name}.docx"

                        # 3. Proses Generate menggunakan fungsi di templates.py
                        is_success = templates.generate_custom_docx(config.FILE_KOMITMEN, temp_filename, context_data)
                        
                        if is_success:
                            file_attachment = temp_filename
                        else:
                            print(f"⚠️ Warning: Gagal membuat surat komitmen untuk {nama}.")
                            file_attachment = None


                    # --- C. PILIH TEMPLATE & RAKIT EMAIL ---
                    message = None
                    
                    # Logic pemilihan template HTML
                    if status == 'selected':
                        print(f"[{count+1}] SENDING: {nama} ({email}) -> SELECTED ✅")
                        html_body = templates.get_html_selected(nama, divisi)
                        
                        message = templates.create_email_object(
                            SENDER_FULL_NAME, email, config.SUBJECT_EMAIL, 
                            html_body, file_attachment
                        )
                    
                    elif status == 'moved':
                        print(f"[{count+1}] SENDING: {nama} ({email}) -> MOVED 🔵")
                        html_body = templates.get_html_moved(nama, divisi) 
                        
                        message = templates.create_email_object(
                            SENDER_FULL_NAME, email, config.SUBJECT_EMAIL, 
                            html_body, file_attachment
                        )
                        
                    elif status == 'not selected':
                        print(f"[{count+1}] SENDING: {nama} ({email}) -> NOT SELECTED ❌")
                        html_body = templates.get_html_not_selected(nama)
                        
                        # Kirim tanpa attachment
                        message = templates.create_email_object(
                            SENDER_FULL_NAME, email, config.SUBJECT_EMAIL, 
                            html_body, None
                        )
                    else:
                        # Skip jika status di CSV aneh/kosong
                        continue

                    # --- D. EKSEKUSI PENGIRIMAN ---
                    service.users().messages().send(userId="me", body=message).execute()
                    print("   └── 🚀 Terkirim!")

                    # --- E. BERSIH-BERSIH (CLEANUP) ---
                    # Hapus file docx sementara agar folder tidak penuh
                    if file_attachment and os.path.exists(file_attachment):
                        os.remove(file_attachment)

                    count += 1
                    
                    # --- F. RATE LIMITING (ANTI SPAM) ---
                    # Jeda acak 5-10 detik agar tidak dianggap bot spam oleh Google
                    time.sleep(random.randint(5, 10))

                except Exception as e:
                    print(f"❌ ERROR pada baris {nama}: {e}")
                    # Pastikan file sementara tetap dihapus meski error
                    if file_attachment and os.path.exists(file_attachment):
                        os.remove(file_attachment)

    except FileNotFoundError:
        print(f"❌ FATAL ERROR: File CSV '{config.CSV_FILENAME}' tidak ditemukan!")
        print("   Pastikan nama file di config.py sesuai dengan file asli.")
    except Exception as e:
        print(f"❌ FATAL ERROR: {e}")

if __name__ == '__main__':
    main()