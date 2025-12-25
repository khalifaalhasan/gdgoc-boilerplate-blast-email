# import os.path
# import base64
# import csv
# import time
# import random
# import mimetypes
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders

# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
# from googleapiclient.discovery import build

# # --- KONFIGURASI ---
# SCOPES = ['https://www.googleapis.com/auth/gmail.send']
# CSV_FILENAME = "data_user.csv"
# FILE_KOMITMEN = "Commitment_Letter.pdf" # Pastikan file ini ada di folder lu!
# SENDER_EMAIL = "dscunsri@gmail.com" # Email Pengirim

# # --- TEMPLATE EMAIL ---
# def get_body_selected(nama, divisi):
#     # Mengambil teks dari dokumen Selected 
#     return f"""
#     <p>Annyeong, Folks!</p>
#     <p>We are absolutely delighted to share some fantastic news! Following the recruitment process, 
#     we are thrilled to inform you that you have been <b>officially SELECTED</b> as the member of 
#     <b>{divisi}</b> at Google Developer Groups on Campus Chapter Universitas Sriwijaya for the 2025/2026 term!</p>
    
#     <p>To finalize your position, please complete the following:</p>
#     <ul>
#         <li><b>Sign the Commitment Letter</b> provided below (attached to this email).</li>
#         <li><b>Reply to this email</b> with the signed letter within <b>24 hours</b>.</li>
#     </ul>
    
#     <p style="color:red;"><b>NOTE: Failure to respond within 24 hours will be considered a RESIGNATION. 
#     Once confirmed, you will be added to the Core Team WhatsApp Group!</b></p>
    
#     <p>We look forward to having you on the GDG on Campus UNSRI team! Get ready to Connect, Learn, and Grow! &lt;&gt;</p>
#     <br>
#     <p>Best Regards,<br>
#     <b>GDG on Campus Organizer</b><br>
#     Chapter Universitas Sriwijaya 2025/2026</p>
#     """

# def get_body_not_selected(nama):
#     # Mengambil teks dari dokumen Not Selected  
#     # NOTE: GANTI LINK WA DI BAWAH INI DENGAN LINK ASLI
#     link_community = "https://chat.whatsapp.com/LPNr9C2O9KdAmuF58xTFFD"
#     link_channel = "https://whatsapp.com/channel/0029Vaw1hRv2ER6q6Vzxrp1k"
    
#     return f"""
#     <p>Annyeong, Folks!</p>
#     <p>Thank you for your interest and enthusiasm in the GDGoC Universitas Sriwijaya Member Recruitment 2025/2026. 
#     We truly appreciate the time and effort you put into your application.</p>
    
#     <p>After careful review of all applicants, we regret to inform you that you were 
#     <b>NOT SELECTED</b> as a GDGoC Member for this recruitment period.</p>
    
#     <p>However, this is not the end of your journey with GDGoC. We value your passion for technology and community, 
#     and we encourage you to stay connected with us through our upcoming programs, events, and activities. 
#     You will also have the opportunity to apply again in future recruitment periods.</p>
    
#     <p>Don’t miss this opportunity to stay connected! Click the link below to accept your invitation and join our community group and channel:</p>
#     <ul>
#         <li><a href="{link_community}">Community Group</a></li>
#         <li><a href="{link_channel}">WhatsApp Channel</a></li>
#     </ul>
    
#     <br>
#     <p>Best Regards,<br>
#     <b>GDG on Campus Organizer</b><br>
#     Chapter Universitas Sriwijaya 2025/2026</p>
#     """

# def create_message_with_attachment(sender, to, subject, message_text, file_path=None):
#     message = MIMEMultipart()
#     message['to'] = to
#     message['from'] = sender
#     message['subject'] = subject

#     msg = MIMEText(message_text, 'html')
#     message.attach(msg)

#     # Logika Attach File (Hanya jika ada file_path)
#     if file_path:
#         content_type, encoding = mimetypes.guess_type(file_path)
#         if content_type is None or encoding is not None:
#             content_type = 'application/octet-stream'
#         main_type, sub_type = content_type.split('/', 1)
        
#         with open(file_path, 'rb') as fp:
#             msg = MIMEBase(main_type, sub_type)
#             msg.set_payload(fp.read())
        
#         encoders.encode_base64(msg)
#         filename = os.path.basename(file_path)
#         msg.add_header('Content-Disposition', 'attachment', filename=filename)
#         message.attach(msg)

#     return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

# def main():
#     # 1. SETUP AUTH (Login Google)
#     creds = None
#     if os.path.exists('token.json'):
#         creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
#     if not creds or not creds.valid:
#         if creds and creds.expired and creds.refresh_token:
#             creds.refresh(Request())
#         else:
#             # Bakal buka browser otomatis buat login akun GDG
#             flow = InstalledAppFlow.from_client_secrets_file(
#                 'credentials.json', SCOPES)
#             creds = flow.run_local_server(port=0)
        
#         with open('token.json', 'w') as token:
#             token.write(creds.to_json())

#     service = build('gmail', 'v1', credentials=creds)
#     print("✅ Login Berhasil sebagai:", SENDER_EMAIL)

#     # 2. BACA CSV DAN KIRIM
#     try:
#         with open(CSV_FILENAME, mode='r', encoding='utf-8-sig') as file:
#             reader = csv.DictReader(file)
            
#             count = 0
#             for row in reader:
#                 try:
#                     nama = row['Name']
#                     email = row['Email']
#                     divisi = row['Division']
#                     status = row['Status'].strip().lower()

#                     # Validasi Email
#                     if email == '-' or '@' not in email:
#                         print(f"⛔ SKIP: {nama} (Email invalid)")
#                         continue

#                     # Tentukan Subject, Body, dan Attachment
#                     subject = "Announcement for Member GDGoC Recruitment 2025/2026"
#                     attachment = None
                    
#                     if status == 'selected':
#                         body = get_body_selected(nama, divisi)
#                         attachment = FILE_KOMITMEN # Lampirkan file komitmen 
#                         print(f"[{count+1}] Mengirim SELECTED ke: {nama}...")
                        
#                     elif status == 'not selected':
#                         body = get_body_not_selected(nama)
#                         attachment = None # Tidak ada lampiran 
#                         print(f"[{count+1}] Mengirim NOT SELECTED ke: {nama}...")
                    
#                     else:
#                         print(f"⚠️ Status '{status}' tidak dikenal. Skip.")
#                         continue

#                     # Buat & Kirim Pesan
#                     message = create_message_with_attachment(SENDER_EMAIL, email, subject, body, attachment)
#                     service.users().messages().send(userId="me", body=message).execute()
                    
#                     print(f"   ✅ TERKIRIM ke {email}")
#                     count += 1
                    
#                     # DELAY (PENTING BIAR GAK KENA BLOKIR)
#                     time.sleep(random.randint(5, 10))

#                 except Exception as e:
#                     print(f"❌ ERROR kirim ke {row['Email']}: {e}")

#     except FileNotFoundError:
#         print("❌ File CSV atau Credentials tidak ditemukan.")

# if __name__ == '__main__':
#     main()



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