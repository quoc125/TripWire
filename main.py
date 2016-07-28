'''
Created on Jul 28, 2016
TripWire
@author: Brandon Royal
         Quoc Le
         Sayeed Tahseen
         Gilbert Vieux
'''
from Email import Email
from cam import cam
from update import update
from FTP import FTPClass
from gpiozero import LightSensor
from time import sleep
import datetime

def main():
    print ("test")
    #in
    ldr = LightSensor(4) ;
    var = 1
    value = 1
    #have the  program loop forever or until the user close the file
    while var != 0:
        var = 1
        if ldr.value != 0:
            toaddr = "tripwiretestemail@gmail.com"  #email address to send email to
            now = datetime.datetime.now()           #time and date that the laser is tripped
            filename = str(now) + ".JPG"                   #name of picture file to send
            #take a picture
            newcam = cam(filename)
            newcam.takePic()
            #send the notification that the wire is tripped with the photo
            newEmail = Email(toaddr, filename)
            newEmail.SendEmail()
            #update the html
            up = update(filename)
            up.updateHTML()
            #upload the file to update the website
            upload = FTPClass()
            upload.UploadFile(filename)
            upload.UploadFile("index.html")
        #won't anymore picture to be taken until the laser hit the sensor
	    while ldr.value !=0:
		    print('0')
	else:
	    print('X')

main()
