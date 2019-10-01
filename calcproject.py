from tkinter import *

cal = Tk()
cal.title("calculator") #title of the window
#operator = ""
text_Input = StringVar()

output =""

txtDisplay = Entry(cal,font=('arial', 20, 'bold'), textvariable=text_Input, bd=30, insertwidth=4,
                            bg="peachpuff", justify='right').grid(columnspan=4)
numbers =[]
#def clear():
#    global output
#    output = ""
#    text_Input.set("")

def click(number):
    global output
    output = output + str(number)  #when a number is clicked the number will be a string and dsiplayed , "added t the otput"
    #numbers = [] #empty list
    text_Input.set(output) #when a number is pressed it it added to output and the display text changes
    #numbers.append(output) #str(number)



def clear():
    output =""
    text_Input.set("")   #clear, makes the output clear, and sets the text input to clear
    numbers.clear()
    print(len(numbers))

def equal():
    global output
    numbers.append(output)  #adds output string to numbers list
    sum = str(eval(output))
    text_Input.set(sum)
    output = ""
    #for x in numbers:
    #    if isinstance(x,str):   #if it is a srting change it to an int
    #        int(x)





#bd = border size  padx = width


#for x in range(0,9): (is there an easier way of doing all this without inputting each one


#========================================ROW 1==========================================================#
btn7 = Button(cal,padx=16, bd=5, fg="black", font=('', 20, 'bold'), text = "7", command = lambda:click(7)).grid(row=1, column = 0)

btn8 = Button(cal,padx=16,bd=5,fg="black", font=('arial',20,'bold'), text="8", command = lambda:click(8)).grid(row = 1, column = 1)

btn9 = Button(cal,padx=16,bd = 5, fg="black", font=('arial', 20, 'bold'), text = "9", command = lambda:click(9)).grid(row=1, column = 2)

Addition = Button(cal,padx=16, bd=5, fg="black", font=('arial', 20, 'bold'), text = "+", command = lambda:click("+")).grid(row=1,column=3)

#========================================ROW 2===========================================================#

btn4 = Button(cal,padx=16, bd=5, fg="black", font=('arial', 20, 'bold'), text = "4", command = lambda:click(4)).grid(row=2, column = 0)

btn5 = Button(cal,padx=16,bd=5,fg="black", font=('arial',20,'bold'), text="5", command = lambda:click(5)).grid(row = 2, column = 1)

btn6 = Button(cal,padx=16,bd = 5, fg="black", font=('arial', 20, 'bold'), text = "6", command = lambda:click(6)).grid(row=2, column = 2)

Subtraction = Button(cal,padx=18, bd=5, fg="black", font=('arial', 20, 'bold'), text = "-", command = lambda:click("-")).grid(row=2,column=3)

#========================================ROW 3==========================================================#

btn1 = Button(cal,padx= 16, bd= 5, fg= "black", font= ('arial', 20, 'bold'), text = "1", command = lambda:click(1)).grid(row = 3, column = 0)

btn2 = Button(cal,padx=16,bd=5,fg="black", font=('arial',20,'bold'), text="2", command = lambda:click(2)).grid(row = 3, column = 1)

btn3 = Button(cal,padx=16,bd = 5, fg="black", font=('arial', 20, 'bold'), text = "3", command = lambda:click(3)).grid(row=3, column = 2)

Multipliation = Button(cal,padx=18, bd=5, fg="black", font=('arial', 20, 'bold'), text = "*", command = lambda:click("*")).grid(row=3,column=3)

#========================================ROW 4===========================================================#

btn0 = Button(cal,padx=16, bd=5, fg="black", font=('arial', 20, 'bold'), text = "0", command = lambda:click(0)).grid(row=4, column = 0)

Decimal = Button(cal,padx=18,bd=5,fg="black", font=('arial',20,'bold'), text=".", command = lambda:click(".")).grid(row = 4, column = 1)

#Power = Button(cal,padx=16,bd=5, fg="black", font=('arial', 20, 'bold'), text = "^").grid(row=4,column=2)

Divsion = Button(cal,padx=18,bd = 5, fg="black", font=('arial', 20, 'bold'), text = "/", command = lambda:click("/")).grid(row=4, column = 3)

#========================================ROW 5============================================================#
Clear = Button(cal, padx = 16, bd=5, fg ="black", font =('arial', 20, 'bold'), text = "C", command = lambda:clear()).grid(row =5, column=0)
Equal = Button(cal, padx=16, bd=5, fg="black", font =('arial',20,'bold'), text = "=", command = lambda:equal()).grid(row=5, column = 3)

cal.mainloop()
