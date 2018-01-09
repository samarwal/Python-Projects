#Family name: Samarth Agarwal
# Student number:  300028989
# Course: IT1 1120 
# Assignment Number 2 Part 1

import math
import random


def primary_school_quiz(flag, n):
    # Your code for primary_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function

    correct=0
    if flag == 0:
        for n in range (n,0,-1):
            x = random.randint(0,10)
            y = random.randint(0,10)
            Answer = input("What is the result of " +str(x) + " - " + str(y) + "?")
            Solution = x-y
            if int(Answer) == Solution:
               print("Correct")
               correct=correct+1
            else:
                print("Wrong")
            m=(correct/n)*100
    if (m>=90):
         print("Congratulations "+name+" !"+ "You’ll probably get an A tomorrow. Now go eat your dinner and go to sleep. Good bye"+name+"!")
    elif (m>=70 and m<90):
         print("You did well "+name+", but I know you can do better. Good bye" +name+"!")
    elif (m<70):
         print("I think you need some more practice")
                
            
                            

    if flag==1:
        for n in range(n,0,-1):
            x= random.randint(0,10)
            y = random.randint(0,10)
            correct=0
            Answer = input("What is the result of " +str(x) + "^" + str(y) + "?")
            Solution = x**y
            if int(Answer) == Solution:
                print("Correct")
                correct=correct+1
            else:
                print("Wrong")
                m=(correct/n)*100
    if (m>=90):
        print("Congratulations "+name+" !"+ "You’ll probably get an A tomorrow. Now go eat your dinner and go to sleep. Good bye"+name+"!")
    elif (m>=70 and m<90):
        print("You did well "+name+ ", but I know you can do better. Good bye"+ name+"!")
    elif (m<70):
        print("I think you need some more practice")
                
            


def high_school_eqsolver(a,b,c):
    # Your code for high_school_quiz function goes here (instead of keyword pass)
    # Your code should include  dosctrings and the body of the function
           if c>0:
                    s1='+'
           elif c<0:
                    s1='-'
           if b>0:
                    s2='+'
           if b<0:
                    s2='-'

                    print('The linear Equation ',s2,b,'x ',s1,c)
           elif(a==0 and b==0 and c==0):
            print('The Quadratic Equation  ',a,'x^2 ',s2,b,'x ',s1,c)
            print("is satisfied for all numbers x")
           elif(a==0 and b!=0 and c!=0):
             print('The Quadratic Equation  ',a,'x^2 ',s2,b,'x ',s1,c)
             print(" is satisfied for no number x ")
            
           else: 
                  print('The Quadratic Equation  ',a,'x^2 ',s2,b,'x ',s1,c)
           d= ((b**2)-(4*a*c))**0.5
           root1 = (-b-d)/(2*a)
           root2 = (-b+d)/(2*a)
           print (root1," and ",root2)
           





# main

# your code for the welcome tmessage goes here

print("\t\t *************************************************************")
print("\t\t *                                                           *")
print("\t\t * __Welcome to my math quiz-generator / equation-solver__   *")
print("\t\t *                                                           *")
print("\t\t *                                                           *")
print("\t\t *************************************************************")

name=input("\n What is your name? ")

status=input("\n Hi "+name+". Are you in? Enter \n1 for primary school\n2 for high school or\n3 for none of the above?\n")

if status=='1':
    # your code goes here
    m=int(input("Enter your choise (0-subtraction and 1-exponentiation): "))
    n=int(input("Enter the number of Questions you want to answer: "))
    if(n==0):
      print("\n No questions will be asked!\n ")
    else:  
        primary_school_quiz(m,n)
        
    
    

elif status=='2':

    # your code for welcome message
    flag=True
    while flag:
        question=input(name+", would you like a quadratic equation solved? ")

        # your code to handle varous form of "yes" goes here

        if question!="yes":
            flag=False
        else:
            print("Good choice!")
            # your code goes here (i.e ask for coefficients a,b and c and call)
            # then make a function call and pass to the fucntion
            # the three coefficients the pupil entered
            x1=int(input("Enter coefficient a: "))
            x2=int(input("Enter coefficient b: "))
            x3=int(input("Enter coefficient c: "))
            high_school_eqsolver(x1,x2,x3)
            
 
else:
    # your code goes here
    print(name+ " you are not a target audience for this software. ")

print("Good bye "+name+"!")



