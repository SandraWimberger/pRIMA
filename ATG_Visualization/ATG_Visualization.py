#Project: pRIMA
#Author: Amir Taheri-Ghahfarokhi
"""
This code will use "turtle" to generate a graphical
representation of a variant table"
"""

import turtle

refseq_len=70 #defines the length of each bar!
bar_height=25 #defines the height of each bar!
base_len=10 #defines the base length, for calculating the length of rectangles!
between_bars=5 #defines the distance between two bars!
fig_start=[20,500]#difines a position of the origin. Every drawing will be relative to this coordinates!

#Let's start the turtle and define the frame of the image.
t=turtle.Turtle()
t.screen.reset()
t.screen.setworldcoordinates(0,0,800,600)
t.speed(0)
t.pensize(5)
t.goto(0,600)
t.goto(800,600)
t.goto(800,0)
t.goto(0,0)

#move the pointer to the fig_start (origin).
t.penup()
t.goto(fig_start[0],fig_start[1])
t.pendown()
t.pensize(1)

#Define a dictionary for colors
shape_fill={"match":"light gray","deletion":"black","insertion":"red","duplication":"yellow"}

#Function to draw a rectangle:
def rect (width,height,pos_x,pos_y,color):
    t.color(color)
    t.penup()
    t.goto(pos_x,pos_y)
    t.pendown()
    t.begin_fill()
    for i in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

#Function to place the pointer at the origin of each variant:
def pointer_origin(var_num):
    t.penup()
    t.goto(fig_start[0],fig_start[1]- var_num*(bar_height+between_bars))
    t.pendown()
    pass

for i in range(10):
    #Match bar:
    pos_x= fig_start[0]
    pos_y= fig_start[1] - i*(bar_height+between_bars)
    width=refseq_len*base_len
    color=shape_fill["match"]
    height=bar_height
    rect(width,bar_height,pos_x,pos_y,color)
    #Variant type-specific drawings:
    var_type="deletion"
    var_len=8
    var_pos=30
    microhomology=0
    mh_len=0
    duplication=0
    if var_type=="deletion":
        width=var_len*base_len
        pos_x=fig_start[0]+var_pos*base_len
        pos_y= fig_start[1] - i*(bar_height+between_bars)
        #draw the white background
        height=bar_height
        rect(width,height,pos_x,pos_y,"white")
        pointer_origin(i)
        #draw the black line
        height=int(bar_height//3)
        pos_y= fig_start[1] - i*(bar_height+between_bars)+(int(bar_height*0.3))
        rect(width,height,pos_x,pos_y,"black")
        if microhomology>0:
            pass
        else:
            pass
        pass
    elif var_type=="insertion":
        
        pointer_origin(i)
        pass
    elif var_type=="duplication":
        
        pointer_origin(i)
        pass
    else:
        pass
    
#move the pointer to the fig_start (origin).
t.penup()
t.goto(fig_start[0],fig_start[1])
t.pendown()

#Read the top10 variants, RefSeq, and sgRNA sequence:


#Deletions with/without microhomology:


#Insrtions/duplications:


#Save the final image as .eps
ts = t.getscreen()
ts.getcanvas().postscript(file="Top10_Variants.eps")

#Save the final image as .pdf

#Close turtle!
turtle.exitonclick()
turtle.done()
