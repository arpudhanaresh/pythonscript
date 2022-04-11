import wget
import time
import os
count;
def autodownload():
     global count;
     while 1:
            wget.download('http://fileupload.arpudhacloud.tk/download.php?id=1&token=fcoZgcU1hmtb8FfLAxYBRVT3tE1Hctqc&download')
            print("sleeping for 5 sec")
            time.sleep(5)
            print("deleting a file")
            os.remove("100MB.bin")
            print("file deleted")
            print("sleeping for 5 sec")
            time.sleep(5)
            count++;
            print("Total number of Count"+str(count));
            
autodownload()
