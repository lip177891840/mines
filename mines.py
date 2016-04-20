#encoding=utf-8
import random
import re


hasFinish=0 	#判断是否结束
row=8 		#行数和列数
column=8

rc =[]		#显示的二维数组
minesNum=1 	#雷数

#得到row,column   初始化rc[],计算雷数量
def init_rc():
	global rc
	global row
	global column
	global minesNum
	global hasFinish
	print 'input row and column that you want'
	find=re.compile(r'[0-9]').findall(raw_input('row:  '))
	row=int(find[0])
	if len(find)>=2:
		column=int(find[1])
	else:
		column=int(re.compile(r'[0-9]').findall(raw_input('column:  '))[0])
	for i in range(row):
		rc.append(['*']*column)
	minesNum=row*column/6
	hasFinish=row*column- minesNum


minesIndex=[]	#存放雷的索引
#根据计算得到雷的数量,随机产生雷,存储在minesIndex(坐标)
def createMines():
	global minesNum
	global minesIndex
	global hasFinish
	minesList=[]
	if minesNum>0:
		while len(minesList)<minesNum:
			mine= random.randint(1,row*column)
			if mine not in minesList:
				minesList.append(mine)
	elif minesNum==0:
		hasFinish=hasFinish-1
		minesList.append(random.randint(1,row*column))
		print hasFinish
	for mine in minesList:
		i=mine/column
		j=mine%column
		if j==0:
			i=i-1
			j=column-1
		else:
			j=j-1
		minesIndex.append([i,j])
	print minesIndex
	global rc
	for mine in minesIndex:
		rc[mine[0]][mine[1]]="M"


save=[]	#存储的一个四连通区域
#当点击不是数字和雷的时候,显示片区,这里采用深度优先
def find(i,j):
	global save
	global row
	global column
	#top
	if i-1>=0 and ([i-1,j] not in save):
		if isNot(i-1,j):
			save.append([i-1,j])
			find(i-1,j)
	#right
	if j+1<=column-1 and ([i,j+1] not in save):
		if isNot(i,j+1):
			save.append([i,j+1])
			find(i,j+1)
	#down
	if i+1<=row-1 and ([i+1,j] not in save):
		if isNot(i+1,j):
			save.append([i+1,j])
			find(i+1,j)
	#left
	if j-1>=0 and ([i,j-1] not in save):
		if isNot(i,j-1):
			save.append([i,j-1])
			find(i,j-1)

#显示连通区的旁边区域
def showNearby():
	global save
	nearby=[]
	for s in save:
		i=s[0]
		j=s[1]
		if i-1>=0 and ([i-1,j] not in nearby):
			if not isNot(i-1,j):
				nearby.append([i-1,j])
		if j+1<=column-1 and ([i,j+1] not in nearby):
			if not isNot(i,j+1):
				nearby.append([i,j+1])
		if i+1>=0 and ([i+1,j] not in nearby):
			if not isNot(i+1,j):
				nearby.append([i+1,j])
		if j-1>=0 and ([i,j-1] not in nearby):
			if not isNot(i,j-1):
				nearby.append([i,j-1])
	for near in nearby:
		rc[near[0]][near[1]]=getNum(near)

#是否在雷及雷旁边8个格子以外
def isNot(i,j):
	isNot=True
	for mine in minesIndex:
		if i-mine[0]>=-1 and i-mine[0]<=1 and j-mine[1]>=-1 and j-mine[1]<=1:
			isNot=False
	return isNot

#打印rc
def printRC():
	for rowList in rc:
		for mine in rowList:
			print mine,
		print ' '

#计算一个点显示的数字
def getNum(mine):
	global minesIndex
	global row
	global column
	num=0
	if not isNot(mine[0],mine[1]):
		num=num+1
	else:
		find(mine[0],mine[1])
	return num

#两种输入
row_column=[0,0]
mine_row_column=[0,0]
next_step=1
#得到输入
#三种模式,r c,m(标记为雷),c(取消标记)
def getInput():
	global row_column
	global mine_row_column
	global next_step
	Input=raw_input('(m,c) r c:  ')
	find=re.compile(r'[0-9]').findall(Input)
	if len(find)>=2:
		if 'm' in Input:
			mine_row_column=[int(find[0])-1,int(find[1])-1]
			next_step=2
		elif 'c' in Input:
			mine_row_column=[int(find[0])-1,int(find[1])-1]
			next_step=3
		else:
			row_column=[int(find[0])-1,int(find[1])-1]
			next_step=1
	else:
		print 'must contains two numbers'
		getInput()

#得到输入后的处理过程
def a_process():
	global rc
	global row_column
	global mine_row_column
	global minesNum
	global next_step
	global hasFinish
	global save
	if next_step==1:
		i=row_column[0]
		j=row_column[1]
		for index in minesIndex:
			if i==index[0] and j==index[1]:
				print 'You falied'
				exit()
		Num=getNum(row_column)
		if Num>=1:
			rc[i][j]=Num
		elif Num==0:
			for s in save:
				#把0的连通区显示出来
				rc[s[0]][s[1]]=0
				#把连通区旁边的显示出来
				showNearby()
			save=[]
		hasFinish=hasFinish-1
	elif next_step==2:
		i=mine_row_column[0]
		j=mine_row_column[1]
		rc[i][j]='?'
	elif next_step==3:
		i=mine_row_column[0]
		j=mine_row_column[1]
		rc[i][j]='*'

def main():
	global row_column
	global minesNum
	global hasFinish
	init_rc()
	createMines()

	while hasFinish>0:
		print hasFinish
		printRC()
		getInput()
		a_process()
	print 'You win'

main()