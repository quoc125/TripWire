'''
Created on Jul 5, 2016

@author: Brandon
'''

from Email import Email
from cam import cam


def main():
    print ("test")

    toaddr = "tripwiretestemail@gmail.com"  #email address to send email to
    filename = "photo.JPG"                   #name of picture file to send
    newCam = cam(filename)
    newCam.takePic()
    newEmail = Email(toaddr, filename)
    newEmail.SendEmail()
main()
