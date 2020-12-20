# monopoly.py

land = {'101':{ 'code':'101',
				'name':'พารากอน',
				'price': 2000,
				'rent': 100},
		'102':{ 'code':'102',
				'name':'รัฐสภา',
				'price': 2000,
				'rent': 100},
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