
import csv

my_dict={}

with open('臺北市空氣品質監測站基本資料.csv', mode = 'r') as inp:
    #reader = csv.reader(inp)
    
    #dict_from_csv = {rows[0]:rows[1] for rows in reader}
    #reader2 = inp.readlines(20)
    reader3 = inp.readlines()
    #for i in inp:
  #      print(i)
    for j in reader3:
        print(j)
  
  