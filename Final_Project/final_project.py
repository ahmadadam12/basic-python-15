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
10. https://stackoverflow.com/questions/2507808/how-to-check-whether-a-file-is-empty-or-not
11. https://docs.anaconda.com/anaconda/user-guide/tasks/install-packages/
12. https://stackoverflow.com/questions/35805078/how-do-i-convert-a-password-into-asterisks-while-it-is-being-entered
"""

from email.mime.base import MIMEBase
import getpass
import stdiomask
import smtplib
import email
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os

def get_contacts(filename):
    #split name and email address from contact book file:
    global names
    names = []
    global emails
    emails = []
    global no_contact
    with open(filename, mode='r', encoding = 'utf-8')as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
        #print(names)
        #print(emails)
        if os.stat(filename).st_size == 0:
            no_contact = True
        else:
            no_contact = False
        #print(no_contact)
        return names, emails, no_contact

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

def delete_contact():
    try:
        get_contacts(contact_book)
        if no_contact == False:
            for a_name,an_email in zip(names,emails):
                print(a_name, " : ",an_email)
            del_name = input("Select names from contact list to be deleted separated by comma (e.g: Andi,Budi): ")
            del_name_list = del_name.split(",")
            #print(del_name_list)
            for a_name in del_name_list:
                i = names.index(a_name)
                del names[i]
                del emails[i]
                #print(names)
                #print(emails)
            list_o = []
            for item in names:
                i = names.index(item)
                o = list(names[i] + " " + emails[i] + "\n")
                list_o.append(o)
            with open('receiverlist.txt', 'w') as am:
                for item in list_o:
                    am.writelines(item)
            with open('receiverlist.txt', 'r') as am:
                am.readlines()
        else:
            print("You don't have a contact. Please add a contact")
    except:
        print("There is no contact list. Please add a contact first.")

login = False
contact_book = 'receiverlist.txt'
while True:
    if login == False:
        print("\n**Welcome to AirMail.exe**\n***Visit Us @https://github.com/ahmadadam12***\n\nThis program sends email using GMail.")
        print("Please Log in with your GMail account.")
        #defining email and password of sender:
        MY_ADDRESS = input("E-mail address: ")
        #use getpass to hide the text, stdiomasuk to asterisk it
        PASSWORD = stdiomask.getpass("Password: ")#input("Password: ")
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
    start = int(input("\nPlease choice your action (input number):\n1. Add Contact (add first then send)\n2. Send Email\n3. View Contact\n4. Delete Contact\n5. Quit Program\n"))
    if start == 1:
        #add new contact to the book
        print("Please write these details:")
        name_contact = input("Please write the name: ")
        mail_contact = input("Please write the e-mail address: ")
        new_contact = name_contact + " " + mail_contact + '\n'
        add_contact(new_contact)
    elif start == 2:
        #feature: able to choose recipient from contact book:
        try:
            get_contacts(contact_book)
            if no_contact == False:
                pass
            else:
                print("You don't have a contact. Please add a contact")
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
        need_attach = input("Put an attachement? (y/n): ")
        #send_attachment(need_attach)
        send_email(need_attach)    
    elif start == 3:
        #view contact book
        try:
            get_contacts(contact_book)
            if no_contact == False:
                for a_name,an_email in zip(names,emails):
                    print(a_name, " : ",an_email)
            else:
                print("You don't have a contact. Please add a contact")
        except:
            print("There is no contact list. Please add a contact first.")
    elif start == 4:
        delete_contact()
    elif start == 5:
        print("Thank you!")
        break
    else:
        print("Incorrect input.")