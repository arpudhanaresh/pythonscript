import wget
import time
import os


count=0;
def autodownload():
     global count;
     while 1:
            filename = wget.download('http://movie.arpudhacheck.online/200MB.zip')
            print("sleeping for 2 sec")
            
            time.sleep(2)
            os.remove(filename)
            print("file deleted")
            count = count+1;
            print("Total number of Count"+str(count));
            
autodownload()
