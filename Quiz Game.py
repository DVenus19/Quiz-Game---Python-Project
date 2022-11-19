print("☆☆☆☆☆☆☆☆☆☆Python Project☆☆☆☆☆☆☆☆☆☆")
print("☆☆☆☆☆☆☆☆☆☆Programmed by: Donasco, Venus M.☆☆☆☆☆☆☆☆☆☆")
print("☆☆☆☆☆☆☆☆☆☆BSCOE 2-2☆☆☆☆☆☆☆☆☆☆")

#In this python program, i am going to create a quiz game
print("Hello and Welcome to my Quiz Game!")
print("Let's test your knowledge shall we? ")
play = input("Do you want to play the quiz game? ")
if play.lower() != 'yes':
	quit()
print("Okay! let's begin the quiz!")
score = 0

answer = input("\n\n ----------Who developed Python Programming Language?---------- \n\n"
"a. wick van rossum\n"
"b. rasmus lerdorf\n"
"c.guido van rossum\n"
"d.niene stom\n")
if answer.lower() == "c":
	print('Correct! Python Language is designed by Dutch programmer Guido van Rossum in the Netherlands')
	score += 1
else:
	print("Incorrect! that's not the answer")

answer = input("\n\n ----------Which of the following is the correct extension of the Python file? ---------- \n\n"
"a. .python\n"
"b. .pl\n"
"c. .p\n"
"d. .py\n")
if answer.lower() == "d":
	print('Correct! .py is the correct extension of the python file ')
	score += 1
else:
	print("Incorrect! that's not the answer")
	
answer = input("\n\n ----------Is Python case sensitive when dealing with identifiers?---------- \n\n"
"a. Yes\n"
"b. No\n"
"c.Machine dependent\n"
"d.none of the above\n")
if answer.lower() == "a":
	print('Correct! Case is always significant')
	score += 1
else:
	print("Incorrect! that's not the answer")
	
answer = input("\n\n ----------Which of the following concepts is not a part of Python?---------- \n\n"
"a. Loops\n"
"b. Dynamic Typing\n"
"c. Pointers\n"
"d. All of the above\n")
if answer.lower() == "c":
	print('Correct! Pointers as a concept is not part of Python')
	score += 1
else:
	print("Incorrect! that's not the answer")
	
answer = input("\n\n ----------Which of the following types of loops are not supported in Python?---------- \n\n"
"a. for\n"
"b. do-while\n"
"c. while\n"
"d. None of the above\n")
if answer.lower() == "b":
	print('Correct! do-while loops are not explicitly a part of the Python Language')
	score += 1
else:
	print("Incorrect! that's not the answer")

print("\n\nCongratulations!! you got " +  str(score)  + " questions correct!!!\n\n")
print("\n\nCongratulations!! you got " +  str((score/ 5 ) *100)  + "%.\n\n")