##
# Python Email Downloader Tool
# -
# - This is intended for an individual user to search emails (via IMAP)
# - and download the email and attachments.
# 
# imap-tools: https://github.com/ikvk/imap_tools#search-criteria
# imap-tools package: https://pypi.org/project/imap-tools/
# imap-tools examples: https://github.com/ikvk/imap_tools/tree/master/examples
#
# imap-tools, download attachments example: https://github.com/ikvk/imap_tools/blob/master/examples/email_attachments_to_files.py
# This Stackoverflow post helped, too: https://stackoverflow.com/questions/41749236/download-a-csv-file-from-gmail-using-python

import credentials_dev as credentials
import config_dev as config
# from imap_tools import MailBox, AND
import emailtools

test = emailtools
print(test)

imap_box = credentials.email['imap_box']
acct_username = credentials.email['username']
pwd = credentials.email['password']

sender_email = 'HomeDepot@order.homedepot.com'
search_text = 'Your Electronic Receipt'

# Step 1 - Enable IMAP communication within Gmail
# Step 2 - Create an "app password" for use with Gmail
#   - Google requires more than a simple username + password for auth
#   - Additionally, MFA is near-standard for Google accounts, and can't
#       really be used with automated solutions like this one.
#   - Google Account > Security > Signing in to Google > App passwords
#       - Create an "app password" for use with this Python script. It 
#       works like an API token.
# Step 3 - Change 'sender_email' and 'search_text' for desired emails
# Step 4 - Run script

# Search mailbox for emails from a specific sender, and text
with MailBox(imap_box).login(acct_username, pwd) as mailbox:
    for msg in mailbox.fetch(AND(from_=sender_email, text=search_text)):
        print(msg.date, msg.subject, len(msg.text or msg.html))

        # This downloads the individual emails (as .eml)
        # Brief explanation of where to look for downloading the individual emails:
        # - https://github.com/ikvk/imap_tools/blob/master/examples/email_to_file.py
        # - https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.as_bytes
        with open(config.local['save_location'] + '{}'.format(str(msg.date)[0:10] + '_' + msg.subject + '.eml'), 'wb') as f:
            f.write(msg.obj.as_bytes()) # this is where the bytes are

        # This downloads the attachments (file extension is embedded in the 'att.filename' variable)
        for att in msg.attachments:
            print(att.filename, att.size)
            with open(config.local['save_location'] + '{}'.format(str(msg.date)[0:10] + '_' + att.filename), 'wb') as f:
                f.write(att.payload)