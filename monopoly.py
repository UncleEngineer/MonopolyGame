# monopoly.py
start = {'S01':{'code':'S01','name':'Start'}}
jail = {'J01':{'code':'J01','name':'Jail'}}
card_name = {'L01':{'code':'L01','name':'Lucky'}}
command_name = {'C01':{'code':'C01','name':'Command'}}
gojail = {'G01':{'code':'G01','name':'Go to Jail'}}
stop = {'T01':{'code':'T01','name':'Stop'}}

land = {'101':{ 'code':'101',
				'name':'กรุงเทพ',
				'price': 2000,
				'rent': 100},
		'102':{ 'code':'102',
				'name':'เชียงใหม่',
				'price': 2000,
				'rent': 100},
		'103':{ 'code':'103',
				'name':'ภูเก็ต',
				'price': 2000,
				'rent': 100},
		'104':{ 'code':'104',
				'name':'นครราชสีมา',
				'price': 2000,
				'rent': 100},
		'105':{ 'code':'105',
				'name':'ปทุมธานี',
				'price': 2000,
				'rent': 100},
		'106':{ 'code':'106',
				'name':'ชลบุรี',
				'price': 2000,
				'rent': 100},
		'107':{ 'code':'107',
				'name':'ระยอง',
				'price': 2000,
				'rent': 100},
		'108':{ 'code':'108',
				'name':'อยุธยา',
				'price': 2000,
				'rent': 100},
		'109':{ 'code':'109',
				'name':'กาญจนบุรี',
				'price': 2000,
				'rent': 100},
		'110':{ 'code':'110',
				'name':'สุพรรณบุรี',
				'price': 2000,
				'rent': 100},
		'111':{ 'code':'111',
				'name':'ตราด',
				'price': 2000,
				'rent': 100},
		'112':{ 'code':'112',
				'name':'ตาก',
				'price': 2000,
				'rent': 100},
		'113':{ 'code':'113',
				'name':'เลย',
				'price': 2000,
				'rent': 100},
		'114':{ 'code':'114',
				'name':'ตรัง',
				'price': 2000,
				'rent': 100},
		'115':{ 'code':'115',
				'name':'ยะลา',
				'price': 2000,
				'rent': 100},
		'116':{ 'code':'116',
				'name':'สตูล',
				'price': 2000,
				'rent': 100},
		'117':{ 'code':'117',
				'name':'พังงา',
				'price': 2000,
				'rent': 100},
		'118':{ 'code':'118',
				'name':'ชุมพร',
				'price': 2000,
				'rent': 100},
		'119':{ 'code':'119',
				'name':'เชียงราย',
				'price': 2000,
				'rent': 100},
		'120':{ 'code':'120',
				'name':'สมุทรสาคร',
				'price': 2000,
				'rent': 100},
		'121':{ 'code':'121',
				'name':'น่าน',
				'price': 2000,
				'rent': 100},
		'122':{ 'code':'122',
				'name':'แพร่',
				'price': 2000,
				'rent': 100},
		'123':{ 'code':'123',
				'name':'สมุทรปราการ',
				'price': 2000,
				'rent': 100},
		'124':{ 'code':'124',
				'name':'อุทัยธานี',
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
		self.location = None
		self.color = 'red'

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

# Generate Box Row 1
for i,r in enumerate(row1):
	x1 = 710 - ((i+1) * boxsize)
	y1 = 710 - boxsize
	x2 = x1 + boxsize
	y2 = 710
	box = canvas.create_rectangle(x1,y1,x2,y2,fill='white')
	newbox = Box(box,x1,y1,x2,y2)
	newbox.info = r
	allbox.append(newbox)
	L = ttk.Label(GUI,text='{}\n{}'.format(r['code'],r['name']),background='white')
	L.place(x=x1 + 5,y=y1 + 5)
# Generate Box Row 2
for i,r in enumerate(row2):
	x1 = 10
	y1 = 710 - (boxsize * (i+2))
	x2 = x1 + boxsize
	y2 = 710 - ((i+1) * boxsize)
	box = canvas.create_rectangle(x1,y1,x2,y2,fill='white')
	newbox = Box(box,x1,y1,x2,y2)
	newbox.info = r
	allbox.append(newbox)
	L = ttk.Label(GUI,text='{}\n{}'.format(r['code'],r['name']),background='white')
	L.place(x=x1 + 5,y=y1 + 5)
# Generate Box Row 3
for i,r in enumerate(row3):
	x1 = 10 + (i*boxsize)
	y1 = 10
	x2 = x1 + boxsize
	y2 = y1 + boxsize
	box = canvas.create_rectangle(x1,y1,x2,y2,fill='white')
	newbox = Box(box,x1,y1,x2,y2)
	newbox.info = r
	allbox.append(newbox)
	L = ttk.Label(GUI,text='{}\n{}'.format(r['code'],r['name']),background='white')
	L.place(x=x1 + 5,y=y1 + 5)
# Generate Box Row 4
for i,r in enumerate(row4):
	x1 = 710 - boxsize
	y1 = 10 + ((i+1)*boxsize)
	x2 = x1 + boxsize
	y2 = y1 + boxsize
	box = canvas.create_rectangle(x1,y1,x2,y2,fill='white')
	newbox = Box(box,x1,y1,x2,y2)
	newbox.info = r
	allbox.append(newbox)
	L = ttk.Label(GUI,text='{}\n{}'.format(r['code'],r['name']),background='white')
	L.place(x=x1 + 5,y=y1 + 5)

print('COUNT:',len(allbox))

#canvas.itemconfig(allbox[5].box,fill='red') #change color of a box

#print(allbox)


allplayer = []

p1 = Player('Loong','P101')
p1.color = 'red'
p2 = Player('Somchai','P102')
p2.color = 'green'



allplayer.append(p1)
allplayer.append(p2)

# ทำให้ player ทุกคนอยู่ที่จุดเริ่มต้น
for py in allplayer:
	allbox[0].players.append(py)
	py.location = allbox[0]


import random

current = 0
countplayer = len(allplayer)
turn = 0

def RunPlayer():
	global turn
	if turn > 0:
		global current
		print('CURRENT:',current)
		rand = random.randint(1,6)
		select = allplayer[current]
		select.move += rand
		print('ครั้งนี้เดินไปตาที่: ', select.move)
		if select.move >= 36:
			canvas.itemconfig(allbox[select.move % 36].box,fill=select.color)
			allbox[select.move  % 36].players.append(select)
			canvas.itemconfig(select.location.box,fill='white')
			select.location = allbox[select.move % 36] # allbox[select.move] ต้อง /
		else:
			canvas.itemconfig(allbox[select.move].box,fill=select.color)
			allbox[select.move].players.append(select)
			canvas.itemconfig(select.location.box,fill='white')
			select.location = allbox[select.move] # allbox[select.move] ต้อง /

		current += 1
		if current == countplayer:
			current = 0
	turn += 1
	GUI.after(2000,RunPlayer)

RunPlayer()
GUI.mainloop()
