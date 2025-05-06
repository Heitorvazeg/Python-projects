import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

sender = os.getenv("SENDER")
receiver = os.getenv("RECEIVER")
password = os.getenv("PASSWORD")
subject = os.getenv("SUBJECT")
text = os.getenv("TEXT")

message = f"""From: {sender}
To: {receiver}
Subject: {subject}\n
{text}
"""

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

try:
    server.login(sender, password)
    print("logged-in")

    server.sendmail(sender, receiver, message)
    print("Email sent!")

except smtplib.SMTPAuthenticationError:
    print("Não foi possivel logar!")

finally:
    server.quit()