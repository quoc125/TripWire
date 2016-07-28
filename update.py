'''
Created on Jul 28, 2016
TripWire
@author: Brandon Royal
         Quoc Le
         Sayeed Tahseen
         Gilbert Vieux
'''
from BeautifulSoup import BeautifulSoup, Tag
import datetime
import os
class update(object):
    def __init__(self, filename):
        self.filename = filename                    #sets the name of the picture file to send
    def updateHTML(self):
        #open the html that is going to be updated
        fileOpened = False
        #if the index existed, update the file
        try:
            html = open('index.html',"r+")
            soup = BeautifulSoup(html)
            fileOpened = True
        #if opening the file failed, created a new index.html file
        except IOError:
            html = """
            <!DOCTYPE html>
            <html>
             <head>
              <title>
               Storage
              </title>
             </head>
             <body>
              <h1 style="text-align:center:">
               Trip Wire
              </h1>
              <h2 style="text.align:center;">
               Team 5
              </h2>
              <h3 style="padding-left:  3px;">
               Client Photos
              </h3>
             </body>
            </html>
            """
            soup = BeautifulSoup(html)


        #define object that will be added to the html
        date =  BeautifulSoup("<p> "+str(datetime.datetime.now()) +"</p>")
        temp = BeautifulSoup('<img src="'+self.filename+'" style="width:304px;height:228px;"/>')

        #insert the object to the html
        soup.body.insert(len(soup.body.contents),date)
        soup.body.insert(len(soup.body.contents),temp)

        #close the file, it it existed
        if fileOpened == True:
            html.close()
        #write the index.html
        with open("index.html", "wb") as file:
            file.write(soup.prettify())
