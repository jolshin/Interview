import email
import smtplib
import imaplib
import ssl

class Mail():
    def __init__(self) -> None:
        self.smtp_service = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
        self.imap_service = imaplib.IMAP4_SSL('imap.yandex.ru', 993)

    # Method connects to SMTP or IMAP depends on if send or recieve mail
    def connect(self, login: str, password: str, service_type: str) -> bool:
        if service_type == 'send':
            self.smtp_service.ehlo()
            self.smtp_service.login(login, password)
            return True
        elif service_type == 'recieve':
            self.imap_service.login(login, password)
            return True
        else:
            return False

    # Method sends mail
    def send(self, login: str, password: str, subject: str, recipient: str, message: str) -> None:
        if self.connect(login, password, 'send'):
            message = f'From: {login}\r\nTo: {recipient}\r\nContent-Type: text/plain; charset="utf-8"\r\nSubject: {subject}\r\n\r\n{message}'
            self.smtp_service.sendmail(login, recipient, message)
            self.smtp_service.quit()

    # Method recieves mails
    def recieve(self, login: str, password: str, header = None) -> str:
        if self.connect(login, password, 'recieve'):
            self.imap_service.select()
            criterion = '(HEADER Subject %s)' % header if header else 'ALL'
            typ, data = self.imap_service.uid('search', None, criterion)
            assert data[0], 'There are no letters with current header'
            for num in data[0].split():
                typ, data = self.imap_service.uid('fetch', num, '(RFC822)')
                #print('Message %s\n%s\n' % (num, email.message_from_bytes(data[0][1])))
                return 'Message %s\n%s\n' % (num, email.message_from_bytes(data[0][1]))
            self.imap_service.close()
            self.imap_service.logout()
        

if __name__ == '__main__':

    new_mail = Mail()

    # Code below is for debug purpose
    #new_mail.send('yourlogin@yandex.ru', 'token', 'subject' ,'toaddr', 'message')
    #new_mail.recieve('yourlogin@yandex.ru', 'token')
