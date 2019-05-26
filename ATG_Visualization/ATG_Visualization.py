#Author: Amir Taheri-Ghahfarokhi
"""
This code will use "turtle" to generate a graphical
representation of a variant table"
"""

import turtle

refseq_len=70 #defines the length of each bar!
bar_height=25 #defines the height of each bar!
base_len=10 #defines the base length that will be used in calculating the length of rectangles!
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

#Background for the top 10 variants:
def match(refseq_len,bar_height,base_len):
    t.color("light gray")
    t.begin_fill()
    for i in range(2):
        t.forward(refseq_len*base_len)
        t.left(90)
        t.forward(bar_height)
        t.left(90)
    t.end_fill()

for i in range(10):    
    match(refseq_len,bar_height,base_len)
    t.right(90)
    t.penup()
    t.forward(bar_height+between_bars)
    t.pendown
    t.left(90)

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
