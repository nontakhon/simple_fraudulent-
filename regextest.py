import re
import pandas as pandas
import email

emails = []

fh = open(r"test_emails.txt","r").read()


contents = re.split(r"From r", fh)
contents.pop(0)


for item in contents:
    emails_dict = {}

    sender = re.search(r"From:.*", item)

    if sender is not None:
        s_email = re.search(r"\w\S*@.*\w", sender.group())
        s_name = re.search(r":.*<", sender.group())
    else:
        s_email = None
        s_name = None

   
    

    if s_email is not None:
        sender_email = s_email.group()
    else:
        sender_email = None
    # Add email address to dictionary.
    emails_dict["sender_email"] = sender_email

    if s_name is not None:
        sender_name = re.sub("s*<", "", re.sub(":s*", "", s_name.group()))
    else:
        sender_name = None

    # Add sender's name to dictionary.
    emails_dict["sender_name"] = sender_name



    recipient = re.search(r"To:.*", item)

    if recipient is not None:
        r_email = re.search(r"\w\S*@.*\w", recipient.group())
        r_name = re.search(r":.*<", recipient.group())
    else:
        r_email = None
        r_name = None

    if r_email is not None:
        recipient_email = r_email.group()
    else:
        recipient_email = None

    emails_dict["recipient_email"] = recipient_email

    if r_name is not None:
        recipient_name = re.sub("\s*<", "", re.sub(":\s*", "", r_name.group()))
    else:
        recipient_name = None

    emails_dict["recipient_name"] = recipient_name
    
    ## ส่วนที่เพิ่มเข้ามา (STATUS)

    status = re.search(r"Status:.*", item)

    if status is not None:
        ro_status = re.search(r"[RO]", status.group())
    else:
        ro_status = None

    if ro_status is not None:
        read_open_status = ro_status.group()
    else:
        read_open_status = None

    emails_dict["Status"] = read_open_status

    emails.append(emails_dict)


print("Number of emails: " + str(len(emails_dict)))

print("n")

# Print first item in the emails list to see how it looks.
for key, value in emails[0].items():
    print(str(key) + ": " + str(emails[0][key]))