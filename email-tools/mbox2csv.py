import mailbox
import csv

writer = csv.writer(open("clean_mail_B.csv", "wb"))
for message in mailbox.mbox('emails/aimee.eng.mbox'):
    writer.writerow(message)