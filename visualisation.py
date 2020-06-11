import tkinter
import random
import time
#------------------------------------------###------------------------------------------------------------------------------------------------------------------------

def swap(x,y):                              ###to swap the bars 
    coordinates0=canvas.coords(x)
    coordinates1=canvas.coords(y)
    canvas.move(x,coordinates1[0]-coordinates0[0],0)
    canvas.move(y,coordinates0[0]-coordinates1[0],0)
    #canvas.itemconfig(y,fill='green')       ###to change color once a bar is palced at its right position
  
    
    

#-------------------------------------------###-----------------------------------------------------------------------------------------------------------------------


    
def s_sort():                               ###to perform actual sorting lowest sosrted first.
    global bars
    global length
    size=len(bars)
  
        
    for x in range(size):
        small=x
        canvas.itemconfig(bars[x],fill="yellow")
        
        yield
       
        for y in range(x+1,size):
            if(length[y]<length[small]):
                canvas.itemconfig(bars[small],fill="red")
                
                canvas.itemconfig(bars[y],fill="yellow")
                yield
                small=y
        
        swap(bars[x],bars[small])
        bars[x],bars[small]=bars[small],bars[x]
        length[x],length[small]=length[small],length[x]
        
        canvas.itemconfig(bars[small],fill='red')
        canvas.itemconfig(bars[x],fill='green')
        yield




def selection_sort():     
    global delay
    delay = s_sort()
    animation()
#-----------------------------------------------------###---------------------------------------------------------------------------------------------------

def b_sort():
    global bars
    global length
    size=len(bars)
    for x in range(size):
        for y in range(size-x-1):
            if(length[y]>length[y+1]):
                
                swap(bars[y],bars[y+1])
                bars[y],bars[y+1]=bars[y+1],bars[y]
                length[y],length[y+1]=length[y+1],length[y]
                
            canvas.itemconfig(bars[y+1],fill='yellow')
            canvas.itemconfig(bars[y],fill='red')
        yield
        canvas.itemconfig(bars[y+1],fill='green')
    canvas.itemconfig(bars[0],fill='green')


def bubble_sort():
    global delay
    delay=b_sort()
    animation()


#-------------------------------------------------###-----------------------------------------------------------------------------------

"""def add_delay():
    for x in range(500):
        pass
    print(1)"""

def merging(start,mid,end):
    global bars
    global length
    i=start
    k=mid+1
    temp_len=[]
    
    arranged=[]
   # print('before',length[start:end+1])
    for _ in range(start,end+1):
        canvas.itemconfig(bars[_],fill='yellow')

    while i<mid+1 and k<end+1:
        if(length[i]<=length[k]):
            arranged.append(bars[i])
            temp_len.append(length[i])
            i+=1
        else:
            arranged.append(bars[k])
            temp_len.append(length[k])
            
            k+=1
    while k<end+1:
        arranged.append(bars[k])
        temp_len.append(length[k])
        k+=1
    while i<mid+1:
        arranged.append(bars[i])
        temp_len.append(length[i])
        
        i+=1
    pos=0
    for cord in range(start,end+1):
        x=canvas.coords(arranged[pos])
        
        canvas.move(arranged[pos],(cord+1)*5-x[0],0)
      
        bars[cord]=arranged[pos]
        length[cord]=temp_len[pos]
        pos+=1
   
    #print('after',temp_len)
    """for _ in range(start,end+1):
        canvas.itemconfig(bars[_],fill='red') """
    
    
"""def funtion(start,mid,end):
    delay=merging(start,mid,end)
    animation()"""
    
     
def m_sort(i,j):
    global bars
    global delay

    if(i<j):
       
        mid=(i+j)//2
        m_sort(i,mid)
        m_sort(mid+1,j)
        """for _ in range(i,j+1):
            canvas.itemconfig(bars[i],fill='yellow')
        yield
        merging(i,mid,j) 
        """
        merging(i,mid,j)
        
    
        
        
           
    
def merge_sort():
    global delay
    global length
    global bars
    
    delay=m_sort(0,len(length)-1)
    
    animation()
    """for _ in range(0,len(bars)-1):
        canvas.itemconfig(bars[_],fill='green')"""
    for x in range(len(bars)):
        c=canvas.coords(bars[x])
        print(c[0],600-c[1])

   
        
#----------------------------------------###---------------------------------------------------------------------------------------------------------------------------            


#-----------------------------------------###---------------------------------------------------------------------------------------------------------------------

#--------------------------------------------###--------------------------------------------------------------------------------------------------------------------







#----------------------------------------------------------------------
def animation():      # <-- commands resuming the sort once the display has been updated
                    
    global delay    # controls the pace of the animation
    if delay is not None:
        try:
            next(delay)
            root.after(10, animation)    # <-- repeats until the sort is complete,
        except StopIteration:            # when the generator is exhausted
            
            delay = None
            return
            
#----------------------------------------------###-----------------------------------------------------------------------------------------------           
def to_create():            #to generate bars and display it on canvas
    global bars             #to store id of bars drawn
    global length           #to store the length of bars
    canvas.delete('bar')    #to clear object previouly created on canvas
    global delay
    global number
    delay=None
    bars=[]
    length=[]
    start = 5
    end = 10
    number=121    
    for x in range(1, number):
        y = random.randint(1, 595)
        temp=canvas.create_rectangle(start,y, end, 600,tags='bar', fill='red')
        bars.append(temp)
        length.append(600-y)
        start += 5
        end += 5
    

#----------------------------------------------###---------------------------------------------------------------------------------------------------------
root=tkinter.Tk()
"""top=tkinter.Frame(root,width = 1350, height = 50, bd = 15,bg="LightSkyBlue1",relief="raise",padx=10,pady=10)
top.pack(side=TOP,fill=X,pady=20)
heading=tkinter.Label(top,text="VISUALisation of ALGOrithm")
heading.pack()"""
canvas = tkinter.Canvas(root, width='1000', height='600')
canvas.pack()
generate=tkinter.Button(root,text='generate_pattern' ,command=to_create)
to_create()
generate.pack()
selection=tkinter.Button(root,text='seletion_sort',command=selection_sort)
selection.pack()
bubble=tkinter.Button(root,text='bubble_sort',command=bubble_sort)
bubble.pack()
merge=tkinter.Button(root,text='merge_sort',command=merge_sort)
merge.pack()
root.mainloop()
