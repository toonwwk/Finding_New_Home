import email
import smtplib
class SendingEmail():
    def __init__(self, receiver, subject, message):
        self.receiver = receiver
        self.subject = subject
        self.message = message

    def sending(self):
        msg = email.message_from_string(self.message)
        msg['From'] = 'toonwwk@hotmail.com'
        msg['To'] = self.receiver
        msg['Subject'] = self.subject
        s = smtplib.SMTP("smtp.live.com", 587)
        s.ehlo()
        s.starttls()
        s.ehlo()
        s.login('toonwwk@hotmail.com', 'atm8116660')
        s.sendmail('toonwwk@hotmail.com', self.receiver, msg.as_string())
        s.quit()