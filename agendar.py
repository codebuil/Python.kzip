import csv
import datetime
import os

def load_agenda():
    if os.path.exists("agenda.txt"):
        with open("agenda.txt", 'r') as file:
            reader = csv.reader(file)
            agenda = list(reader)
        return agenda
    else:
        return []

def save_agenda(agenda):
    with open("agenda.txt", 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(agenda)

def check_due_items(agenda):
    current_time = datetime.datetime.now()
    due_items = []
    for item in agenda:
        item_time = datetime.datetime.strptime(item[0] + " " + item[1], "%m/%d/%Y %H:%M")
        if item_time < current_time:
            print_item(item)
            input("Press Enter to remove item from the agenda: ")
            agenda.remove(item)
            save_agenda(agenda)
    

def print_item(item):
    print(f"Date: {item[0]}, Time: {item[1]}, Caption: {item[2]}")


print("\x1bc\x1b[43;30m")

agenda = load_agenda()

while True:
    data = input("Enter date, time, caption (or press Enter to finish): ")
    if data == '':
        break
    data = data.split(',')
    agenda.append([data[0].strip(), data[1].strip(), data[2].strip()])

save_agenda(agenda)
while 1:
    check_due_items(agenda)
    if len(agenda)==0:
        break
  

