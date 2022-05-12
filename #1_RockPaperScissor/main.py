import random

print(" Write 0 for ROCK \n Write 1 for PAPER \n Write 2 for SCISSORS /n ")
userInput = int(input())

computerInput = random.randint(0, 2)

lList = [

    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
    ,
    '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
    ,
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

]

winner = '''__$$$$_______________$$$$
_$____$_____________$____$
$____$_____________ $_____$
$____$_______________$____$
$____$$$$$$$$$$$$$$$$$____$
$____$$$$$$$$$$$$$$$$$____$
$____$$$$$$$$$$$$$$$$$$___$
_$___$$$$$$$$$$$$$$$$$$__$
_$___$$$$$$$$$$$$$$$$$$__$
__$__$$$$$$$$$$$$$$$$$$_$
___$_$$$$$$$$$$$$$$$$$_$
____$$$$$$$$$$$$$$$$$$$
_____$$$$$$$$$$$$$$$$$
______$$$$$$$$$$$$$$$
_______$$$$$$$$$$$$$
________$$$$$$$$$$$
_________$$$$$$$$$
__________$$$$$$$
___________$$$$$
_______$$$$$$$$$$$$$'''

print(" You \n " + lList[userInput])
print("\n----xxxx----xxxxx-----\n")
print(" Computer \n " + lList[computerInput] + " \n ")

if userInput > computerInput:
    print(" You Win ")
    print(winner)

elif userInput < computerInput:
    print(" Computer Win \n")
    print(winner)
    print("\n Try again better luck next time ")

else:
    print(" Match draw ")
 