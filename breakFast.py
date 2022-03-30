#Get input and use it to determine what happens next
#Handle bad input without crashing
#Be flexible with the input the user can enter
#Print messages to the console, with a short pause after each one
#Allow the player to order again if they like

#user input in case of choice

#displays the information before a user orders
import time

print("Hello! I am Bob, the Breakfast Bot.")
time.sleep(2)
print("Today we have two breakfasts available.")
time.sleep(2)
print("The first is waffles with strawberries and whipped cream.")
time.sleep(2)
print("The second is sweet potato pancakes with butter and syrup.")
time.sleep(2)
        

user_response =""

#loop, asking the user for input over and over
while user_response != "waffles" and user_response != "pancakes" :
        user_response = input("Please place your order. Would you like waffles or pancakes?\n").lower() 
        
#user selects waffles or pancakes
        if "waffles" in user_response:
            print("Waffles it is!")
            break
    
        elif "pancakes" in user_response:
            print("Pancakes it is!")
            break
 #when response not available   
        else:
            print("""Sorry, Your order is currently not available.""")

print("Your order will be ready shortly")
time.sleep(2)

second_order= input("Would you like to place another order? Please say 'yes' or 'no: \n").lower()

if "no" in second_order:
    print("Ok! Goodbye..See you next time")
    time.sleep(2)
     break

elif 'yes' in second_order:
    print("Very good, I'm happy to take another order.")
time.sleep(2)