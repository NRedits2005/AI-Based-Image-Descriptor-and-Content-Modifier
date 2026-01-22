import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os

# ------------------- READ ARGS -------------------
if len(sys.argv) < 5:
    print("Usage: send_mail.py <name> <email> <description> <image_path>")
    sys.exit(1)

user_name = sys.argv[1]
user_email = sys.argv[2]
description = sys.argv[3]
image_path = sys.argv[4]

# ------------------- EMAIL SETUP -------------------
SENDER_EMAIL = "naveenmadhan86@gmail.com"
APP_PASSWORD = "ypwq eime khpq ctij"

msg = MIMEMultipart()
msg["From"] = SENDER_EMAIL
msg["To"] = user_email
msg["Subject"] = "Your Image Description"

# Email body
body = f"Hello {user_name},\n\nHere is the description you requested:\n\n{description}\n\nBest Regards,\nNaveen Raj K"
msg.attach(MIMEText(body, "plain"))

# Attach image
if os.path.exists(image_path):
    with open(image_path, "rb") as f:
        mime = MIMEBase("image", "png", filename=os.path.basename(image_path))
        mime.add_header("Content-Disposition", "attachment", filename=os.path.basename(image_path))
        mime.add_header("X-Attachment-Id", "0")
        mime.add_header("Content-ID", "<0>")
        mime.set_payload(f.read())
        encoders.encode_base64(mime)
        msg.attach(mime)

# ------------------- SEND EMAIL -------------------
try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(SENDER_EMAIL, APP_PASSWORD)
        smtp.send_message(msg)
    print("Email sent successfully!")
    sys.exit(0)
except Exception as e:
    print(f"Error: {e}")
    sys.exit(1)
