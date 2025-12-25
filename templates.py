import os
import base64
import mimetypes
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
from email import encoders
import config

def get_html_selected(nama, divisi):
    """HTML Lolos: Body Hijau Muda, Footer Hijau Pekat"""
    return f"""
    <html>
    <body style="margin:0; padding:0; background-color:#ffffff; font-family: 'Google Sans', Arial, sans-serif;">
        <div style="max-width: 600px; margin: 0 auto; border: 1px solid #eeeeee;">
            
            <img src="cid:header_image" style="width: 100%; display: block;">

            <div style="background-color: #dbead5; padding: 40px 30px; color: #000000; font-size: 14px; line-height: 1.6;">
                <p style="font-weight: bold; margin-top:0;">{config.SUBJECT_EMAIL}</p>
                <p>Annyeong, Folks!</p>
                
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
                <img src="cid:footer_logo" style="width: 80px; display: inline-block;">
            </div>
            
        </div>
    </body>
    </html>
    """

def get_html_not_selected(nama):
    """HTML Tidak Lolos: Body Pink, Footer Merah Salmon"""
    return f"""
    <html>
    <body style="margin:0; padding:0; background-color:#ffffff; font-family: 'Google Sans', Arial, sans-serif;">
        <div style="max-width: 600px; margin: 0 auto; border: 1px solid #eeeeee;">
            
            <img src="cid:header_image" style="width: 100%; display: block;">

            <div style="background-color: #fadadd; padding: 40px 30px; color: #000000; font-size: 14px; line-height: 1.6;">
                <p style="font-weight: bold; margin-top:0;">{config.SUBJECT_EMAIL}</p>
                <p>Annyeong, Folks!</p>
                
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
                <img src="cid:footer_logo" style="width: 80px; display: inline-block;">
            </div>
            
        </div>
    </body>
    </html>
    """

def create_email_object(sender, to, subject, html_content, img_header_path, img_logo_path, attachment_pdf=None):
    """Fungsi Teknis Merakit Email"""
    message = MIMEMultipart('related')
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    msg_alternative = MIMEMultipart('alternative')
    message.attach(msg_alternative)
    
    # Attach HTML
    msg_text = MIMEText(html_content, 'html')
    msg_alternative.attach(msg_text)

    # Attach Images (Header & Logo Footer)
    # Perhatikan CID-nya: <header_image> dan <footer_logo>
    for path, cid_name in [(img_header_path, '<header_image>'), (img_logo_path, '<footer_logo>')]:
        if os.path.exists(path):
            with open(path, 'rb') as f:
                img = MIMEImage(f.read())
                img.add_header('Content-ID', cid_name)
                img.add_header('Content-Disposition', 'inline')
                message.attach(img)
        else:
            print(f"⚠️ Warning: Gambar {path} tidak ditemukan!")

    # Attach PDF
    if attachment_pdf and os.path.exists(attachment_pdf):
        content_type, encoding = mimetypes.guess_type(attachment_pdf)
        if content_type is None or encoding is not None:
            content_type = 'application/octet-stream'
        main_type, sub_type = content_type.split('/', 1)
        with open(attachment_pdf, 'rb') as fp:
            msg = MIMEBase(main_type, sub_type)
            msg.set_payload(fp.read())
        encoders.encode_base64(msg)
        filename = os.path.basename(attachment_pdf)
        msg.add_header('Content-Disposition', 'attachment', filename=filename)
        message.attach(msg)

    return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}