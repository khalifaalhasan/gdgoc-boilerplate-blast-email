import src.config as config

def get_certificate_email_body(nama, role):
    return f"""
    <html>
    <body style="margin:0; padding:0; background-color:#f4f4f4; font-family: 'Google Sans', Arial, sans-serif;">
        <div style="max-width: 600px; margin: 20px auto; background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 5px rgba(0,0,0,0.1);">
            
            <img src="{config.URL_HEADER}" style="width: 100%; display: block; pointer-events: none;" alt="Header">

            <div style="padding: 40px 30px; color: #333333; font-size: 14px; line-height: 1.6;">
                
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
                
                GDG on Campus Universitas Sriwijaya 2026</p>
            </div>

            <div style="background-color: #fce4e4; padding: 30px; text-align: center; border-top: 1px solid #f9d8d8;">
                
                <img src="{config.URL_ICON}" style="width: 80px; margin-bottom: 10px; pointer-events: none;" alt="Icon GDG">
                
                <div style="color: #202124; font-size: 18px; font-weight: bold; margin-bottom: 2px;">Google Developer Group</div>
                <div style="color: #ff5c77; font-size: 16px; margin-bottom: 20px;">Universitas Sriwijaya</div>
                
                <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top: 15px;">
                    <tr>
                        <td align="center" style="font-size: 14px; padding-bottom: 10px;">
                            <a href="{config.LINK_INSTAGRAM}" style="color: #ea4335; text-decoration: underline; font-weight: bold;">Instagram</a> 
                            <span style="color: #ea4335; margin: 0 5px;">|</span> 
                            <a href="{config.LINK_WEBSITE}" style="color: #ea4335; text-decoration: underline; font-weight: bold;">Website</a> 
                            <span style="color: #ea4335; margin: 0 5px;">|</span> 
                            <a href="{config.LINK_LINKEDIN}" style="color: #ea4335; text-decoration: underline; font-weight: bold;">LinkedIn</a> 
                            <span style="color: #ea4335; margin: 0 5px;">|</span> 
                            <a href="{config.LINK_TIKTOK}" style="color: #ea4335; text-decoration: underline; font-weight: bold;">TikTok</a>
                        </td>
                    </tr>
                </table>
            </div>
            
        </div>
    </body>
    </html>
    """