import wget
import time
import os


count=0;
def autodownload():
     global count;
     while 1:
            filename = wget.download('http://fileupload.arpudhacloud.tk/download.php?id=1&token=fcoZgcU1hmtb8FfLAxYBRVT3tE1Hctqc&download')
            print("sleeping for 2 sec")
            
            time.sleep(2)
            os.remove(filename)
            print("file deleted")
            count = count+1;
            print("Total number of Count"+str(count));
            
autodownload()
