import mysql.connector
import wget
import time
import os

mydb = mysql.connector.connect(
  host="arpudhacloud.tk",
  database='pqurufmu_checkdatabase',
  user="pqurufmu_arpudha",
  password="arpudha@123"

)
count = 0
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

            select_count_query = """select total_count from downloadcount where name = "total" """
            cursor = mydb.cursor()
            cursor.execute(select_count_query)
            total_count=cursor.fetchall()
            print(int(total_count[-1][-1]))
            final_count_value = int(total_count[-1][-1])

            final_count_value = final_count_value+1
            mySql_update_query = f"""UPDATE downloadcount SET total_count = {final_count_value} where name = "total"  """

            cursor = mydb.cursor()
            cursor.execute(mySql_update_query)
            mydb.commit()

autodownload()



