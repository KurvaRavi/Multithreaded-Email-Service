import smtplib


# The login function
def login(emailID, password=None):
    if password == None:
        # Ask for password
        password = input(f"Enter password of {emailID}: ")

    # Create server and establish secure connection
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)
    server.starttls()

    # Login using emailID and password
    server.login(emailID, password)
    print("Login Successful")

    # Return Server
    return server
