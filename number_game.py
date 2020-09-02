import random
r=random.randint(1,20)
while(True):
	print("guess a number")
	n=int(input())
	if(n>r):
		print("worng guess!! try a smaller number")
	elif(n<r):
		print("wrong guess!! try a greater number")
	else:
		print("congrats!! you've guessed the right number")
		break;