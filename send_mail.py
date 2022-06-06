from notification.models import Notification
import base64
import ssl
import env
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


def send_email(parsed):
    files = parsed.get('files', [])
    stringify_files = []
    for i in files:
        stringify_files.append(i.get('name', '') + '.' + i.get('extension', ''))

    parsed['sender'] = env.EMAIL
    parsed['files'] = stringify_files
    notify = Notification(parsed)

    msg = MIMEMultipart()

    msg['From'] = env.EMAIL
    msg['To'] = notify.receiver

    msg['Subject'] = notify.title

    msg.attach(MIMEText(notify.message))

    for f in files:
        part = MIMEBase('application', "octet-stream")

        try:
            data = base64.b64decode(f.get('data', None))
        except UnicodeDecodeError:
            data = ''
        part.set_payload(data)
        encoders.encode_base64(part)
        part['Content-Disposition'] = 'attachment; filename=' + f.get('name', None) + '.' + f.get('extension', None)
        msg.attach(part)

    context = ssl._create_unverified_context()
    smtp = smtplib.SMTP(env.SERVER, 25)
    smtp.starttls(context=context)
    smtp.login(env.EMAIL, env.PASSWORD_EMAIL)
    smtp.sendmail(env.EMAIL, notify.receiver, msg.as_string())
    smtp.quit()

