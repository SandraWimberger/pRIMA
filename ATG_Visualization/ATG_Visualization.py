"""
Import required modules!
"""
import tkinter as tk #Load the tkinter module with alias 'tk' for graphic interface.
import turtle #Load the turyle module for drawings.
import pandas as pd #Load the Pandas libraries with alias 'pd' to read csv files.

"""
Read inputs!
"""

data = pd.read_csv("test_dataset.csv") # Read data from file 'filename.csv'
refseq="TGCCTGCATTTTAGTCGTGAGATGGAGAATAAAGAAACTCTCAAAGGGTTGCACAAGATGGATGATCGTCCAGAGGAACGAATGATCAGGGAGAAACTGAAGGCAACCTGTATGCCAGCCTGGAAGCACGAATGGTTGGAAAGGAGAAATAGGCGAGGGCCTGTGGTAAGTGGCTATGGG"
sgrna="AGCCTGGAAGCACGAATGGT"
num_visualized_var = 10 #Define number of variants to be visualized!
show_window = True

"""
Check if inputs make sense!
"""
refseq.upper()#Capitalize refseq!
sgrna.upper()#Capitalize sgRNA!
 
def reverse_complement(dna):#ReverseComplement function.
    #copied from: 
    #https://codereview.stackexchange.com/questions/151329/reverse-complement-of-a-dna-string
    complement = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
    return ''.join([complement[base] for base in dna[::-1]])

refseq_rc=reverse_complement(refseq)

#Check if the sgRNA sequence exist in the refseq, and determine the cut_site:
if refseq.find(sgrna)>0:
    orientation="Fwd"
    cut_site=refseq.find(sgrna)+len(sgrna)-3 #CutSite for SpCas9.
elif refseq_rc.find(sgrna):
    orientation="Rev"
    cut_site=len(refseq)-(refseq_rc.find(sgrna)+len(sgrna)-3)  #CutSite for SpCas9.
else:
    print("sgRNA doesn't exist in RefSeq!")
    exit()
#Check if sgRNA length is in the range:
if len(sgrna)<10 or len(sgrna)>30:
    print("sgRNA length is not in range!")
    exit()

"""
Setting up the global variables and functions!
"""
refseq_len=70 #defines the length of each bar!
bar_height=21 #defines the height of each bar!
base_len=9.5 #defines the base length, for calculating the length of rectangles!
between_bars=5 #defines the distance between two bars!

frame_width=840 #defines the window width.
frame_height=640 #defines the window height.
window=tk.Tk() #creates a window. 
# Tkinter create a canvas to draw on.
canvas=tk.Canvas(master=window,width=frame_width,height=frame_height)
canvas.pack() #Packs the canvas to the window.

t=turtle.RawTurtle(canvas) 
if show_window==False:
    window.withdraw() #This hides the window to speed up the code.
else:
    pass
t.pencolor('black')

"""
Draw a frame!
"""
up_left=[-frame_width/2,frame_height/2]
t.speed(0)
t.pensize(5)
t.penup()
t.goto(up_left[0],up_left[1])
t.pendown()
t.goto(up_left[0]+800,up_left[1])
t.goto(up_left[0]+800,up_left[1]-600)
t.goto(up_left[0],up_left[1]-600)
t.goto(up_left[0],up_left[1])

"""
Define an important coordinates that all drawings will be drawn
relative to this position.
"""
fig_start=[up_left[0]+20,up_left[1]-100]
t.penup()
t.goto(fig_start[0],fig_start[1])
t.pendown()
t.pensize(1)

"""
Define the border and fill color dictionary.
"""
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
            "microhomology_border":"black",
            "sgrna_border":"gray",
            "sgrna":"pink",
            "sgrna_text":"black",
            "pam":"yellow",
            "pam_border":"orange",
            "cut_line":"green"
            }

"""
Main functions to draw rectangle, rhombus and lines!
"""
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

#Function to draw a line:
def vertical_line(pos_x,pos_y,size,line_color):
    t.color(line_color)
    t.penup()
    t.goto(pos_x,pos_y)
    t.pendown()
    t.right(90)
    t.forward(size)
    t.left(90)
    
"""
Initiate drawing!
"""

for i in range(num_visualized_var):
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
    #Convert reference positions:
    var_pos=data.loc[i,'Reference Position']
    var_pos= var_pos-(cut_site-35)
    if var_pos<0:
        var_len=var_len+var_pos
        var_pos=0
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
        t.write(text, move=False, align="center", font=("Arial", 12, "bold"))
        pointer_origin(i)
    else:
        pass
    
    t.penup()
    pos_x= fig_start[0]+refseq_len*base_len+10
    pos_y= fig_start[1] - i*(bar_height+between_bars)
    t.goto(pos_x,pos_y)
    t.pendown()
    text="%05.2f"%float(rel_freq)+"%"
    t.write(text, move=False, align="left", font=("Arial", 12, "bold"))
    
#Function to draw the guide on top!
def top_guide(sgrna,orientation):
    t.penup()
    t.goto(fig_start[0]+5*base_len,fig_start[1]+ 2*(bar_height+between_bars))
    t.pendown()
    t.pensize(4)
    t.forward(60*base_len)
    text=-30
    for i in range(7):
        t.penup()
        t.goto(fig_start[0]+5*base_len+i*10*base_len,fig_start[1]+ 2*(bar_height+between_bars))
        t.pendown()
        t.pensize(4)
        t.left(90)
        t.forward(base_len)
        t.write(text, move=False, align="center", font=("Arial", 12, "bold"))
        text+=10
        t.right(90)
    t.pensize(1)
    width=len(sgrna)*base_len
    height=bar_height
    border_color=shape_fill["sgrna_border"]
    fill_color=shape_fill["sgrna"]
    pos_y=fig_start[1]+ (bar_height+between_bars)
    line_size=num_visualized_var*(bar_height+between_bars)+between_bars
    if orientation=="Rev":
        offset_left=32*base_len
        pos_x=fig_start[0]+offset_left
        rect(width,height,pos_x,pos_y,border_color,fill_color)
        #sgRNA text:remember that sgRNA needs to be revComp
        t.color(shape_fill["sgrna_text"])
        t.write(reverse_complement(sgrna), move=False, align="left", font=("Courier New", 13, "bold"))
        #draw vertical lines
        line_color=shape_fill["sgrna_border"]
        vertical_line(pos_x,pos_y,line_size,line_color)
        vertical_line(pos_x+len(sgrna)*base_len,pos_y,line_size,line_color)
        #draw PAM
        width=3*base_len
        pos_x= fig_start[0]+offset_left - 3*base_len+t.pensize()
        rect(width-2*t.pensize(),height,pos_x,pos_y,shape_fill["pam_border"],shape_fill["pam"])
        line_color=shape_fill["pam_border"]
        vertical_line(pos_x,pos_y,line_size,line_color)        
    elif orientation=="Fwd":
        offset_left=(35-(len(sgrna)-3))*base_len
        pos_x=fig_start[0]+offset_left
        rect(width,height,pos_x,pos_y,border_color,fill_color)
        #sgRNA text:
        t.color(shape_fill["sgrna_text"])
        t.write(sgrna, move=False, align="left", font=("Courier New", 13, "bold"))
        #draw vertical lines
        line_color=shape_fill["sgrna_border"]
        vertical_line(pos_x,pos_y,line_size,line_color)
        vertical_line(pos_x+len(sgrna)*base_len,pos_y,line_size,line_color)
        #draw PAM
        width=3*base_len
        pos_x= fig_start[0]+38*base_len+t.pensize()
        rect(width-2*t.pensize(),height,pos_x,pos_y,shape_fill["pam_border"],shape_fill["pam"])
        line_color=shape_fill["pam_border"]
        vertical_line(pos_x+3*base_len-t.pensize(),pos_y,line_size,line_color)
    #draw cut line:
    pos_x=fig_start[0]+35*base_len
    line_color=shape_fill["cut_line"]
    vertical_line(pos_x,pos_y+bar_height,line_size+bar_height,line_color)
    
top_guide(sgrna,orientation)

#move the pointer to the fig_start (origin).
t.penup()
t.goto(fig_start[0],fig_start[1])
t.pendown()

"""
Save the output.
"""
#Save the final image as .eps
ts = t.getscreen()
file_name="out_Top10_Variants.eps"
ts.getcanvas().postscript(file=file_name)

if show_window==False:
    window.destroy()
else:
    window.mainloop()