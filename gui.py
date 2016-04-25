#coding:utf-8
import random
import gtk
row=8
column=8


class Mine(gtk.Button):
	def __init__(self):
		super(Mine,self).__init__()
		self.num=0

		self.image=gtk.Image()
		self.image.set_from_file('b.gif')

		self.set_image(self.image)
		self.set_size_request(50,50)
		self.connect('clicked',self.click)

	def click(self,widget):
		if self.num==-1:
			self.image.set_from_file('m.gif')
		if self.num==0:
			self.image.set_from_file('0.png')
		if self.num==1:
			self.image.set_from_file('1.png')
		if self.num==2:
			self.image.set_from_file('2.png')
		if self.num==3:
			self.image.set_from_file('3.png')
		if self.num==4:
			self.image.set_from_file('4.png')
		if self.num==5:
			self.image.set_from_file('5.png')
		if self.num==6:
			self.image.set_from_file('6.png')



class mines(gtk.Window):
	# 返回为每个mine初始化的num
	def getInitNum(self,i):
		num=0
		scope=[9,8,7,1,-1,-7,-8,-9]
		scopeLeft=[8,7,-1,-8,-9]
		scopeRight=[9,8,1,-7,-8]
		for index in self.minesIndex:
			devide=i-index
			if devide==0:
				return -1
			if i%8==0 and devide in scopeLeft:
				num=num+1
			elif i%8==7 and devide in scopeRight:
				num=num+1
			elif i%8!=0 and i%8!=7 and  devide in scope:
				num=num+1
		return num
	#初始化雷索引
	def createMinesIndex(self):
		self.minesIndex=[]
		minesSum=9
		while len(self.minesIndex)<minesSum:
			mine= random.randint(0,8*8-1)
			if mine not in self.minesIndex:
				self.minesIndex.append(mine)
		print self.minesIndex

	def createMines(self,row=8,column=8):
		#存储mines对象的list
		self.minesList=[]
		self.createMinesIndex()
		self.table=gtk.Table(row,column,True)
		for i in range(row*column):
			mButton=Mine()
			self.minesList.append(mButton)
			self.table.attach(mButton,i%row,i%row+1,i/column,i/column+1)
			mButton.connect('clicked',self.clicked,i)
			mButton.num=self.getInitNum(i)
		

	def __init__(self):
		super(mines,self).__init__()
		self.createMines()

		self.add(self.table)
		self.show_all()
		self.connect('destroy',gtk.main_quit)
		self.hasCheckList=[]
		# self.minesList[0].image.set_from_file('6.gif')

	#使用深度优先搜索数字为0的并显示出来
	def clicked(self,widget,i,row=8,column=8):
		print str(widget.num)+" *** "+str(i)

		if(widget.num !=0 and widget.num !=-1):
			widget.click(widget)

		if(widget.num==0):
			if i not in self.hasCheckList:
				self.hasCheckList.append(i)
			print self.hasCheckList
			widget.click(widget)
			if(i>=8 and self.minesList[i-8].num!=-1 and i-8 not in self.hasCheckList):
				self.clicked(self.minesList[i-8],i-8)
			if(i>=1 and self.minesList[i-1].num!=-1 and i-1 not in self.hasCheckList):
				self.clicked(self.minesList[i-1],i-1)
			if(i+1<=row*column-1 and self.minesList[i+1].num!=-1 and i+1 not in self.hasCheckList):
				self.clicked(self.minesList[i+1],i+1)
			if(i+8<=row*column-1 and self.minesList[i+8].num!=-1 and i+8 not in self.hasCheckList):
				self.clicked(self.minesList[i+8],i+8)

m=mines()
gtk.main()