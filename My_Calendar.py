"""so here i have built an calendar with variety of options for you to do !,  why dont you give it a try"""

from time import sleep, strftime

U = input("Enter your name: ")

calender = {

}

def welcome():
    print("Welcome ," + U + ".")
    print("The Calendar issss OPENING....!!!")
    sleep(1)
    print("Today is: " + strftime("%A %B %d,,%Y"))
    print("What would you like to do ??" + U)

def start_calendar():
    welcome()
    start = True

    while start:
        user_choice = input("A to Add, U to Update, V to View, D to Delete, X to Exit: ")
        user_choice = user_choice.upper()

        if user_choice == 'V':
            if len(calender.keys()) < 1:
                print("Calender is empty.")
            else:
                print(calender)

        elif user_choice == 'U':
            date = input("What date?")
            update = input("Enter the update: ")
            calender[date] = update
            print("Update successful")

        elif user_choice == 'A':
            event = input("Enter event:")
            date = input("Enter date (MM/DD/YYYY):")

            if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
                print("invalid date entered retry again ")
                try_again = input("Try Again? Y for Yes,N for No: ")
                try_again = try_again.upper()

                if try_again == 'Y':
                    continue
                else:
                    start = False
            else:
                calender[date] = event
                print("event was successfully added")
                print(calender)

        elif user_choice == 'D':
            if len(calender.keys()) < 1:
                print("calender is empty")
                print(calender)
            else:
                event = input("What event??")
                for date in list(calender.keys()):
                    if event == calender[date]:
                        del calender[date]
                        print("Deletion Complete")
                        print(calender)
                    else:
                        print("Incorrect Event was specified")

        elif user_choice == 'X':
            start = False

        else:
            print("Invalid Command")
            start = False

start_calendar()