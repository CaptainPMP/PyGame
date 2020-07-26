# main.py

import pygame
import math
import random
from pygame import mixer

#Set up เริ่มต้นให้ทำงาน
pygame.init()

#ปรับขนาดหน้าจอ
WIDTH = 1000
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption('Captain vs Covid-19')#เซ็ตชื่อเกม
icon = pygame.image.load('icon.png')#โหลดภาพเข้ามาใน pygame
pygame.display.set_icon(icon)#สั่ง set icon

background = pygame.image.load('background.png')
####################UNCLE######################
# 1 - player - uncle.png

psize = 128

pimg = pygame.image.load('uncle.png')
px = 100 # จุดเริ่มต้นแกน X แนวนอน
py = HEIGHT - psize #จุดเริ่มต้นแกน Y
pxchange = 1
def Player(x,y):
	screen.blit(pimg,(x,y))#blit = วางภาพในหน้าจอ


####################ENEMY######################
# 2 - enemy - virus.png
esize = 64
emig = pygame.image.load('virus.png')
ex = 50
ey = 0
eychange = 1
def Enemy(x,y):
	screen.blit(emig,(x,y)) 
##################MULTI-ENEMY##################
exlist = [] #ตำแหน่งแกน x ของ enemy
eylist = [] #ตำแหน่งแกน y ของ enemy
ey_change_list = [] #ความเร็วของ enemy
allenemy = 5 # จำนวนของ enemy ทั้งหมด

for i in range(allenemy):   
	exlist.append(random.randint(50,WIDTH - esize))
	eylist.append(random.randint(0,100))
	#ey_change_list.append(random.randint(1,5)) #สุ่มความเร็วให้ enemy
	ey_change_list.append(1) #กำหนดความเร็วเป็น 1 ก่อนแล้วค่อยเพิ่มหลังจากยิงโดน
####################MASK######################
# 3 - mask - mask.png
msize = 32
mimg = pygame.image.load('mask.png')
mx = 100
my = HEIGHT - psize
mychange = 20 #ปรับความเร็วของ layer
mstate = 'ready'

def fire_mask(x,y):
	global mstate
	mstate = 'fire'
	screen.blit(mimg,(x,y))
####################COLLISION##################
def isCollision(ecx,ecy,mcx,mcy):
	#isCollision เช็คว่าชนกันหรือไม่? หากชนให้บอกว่า ชน (True)
	distance = math.sqrt(math.pow(ecx - mcx,2) + math.pow(ecy - mcy,2))
	print(distance)
	if distance < (esize / 2) + (msize / 2) :
		#(esize / 2) + (msize / 2) ระยะที่ชนกัน
		return True
	else:
		return False
####################SCORE######################

allscore = 0 
font = pygame.font.Font('angsana.ttc',50)

def showscore():
	score = font.render('คะแนน: {} คะแนน'.format(allscore),True,(255,255,255))
	screen.blit(score,(30,30))

####################SOUND######################
pygame.mixer.music.load('beach.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play(-1)


sound = pygame.mixer.Sound('virusaleart.wav')
sound.play()
####################GAME OVER SCREEN###############
fontover = pygame.font.Font('angsana.ttc',120)
fontover2 = pygame.font.Font('angsana.ttc',80)
playsound = False
gameover = False
def GameOver():
	global playsound
	global gameover
	overtext = fontover.render('Game Over',True,(255,0,0))
	screen.blit(overtext,(300,300))
	overtext2 = fontover.render('Press [n] New Game',True,(255,0,0))
	screen.blit(overtext2,(250,400))
	if playsound == False:
		gsound = pygame.mixer.Sound('gameover.wav')
		gsound.play()
		playsound = True
	#if gameover == False:
	#	gameover = True


####################GAME LOOP######################

clock = pygame.time.Clock() #game clock
running = True #บอกให้โปรแกรมทำงาน
FPS = 30 # frame rate


while running:

	screen.blit(background,(0,0))
	for event in pygame.event.get():
		# รันลูปแล้วเช๊็คว่ามีการกดปิดเกมหรือไม่ [x]
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				pxchange = -10
			if event.key == pygame.K_RIGHT:
				pxchange = 10

			if event.key == pygame.K_SPACE:
				if mstate == 'ready':
					b1 = pygame.mixer.Sound('laser2.wav')
					b1.play()
					'''mx = px + 100 #ขยับออกมาให้ชิดมือด้านขวา'''
					mx = px + 50
					fire_mask(mx,my)
			if event.key == pygame.K_n:
				#gameover = False
				playsound = False
				allscore = 0 
				for i in range(allenemy):
					eylist[i] = random.randint(0,100)
					exlist[i] = random.randint(50,WIDTH - esize)


		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				pxchange = 0


	#########################RUN PLAYER ##############################
	#px,py จุดเริ่มต้น player
	Player(px,py)
	### ทำให้ player ขยับซ้ายขวาเมื่อชนขอบจอ
	
	if px <= 0:
		#หากชนขอบจอซ้าย ให้ปรับค่า pxchange เป็น +1
		px = 0
		px =+ pxchange #px = px + 1
	elif px >= WIDTH - psize:
		#WIDTH  (ความกว้างของหน้าจอ - ความกว้างของ uncle)
		#หากชนขอบจอขวา ให้ปรับค่า pxchange เป็น -1
		px = WIDTH - psize
		px += pxchange
	else:
		#หากอยู่ระหว่างหน้าจอจะทำการบวก/ลบ ตาม pxchange
		px += pxchange
	
	###############################RUN ENEMY SINGLE###########################
	'''for i in range(5):'''
	#Enemy(ex,ey)
	#ey += eychange

	###############################RUN MULTI ENEMY#####################
	for i in range(allenemy):
		#เพิ่มความเร็วของ enemy
		if eylist[i] > HEIGHT - esize and gameover == False:
			for i in range(allenemy):
				eylist[i] = 1000
			GameOver()
			break



		eylist[i] += ey_change_list[i]
		collisionmulti = isCollision(exlist[i], eylist[i], mx, my)
		if collisionmulti:
			my = HEIGHT - psize
			mstate = 'ready'
			eylist[i] = 0
			exlist[i] = random.randint(50,WIDTH - esize)
			allscore += 1
			ey_change_list[i] += 1
			sound = pygame.mixer.Sound('broken.wav')
			sound.play()
		Enemy(exlist[i], eylist[i])


	#########################FIRE MASK##########################
	if mstate == 'fire':
		fire_mask(mx,my)
		my = my - mychange # my -= mychange

	#เช็คว่า Mask วิ่งไปชนขอบบนแล้วยัง? ถ้าชนให้ state เปลี่ยนเป็นพร้อมยิง (ready)
	if my <= 0:
		my = HEIGHT - psize
		mstate = 'ready'


	# เช็คว่าชนกันหรือไม่?
	collision = isCollision(ex,ey,mx,my)
	if collision:
		my = HEIGHT - psize
		mstate = 'ready'
		ey = 0
		ex = random.randint(50,WIDTH - esize) 
		#สุ่มตำแน่งความกว้างหน้าจอ - ขนาดของไวรัส




	showscore()
	print(px)
	pygame.display.update()
	pygame.display.flip()
	pygame.event.pump()
	screen.fill((0,0,0))
	clock.tick(FPS)
	

