from BeautifulSoup import BeautifulSoup, Tag
import datetime
import os
class update(object):
    def __init__(self, filename):
        self.filename = filename                    #sets the name of the picture file to send
    def updateHTML(self):
        #open the html that is going to be updated
        html = open('index.html',"r+")
        soup = BeautifulSoup(html)

        #define object that will be added to the html
        date =  BeautifulSoup("<p> "+str(datetime.datetime.now()) +"</p>")
        temp = BeautifulSoup('<img src="'+self.filename+'" style="width:304px;height:228px;"/>')

        #insert the object to the html
        soup.body.insert(len(soup.body.contents),date)
        soup.body.insert(len(soup.body.contents),temp)

        #update the html
        html.close()
        with open("index.html", "wb") as file:
            file.write(soup.prettify())
