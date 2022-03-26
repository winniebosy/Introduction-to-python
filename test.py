
from doctest import OutputChecker


message = input("What is your char")

for ch in message:
    # Add your code here.
    if ch =='?':
        print('snese much curiosity in you, i do')
    else:
        print('Enthusiastic, you are')




#EX EXAMPLE
#Exercise: Word triangle
# In the workspace below you'll find a partially completed for loop.

#Your goal is to finish the loop so that it prints out the following:
#d
#de
#def
#defi
#defin
#defini
#definit
#definite
#definitel
#definitely

word = "definitely"
length = len(word)

for n in range(length):
    # Add your code here.
    print(word[:n+1])


#write a function that will produce the below
#abracadabra
#abracadabr
#abracadab
#abracada
#abracad
#abraca
#abrac
#abra
#abr
#ab
#a




    def word_triangle(word):
    # Add your code here
    length= len(word)
    for n in range(length):
        print(word[:length-n])
              
word_triangle("abracadabra")

#explanantion
#the slice expression here is word[:length - n]. Since length stays the same while n grows, 
# this means that on each pass through the loop, 
# length - n gets smaller and smaller, from length down to 1. 
# And that means that on each pass, the string that gets printed will be a shorter and shorter piece of word.

