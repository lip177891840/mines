import sys
sys.setrecursionlimit(1000000)
save=[]
#list=[[1,1],[1,1]]
list=[[1,1,'*','*','*'],['*',1,1,'*','*'],['*','*','*','*','*'],['*',1,1,1,'*'],['*','*','*',1,'*']]
for i in list:
	for j in i:
		print j,
	print ''

def find(i,j):
	global save
	#top
	if i-1>=0 and ([i-1,j] not in save):
		if list[i-1][j]==1:
			save.append([i-1,j])
			find(i-1,j)
	#right
	if j+1<=4 and ([i,j+1] not in save):
		if list[i][j+1]==1:
			save.append([i,j+1])
			find(i,j+1)
	#down
	if i+1<=4 and ([i+1,j] not in save):
		if list[i+1][j]==1:
			save.append([i+1,j])
			find(i+1,j)
	#left
	if j-1>=0 and ([i,j-1] not in save):
		if list[i][j-1]==1:
			save.append([i,j-1])
			find(i,j-1)

find(2,4)
print save