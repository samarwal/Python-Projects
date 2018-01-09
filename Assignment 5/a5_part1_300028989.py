#Name: Samarth Agarwal
#Student number:  300028989
#Course: IT1 1120 
#Assignment Number 5, Part 1


#Question 1a)
def largest_34(a):
    '''(list)->int
    returns the sum of the 3rd and 4th largest values in the list a
    Precondition: a has at least 4 elements
    '''
    temp_list = []
    for item in a:
        temp_list.append(item)

    big = max(temp_list)
    temp_list.pop(temp_list.index(big))
    sec_big = max(temp_list)
    temp_list.pop(temp_list.index(sec_big))
    thd_big = max(temp_list)
    temp_list.pop(temp_list.index(thd_big))
    frth_big = max(temp_list)
    temp_list.pop(temp_list.index(frth_big))
    return frth_big + thd_big



#Question 1b)
def largest_third(a):
    '''(list)->int
    Returns the sum of the len(a)//3 of the largest values in the list a
    Precondition: Numbers in the list a are all distinct and that the
    list a has at least 3 elements'''
    emp_list = []
    for item in a:
        emp_list.append(item)

    emp_list.sort()

    return sum(emp_list[-len(a)//3:])


#Question 1c)
def third_at_least(a):
    '''(list)->int
    Returns a value in a that occurs at least len(a)//3 + 1 times.
    If no such element exists in a, then the function returns None'''
    a_list = []
    for item in a:
        a_list.append(item)

    a_list.sort()
    
    time = len(a)//3 + 1
    counter = 0
    for i in range(len(a_list)):
        if i + time < len(a_list) and a_list[i] == a_list[i + time-1]:
            return a_list[i]

    return None

#Question 1d)
def sum_tri(a,x):
    '''(list)->bool
    Returns whether there exists indices i, j and k such that
    a[i]+a[j]+a[k]=x'''
    a.sort()
    for i in range(len(a)):
        j = i
        k = len(a) - 1
        while j <= k:
            if a[i] + a[j] + a[k] == x:
                return True
            elif a[i] + a[j] + a[k] > x:
                k -= 1
            else:
                j += 1
    return False






