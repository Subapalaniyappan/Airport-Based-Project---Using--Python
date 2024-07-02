def ticket_verification():
    print("Welcome to Chennai International Airport")
    check=input("Is this ticket valid? (press 'yes'): ")
    if check == "yes":
        print("Your ticket is Valid, You are allowed to next process.")
        covid_19_verification()
    else:
        print("Sorry your ticket is invalid.")
def covid_19_verification():
    print("Please go to 1st gate for covid checking")
    check=input("Is this report is Negative or Positive: ")
    if check =="negative":
        print("Your eligible to travel, You are allowed for the next process.")
        immigration_verification()
    else:
        check=="positive"
        print(" Sorry your not eligible to travel for 90 days.")
def immigration_verification():
    print("Please go to 2nd gate for immigration checking")
    check=input("Is this visa is valid? (press 'yes'): ")
    check=input("Is this all proof is ok? (press'yes'): ")
    if check=="yes":
        print("Your eligible to travel, You are allowed for the next process.")
        bag_weight_verification()
    else:
        print("Sorry your proof is invalid so your not allow to travel. ")
def bag_weight_verification():
    print("Please go to 3rd gate for bag weight checking")
    check=input("Enter passenger's bag weight: ")
    if check<="25":
        print("Your eligible to travel, You are allowed for the next process.")
        boarding_pass_verification()
    else:
        print("Please reduce the bag weight or give the fine amount rs 500 per kg")
def boarding_pass_verification():
    print("please give your passport")
    check=input("Is this all ok (press 'yes'): ")
    if check=="yes":
        print("This is your boarding pass")
        print("Thank You for Flying with Us Happy Journey:) ")
    else:
        print("Sorry your proff is invalied")
def main():
    print( "CHENNAI INTERNATIONAL AIRPORT" )
    print("press 1 for ticket verification result")
    print("press 2 for covid 19 verification result")
    print("press 3 for immigration verification result")
    print("press 4 for bag weight result")
    print("press 5 for boarding pass result")
    passenger=input("Enter your verification details: ")
    if passenger=="1":
        ticket_verification()
    elif passenger=="2":
        covid_19_verification()
    elif passenger=="3":
        immigration_verification()
    elif passenger=="4":
        bag_weight_verification()
    elif passenger=="5":
        boarding_pass_verification()
    else:
        print("(please enter 1 to 5 only)")
main()
