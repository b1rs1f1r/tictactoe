tahta=[["___","___","___"],["___","___","___"],["___","___","___"]]

print("\n"*15)

for z in tahta:
	print("\t".expandtabs(30),*z,end="\n"*3)

kazanma_ölçütü=[[[0, 0], [1, 0], [2, 0]],
[[0, 1], [1, 1], [2, 1]],
[[0, 2], [1, 2], [2, 2]],
[[0, 0], [0, 1], [0, 2]],
[[1, 0], [1, 1], [1, 2]],
[[2, 0], [2, 1], [2, 2]],
[[0, 0], [1, 1], [2, 2]],
[[0, 2], [1, 1], [2, 0]]]

x_durumu=[]
o_durumu=[]

sıra=1

while True:
	if sıra % 2 == 0:
		işaret="X".center(3)
	else:
		işaret="O".center(3)

	print()
	print("İŞARET: {}\n".format(işaret))

	x=input("yukarıdan aşağıya [1,2,3]: ".ljust(30))
	if x=="q":
		break

	y=input("soldan sağa [1,2,3]: ".ljust(30))
	if y=="q":
		break

	x=int(x)-1
	y=int(y)-1

	print("\n"*15)

	if tahta[x][y]=="___":
		tahta[x][y]=işaret
		if işaret=="X".center(3):
			x_durumu+=[[x,y]]
		elif işaret=="O".center(3):
			o_durumu+=[[x,y]]
		sıra+=1
	else:
		print("\nORASI DOLU! TEKRAR DENEYİN.\n")

	for z in tahta:
		print("\t".expandtabs(30),*z,end="\n"*3)

	for z in kazanma_ölçütü:
		o=[v for v in z if v in o_durumu]
		x=[v for v in z if v in x_durumu]
		
		if len(o)==len(z):
			print("O KAZANDI!")
			quit()
		if len(x)==len(z):
			print("X KAZANDI!")
			quit()