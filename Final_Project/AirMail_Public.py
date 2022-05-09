"""
These codes credits go to: 
1. https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/
2. https://stackoverflow.com/questions/38825943/mimemultipart-mimetext-mimebase-and-payloads-for-sending-email-with-file-atta
3. https://python.hotexamples.com/examples/email.mime.multipart/MIMEMultipart/-/python-mimemultipart-class-examples.html
4. https://www.w3schools.com/
5. https://stackoverflow.com/questions/62319056/how-to-print-a-loops-result-horizontally-with-a-string-in-python
6. https://stackoverflow.com/questions/63044254/attributeerror-list-object-has-no-attribute-encode-when-sending-an-email
7. https://stackoverflow.com/questions/25346001/add-excel-file-attachment-when-sending-python-email
8. https://realpython.com/python-send-email/#adding-attachments-using-the-email-package
9. https://docs.python.org/3/library/email.message.html
"""

from email.mime.base import MIMEBase
import smtplib
import email
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def get_contacts(filename):
    #split name and email address from contact book file:
    global names
    names = []
    global emails
    emails = []
    with open(filename, mode='r', encoding = 'utf-8')as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
        return names, emails

def add_contact(new_contact):
    with open(contact_book, 'a', encoding = 'utf-8') as contact_list:
        contact_list.write(new_contact)

def send_email(need_attach):
    if need_attach == 'n':
        pass
    else:
        attach_loc = input("Input file location: ")
        attach_name = input("Describe your file name and extentsion (e.g: attachment.pdf): ")
        with open(attach_loc, 'rb') as attachment:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())
        # Encode file in ASCII characters to send by email 
        encoders.encode_base64(part)
        # Add header as key/value pair to attachment part
        part.add_header('Content-Disposition', 'attachment', filename=attach_name)

    for name,email in zip(recipient_name_list,recipient_email_list):
        msg = MIMEMultipart()  #create a message
        msg['From'] = MY_ADDRESS
        msg['To'] = ", ".join(recipient_email_list) #this msg['To'] only accept string
        msg['Subject'] = subject
        
        msg.attach(MIMEText(message_text))
        if need_attach == 'n':
            pass
        else:
            msg.attach(part)

    try:
        s.send_message(msg)
        del msg
        print("Email sent")
    except:
        print("error sending email")    
    #Terminate SMTP Session and close connection
    s.quit()

login = False
while True:
    if login == False:
        print("\n**Welcome to AirMail.exe**\n\nThis program is to send your email using GMail.")
        print("Please Log in with your GMail account.")
        #defining email and password of sender:
        MY_ADDRESS = input("E-mail address: ")
        PASSWORD = input("Password: ")
        contact_book = 'receiverlist.txt'
        try:
            s = smtplib.SMTP(host = 'smtp.gmail.com', port = 587)
            s.starttls()
            s.login(MY_ADDRESS,PASSWORD)
            print("Login success!")
            login = True
        except:
            print("Cannot find your account.\nMay be you could lower your security.\nFor reference: https://myaccount.google.com/lesssecureapps")
            continue
    else:
        pass
    start = int(input("\nPlease choice your action (input number):\n1. Add Contact (add first then send)\n2. Send Email\n3. View Contact\n4. Quit Program\n"))
    if start == 1:
        #add new contact to the book
        print("Please write these details:")
        name_contact = input("Please write the name: ")
        mail_contact = input("Please write the e-mail address: ")
        new_contact = name_contact + " " + mail_contact
        add_contact(new_contact)
    elif start == 2:
        #feature: able to choose recipient from contact book:
        try:
            get_contacts(contact_book)
        except:
            print("There is no contact list. Please add a contact first.")
            continue
        for a_name,an_email in zip(names,emails):
            print(a_name, " : ",an_email)
        recipient_name = input("Select recipient by inputting names from the list seperated by comma (e.g: Budi): ")
        recipient_name_list = recipient_name.split(",")
        recipient_email_list = []
        for a_send_to in recipient_name_list:
            if a_send_to in names:
                i = names.index(a_send_to)
                recipient_email_list.append(emails[i])
            else: 
                print("Wrong recipient input. Please check again. \n")
                break
        #showing email format to user:
        print(f"Recipient: ", end = '')
        for r in recipient_email_list:
            print(r, end=', ')
        subject = input("\nSubject: ")
        message_text = input("Message: ")    
        need_attach = input("Put attachement? (y/n): ")
        #send_attachment(need_attach)
        send_email(need_attach)    
    elif start == 3:
        #view contact book
        try:
            get_contacts(contact_book)
            for a_name,an_email in zip(names,emails):
                print(a_name, " : ",an_email)
        except:
            print("There is no contact list. Please add a contact first.")
    elif start == 4:
        print("Thank you!")
        break
    else:
        print("Incorrect input.")