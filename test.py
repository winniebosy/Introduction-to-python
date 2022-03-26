
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
