#Get input and use it to determine what happens next
#Handle bad input without crashing
#Be flexible with the input the user can enter
#Print messages to the console, with a short pause after each one
#Allow the player to order again if they like

#user input in case of choice

#displays the information before a user orders
import time

#function for printing messages
def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)
    

def valid_input(prompt, option1, option2):
    while True:
        response = input(prompt).lower() #getting user input and is case insensitive
        #getting and assessing user response
        if option1 in response:
            break
        elif option2 in response:
             break
        else:
            print_pause("Sorry, I do not Understand")
    return response


def intro():
   print_pause("Hello! I am Bob, the Breakfast Bot.")
   print_pause("Today we have two breakfasts available.")
   print_pause("The first is waffles with strawberries and whipped cream.")
   print_pause("The second is sweet potato pancakes with butter and syrup.") 
   
   #getting customer order
def get_order():
       response = valid_input("Please place your order. "
                              "Would you like waffles or pancakes? \n",
                              "waffles", "pancakes")   
       
       if "waffles" in response:
            print_pause("Waffles it is!") 
       elif "pancakes" in response:
           print_pause("Pancakes it is!") 
       print_pause("Your order will be ready shortly")
       
       order_again()


def order_again():
    response = valid_input("Would you like to place another order? "
                           "Please enter 'yes' or 'no'.\n",
                            "yes", "no")
    if "no" in response:
        print_pause("Thank you for your time")
    elif "yes" in response:
        print_pause("Awesome! I am happy to take another order.")
        get_order()


def order_breakfast():
    intro()
    get_order()
    
    
order_breakfast()
    
    
            