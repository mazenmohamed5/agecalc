def age():
    agee=input("enter your age: ")
    age_selection = input("do you want your age in minutes or seconds?\n")
    seconds = int(agee) * 365 * 24 * 60 *60 
    minutes = int(agee) * 365 * 24 * 60

    if age_selection == "minutes":
        print("your age in minutes = {} minutes".format(minutes))

    elif age_selection == "seconds":
        print("your age in seconds = {} seconds".format(seconds))

    else: 
        print("please choose minutes or seconds")


   
age()   


    