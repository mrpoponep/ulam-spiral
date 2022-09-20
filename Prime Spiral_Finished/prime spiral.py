import pygame as py
import math
PRIME=[2,3,5,7]
py.init()
SIZE=1005
WIN = py.display.set_mode([SIZE, SIZE])
SCALE=5
NUM=int(SIZE/SCALE)
DOT=py.image.load("rs/dot2.png")
DOT=py.transform.scale(DOT,(SCALE,SCALE))
DOT=py.image.load("rs/dot2.png")
DOT=py.transform.scale(DOT,(SCALE,SCALE))
RED_DOT=py.image.load("rs/red-dot.png")
RED_DOT=py.transform.scale(RED_DOT,(SCALE,SCALE))
GRAY_DOT=py.image.load("rs/gray_dot.png")
GRAY_DOT=py.transform.scale(GRAY_DOT,(SCALE,SCALE))
x,y=math.floor(NUM/2),math.floor(NUM/2)

dir = 'r'
turn_point=2
step=1.5

def checkprime(num):    
    for i in PRIME:
        if num%i==0:
            return False
    return True
class Piece:
    def __init__(self,x,y,num):
        self.x=x
        self.y=y
        self.num=num
        self.prime=False
        self.img=DOT

    def draw(self):
        if self.num==1:
            self.img=RED_DOT
        elif self.prime==False:
            self.img=GRAY_DOT
        WIN.blit(self.img,(self.x*SCALE,self.y*SCALE))
        
def gen_num(piece_list):
    global dir 
    if piece_list[-1].num < (NUM)*(NUM):    
        if dir=='r':
            piece_list.append(Piece(piece_list[-1].x+1,piece_list[-1].y,piece_list[-1].num+1))
        if dir=='l':
            piece_list.append(Piece(piece_list[-1].x-1,piece_list[-1].y,piece_list[-1].num+1))
        if dir=='u':
            piece_list.append(Piece(piece_list[-1].x,piece_list[-1].y-1,piece_list[-1].num+1))
        if dir=='d':
            piece_list.append(Piece(piece_list[-1].x,piece_list[-1].y+1,piece_list[-1].num+1))
        set_step(piece_list)
def turn():
    global dir 
    if dir=='r':
        dir='u'
    elif dir=='u':
        dir='l'
    elif dir=='l':
        dir='d'
    elif dir=='d':
        dir='r'
def set_step(piece_list):
    global dir
    global turn_point
    global step
    if piece_list[-1].num == turn_point:
        turn()
        turn_point+=math.floor(step)
        step+=0.5
def main(PRIME):    
    piece_list=[Piece(x,y,1)]
    running = True
    clock = py.time.Clock()
    for num in range(2,(NUM+10)**2):    
        if checkprime(num):
            PRIME.append(num)
        gen_num(piece_list)
    print(len(PRIME))
    print(NUM)
    while running:
        WIN.fill((255,255,255))
        #clock.tick(1)
        #gen_num(piece_list)
        
        for i in piece_list:
            if i.num == PRIME[0] :    
                i.prime=True
                PRIME.pop(0)
            i.draw()
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
        py.display.flip()
    py.quit()

main(PRIME)