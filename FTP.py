'''
Created on Jul 28, 2016
TripWire
@author: Brandon Royal
         Quoc Le
         Sayeed Tahseen
         Gilbert Vieux
'''
from ftplib import FTP



class FTPClass(object):

    '''
    Currently unused but kept for future updates
    '''
    def __init__(self):
        None
    '''
    Function used to upload a file to the FTP server.
    File is uploaded to the "pics" folder on the FTP server
    '''
    def UploadFile(self, filename):
        ftp = FTP('tripwire.net16.net')
        ftp.login('a7709364', 'tripwire123')
        ftp.cwd('public_html')
        ftp.storbinary("STOR "  + filename, open(filename, "rb"), 1024)


    '''
    Function used to download a file from the FTP server.
    Currently not needed but here for future updates.
    File is downloaded to the current directory
    '''
    def DownloadFile(self, file):
        ftp = FTP('tripwire.net16.net')
        ftp.login('a7709364', 'tripwire123')
        ftp.cwd('public_html/pics/')
        ftp.retrbinary("RETR " + file ,open(file, 'wb').write)
