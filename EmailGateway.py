"""Sending Emails from gmail"""

import smtplib


class EmailGateway:
    server_port =587
    def __init__(self,*args,**kwargs) -> None:
        self.configure()

    def configure(self):
        s = smtplib.SMTP('smtp.gmail.com',self.server_port)
        print('MAIL'.center(100,'-'))
        print(s.__dict__)
        print('ENDMAIL'.center(100,'-'))
        s.starttls()
        s.login('r.somani.26@gmail.com')
        message = "This is Life"
        s.sendmail('r.somani.26@gmail.com','somani.classes@outlook.com')
        s.quit()



e = EmailGateway()



        