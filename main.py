from Email import Email
from cam import cam
from update import update
from FTP import FTPClass
from gpiozero import LightSensor
from time import sleep
import datetime

def main():
    print ("test")
    sleep(15)
    ldr = Lightsensor(4) ;
    var = 1
    value = 1
    while var != 0:
        var = 1
        if ldr.value != 0:
            toaddr = "tripwiretestemail@gmail.com"  #email address to send email to
            now = datetime.datetime.now()
            filename = str(now) + ".JPG"                   #name of picture file to send
            newcam = cam(filename)
            newcam.takePic()
            newEmail = Email(toaddr, filename)
            newEmail.SendEmail()
            up = update(filename)
            up.updateHTML()
            upload = FTPClass()
            upload.UploadFile(filename)
            upload.UploadFile("index.html")
            sleep(2)
        else:
            print('x')
main()
