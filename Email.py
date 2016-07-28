'''
Created on Jul 28, 2016
TripWire
@author: Brandon Royal
         Quoc Le
         Sayeed Tahseen
         Gilbert Vieux
'''
import os
import smtplib
# import Email
# import email.mime.multipart
# import email.mime.text
# import email.mime.base
# import email.mime.image
# from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
#from smtplib import toaddrs
# from macpath import basename

#if __name__ == '__main__':
#    pass

class Email(object):

    def __init__(self, toaddr, filename):
        self.toaddr = toaddr                        #sets the address the email will be sent to
        self.filename = filename                    #sets the name of the picture file to send

    def SendEmail(self):
        fromaddr = "tripwiretestemail@gmail.com"    #email address that will be sending the email

        msg = MIMEMultipart()                       #Allows the message to have multiple parts

        msg['From'] = fromaddr
        msg['To'] = self.toaddr
        msg['Subject'] = "Test Email"

        body = "Test"

        msg.attach(MIMEText(body, 'plain'))


        attachment = open( self.filename, "rb").read()     #get the picture file to attach
        image = MIMEImage(attachment, name=os.path.basename(self.filename))
        # part = ('application', 'octet-stream')
        # part.set_payload((attachment).read())
        # encoders.encode_base64(part)
        # part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

        msg.attach(image)

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromaddr, "tripwire")
        text = msg.as_string()
        server.sendmail(fromaddr, self.toaddr, text)
        server.quit()


    # try:

        # print ("Successfully sent email")
    # except smtplib.SMTPException:
        # print ("Error: unable to send email")
