from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


# A class that represents a mail template
class Mail():

    def __init__(self, emailID, username, template):
        self.emailID = emailID
        self.username = username

        self.msg = MIMEMultipart('alternative')

        with open(template, 'r') as f:
            data = f.read()

        subject, text, html = data.split('~~~')
        self.subject = subject.strip()
        self.text = text.strip()
        self.html = html.strip()

    # Generate the message from the user info
    def generate_message(self, user):

        self.subject = self.subject.format(
            name=user['Name'],
            email=user['Email']
        )

        self.text = self.text.format(
            name=user['Name'],
            email=user['Email']
        )

        self.html = self.html.format(
            name=user['Name'],
            email=user['Email']
        )

        self.msg.attach(MIMEText(self.text, 'plain'))
        self.msg.attach(MIMEText(self.html, 'html'))
        self.msg['From'] = formataddr(
            (str(Header(self.username, 'utf-8')), self.emailID)
        )

        self.msg['To'] = user["Email"]
        self.msg['Subject'] = self.subject

        return self.msg

    def attachment(self, attachment):
        with open(attachment, 'rb') as f:
            file = MIMEBase("application", "octet-stream")
            file.set_payload(f.read())

        encoders.encode_base64(file)

        file.add_header(
            "Content-Disposition",
            f"attachment; filename= {attachment}",
        )

        self.msg.attach(file)
