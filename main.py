# main.py



import pygame

#Set up เริ่มต้นให้ทำงาน
pygame.init()

#ปรับขนาดหน้าจอ
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('Captain vs Covid-19')#เซ็ตชื่อเกม
icon = pygame.image.load('icon.png')#โหลดภาพเข้ามาใน pygame
pygame.display.set_icon(icon)#สั่ง set icon

####################UNCLE######################
# 1 - player - uncle.png

psize = 128

pimg = pygame.image.load('uncle.png')
px = 100 # จุดเริ่มต้นแกน X แนวนอน
py = HEIGHT - psize #จุดเริ่มต้นแกน Y
pxchange = 1
def Player(x,y):
	screen.blit(pimg,(x,y))

####################UNCLE######################
# 2 - enemy - virus.png



####################UNCLE######################
# 3 - mask - mask.png



####################UNCLE######################


running = True #บอกให้โปรแกรมทำงาน
FPS = 60
clock = pygame.time.Clock()

while running:
	for event in pygame.event.get():
		# รันลูปแล้วเช๊็คว่ามีการกดปิดเกมหรือไม่ [x]
		if event.type == pygame.QUIT:
			running = False
	#px,py จุดเริ่มต้น player
	Player(px,py)
	if px <= 0:
		pxchange = 1
		px =+ pxchange #px = px + 1
	elif px >= WIDTH - psize:
		#WIDTH 	(ความกว้างของหน้าจอ - ความกว้างของ uncle)
		pxchange = -1
		px += pxchange
	else:
		px += pxchange

	print(px)
	pygame.display.update()
	clock.tick(FPS)

