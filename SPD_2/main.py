import scheduling_2
import time
import csv


set_index = 0
data_dir = "data/"
default_data_file = "neh.data.txt"


ans = True
while ans:
    if not default_data_file:
        file_name = "data/" + str(input("Enter name of the data file: "))
    else:
        file_name = data_dir + default_data_file
    dummy = scheduling_2.read_data_file(file_name, set_index+1, no_names=False)[set_index]
    print("""
    0.Exit/Quit
    1.Bruteforce
    2.Johnson rule
    3.Naive scheduling
    4.NEH
    """)
    ans = 4 #int(input("What would you like to do? "))
    if ans == 0:
        print("/n Goodbye")
    elif ans == 1:
        if scheduling_2.verify_dataset(dummy):
            print("Cmax: ", scheduling_2.bruteforce(dummy))
            print(dummy.schedule)
            scheduling_2.gantt_chart(dummy)
        else:
            print("Dataset is not in correct format!")
    elif ans == 2:
        if scheduling_2.verify_dataset(dummy):
            print("Cmax: ", scheduling_2.johnson_rule_multiple(dummy))
            print(dummy.schedule)
            scheduling_2.gantt_chart(dummy)
        else:
            print("Dataset is not in correct format!")
    elif ans == 3:
        if scheduling_2.verify_dataset(dummy):
            print("Cmax: ", scheduling_2.naive(dummy))
            print(dummy.schedule)
            scheduling_2.gantt_chart(dummy)
        else:
            print("Dataset is not in correct format!")
    elif ans == 4:
        if scheduling_2.verify_dataset(dummy):
            print("Cmax0: ", scheduling_2.neh(dummy))
            print(dummy.schedule)
            #scheduling_2.gantt_chart(dummy)
            print("Cmax1: ", scheduling_2.neh1(dummy))
            print(dummy.schedule)
            #scheduling_2.gantt_chart(dummy)
            print("Cmax2: ", scheduling_2.neh2(dummy))
            print(dummy.schedule)
            #scheduling_2.gantt_chart(dummy)
            print("Cmax3: ", scheduling_2.neh3(dummy))
            print(dummy.schedule)
            #scheduling_2.gantt_chart(dummy)
        else:
            print("Dataset is not in correct format!")
    else:
        print("\n Not valid choice try again")
    ans = False