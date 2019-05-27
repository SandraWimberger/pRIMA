#Project: pRIMA
#Author: Amir Taheri-Ghahfarokhi
#This code will use "turtle" to generate 
#a graphical representation of a variant table

"""
Read inputs!
"""
import pandas as pd #Load the Pandas libraries with alias 'pd' 
data = pd.read_csv("test_dataset.csv") # Read data from file 'filename.csv'
#print(data.head())# Preview the first 5 lines of the loaded data 
refseq=""
sgrna=""

"""
Setting up the global variables and functions!
"""

import turtle #Load the Pandas libraries for drawings.

refseq_len=70 #defines the length of each bar!
bar_height=21 #defines the height of each bar!
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
shape_fill={"match":"light gray",
            "match_border":"light gray",
            "deletion":"black",
            "deletion_border":"black",
            "insertion":"red",
            "insertion_border":"black",
            "duplication":"yellow",
            "duplication_border":"black",
            "microhomology":"cyan",
            "microhomology_border":"black"
            }

#Function to draw a rectangle:
def rect (width,height,pos_x,pos_y,border_color,fill_color):
    t.color(border_color,fill_color)
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

#Function to draw a rhombus:
def rhombus (pos_x,pos_y,border_color,fill_color):
    t.color(border_color,fill_color)
    t.penup()
    t.goto(pos_x,pos_y)
    t.pendown()
    t.begin_fill()
    t.left(45)
    for i in range(4):
        t.forward(base_len/2)
        t.left(90)
    t.end_fill()
    t.right(45)
    t.penup()
    t.goto(pos_x,pos_y-bar_height/1.33)
    t.pendown()

#Function to place the pointer at the origin of each variant:
def pointer_origin(var_num):
    t.penup()
    t.goto(fig_start[0],fig_start[1]- var_num*(bar_height+between_bars))
    t.pendown()
    pass

"""
Initiate drawing!
"""

for i in range(10):
    #Match bar:
    pos_x= fig_start[0]
    pos_y= fig_start[1] - i*(bar_height+between_bars)
    width=refseq_len*base_len
    border_color=shape_fill["match_border"]
    fill_color=shape_fill["match"]
    height=bar_height
    rect(width,bar_height,pos_x,pos_y,border_color,fill_color)
    #Variant type-specific drawings:
    var_type=data.loc[i,'Type']
    var_len=data.loc[i,'Length']
    var_pos=data.loc[i,'Reference Position']-100
    allele=data.loc[i,'Allele']
    mh_len=data.loc[i,'MicroHomology']
    duplication=data.loc[i,'Duplication']
    rel_freq=data.loc[i,'Rel. Freq.']
    if var_type=="Deletion":
        width=var_len*base_len
        pos_x=fig_start[0]+var_pos*base_len
        pos_y= fig_start[1] - i*(bar_height+between_bars)
        #draw the white background
        height=bar_height
        rect(width,height,pos_x,pos_y,"white","white")
        pointer_origin(i)
        #draw the black line
        height=int(bar_height//3)
        pos_y= fig_start[1] - i*(bar_height+between_bars)+(bar_height*0.333)
        border_color=shape_fill["deletion_border"]
        fill_color=shape_fill["deletion"]
        rect(width,height,pos_x,pos_y,border_color,fill_color)
        if mh_len>0:
            pos_y= fig_start[1] - i*(bar_height+between_bars)+(bar_height*0.667)
            width=mh_len*base_len
            border_color=shape_fill["microhomology_border"]
            fill_color=shape_fill["microhomology"]
            rect(width,height,pos_x,pos_y,border_color,fill_color)
            pos_x=fig_start[0]+(var_pos+var_len)*base_len
            rect(width,height,pos_x,pos_y,border_color,fill_color)
    elif var_type=="Insertion":
        pos_x=fig_start[0]+var_pos*base_len
        pos_y= fig_start[1] - i*(bar_height+between_bars)+bar_height/1.67 
        if duplication=="Detected":
            fill_color=shape_fill["duplication"]
            border_color=shape_fill["duplication_border"]
        else:
            fill_color=shape_fill["duplication"]
            border_color=shape_fill["insertion_border"]
        rhombus (pos_x,pos_y,border_color,fill_color)
        t.color("black")
        if var_len<5:
            text=allele
        else:
            text=str(var_len)
        t.write(text, move=False, align="center", font=("Arial", 14, "bold"))
        pointer_origin(i)
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
ts.getcanvas().postscript(file="out_Top10_Variants.eps")

#Save the final image as .pdf

#Close turtle!
turtle.exitonclick()
turtle.done()
