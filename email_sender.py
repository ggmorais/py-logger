import smtplib, ssl

port = 465  # For SSL
smtp_server = ""
sender_email = ""  # Enter your address
receiver_email = ""  # Enter receiver address
password = ""
message = ""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)