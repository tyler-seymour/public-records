# -*- coding: utf-8 -*-

import email
import bs4
import mailbox

mbox = mailbox.mbox('./emails/shanthi.gonzales.mbox')

# The number of emails in the mbox file.
print(len(mbox.keys()))

# The "Delivered-To" header of the first email.
print(mbox[0].get('Delivered-To'))


for message in mbox:
    # subj = message['subject']
    # sender = message['from']
    # content = message.get_payload()
    # print(content)
    # print(message['to'])
    # list2 = [x.replace('\n', '') for x in message['to']]
    print([message['from'], message['to'], message['subject'], message['date'], message['text']])

for item in mbox.iteritems():
    print(item)

#text = ''

# def handle(s):
#     global text
#     soup = bs4.BeautifulSoup(s, 'html.parser')
#     for elem in soup.findAll(['script', 'style']):
#         elem.extract()
#     text = text + '\n' + soup.get_text()
#
# for msg in mbox:
#     pyl = msg.get_payload(decode=True)
#     if pyl is None:
#         pyl = msg.get_payload()
#     if type(pyl) == list:
#         p = pyl[0]
#         q = p.get_payload(decode=True)
#         if q is not None:
#             handle(q)
#         else:
#             r = p.get_payload()
#             if type(r) == list:
#                 handle(str(r[0]))
#             else:
#                 handle(r)
#     else:
#         handle(pyl)
#         pass
#
# print(text.encode('utf8'))
