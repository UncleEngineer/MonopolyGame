# monopoly.py
start = {'S01':{'code':'S01','name':'Start'}}
jail = {'J01':{'code':'J01','name':'Jail'}}
card_name = {'L01':{'code':'L01','name':'Lucky'}}
command_name = {'C01':{'code':'C01','name':'Command'}}
gojail = {'G01':{'code':'G01','name':'Go to Jail'}}
stop = {'T01':{'code':'T01','name':'Stop'}}

land = {'101':{ 'code':'101',
				'name':'พารากอน',
				'price': 2000,
				'rent': 100},
		'102':{ 'code':'102',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100},
		'103':{ 'code':'103',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100},
		'104':{ 'code':'104',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100},
		'105':{ 'code':'105',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100},
		'106':{ 'code':'106',
				'name':'พารากอน',
				'price': 2000,
				'rent': 100},
		'107':{ 'code':'107',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100},
		'108':{ 'code':'108',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100},
		'109':{ 'code':'109',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100},
		'110':{ 'code':'110',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100},
		'111':{ 'code':'111',
				'name':'พารากอน',
				'price': 2000,
				'rent': 100},
		'112':{ 'code':'112',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100},
		'113':{ 'code':'113',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100},
		'114':{ 'code':'114',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100},
		'115':{ 'code':'115',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100},
		'116':{ 'code':'116',
				'name':'พารากอน',
				'price': 2000,
				'rent': 100},
		'117':{ 'code':'117',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100},
		'118':{ 'code':'118',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100},
		'119':{ 'code':'119',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100},
		'120':{ 'code':'120',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100},
		'121':{ 'code':'121',
				'name':'พารากอน',
				'price': 2000,
				'rent': 100},
		'122':{ 'code':'122',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100},
		'123':{ 'code':'123',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100},
		'124':{ 'code':'124',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100}
			 }

property_name = {'201':{ 'code':'201',
						 'name':'บ้าน',
						 'price': 1000,
						 'rent_percent': 10},
				 '202':{ 'code':'202',
						 'name':'โรงแรม',
						 'price': 3000,
						 'rent_percent': 30}
			}

lucky_card = {'301':{ 'code':'301',
					  'name':'ถูกหวย',
					  'detail':'สะดุดล้มเจอเลข ถูกหวย 1000 บาท',
					  'money': 1000},
			  '302':{ 'code':'302',
					  'name':'ค่าปรับ',
					  'detail':'ขับรถเร็วเจอค่าปรับ 500 บาท',
					  'money': -500},
			 
			}

command = {'401':{ 'code':'401',
				   'name':'เดินหน้า',
				   'detail':'เจอผู้ใหญ่ใจดีมีเครื่องบินเดินหน้า 10 ครั้ง',
				   'move': 10,
				   'stop':False,
				   'jail':False},
			'402':{ 'code':'402',
				   'name':'ถอยหลัง',
				   'detail':'ขึ้นรถผิดสายเสียเวลาไป 10 ครั้ง',
				   'move': -10,
				   'stop':False,
				   'jail':False},
			'403':{ 'code':'403',
				   'name':'ติดคุก',
				   'detail':'ไม่จ่ายค่าปรับติดคุก',
				   'move': 0,
				   'stop':True,
				   'jail':True}, 
			}

print(command['401'])


class Player:

	def __init__(self,name,ID):
		self.id = ID
		self.name = name
		self.money = 0
		self.status = 'standby'
		self.property = []
		self.land = []
		self.move = 0

class Banker:

	def __init__(self):
		self.id = 0
		self.name = 'Bank of Uncle'
		self.money = 1000000000
		self.all_property = []
		self.all_land = {}
		self.all_lucky_card = []
		self.all_command = []

class Box:

	def __init__(self,box,x1,y1,x2,y2):
		self.box = box
		self.info = None
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.players = []


###############DEFINE 1#################
row1 = [] # 10 - ST1,LD6,L1,C1,J1
for i in range(1,7):
	row1.append(land[str(100+i)])

row1.insert(0,start['S01'])
row1.insert(2,card_name['L01'])
row1.insert(4,command_name['C01'])
row1.append(jail['J01'])
###############DEFINE 2#################
row2 = [] # 8 - LD6, L1, C1
for i in range(7,13):
	row2.append(land[str(100+i)])
row2.insert(2,card_name['L01'])
row2.insert(4,command_name['C01'])
###############DEFINE 3#################
row3 = [] # 10 - LD8, L1, C1
for i in range(13,19):
	row3.append(land[str(100+i)])
row3.insert(0,stop['T01'])
row3.insert(2,card_name['L01'])
row3.insert(4,command_name['C01'])
row3.append(gojail['G01'])
###############DEFINE 4#################
row4 = [] # 8 - 
for i in range(19,25):
	row4.append(land[str(100+i)])
row4.insert(2,card_name['L01'])
row4.insert(4,command_name['C01'])

print(len(row1),len(row2),len(row3),len(row4))

from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.geometry('1200x720')
GUI.title('Monopoly Game by Uncle Engineer')

canvas = Canvas(GUI,width=710,height=710)
canvas.place(x=0,y=0)

allbox = []

boxsize = 70

for i,r in enumerate(row1):
	x1 = 710 - ((i+1) * boxsize)
	y1 = 710 - boxsize
	x2 = x1 + boxsize
	y2 = 710
	box = canvas.create_rectangle(x1,y1,x2,y2,fill='white')
	newbox = Box(box,x1,y1,x2,y2)
	newbox.info = r
	allbox.append(newbox)

'''
x1 = 710 - boxsize
	y1 = 710 - (i * boxsize)
	x2 = 710
	y2 = y1 + boxsize

'''

canvas.itemconfig(allbox[5].box,fill='red') #change color of a box

print(allbox)

GUI.mainloop()
