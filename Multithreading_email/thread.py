import pandas as pd
import email_lib
from threading import Thread
import time


# Set the location of data.
DATA_DIR = './datasets/'
DATA_NAME = 'example.csv'

data = pd.read_csv(DATA_DIR + DATA_NAME)

# Required for attachments.
file = 'test.jpg'

# Set the email and username
emailID = '<<< Enter your Email ID here >>>'
username = '<<< Enter your Email ID Username here >>>'

# The template file
template = './templates/template.tmplt'


# Login to server
server = email_lib.login(emailID)
print('Starting to send mails.')

tic = time.time()

class EmailThread(Thread):
    def __init__(self, user):
        self.email_to = user
        Thread.__init__(self)

    def run (self):
        mail = email_lib.Mail(emailID, username, template)
        # Create a user context
        context = {
            'Index': self.email_to[0],
            'Email': self.email_to[1],
            'Name': self.email_to[2]
        }

        # Add attachment
        mail.attachment(file)
        message = mail.generate_message(context)

        # Send the email
        print(f"Sent mail to {context['Email']}, {context['Name']}")
        server.send_message(message)

for user in data.itertuples():
    EmailThread(user).start()

toc = time.time()

total_emails = data.shape[0]
time_taken = toc-tic

print(f"Finished sending {total_emails} emails in {time_taken}secs at {total_emails/time_taken} mails/sec")
