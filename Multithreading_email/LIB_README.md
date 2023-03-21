# Email Lib

### A library to automate sending of emails and templating

## Requirements

- Python 3.5 or later
- Pandas for python

## How to Use

1. ### Creating a template

   The library uses a new file format with extension
   `.tmplt`. These are "template" files which help to
   create templates for emails.

   This file is used to create a template of the mail that you wish to send. A template file has 3 parts.
   They are written in sequence w.r.t. the order they should appear in the template file.

   - The subject
   - Text content
   - HTML content

   Each of these sections are separated by 3 tilde characters "~~~".

   Example of the template file.

   ```
   This is the subject.

   ~~~

   This is the plain text component of the email.

   ~~~

   <strong>This is the HTML component of this email</strong>

   <p>This component supports HTML tags and formatting.</p>
   ```

   Template files also support context injections. Thus they are dynamic and can be changed to customise an email.

   In order to make template files dynamic, python string formating syntax must be followed.

   If your context has a "name" property, use curly braces surrounding "name". In the final email. eg: `Hello {name}!`.

   `{name}` will be replaced by the name variable in the context.

   See examples in the templates directory for more clarity.

2. ### Writing Python code

   To send emails import the email_lib library.

   ```python
   import email_lib
   ```

   To read data from csv files we import pandas.

   ```python
   import pandas as pd
   ```

   Reading data from CSV files and looping over the dataset is not covered here. Refer to `example.py` for sample code.

   Then we need information about the sender.
   Write the following details in the code which corresponds to the email address you want to send it to.

   ```python
   emailID = 'sampleemail@gmail.com'
   username = 'Sample User Name'
   ```

   Also write in the code the location of the template file.

   ```python
   template = './templates/template.tmplt'
   ```

   Here the template is stored in a separate folder called `templates` with a file `template.tplt`.

   Now we need to establish a connection with smtp servers and secure it. This is done by the login function.

   To get a server object use the login function.

   ```python
   server = email_lib.login(emailID)
   ```

   You will have to manually enter the password once the script is run.

   This `server` object can now be used to send mails however we now need to create an mail to send it.

   This process is made quite fast with the use of the template files.

   We will now create an email object that represents are template which is not yet customised.

   To create an email object, use the following code

   ```python
   mail = email_lib.Mail(emailID, username, template)
   ```

   This constructs a mail template which can now be edited to customise it.

   To make a customisable email, we must have a context that should be available to the template. Eg - Online Users might have email addresses and Names and phone numbers.

   These 3 properties must be available in the context so that these can be injected into the template file.

   A context is an python dictionary with all the properties to be injected listed.

   For the given data:

   | Index | Email                          | Name           |
   | ----- | ------------------------------ | -------------- |
   | 1     | reddy.17@iitj.ac.in            | Sainath Reddy  |
   | 2     | kurva.1@iitj.ac.in             | Kurva Ravi     |

   The following context can be formed.

   ```python
    context = {
        'Index': user[0],
        'Email': user[1],
        'Name': user[2]
    }
   ```

   Once a context is formed we can create the custom message from the template.

   To obtain the final message. Use the `generate_message` method of the Mail class. You must pass the context variable in the function.

   This will customise the email to suit the context. Which in this case is the user's Email and name.

   ```python
   message = mail.generate_message(context)
   ```

   Finally send the email using the server object from earlier and pass the message to be sent. In this case it is the `message` variable.

   ```python
   server.send_message(message)
   ```

- ### Optional Changes.

  To add attachments to emails.

  First define the path of the attachment. It can be any file supported by emails services which are not filtered by spam and virus filters.

  ```python
  file = 'test.jpg'
  ```

  And create an email object using steps given above.

  Before we generate our custom message by using `generate_message()`. We must add the attachment to the email.

  Use the `attachment` method of the Mail class to add files.

  ```python
  mail.attachment(file)
  ```

  Now the email has an attachment with it. Multiple attachments can be added by repeating the above step.

  Now we can generate the message and send it as usual.

## Note:

For each email that is sent, a new Mail instance must be created. If the same mail instance is sent to multiple users, it will be rejected as spam. Observe in `example.py` the Mail instances are created **inside** the for loop.

If objects are created outside of the for loop. They will be rejected.
