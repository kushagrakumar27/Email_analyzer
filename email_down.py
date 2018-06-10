import getpass, imaplib, os, datetime, email

user = raw_input("Enter your GMail username:")
pwd = getpass.getpass("Enter your password: ")

# connecting to the yahoo imap server
conn = imaplib.IMAP4_SSL("imap.gmail.com")
try:
    conn.login(user,pwd)
except imaplib.IMAP4.error:
    print "Failed To Login"
    sys.exit(1)

conn.list() #retrieving the mailbox associated with the account
conn.select("INBOX") # here you can choose a mail box like INBOX instead

resp, items = conn.search(None, "(SENTSINCE 02-Jan-2018)") # response code and the data returned by the server. The response code returns OK (unless an error has been encountered). It also specifies the searching criteria for searching. items is an array of space separated string containing the ids for each email generated with the above search command.
id_list = items[0].split() # id_list is list of all the ids. 
print id_list

f1="email_down.txt"
fi=open(f1, 'w')

for emailid in id_list:
    resp, data = conn.fetch(emailid, "(RFC822)") # fetching the mail corresponfing to each id of id_list. "`(RFC822)`" means "get the whole stuff", but you can ask for headers only, etc
    raw_email = data[0][1] # getting the mail content
    mail = email.message_from_string(raw_email) # parsing the mail content into familiar EmailMessage object

    #Check if any attachments at all
    if mail.get_content_maintype() != 'multipart':
        continue

    fi.write ("["+mail["From"]+"]"+"::" +"\t" + mail["Subject"]+"::" +"\t" + mail["Received"]+"::" +"\t" +resp +"::" +"\t" + "".join(emailid) +"\n")

conn.close()
conn.logout()

