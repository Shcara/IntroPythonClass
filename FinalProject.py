#Program is a casino slots game
#User will have multiple points at which they can quit
#User will be dismissed if they run out of money




#imported needed Python modules
import random
import time

#welcome message and name input
print("Welcome to the Schmidt Casino!\n")
print("What is your name?")
name_player = input()
print("Welcome " + name_player.title() + ".") 

#Asking if user would like to play slots and getting initial money amount to play with
def ask_user():
	user_answer = input("Would you like to play slots? Yes or No? ")
	if user_answer == 'yes' or user_answer == 'Yes' or user_answer == 'YES':
		print("Wonderful let's get started!")
	elif user_answer == 'no' or user_answer == 'No' or user_answer == 'NO':
		print("Ok! Thanks for trying our game. Have wonderful day!")
		exit()
	else:
		print("I'm sorry I don't understand your response. This game will terminate.")
	print("\n\n")
	print("****************************************************")
	print("****************************************************")
	print("****************************************************")
	print("****************************************************")
	print("****************************************************")
	print("****************************************************")
	print("****************************************************")
	print("****************************************************")
	print("****************************************************")
	print("\n\n")
	print("Each pull of the slot machine is 1 dollar.")
	global gambling_money
	gambling_money = int(input("Please enter how many dollars would you like to load as an integer number: "))
	if gambling_money > 0:
		number_of_pulls = int((gambling_money)/1)
		print("\n")
		print(f'${gambling_money} will allow you {number_of_pulls} attempt to win at slots')
		print("Winning numbers are 7 7 7")
	else:
		print("I'm sorry that is not an integer number. Please try our game again. Goodbye")
		exit()


#defining slot machine function 
def slot_machine():
	global gambling_money
	ready_answer = input("Are you ready to begin? Yes or No? ")
	if ready_answer == 'yes' or ready_answer == 'Yes' or ready_answer == 'YES':
		print("Ok here we go!")
		print("\n\n")
		time.sleep(1)
	elif ready_answer == 'no' or ready_answer == 'No' or ready_answer == 'NO':
		print("Ok! Thanks for trying our game. Have wonderful day!")
		exit()
	else:
		print("I'm sorry I don't understand your response. This game will terminate.")
		exit()
		
	#defining random number generators for slot results
	number1 = random.randint(1,9)
	number2 = random.randint(1,9)
	number3 = random.randint(1,9)
	
	
	#visual for slot machine
	print("***********************************************************")
	print("***********************************************************")
	print("***********************************************************")
	print("***********************************************************")
	print("***********************************************************")
	print("***********************************************************")
	print("***********************************************************")
	print(f"*************",number1,"*************",number2,"************",number3,"************")
	print("***********************************************************")
	print("***********************************************************")
	print("***********************************************************")
	print("***********************************************************")
	print("***********************************************************")
	print("***********************************************************")
	print("***********************************************************")
	print("\n\n")
	
	#winning or losing statement
	if number1 == number2 == number3 == 7:
		print("Congratulations! You are a Winner!!!!")
		print("You won a new car!!")
		print("\n\n")
	else:
		print("Sorry you are not a winner this time.")
		print("\n\n")
	time.sleep(2)
	gambling_money = gambling_money - 1
	
	#determines if user has money to keep playing and also wants to keep playing
	if gambling_money > 0:
		print(f'You have ${gambling_money} left. Would you like to play again? Yes or No?')
		repeat = input()
	else:
		print("You are out of money. Please come again!")
		exit()
	
	if gambling_money > 0 and repeat == 'Yes' or repeat == 'yes' or repeat == 'YES':
		slot_machine()
	else:
		print("Thank you for playing! Please come again!")
		exit()


#main program fuction calling section
ask_user()
slot_machine()
