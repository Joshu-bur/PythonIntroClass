
#Title:  Assignment 5
#Developer:  Joshua Burwell
#Created on:  4/29/2018
#Class:  IT FDN 100 A
#Purpose: Allows user to create and edit lists.
    #First intro into lists and dictionaries

#---all data here---#

objFileLoc = "C:\_PythonClass\Todo.txt"
objTxtFile = ""
list_ToDo = []
flag = 0
dict_item = {}
dict_key = ""
dict_val = ""
str_opt = ""
item_input = ""
Priority_Input = ""
Options = "\n\
\t1: Show Current List\n\
\t2: Add More To Your List\n\
\t3: Remove/Complete a Task\n\
\t4: Save Your List\n\
\t5: Exit\n"
dict_intro = "Item, Priority\n"

############### 1- Inputs ##############

#This pulls out the existing info in the .txt file
#puts together list of items and priorities
objTxtFile = open(objFileLoc, "r")
for row in objTxtFile:
    dict_key = row.strip().split(",")[0]
    dict_val = row.strip().split(",")[1]
    dict_item = {dict_key: dict_val}
    list_ToDo += [dict_item]
objTxtFile.close()

#displays list_ToDo
print("\n" + dict_intro)
for dict_item in list_ToDo:
    for dict_key in dict_item:
        print(dict_key + ", " + dict_item[dict_key])

#Display Menu of options for user to choose from
#Continues to loop through the options until the user chooses to exit
while True:
    print("\nSelect a command below (1-5)")
    print(Options)
    Flag = 0
    Options = input("Command Selection: ")

    #Display 'ToDo' list
    if Options == "1":
        print("\n Here is your list!")
        #print("\n" + dict_intro)
        for dict_item in list_ToDo:
            for dict_key in dict_item:
                print(dict_key + ", " + dict_item[dict_key])

    #New item
    elif Options == "2":
        item_input = input("Add to your 'ToDo' list: ")
        if item_input == "":
            print("Sorry, not saved.")
            continue
        else:
            for dict_item in list_ToDo:
                for dict_key in dict_item:
                    if dict_key == item_input.title():
                        flag += 1
                    else: flag += 0
            if flag > 0:
                print("\nYou've already added this!")
            else:
                while True:
                    Priority_Input = input("High, medium, or low priority task?: ")
                    if Priority_Input != "":
                        dict_item = {item_input.title(): Priority_Input.lower()}
                        list_ToDo += [dict_item]
                        break
                    else: print("Priority can't be blank.")

    #Delete from list and check to see if it's there
    elif Options == "3":
        item_input = input("What task did you complete?: ")
        for dict_item in list_ToDo:
            for dict_key in dict_item:
                if dict_key == item_input.title():
                    list_ToDo.remove(dict_item)
                    flag += 1
                else: flag += 0
        if flag > 0:
            print("\n'The item has been crossed off your list.")
        else: print("\nI don't recognize this, try telling me again.")

    #to save the file
    elif Options == "4":
        objTxtFile = open(objFileLoc, "w")
        for dict_item in list_ToDo:
            for dict_key in dict_item:
                objTxtFile.write(dict_key.title() + "," + dict_item[dict_key] + "\n")
        objTxtFile.close()
        print("\nYour file was saved.")

    #Quit
    elif Options == "5":
        objTxtFile = open(objFileLoc, "w")
        for dict_item in list_ToDo:
            for dict_key in dict_item:
                objTxtFile.write(dict_key.title() + "," + dict_item[dict_key] + "\n")
        objTxtFile.close()
        break

    #loop for errors
    else: print("Not a choice! Try again.")
