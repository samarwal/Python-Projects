#Name: Samarth Agarwal
#Student number:  300028989
#Course: IT1 1120 
#Assignment Number 5, Part 2


class Point:
    'class that represents a point in the plane'

    def __init__(self, xcoord=0, ycoord=0):
        ''' (Point,number, number) -> None
        initialize point coordinates to (xcoord, ycoord)'''
        self.x = xcoord
        self.y = ycoord

    def setx(self, xcoord):
        ''' (Point,number)->None
        Sets x coordinate of point to xcoord'''
        self.x = xcoord

    def sety(self, ycoord):
        ''' (Point,number)->None
        Sets y coordinate of point to ycoord'''
        self.y = ycoord
        
    def get(self):
        '''(Point)->tuple
        Returns a tuple with x and y coordinates of the point'''
        return (self.x, self.y)

    def move(self, dx, dy):
        '''(Point,number,number)->None
        changes the x and y coordinates by dx and dy'''
        self.x += dx
        self.y += dy

    def __eq__(self, other):
        '''(Point,Point)->bool
        Returns True if self and other have the same coordinates'''
        return self.x == other.x and self.y == other.y
    def __repr__(self):
        '''(Point)->str
        Returns canonical string representation Point(x, y)'''
        return 'Point('+str(self.x)+','+str(self.y)+')'
    def __str__(self):
        '''(Point)->str
        Returns nice string representation Point(x, y).
        In this case we chose the same representation as in __repr__'''
        return 'Point('+str(self.x)+','+str(self.y)+')'


class Rectangle:
    'class that represents a rectangle in a plane'
    
    def __init__(self, bottomL, topR, color):
        ''' (Rectangle, Point, Point, string) -> None
        initialize rectangle'''
        self.bottomL = bottomL
        self.topR = topR
        self.color = color

    def get_bottom_left(self):
        '''(Rectangle)->Point
        Returns bottom left point of rectangle'''
        return self.bottomL

    def get_top_right(self):
        '''(Rectangle)->Point
        Returns top right point of rectangle'''
        return self.topR

    def get_color(self):
        '''(Rectangle)->str
        Returns the color of rectangle'''
        return self.color
    
    def reset_color(self, color):
        '''(Rectangle, string)->none
        Returns bottom left point of rectangle'''
        self.color = color

    def get_perimeter(self):
        '''(Rectangle) -> num
        Return the perimeter of the rectangle'''
        return abs(self.bottomL.x - self.topR.x)*2 + abs(self.bottomL.y - self.topR.y)*2

    def get_area(self):
        '''(Rectangle) -> num
        Return the area of the rectangle'''
        return abs(self.bottomL.x - self.topR.x)*abs(self.bottomL.y - self.topR.y)

    def move(self, dx, dy):
        '''(Rectangle, number, number)->none
        moves rectangle by dx and dy'''
        self.bottomL.move(dx, dy)
        self.topR.move(dx, dy)

    def intersects(self,other):
        '''(Rectangle, Rectangle)->bool
        returns whether the two rectangles in an argument intersect'''
        return (self.bottomL.x <= other.topR.x and
                self.topR.x >= other.bottomL.x and
                self.bottomL.y <= other.topR.y and
                self.topR.y >= other.bottomL.y)

    def contains(self,x,y):
        '''(Rectangle, int, int) -> bool
        Returns whether the point (x,y) is inside of the calling rectangle'''
        return self.bottomL.x<=x<=self.topR.x and self.bottomL.y<=y<=self.topR.y

    def __eq__(self,other):
        '''(Rectangle, Rectangle)->bool
        Returns True if self and other are equal rectangles'''
        return (self.bottomL == other.bottomL and
                self.topR == other.topR and
                self.color == other.color)

    def __repr__(self):
        '''(Rectangle)->str
        Returns canonical string representation of rectangle
        Rectangle(Point1(x,y), Point2(a,b), "color")'''
        return "Rectangle("+str(self.bottomL)+", "+str(self.topR)+", '"+self.color+"')"

    def __str__(self):
        '''(Rectangle)->str
        Returns nice string representation Rectangle(Point, Point, string).'''
        return "I am a "+self.color+" rectangle with bottom left corner at ("+str(self.bottomL.x)+", "+str(self.bottomL.y)+") and top right corner at ("+str(self.topR.x)+", "+str(self.topR.y)+")."
        

class Canvas:
    'class that contains rectangles in a plane'

    def __init__(self, rec=[]):
        ''' (Canvas) -> None
        Initialize Canvas with an empty list representing the list of
        rectangles on the canvas.
        '''
        self.rec = rec

    def add_one_rectangle(self, r):
        ''' (Canvas, rectangle) -> None
        add Rectangle to Canvas'''
        self.rec.append(r)

    def count_same_color(self, color):
        ''' (Canvas, string) -> int
        Return the count of rectangles in canvas with color "color" '''
        count = 0
        for i in self.rec:
            if i.get_color() == color:
                count += 1
        return count
    
    def total_perimeter(self):
        ''' (Canvas) -> num
        Returns the sum of the perimeters of rectangles in the canvas.
        '''
        perimeter = 0
        
        for rectangle in self.rec:
            perimeter += rectangle.get_perimeter()
        return perimeter

    def min_enclosing_rectangle(self):
        ''' (Canvas) -> Rectangle
        Returns minimum enclosing rectangle that contains all the
        rectangles in the calling canvas.
        '''

        min_x = self.rec[0].get_bottom_left().x
        min_y = self.rec[0].get_bottom_left().y
        max_x = self.rec[0].get_top_right().x
        max_y = self.rec[0].get_top_right().y
        
        for k in self.rec:
            if min_x > k.get_bottom_left().x:
                min_x = k.get_bottom_left().x
            if min_y > k.get_bottom_left().y:
                min_y = k.get_bottom_left().y
            if max_x < k.get_top_right().x:
                max_x = k.get_top_right().x
            if max_y < k.get_top_right().y:
                max_y = k.get_top_right().y

        return Rectangle(Point(min_x, min_y), Point(max_x, max_y), "red")
    

    def common_point(self):
        ''' (Canvas) -> bool
        returns whether rectangles in Canvas contain a common point'''
        for j in self.rec:
            for k in self.rec:
                if not j.intersects(k):
                    return False
        return True

    def __len__(self):
        ''' (Canvas) -> num
        Returns the size of the canvas.
        '''

        return len(self.rec)

    def __repr__(self):
        '''(Canvas)->str
        Returns canonical string representation of canvas
        '''
        
        return "Canvas("+str(self.rec)+")"    
        
    
    

    
    
    
    
    
    
    

        
        
        
        
    

    
    

    

    

    

    

    

    

    
