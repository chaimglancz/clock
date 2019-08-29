from tkinter import *
import time
from  math import radians, sin, cos
def S(x):
    return sin(radians(x))
def C(x):
    return cos(radians(x))
def digi():
    tm=time.time()-14400#for summer
    #tm=time.time()-18000#for winter
    hour=int((tm%86400)//3600)
    if hour>11:
        hour-=12
        gg='PM'
    else:
        gg='AM'
    if hour==0: hour=12    
    hour=str(hour)
    minute=str(int((tm%3600)//60))
    if len(minute)<2:minute='0'+minute
    second=str(int(tm%60))
    if len(second)<2:second='0'+second
    dd=hour+':'+minute+':'+second
    btm.configure(text=dd,font=('Arial','80'))
    ampm.configure(text=gg,font=('Arial','20'))
    btm.after(100,digi)
def newx(xy,deg):
    if deg==90:return -xy[1]
    if deg==270:return xy[1]
    else:return xy[0]/C(deg)-(xy[1]+xy[0]*S(deg)/C(deg))*S(deg)
def newy(xy,deg):return(xy[1]+xy[0]*S(deg)/C(deg))*C(deg)                        
def move() :
    tm=time.time()-14400#for summer
    #tm=time.time()-18000#for winter
    hour=(tm%86400)/3600
    if hour>=12:
        hour-=12 
    hour*=30
    minute=6*(tm%3600)/60
    second=(int(tm%60))*6
    tp.coords(h_hndl,250+newx(h1,hour), 250+newy(h1,hour), 250+newx(h2,hour), 250+newy(h2,hour),
                 250+newx(h3,hour), 250+newy(h3,hour), 250+newx(h4,hour), 250+newy(h4,hour))
    tp.coords(m_hndl,250+newx(m1,minute), 250+newy(m1,minute), 250+newx(m2,minute), 250+newy(m2,minute),
                 250+newx(m3,minute), 250+newy(m3,minute), 250+newx(m4,minute), 250+newy(m4,minute))
    tp.coords(s_hndl,250+newx(s1,second), 250+newy(s1,second), 250+newx(s2,second), 250+newy(s2,second),
                 250+newx(s3,second), 250+newy(s3,second), 250+newx(s4,second), 250+newy(s4,second))
    tp.after(100,move)    
tk=Tk()
tk.geometry('500x650')
tk.title('clock')
btm=Label(tk)
btm.place(width=450,height=150,x=0,y=500)
btm.configure(bg='#ffa0a0')
btmrt=Frame(tk)
btmrt.place(width=50,height=150,x=450,y=500)
btmrt.configure(bg='#ffa0a0')
ampm=Label(btmrt)
ampm.place(width=50,height=30,x=0,y=85)
ampm.configure(bg='#ffa0a0')
digi()

tp=Canvas(tk)
tp.place(width=500,height=500,x=0,y=0)
tp.configure(bg='#ffffa0')
tp.create_oval(240 , 240 , 260 , 260 , fill='#000000')
for i in range(1,13):
    tp.create_text(250+(215*S(i*30)),250-(215*C(i*30)),text=str(i),font=('Arial','50'))  
tm=time.time()-14400#for summer
#tm=time.time()-18000#for winter
hour=(tm%86400)/3600
if hour>11:
    hour-=12  
hour*=30
minute=6*(tm%3600)/60
second=(int(tm%60))*6
h1 = [  6,   40 ]
h2 = [ -6,   40 ]
h3 = [ -6, -100 ]
h4 = [  6, -100 ]    
m1 = [  4,   50 ]
m2 = [ -4,   50 ]
m3 = [ -4, -180 ]
m4 = [  4, -180 ]
s1 = [  2,   40 ]
s2 = [ -2,   40 ]
s3 = [ -2, -230 ]
s4 = [  2, -230 ]
h_hndl= tp.create_polygon(250+newx(h1,hour), 250+newy(h1,hour), 250+newx(h2,hour), 250+newy(h2,hour),
                      250+newx(h3,hour), 250+newy(h3,hour), 250+newx(h4,hour), 250+newy(h4,hour))
m_hndl= tp.create_polygon(250+newx(m1,minute), 250+newy(m1,minute), 250+newx(m2,minute), 250+newy(m2,minute),
                      250+newx(m3,minute), 250+newy(m3,minute), 250+newx(m4,minute), 250+newy(m4,minute))
s_hndl= tp.create_polygon(250+newx(s1,second), 250+newy(s1,second), 250+newx(s2,second), 250+newy(s2,second),
                      250+newx(s3,second), 250+newy(s3,second), 250+newx(s4,second), 250+newy(s4,second))
move()
tk.mainloop()















