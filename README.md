# Multithreading Email Service

### This folder contains the Report, PPT and `Multithreading_email` folder which contains the source code of the project.

### In the `Multithreading_email` folder,
- There is a `LIB_README.md` file, which contains information regarding the `.tmplt` files, library implimentation and its usage.
- The `example.py` file is just a simple usage of the `email_lib` library.
- The `thread.py` file is the multithreaded version of it.
- Before you run any of `example.py` or `thread.py`, edit the instances of `emailID` and `username` in those files with your Email ID and Username, from which you want to send the mails.
- Now run the following command to send the mails normally to all the users in the csv file and enter the password of the `emailID` provided earlier when prompted (make sure you are in the `Multithreaded_email` directory before you run the command)
    ```
    python3 example.py
    ```
- Then run the following command to send the mails through multiple threads and observe the speed-up
    ```
    python3 thread.py
    ```
### **Note:** Refer to the `LIB_README.md` file in the `Multithreading_email` folder, to clearly understand about the email_lib library.