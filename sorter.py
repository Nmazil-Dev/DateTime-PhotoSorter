import os
from PIL import Image
from datetime import datetime

#Access the images folder at this path 
path = "C:/Users/ANDY/Desktop/IphonePics/Photos"
student_path = "C:/Users/ANDY/Desktop/IphonePics/"
students = ["JB", "MF", "BT", "JW"]
entries = os.listdir(path)
for student in students:
    try:
        os.mkdir(student_path + student)
    except FileExistsError:
        print("Already exists")

for entry in entries:
    if entry[-3:] == "JPG" or entry[-3] == "MOV":
            photo_path = path + "/" + entry
            try:
                date_time = Image.open(photo_path)._getexif()[36867].split(" ") 
            except KeyError:
                continue

            date_time[0]= date_time[0].replace(":","-",3)
            date_time[1] = date_time[1][:-3]
            date = datetime.strptime(date_time[0], '%Y-%m-%d')
            hour = int(date_time[1][:2])
            minutes = int(date_time[1][-2:])
            if date.weekday() >= 0 and date.weekday() <= 4 and hour < 14 and hour > 7:
                print(date.weekday())
                print(date_time[1])
                print(minutes)
                if hour == 9 and minutes  < 32 or hour == 10 and minutes < 46 or hour == 11 and minutes < 30 or hour == 12 and minutes >= 30 or hour == 13:
                    mkdir_path = student_path + students[0] + "/" + entry
                    os.rename(photo_path, mkdir_path)
                    print (date_time, "JB")
                elif  hour == 9 and minutes > 30:
                    mkdir_path = student_path + students[1] + "/" + entry
                    os.rename(photo_path, mkdir_path)
                    print(date_time, "MF")
                elif hour == 10 and minutes >= 45 or hour == 11 and minutes < 15:
                    mkdir_path = student_path + students[2] + "/" + entry
                    os.rename(photo_path, mkdir_path)
                    print(date_time, "BT")
                elif hour == 11 and minutes >= 30 or hour == 12 and minutes < 30:
                    mkdir_path = student_path + students[3] + "/" + entry
                    os.rename(photo_path, mkdir_path)
                    print(date_time, "JW")
            # date = date_time[0]
            # time = date_time[1]
            # print(date)
            # print(time)