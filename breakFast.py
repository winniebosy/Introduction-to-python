#Get input and use it to determine what happens next
#Handle bad input without crashing
#Be flexible with the input the user can enter
#Print messages to the console, with a short pause after each one
#Allow the player to order again if they like

#user input in case of choice

#displays the information before a user orders
import time

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

print_pause("Hello! I am Bob, the Breakfast Bot.")
print_pause("Today we have two breakfasts available.")
print_pause("The first is waffles with strawberries and whipped cream.")
print_pause("The second is sweet potato pancakes with butter and syrup.")

        

while True:
#loop, asking the user for input over and over
        while True:
            user_response = input("Please place your order. Would you like waffles or pancakes?\n").lower() 
        
#user selects waffles or pancakes
            if "waffles" in user_response:
                print("Waffles it is!")
                print("Your order will be ready shortly")
                break
    
            elif "pancakes" in user_response:
                print("Pancakes it is!")
                print("Your order will be ready shortly")
                break
 #when response not available   
            else:
                print("""Sorry, Your order is currently not available.""")
            time.sleep(2)
            
        while True: 

          second_order= input("Would you like to place another order? Please say 'yes' or 'no: \n").lower()
       
          if "no" in second_order:
                print("OK! Thank you.See you next time")
                time.sleep(2)
                break
           
          elif 'yes' in second_order:
                print("Very good, I'm happy to take another order.")
                time.sleep(2)
          else:
                print("I do not understand your order")
                time.sleep(1)
                break
            #breaking the loop
        