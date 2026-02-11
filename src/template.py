def get_certificate_email_body(nama, role):
    """
    Mengembalikan string HTML untuk email sertifikat.
    Menggunakan cid:header dan cid:footer untuk image embedding.
    """
    return f"""
    <html>
    <body style="margin:0; padding:0; background-color:#f4f4f4; font-family: 'Google Sans', Arial, sans-serif;">
        <div style="max-width: 600px; margin: 20px auto; background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            
            <img src="cid:header_image" style="width: 100%; display: block;" alt="Header">

            <div style="padding: 40px 30px; color: #333333; font-size: 14px; line-height: 1.6;">
                
                <h2 style="color: #0F9D58; text-align: center; margin-top: 0;">Thank You! 🌟</h2>
                
                <p>Annyeong, <b>{nama}</b> 🤩👋</p>

                <p>Greetings from the GDGoC UNSRI team!</p>

                <p>We just want to say a massive <b>THANK YOU</b> for joining us at our recent event as a <b>{role}</b>. Your presence has truly sparked a light in our community! 🔥✨</p>

                <p>To celebrate your meaningful contribution, we are honored to present this certificate to you. You earned it! 🏆</p>

                <div style="background-color: #e8f0fe; border-left: 4px solid #4285f4; padding: 15px; margin: 20px 0;">
                    <strong>📂 Certificate Access:</strong><br>
                    Please find your certificate attached below in this email (PDF).
                </div>

                <p>Don’t keep this achievement to yourself! Share your certificate on social media and let the world know about your growth. Time to Flex! 😎</p>

                <p>Make sure to tag <b>@googlefordevs</b>, <b>@googlestudents</b>, <b>@gdgocindonesia</b>, and <b>@gdgunsri</b>. Don't forget to use the hashtag <b>#GoogleDeveloperGroupsOnCampus</b> so we can repost your story! 📲💥</p>

                <p>Keep shining and keep inspiring, Folks! 🚀</p>
                
                <br>
                <p style="margin-bottom:0;">Best regards,</p>
                <p><b>{role} Team</b><br>
                GDG on Campus Universitas Sriwijaya 2026</p>
            </div>

            <img src="cid:footer_image" style="width: 100%; display: block;" alt="Footer">
            
        </div>
    </body>
    </html>
    """