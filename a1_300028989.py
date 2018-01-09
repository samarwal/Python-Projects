#Family name: Samarth Agarwal
# Student number:  300028989
# Course: IT1 1120 
# Assignment Number 1

import turtle
import math

########################
# Question 1
########################

def mh2kh(s):
    '''(number)->number
    Returns the speed in kilometres/hour with a given speed in miles/hour ''' 
    d= s*1.60934
    return d

########################
# Question 2
########################

def pythagorean_pair(a,b):
    '''(number,number)->number
    Returns true if a & b are pythagorean pair and false otherwise
    Precondition: a and b are integers
    '''
    c2=(a**2)+(b**2)
    c=math.sqrt(c2)
    mod =c2%c
    return mod==0

########################
# Question 3
########################

def in_out(xs,ys,s):
    '''(number,number,number)->number
    Prints true if the given query point is inside of the given square, otherwise prints false
    Precondition: side is a non-negative number
    '''
    x=int(input("Enter a number for the x coordinate of a query point: "))
    y=float(input("Enter a number for the y coordinate of a query point: "))
    return (xs<=s and ys<=s)


########################
# Question 4
########################

def safe(n):
    '''(number)->number
    Returns true if 'n' is safe and false otherwise
    Precondition: 'n' is a non-negative integer where 'n' has at most 2 digits
    '''
    num1=n%10
    num2=n%9
    return (num1 !=9 and num2 !=0)


########################
# Question 5
########################

def quote_maker(quote,name,year):
    '''(String,String,Number)->String
    Returns the Quote String 
    '''
    print("In",year,",a person called",name,"said:","'"+quote+"'")
    return ;


########################
# Question 6
########################

def quote_displayer():
    '''(None)-> String
    Returns the Quote String 
    '''
    quote= input("Give me a quote: ")
    name= input("Who said that?: ")
    year= input("What year did she/he say that?: ")
    return quote_maker(quote,name,year)

########################
# Question 7
########################

def rps_winner():
    '''(None)-> None
    Determines the result of rock, paper, scissors game given choices of player 1 and player 2
    '''
    p1= input("What choice did Player 1 make? \n Type one of the following options: rock,paper,scissors: ")
    p2= input("What choice did Player 2 make?\n Type one of the following options: rock,paper,scissors: ")
    len1= len(p1)
    len2= len(p2)
    win = len1-len2
    print("Player 1 wins, That is  ",win==-4 or win==3 or win==1 , "\n It is a tie. That is  " , win==0)
    

 ########################
# Question 8
########################

def fun(x):
    '''(Number)-> Number
    Solves the equation for y and returns y
    Precondition: x is a positive number
    '''
    y=math.log( (x+3),10)/(4)
    return y


 ########################
# Question 9
########################

def ascii_name_plaque(name):
    '''(String)-> Drawing
    Draws a name plaque
    Precondition: 'name' is a string
    '''
    a=len(name)
    print((8+a)*("*"),"\n*" , (a+4)*(" "), "*", "\n*", ("__"+ name +"__"), "*", "\n*" , (a+4)*(" "), ("*\n" + (8+a)*("*")))
  


 ########################
# Question 10
########################

def draw_bike():
    '''(None)->None
     Draws a bike using turtle graphics'''
    
    wn = turtle.Screen()
    bike_drawing=turtle.Turtle()
    
     #left wheel
    bike_drawing.penup()
    bike_drawing.setx(-125)
    bike_drawing.sety(-100)
    bike_drawing.pendown()
    bike_drawing.dot(150,'gray')
    bike_drawing.dot(130,'white')
    bike_drawing.dot(30,'black')
    bike_drawing.dot(25,'gray')
    
     #right wheel
    bike_drawing.penup()
    bike_drawing.setx(125)
    bike_drawing.sety(-100)
    bike_drawing.pendown()
    bike_drawing.dot(150,'gray')
    bike_drawing.dot(130,'white')
    bike_drawing.dot(30,'black')
    bike_drawing.dot(25,'gray')
    
     #metal
    bike_drawing.left(135)
    bike_drawing.pensize(8)
    bike_drawing.pencolor('blue')
    bike_drawing.forward(50)
    bike_drawing.right(45)
    bike_drawing.forward(100)
    
     #handle
    bike_drawing.left(75)
    bike_drawing.pencolor('pink')
    bike_drawing.fd(20)
    bike_drawing.bk(40)
    bike_drawing.fd(20)
    bike_drawing.penup()
    bike_drawing.left(105)
    bike_drawing.pencolor('blue')
    bike_drawing.fd(7)
    bike_drawing.pendown()
    bike_drawing.fd(18)
    bike_drawing.right(90)
    bike_drawing.fd(150)

    #seat
    bike_drawing.right(70)
    bike_drawing.fd(20)
    bike_drawing.left(70)
    bike_drawing.pencolor('brown')
    bike_drawing.fd(20)
    bike_drawing.bk(40)
    bike_drawing.fd(20)
    bike_drawing.left(110)
    bike_drawing.penup()
    bike_drawing.fd(7)
    bike_drawing.pendown()
    bike_drawing.pencolor('blue')
    bike_drawing.fd(110)

    #gear
    bike_drawing.penup()
    bike_drawing.fd(20)
    bike_drawing.pendown()
    bike_drawing.dot(50,'black')
    bike_drawing.dot(45,'gray')
    bike_drawing.dot(30,'black')
    bike_drawing.dot(25,'white')
    bike_drawing.penup()
    bike_drawing.lt(110)
    bike_drawing.fd(27)
    bike_drawing.pendown()
    bike_drawing.goto(90,5)
    bike_drawing.penup()
    bike_drawing.goto(-60,5)
    bike_drawing.pendown()
    bike_drawing.goto(-115,-90)
    bike_drawing.penup()
    bike_drawing.goto(-110,-100)
    bike_drawing.pendown()
    bike_drawing.seth(90)
    bike_drawing.right(90)
    bike_drawing.forward(65)
    bike_drawing.penup()
    bike_drawing.forward(25)
    bike_drawing.lt(75)
    bike_drawing.fd(25)
    bike_drawing.pendown()
    
     #top pedal
    bike_drawing.pencolor("black")
    bike_drawing.fd(20)
    bike_drawing.rt(90)
    bike_drawing.fd(10)
    bike_drawing.bk(20)
    bike_drawing.fd(10)
    bike_drawing.lt(90)
    
     #bottom pedal
    bike_drawing.penup()
    bike_drawing.bk(70)
    bike_drawing.lt(10)
    bike_drawing.pendown()
    bike_drawing.bk(20)
    bike_drawing.rt(90)
    bike_drawing.fd(10)
    bike_drawing.bk(20)

    
      
 ########################
# Question 11
########################

def alogical(n):
    '''(Number)-> Number
    Returns the minimum number of times that 'n' needs to be divided by 2 in order to get a number equal or smaller than 1
    Preconditon: 'n' is bigger or equal to 1
    '''
    return int(math.log(n,2)+1)


 ########################
# Question 12
########################

def time_format(h,m):
    '''(number,number)-> String
    Returns the time as descriptive string
    Precondition: 'h' (integer 0 to 23) and 'm' (integer 0 to 59)
    '''
    min=int(5*round(float(m)/5))

    if m==0 or min==0:
     print( h,"o'clock. ")
    elif min==30:
         print("half past",h , " o'clock.")
    elif m<30 and m>0: 
         print(min," minutes past ",h,"o'clock.")
    elif m>30:
         if h==23:
             print(int(60-min)," minutes to 0 o'clock.")
         else:
             print(int(60-min)," minutes to ",(h+1)," o'clock.")
             

 ########################
# Question 13
########################

def cad_cashier(price,payment):
    '''(number,number)-> number
    Returns a real number with 2 decimal places representing the change the customer should get in Canadian dollars
    Preconsitions: 'price' and 'payment' are two real non-negative nummbers with two decimals, also the seocond decimal place in 'payment' is 0 to 5 
    '''
    x=0.05*round(float(price)/0.05)
    change=round(payment - x,2)
    return change


 ########################
# Question 14
########################

def min_CAD_coins(price,payment):
    '''(number,number)-> number
    Returns the minimum number of coins that the cashier can return in terms of toonies, loonies, quarters, dimes, and nickels
    Preconditions: 'price' and 'payment' are two real non-negative nummbers with two decimals, also the seocond decimal place in 'payment' is 0 to 5 
    '''
    change=cad_cashier(price,payment)
    t= int(change//2)
    l= int((change - (t*2)))
    q= int(((change - (t*2)-l)//0.25))
    d= int((change - (t*2)-l -(q*0.25))//0.1)
    n= int((change - (t*2)-l -(q*0.25) - (d*0.1))/0.5)
    return(t,l,q,d,n)





    

    

