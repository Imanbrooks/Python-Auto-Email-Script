import smtplib

smtp_server = smtplib.SMTP('smtp.gmail.com', 587)
smtp_server.starttls()
smtp_server.login('isaiahlbrooks@gmail.com', 'zanzpgjnonloioza')

from_address = ''
to_address = ['']
subject = 'Python Auto Email Test'
body = 'This is a test email sent from Python!'
message = f'Subject: {subject}\n\n{body}'

smtp_server.sendmail(from_address, to_address, message)

smtp_server.quit()

print('Email sent successfully to all recipients!')


