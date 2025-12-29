import os
import base64
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from docxtpl import DocxTemplate # Pastikan sudah pip install docxtpl
import config

# ==========================================
# 1. FUNGSI GENERATE WORD (LOGIC BARU)
# ==========================================
def generate_custom_docx(template_path, output_path, context_data):
    """
    Membuka file template, me-replace variabel {{...}}, 
    dan menyimpan hasilnya ke file baru.
    """
    try:
        doc = DocxTemplate(template_path)
        doc.render(context_data) # Proses replace nama & divisi
        doc.save(output_path)
        return True
    except Exception as e:
        print(f"❌ Error saat membuat DOCX: {e}")
        return False

# ==========================================
# 2. TEMPLATE HTML (TIDAK PERLU DIUBAH)
# ==========================================

def get_html_selected(nama, divisi):
    # ... (Biarkan kode HTML selected kamu yang tadi) ...
    return f"""
    <html>
    <body style="margin:0; padding:0; background-color:#ffffff; font-family: 'Google Sans', Arial, sans-serif;">
        <div style="max-width: 600px; margin: 0 auto; border: 1px solid #eeeeee;">
            <img src="{config.URL_HEADER}" style="width: 100%; display: block;">
            <div style="background-color: #dbead5; padding: 40px 30px; color: #000000; font-size: 14px; line-height: 1.6;">
                <p style="font-weight: 800; margin-top:0; font-size: 16px; text-align: center;">{config.SUBJECT_EMAIL}</p>
                <p>Annyeong, {nama}!</p>
                
                <p>We are absolutely delighted to share some fantastic news! Following the recruitment process, 
                we are thrilled to inform you that you have been <b>officially SELECTED</b> as the member of 
                <b>{divisi}</b> at Google Developer Groups on Campus Chapter Universitas Sriwijaya for the 2025/2026 term!</p>
                
                <p>To finalize your position, please complete the following:</p>
                <ol style="padding-left: 20px;">
                    <li><b>Sign the Commitment Letter</b> provided below (or attached to this email).</li>
                    <li><b>Reply to this email</b> with the signed letter within <b>24 hours</b>.</li>
                </ol>
                
                <p><b>NOTE:</b> Failure to respond within <b>24 hours</b> will be considered a 
                <b>RESIGNATION</b>. Once confirmed, you will be added to the Core Team WhatsApp Group!</p>
                
                <p>We look forward to having you on the GDG on Campus UNSRI team! Get ready to <b>Connect, Learn, and Grow!</b> &lt;&gt;</p>
                <br>
                <p style="margin-bottom:0;"><b>Best Regards,</b><br>
                <b>GDG on Campus Organizer</b><br>Chapter Universitas Sriwijaya 2025/2026</p>
            </div>
            <div style="background-color: #93c47d; padding: 20px; text-align: center;">
                <img src="{config.URL_LOGO}" style="width: 80px; display: inline-block;">
            </div>
        </div>
    </body>
    </html>
    """

def get_html_not_selected(nama):
    # ... (Biarkan kode HTML not selected kamu yang tadi) ...
    return f"""
    <html>
    <body style="margin:0; padding:0; background-color:#ffffff; font-family: 'Google Sans', Arial, sans-serif;">
        <div style="max-width: 600px; margin: 0 auto; border: 1px solid #eeeeee;">
            <img src="{config.URL_HEADER}" style="width: 100%; display: block;">
            <div style="background-color: #fadadd; padding: 40px 30px; color: #000000; font-size: 14px; line-height: 1.6;">
                <p style="font-weight: 800; margin-top:0; font-size: 16px; text-align: center;">{config.SUBJECT_EMAIL}</p>
                <p>Annyeong, {nama}!</p>
                <p>Thank you for your interest and enthusiasm in the <b>GDGoC Universitas Sriwijaya Member Recruitment 2025/2026</b>. 
                We truly appreciate the time and effort you put into your application.</p>
                <p>After careful review of all applicants, we regret to inform you that you were 
                <b>NOT SELECTED</b> as a GDGoC Member for this recruitment period.</p>
                <p>However, this is not the end of your journey with GDGoC. We encourage you to stay connected with us through our 
                <b>upcoming programs, events, and activities</b>.</p>
                <p><b>Don’t miss this opportunity to stay connected!</b> Click the link below to accept your invitation and join our community group and channel:</p>
                <ul style="padding-left: 20px;">
                    <li><a href="{config.LINK_COMMUNITY_GROUP}" style="color: #0056b3;">Community Group</a></li>
                    <li><a href="{config.LINK_WA_CHANNEL}" style="color: #0056b3;">WhatsApp Channel</a></li>
                </ul>
                <br>
                <p style="margin-bottom:0;"><b>Best Regards,</b><br>
                <b>GDG on Campus Organizer</b><br>Chapter Universitas Sriwijaya 2025/2026</p>
            </div>
            <div style="background-color: #e06666; padding: 20px; text-align: center;">
                <img src="{config.URL_LOGO}" style="width: 80px; display: inline-block;">
            </div>
        </div>
    </body>
    </html>
    """

def get_html_moved(nama, divisi_baru):
    # ... (Biarkan kode HTML moved kamu yang tadi) ...
    return f"""
    <html>
    <body style="margin:0; padding:0; background-color:#ffffff; font-family: 'Google Sans', Arial, sans-serif;">
        <div style="max-width: 600px; margin: 0 auto; border: 1px solid #eeeeee;">
            <img src="{config.URL_HEADER}" style="width: 100%; display: block;">
            <div style="background-color: #e8f0fe; padding: 40px 30px; color: #000000; font-size: 14px; line-height: 1.6;">
                <p style="font-weight: 800; margin-top:0; font-size: 16px; text-align: center;">{config.SUBJECT_EMAIL}</p>
                <p>Annyeong, {nama}!</p>
                <p>We have an important update regarding your application. While we could not place you in your initial choice of division, 
                our team was <b>highly impressed by your potential and profile</b>.</p>
                <p>Therefore, we are excited to offer you a spot as a member of:</p>
                <p style="font-size: 18px; font-weight: bold; color: #1967d2; text-align: center;">
                    ✨ {divisi_baru} ✨
                </p>
                <p>We believe your skills will thrive in this division! To accept this offer and finalize your position, please complete the following:</p>
                <ol style="padding-left: 20px;">
                    <li><b>Sign the Commitment Letter</b> provided below (or attached to this email).</li>
                    <li><b>Reply to this email</b> with the signed letter within <b>24 hours</b>.</li>
                </ol>
                <p><b>NOTE:</b> Failure to respond within <b>24 hours</b> will be considered a 
                <b>RESIGNATION</b>.</p>
                <p>We look forward to having you on the GDG on Campus UNSRI team! Get ready to <b>Connect, Learn, and Grow!</b> &lt;&gt;</p>
                <br>
                <p style="margin-bottom:0;"><b>Best Regards,</b><br>
                <b>GDG on Campus Organizer</b><br>Chapter Universitas Sriwijaya 2025/2026</p>
            </div>
            <div style="background-color: #4285f4; padding: 20px; text-align: center;">
                <img src="{config.URL_LOGO}" style="width: 80px; display: inline-block;">
            </div>
        </div>
    </body>
    </html>
    """

# ==========================================
# 3. FUNGSI RAKIT EMAIL (SUDAH DIBERSIHKAN)
# ==========================================
# templates.py

# Hapus parameter img_header_path dan img_logo_path dari dalam kurung!
def create_email_object(sender, to, subject, html_content, attachment_path=None):
    
    message = MIMEMultipart()
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    # 1. Attach HTML Body
    msg_text = MIMEText(html_content, 'html')
    message.attach(msg_text)

    # 2. Attach File Word/PDF (Hanya jika ada)
    if attachment_path and os.path.exists(attachment_path):
        content_type, encoding = mimetypes.guess_type(attachment_path)
        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
        
        main_type, sub_type = content_type.split('/', 1)
        
        with open(attachment_path, 'rb') as fp:
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(fp.read())
        
        encoders.encode_base64(msg)
        filename = os.path.basename(attachment_path)
        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        
        message.attach(msg) # <--- Ini satu-satunya "attach" yang boleh ada untuk file

    # --- BAGIAN DI BAWAH INI JANGAN ADA LAGI ---
    # with open(img_header, 'rb')... -> HAPUS
    # message.attach(img)...         -> HAPUS
    # -------------------------------------------

    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}