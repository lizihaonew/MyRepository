# -*- coding: utf-8 -*-
# @Author  : Li Zihao
# @Time    : 2020/12/30 15:08
# @File    : IOS_monkey.py


from exchangelib import Credentials, Account, DELEGATE, Message, HTMLBody, FileAttachment
import base64
import os

myemail_account = 'lizihao@dangdang.com'
myemail_password = str(base64.b64decode('YUExMjM0NTY='), 'utf-8')


def send_email(title, body, recipiers, path=None):
    print('email sending...')
    creds = Credentials(
        username=myemail_account,
        password=myemail_password
    )
    account = Account(
        primary_smtp_address=myemail_account,
        credentials=creds,
        autodiscover=True,
        access_type=DELEGATE
    )
    m = Message(
        account=account,
        subject=title,
        body=HTMLBody(body),
        to_recipients=recipiers
    )
    if path:
        with open(path, 'rb') as f:
            cont = f.read()
        attch_file = FileAttachment(name='ios_monkey.log', content=cont)
        m.attach(attch_file)

    m.send()


if __name__ == '__main__':
    email_title = 'title_test'
    email_body = 'body_test'
    email_recier = ['lizihao@dangdang.com']
    att_file = '/Users/xujuan/Downloads/MyRepository/mydemos/IOS_monkey/logs/20210106162427.log'
    # send_email(email_title, email_body, email_recier, att_file)
    print(os.path.getsize(att_file))

