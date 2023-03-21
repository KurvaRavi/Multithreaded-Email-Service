import pandas as pd
import email_lib
# import re

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

# Loop through each user in database
for user in data.itertuples():
    # Create a mail class which contains the mail contents.
    mail = email_lib.Mail(emailID, username, template)
    # Create a user context
    context = {
        'Index': user[0],
        'Email': user[1],
        'Name': user[2]
    }

    # Add attachment
    mail.attachment(file)
    message = mail.generate_message(context)

    # Send the email
    server.send_message(message)
    print(f"Sent mail to {context['Email']}, {context['Name']}")

toc = time.time()

total_emails = data.shape[0]
time_taken = toc-tic

print(f"Finished sending {total_emails} emails in {time_taken}secs at {total_emails/time_taken} mails/sec")
