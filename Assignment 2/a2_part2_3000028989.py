#Family name: Samarth Agarwal
# Student number:  300028989
# Course: IT1 1120 
# Assignment Number 2 Part 2

import math

########################
# Question 2.1
########################

def min_enclosing_rectangle(r,x,y):
    '''(int,int,int) -> integer
    Preconditions: Enter a non negative integer
    The function returns  return the x- and y-coordinates of the bottom-left corner of the rectangle
    '''
    if r<0:
       return None
    else:
       return (x-r,y-r)
    

########################
# Question 2.2
########################

def series_sum():
    '''(None) -> integer
    Preconditions: Enter a non negative integer
    The function returns the sum of the series for the given integer n
    '''
    n=int(input("Please enter a non-negative integer:"))
    if n<0:
        return None
    sum1=1000
    for i in range (1,n+1):
        sum1=sum1+(1/(i**2))
        return sum1
    

########################
# Question 2.3
########################

def pell(n):
    '''(integer) -> integer
    Preconditions: Enter a non negative integer
    The function returns the pell number for the given integer n
    '''
    if n<0:
         return None
    if n<=2:
        return n
    else:
        x = (((((1+math.sqrt(2))**n)-((1-math.sqrt(2))**n)))//(2*math.sqrt(2))) + 1
        return x
    

########################
# Question 2.4
########################

def countMembers(s):
    '''(string) -> integer
    Preconditions: Enter string in quoatation marks
    The function returns the number of extraordinary characters from string
    '''
    l = list(s)
    a=0
    for j in range(len(l)):
        if l[j]>= 'e' and l[j] <= 'j':
            a+=1
        elif l[j] >= 'F' and l[j] <= 'X':
            a+=1
        elif l[j] >= str(2) and l[j] <= str(6):
            a+=1
        elif l[j] == '!' or l[j] == ',' or l[j] == '\\':
            a+=1
    return a


########################
# Question 2.5
########################

def casual_number(s):
    '''(string) -> integer
    Preconditions: To obtain an integer, enter an integer in quotations
    The function returns the integer entered without the commas
    '''
    leftover = s.replace("-","").replace(",","")
    for j in range (0,10):
        leftover = leftover.replace(str(j),"")
    if ((leftover != "") or (s.count("-")>1) or (s.replace("-","").replace(",","") == "")):
        return None
    else:
        if (s.count(",") > 0):
            splitted = s.replace("-","").split(",")
            if (len(splitted[0]) > 3):
                return None
            for j in range(1,s.count(",")):
                if (len(splitted[j]) != 3):
                    return None
    return s.replace(",","")


########################
# Question 2.6
########################

def alienNumbers(s):
    '''(str) -> int
    Precondition: The characters given are specified by alien language
    Returns the calculated integer according to the string given of alien language
    '''
    return (s.count("T") * 1024 + s.count("y") * 598 + s.count("!") * 121 + s.count("a") * 42 + s.count("N") * 6 + s.count("U") * 1)


########################
# Question 2.7
########################

def alienNumbersAgain(s):
    '''(str) -> int
    Precondition: The chracters given are specified by the alien language
    Returns the calculated integer according to the string given of alien language
    '''
    accum = 0
    for i in s:
        if i == "T":
            accum = accum + 1024
        elif i == "y":
            accum = accum + 598
        elif i == "!":
            accum = accum + 121

        elif i == "a":
            accum = accum + 42
        elif i == "N":
            accum = accum + 6
        elif i == "U":
            accum = accum + 1
    return accum


########################
# Question 2.8
########################

def encrypt(s):
    '''(str) -> string
    Precondition: The 's' is a string
    Returns returns a string which is the encrypted version of s.
    '''
    s = s[::-1]
    end = ""
    if (len(s)//2 == 0):
        return(s)
    elif(len(s)%2 != 0):
        x = len(s)//2
        for j in range(0,x):
            end+=s[j]+s[len(s)-1-j]
        return(end + s[len(s)//2])
    else:
        x = len(s)//2
        for j in range(0,x):
            end+=s[j]+s[len(s)-1-j]
        return(end)

    
        
########################
# Question 2.9
########################

def oPify(s):
    '''(str) -> string
    Precondition: The 's' is a string
    Returns a string with the letters o and p inserted between every pair of consecutive characters of s, as follows
    '''
    ans = ""
    count = 0
    if (len(s) <= 1):
        return(s)
    for i in range(0,len(s)):
        x = s[i]
        if (x.isalpha() != True):
            ans+=x
        else:
            if (i == 0):
                if (x.isupper()):
                    ans+=x+"O"
                else:
                    ans+=x+"o"
            elif (i == (len(s) - 1)):
                if(s[i-1].isalpha() == True):
                    if (x.isupper()):
                        ans+="P"+x
                    else:
                        ans+="p"+x
                else:
                    ans+=x
            else:
                if (s[i+1].isalpha()):
                    if (x.isupper()):
                        ans+="P" + x + "O"
                    else:
                        ans+="p" + x + "o"
                else:
                    if (x.isupper()):
                        ans+="P" + x
                    else:
                        ans+="p" + x
                    
    return(ans)


########################
# Question 2.10
########################

def nonrepetitive(s):
    '''(str) -> String
    Precondition: The 's' is a string
    Returns the True if 's' is nonrepetitive and False otherwise
    '''
    for j in range(1,len(s)):
        for z in range(0,len(s),j):
            if((str(s[z:z+j]+s[z:z+j]) in s) == True):
                return(False)
    return(True)










