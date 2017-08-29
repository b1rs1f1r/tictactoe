board=[["___","___","___"],["___","___","___"],["___","___","___"]]

print("\n"*15)

for z in board:
	print("\t".expandtabs(30),*z,end="\n"*3)

winning_standart=[[[0, 0], [1, 0], [2, 0]],
[[0, 1], [1, 1], [2, 1]],
[[0, 2], [1, 2], [2, 2]],
[[0, 0], [0, 1], [0, 2]],
[[1, 0], [1, 1], [1, 2]],
[[2, 0], [2, 1], [2, 2]],
[[0, 0], [1, 1], [2, 2]],
[[0, 2], [1, 1], [2, 0]]]

x_status=[]
o_status=[]

row=1

while True:
	if row % 2 == 0:
		sign="X".center(3)
	else:
		sign="O".center(3)

	print()
	print("SIGN: {}\n".format(sign))

	x=input("top to bottom [1,2,3]: ".ljust(30))
	if x=="q":
		break

	y=input("left to right [1,2,3]: ".ljust(30))
	if y=="q":
		break

	x=int(x)-1
	y=int(y)-1

	print("\n"*15)

	if board[x][y]=="___":
		board[x][y]=sign
		if sign=="X".center(3):
			x_status+=[[x,y]]
		elif sign=="O".center(3):
			o_status+=[[x,y]]
		row+=1
	else:
		print("\nHERE ISN'T EMPTY. TRY AGAIN.\n")

	for z in board:
		print("\t".expandtabs(30),*z,end="\n"*3)

	for z in winning_standart:
		o=[v for v in z if v in o_status]
		x=[v for v in z if v in x_status]
		
		if len(o)==len(z):
			print("O WON!")
			quit()
		if len(x)==len(z):
			print("X WON!")
			quit()