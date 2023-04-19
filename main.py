from random import *
from numpy import array

x=0
y=0
r=1
i=0
m="x"
n="y"
s="state"
t=array([int]*10)
ts=array([int]*10)
tw=array([int]*10)
e=dict(m=int,n=int,s=str)
def forward():
    #rotate both motor 180
    global x,y,r
    
    if r==1:
        y+=1
    elif r==0:
        x+=1
    elif r==2:
        x-=1
    elif r==3:
        y-=1
    return x,y

def right():
    global r
    #rotate left motor 90
    #rotate right motor -90
    if r>=1:
        r-=1
    else:
        r=3


def left():
    global r
    #rotate left motor 90
    #rotate right motor -90
    if r<=2:
        r+=1
    else:
        r=0
        
def cf():
    global x,y
    for i in range(len(t)):
        try:
            if x==t[i]['x'] and y==t[i]['y']:
                print(x,y,t[i]['x'],t[i]['y'])
                e[s]="warning"
            else:
                print(x,y,t[i]['x'],t[i]['y'])
                e[s]="safe"
        except:
            break
def map(a,b,c,i):
    global x,y
    e.clear()
    if a==b==c==0:
        w=randint(0,2)
        if w==0:
            right()
            forward()
        elif w==1:
            forward()
        elif w==2:
            left()
            forward()
        e[m]=x
        e[n]=y
        cf()
        print(e[m],e[n],e)
        t[i]=e.copy()
        print(t[i])
        e.clear()
    if a==b==0 and c==1:
        w=randint(0,1)
        
        if w==0:
            right()
            forward()
        elif w==1:
            forward()
        e[m]=x
        e[n]=y
        cf()
        print(e[m],e[n],e)
        t[i]=e.copy()
        e.clear()
        
    if a==1 and b==0 and c==0:
        w=randint(1,2)
        if w==1:
            forward()
        elif w==2:
            left()
            forward()
        e[m]=x
        e[n]=y
        cf()
        print(e[m],e[n],e)
        t[i]=e.copy()
        e.clear()
    if a==0 and b==1 and c==0:
        w=randint(0,2)
        while w==1:
            w=randint(0,2)
        
        if w==0:
            right()
            forward()
        elif w==2:
            left()
            forward()
        e[m]=x
        e[n]=y
        cf()
        print(e[m],e[n],e)
        t[i]=e.copy()
        e.clear()
    if a==0 and b==c==1:
        right()
        forward()
        e[m]=x
        e[n]=y
        cf()
        print(e[m],e[n],e)
        t[i]=e.copy()
        e.clear()
    if c==0 and b==a==1:
        left()
        forward()
        e[m]=x
        e[n]=y
        cf()
        print(e[m],e[n],e)
        t[i]=e.copy()
        e.clear()
    if b==0 and c==a==1:
        forward()
        e[m]=x
        e[n]=y
        cf()
        print(e[m],e[n],e)
        t[i]=e.copy()
        e.clear()
        
def tree():
    for i in range(len(t)):
        try:
            if t[i]['state']=="safe":
                print(t[i])
                ts[i]=t[i]
            elif t[i]['state']=="warning":
                tw[i]=t[i]
        except Exception as e: print(e)
    
        

    
def test():
    global r
    map(1,0,1,0)
    r=3
    map(1,0,1,1)
    r=1
    map(1,0,1,2)
    
        
     
    
            
        

        

        






    


