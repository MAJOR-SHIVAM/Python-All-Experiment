# """AIM of the Experiment = Write a Python program which accepts the radius of a circle from the user and
# compute the area."""

# Roll_No = 231030308
# print("Your Roll Number is : ", Roll_No)
# print("\n")

#WAP to print last 3 digit of your roll no with two decimal place
# Roll_No = float(input("Enter last three digit of your Roll Number : "))
# print("{:.2f}".format(Roll_No))

# print("-----------------AIM - TO FIND THE RADIUS OF CIRCLE----------------------")
# x = input("Enter the value of Circle to get radius :  ")
# area = 3.14  * x * x
# print("Area of the circle is = ", area)

#WAP to find the version of Python using import platform lib

# import platform
# print("Python version = ", platform.python_version())




#WAP to find the area of circle

# radius = float(input("Enter the value of radius to find the area of circle :  "))
# area = 3.14 * radius * radius
# print("Area of the circle is = ", area)





#Write a Python program to display the current date and time.

# import datetime
# Time = datetime.datetime.now()
# #print("Current date and time : ")
# print(Time.strftime("Current date and time : %d-%m-%Y %H:%M:%S"))



#Write a Python program which accepts the radius of a circle from the user and
#compute the area.



# import math

# radius = float(input("Enter the value of radius to find the area of circle :  "))
# area = math.pi * radius * radius
# print("Area of the circle is = ", area)

#-----------------------------------------------------------------------------------------------



# Write a Python program which accepts the user's first and last name and print them
# in reverse order i.e., input "Shivam" then output "mavihs" with a space between them.

#Roll_No = 231030308
# print("Your Roll Number is : 231030308")
# name = input("Enter your name = ")
# z = name.split(" ")
# z.reverse()
# print(z)
# print(name[::-1])



# Write a Python program to display the first and last colors from the following list.
# color_list = ["Red","Green","White" ,"Black"].

# print("Roll Number = 231030308")
# color_list = ["Red", "Green", "White", "Black"]
# print("First color is : ", color_list[0])
# print("Last color is : ", color_list[-1])

#--------------------------------------------------------------------------------------------------------------





# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference. Write a Python
# program to test whether a number is within 100 of 1000 or 2000. Write a Python program to check whether a specified value is contained in a group of
# values. Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False


# print("Roll Number : 231030229")
# num = int(input("Enter the number: "))
# if num > 17:
#     print((abs(num-17))*2)
# else:
#     print(17-num)

# num = int(input("Enter the number: "))
# if num >= 900 and num <= 1100:
#     print("Number is within 100 of 1000")
# elif num >= 1900 and num <= 2100:
#     print("Number is within 100 of 2000")
# else:
#     print("Number is not within 100 of 1000 or 2000")

# val = int(input("Enter the value :"))
# input_list = [1, 5, 8, 3]
# if val in input_list:
#     print(f"{val} is in the list")
# else:
#     print(f"{val} is not in the list")


#----------------------------------------------------------------------------------------------------------



# Write a Python program to print all even numbers from a given numbers list in the
# same order and stop the printing if any numbers that come after 237 in the sequence.
# Sample numbers list :
# numbers = [
# 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615,
# 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950,
# 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81,
# 379, 843, 831, 445, 742, 717, 9

# print("Roll Number = 23103308")
# numbers = [386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 
# 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 
# 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 
# 379, 843, 831, 445, 742, 717, 958,743, 527] 

# for x in numbers:
#         if int(x) == 237:    break
#         if int(x) % 2 == 0:  print(x, end=" ")





# print("Roll Number = 231030308")
# with open("Experiment/Experiment_6.txt", "r") as myFile:
#     str = myFile.read().split(", ")
#     for x in str:
#         if int(x) == 237:    break
#         if int(x) % 2 == 0:  print(x, end=" ")



#------------------------------------------------------------------------------------------------------------------



# Write a Python program that accepts a single integer value entered by the user. If the value entered is less than one, the program prints nothing. If the user enters a positive integer, n, the program prints an n×n box drawn with * characters. If the users enters 1, for example, the program prints * If the user enters a 2, it prints ** ** An entry of three yields.
# print("Roll Number = 231030308")
# n = int(input("Enter a positive integer: "))
# if n >= 1: print(('\n' + '*' * n) * n)






#------------------------------------------------------------------------------------------------
# Write a Python program to sum of two given integers. However, if the sum is
# between 15 to 20 it will return 20. Write a Python program to compute the future
# value of a specified principal amount, rate of interest, and a number of years.
# Test Data : amt = 10000, int = 3.5, years = 7 Expected Output : 12722.79




# print("Roll Number = 231030308")
# s1 = int(input("Enter NUmber 1 = "))
# s2 = int(input("Enter NUmber 1 = "))
# sum = s1 + s2
# if 15 <= sum <= 20:
#     sum = 20
# print("Sum of",s1,"+",s2,":",sum)


# print("Roll Number = 231030308")
# amt = float(input("Enter the Principal Amount : "))
# r = float(input("Enter the Annual Interest : ")) 
# t = float(input("Enter the Time : "))
# future = amt * (1 + (r/100))**t
# print("Formula : Future Value = P * (1 + R)**T")
# print("Expected Output :", future)








# Q9--------10/09/24
# Write a Python program to create an array of 5 integers and display the array items.
# Access individual element through indexes. Write a Python program to convert an
# array to an ordinary list with the same items. 

# print("Roll Number = 231030222")
# import array
# x = array.array('i', [1,2,3,4,5])
# print(x)

# for i in range (len(x)):
#     print(x[i])

# b = list(x)
# print(b)





# # find out a sinusoidal data for the follwing question y(t) = sin(20 pi t) when 0 <= t <=10. Use only lambda and map function. make this program a generailesed form.

# import math
# t = list(map(lambda x : x/10, range(10)))
# y = list(map(lambda x : math.sin(20 * math.pi * x), t))
# print(t)
# print(y)






# 17-09-24

# Write a Python program to display all the member name of an enum class ordered by 
# their values. Expected Output: 
# Country Name ordered by Country Code: Afghanistan 
# Algeria Angola Albania Andorra 
# Antarctica


# from enum import Enum
# print("231030308")
# class country(Enum):
#     Afghanistan = 93
#     Algeria = 355
#     Antarctica = 213
#     UK = 376
#     Russia = 244
#     Ukraine = 672

# for x in sorted(country, key=lambda s: s.name):
#     print(x.name)




# by list comprehension


# from enum import Enum
# print("231030308")
# class country(Enum):
#     Afghanistan = 93
#     Algeria = 355
#     Antarctica = 213
#     UK = 376
#     Russia = 244
#     Ukraine = 672
# thislist = [print(x.name, x.value) for x in sorted (country, key= lambda x:x.value)]






# Write a Python program to get all values from an enum class.
# Expected output: [93, 355, 213, 376, 244, 672].


# from enum import Enum
# print("231030308")
# class country(Enum):
#     Afghanistan = 93
#     Algeria = 355
#     Antarctica = 213
#     UK = 376
#     Russia = 244
#     Ukraine = 672



# for x in sorted(country, key=lambda s: s.value):
#     print(x.value)



















# Write a Python program to get an array buffer information Expected Output: 
# Array buffer start address in memory and number of elements. 
# (25855056, 2)


# from array import array
# import array
# print("231030308")
# arr = array.array('i', [10, 20])
# print(arr)
# print(arr.buffer_info())




#-------------------------------------------------------------------------------------------------------------


#21/09/24

# Write a Python program to push three items into a heap and return the smallest item 
# from the heap. Also Pop and return the smallest item from the heap 
# ExpectedOutput: 
# Items in the heap: 
# ('V', 1) 
# ('V', 3) 
# ('V', 2) 
# The smallest item in the heap: ('V', 1) 
# Pop the smallest item in the heap: ('V', 2) 
# ('V', 3)








# import heapq
# print('Roll Number : 231030308')
# heap = []
# heapq.heappush(heap, ('V', 1))
# heapq.heappush(heap, ('V', 3))
# heapq.heappush(heap, ('V', 2))
# print("Items in the heap are...")
# for x in heap:
#     print(x)
# smallest = heapq.heappop(heap)
# print("The smallest item in the heap is: ", smallest)
# print("Pop the smallest item in the heap: ", heap[0])
# print(heap)









# def run_heap_example():
#     import heapq
#     heap = []
#     heapq.heappush(heap, ('V', 1))
#     heapq.heappush(heap, ('V', 3))
#     heapq.heappush(heap, ('V', 2))
#     print("Items in the heap are...")
#     for x in heap:
#         print(x)
#     smallest = heapq.heappop(heap)
#     print("The smallest item in the heap is: ", smallest)
#     print("Pop the smallest item in the heap: ", heap[0])
#     print(heap)

# run_heap_example()





# print("Roll number: 231030308")
# def print_big_enough(x,y):
#  print([i for i in x if i>y])
# A = [2,4,6,8,10]
# print(A)
# print_big_enough (A,5)



#-------------------------------------------------------------------------------------------------
#28/09/24

# Write a function called draw_rectangle that takes a Canvas and a Rectangle as 
# arguments and draws a representation of the Rectangle on the Canvas. 2. Add an 
# attribute named color to your Rectangle objects and modify draw_rectangle so that it 
# uses the color attribute as the fill color. 3. Write a function called draw_point that 
# takes a Canvas and a Point as arguments and draws a representation of the Point on 
# the Canvas. 4. Define a new class called Circle with appropriate attributes and 
# instantiate a few Circle objects. Write a function called draw_circle that draws circles 
# on the canvas. 5. Write a program that draws the national flag of the India. Hint: you 
# can draw a polygon like this: points 
# = [[-150,-100], [150, 100], [150, -100]] canvas.polygon(points, 
# fill='saffron,white,green')


# import tkinter as tk
# import math
# print("Roll Number : 231030308")
# def draw_flag(canvas):
    
#     canvas.create_rectangle(50, 50, 350, 100, fill='#FF9933', outline='black')
#     canvas.create_rectangle(50, 100, 350, 150, fill='white', outline='black')
#     canvas.create_rectangle(50, 150, 350, 200, fill='#138808', outline='black')
#     canvas.create_rectangle(60, 50, 50, 500, fill='#964B00', outline='black')
#     canvas.create_rectangle(35, 500, 75, 525, fill='#964B00', outline='black')
#     canvas.create_line(50, 50, 50, 525, fill='#F8E231', width=5)
#     draw_chakra(canvas, 200, 125)


# def draw_chakra(canvas, x, y):
#     canvas.create_oval(x - 25, y - 25, x + 25, y + 25, outline='navy', width=2)

#     for i in range(24):
#         angle = 2 * math.pi * i / 24  
#         x1 = x  
#         y1 = y
#         x2 = x + 25 * math.cos(angle)  
#         y2 = y + 25 * math.sin(angle)
#         canvas.create_line(x1, y1, x2, y2, fill='navy', width=2)

# def main():
#     root = tk.Tk()
#     root.title("National Flag of India")

#     canvas = tk.Canvas(root, width=1000, height=900, bg="white")
#     canvas.pack()

#     draw_flag(canvas)

#     root.mainloop()
 
# if __name__ == "__main__":
#     main()










# from TurtleWorld import *
# from random import randint

# class Wobbler(Turtle):
#     """a Wobbler is a kind of Turtle with attributes for speed and
#     clumsiness."""

#     def __init__(self, world, speed=1, clumsiness=60, color='red'):
#         Turtle.__init__(self, world)
#         self.delay = 0
#         self.speed = speed
#         self.clumsiness = clumsiness
#         self.color = color

#         # move to the starting position
#         self.pu() 
#         self.rt(randint(0,360))
#         self.bk(150)

#     def step(self):
#         """step is invoked by TurtleWorld on every Wobbler, once
#         per time step."""
        
#         self.steer()
#         self.wobble()
#         self.move()

#     def move(self):
#         """move forward in proportion to self.speed"""
#         self.fd(self.speed)

#     def wobble(self):
#         """make a random turn in proportion to self.clumsiness"""
#         dir = randint(0,self.clumsiness) - randint(0,self.clumsiness)
#         self.rt(dir)

#     def steer(self):
#         """steer the Wobbler in the general direction it should go.
#         Postcondition: the Wobbler's heading may be changed, but
#         its position may not."""
#         self.rt(10)

# def make_world(constructor):

#     # create TurtleWorld
#     world = TurtleWorld()
#     world.delay = .01
#     world.setup_run()

#     # make three Wobblers with different speed and clumsiness attributes
#     colors = ['orange', 'green', 'purple' ]
#     i = 1.0
#     for color in colors:
#         t = constructor(world, i, i*30, color)
#         i += 0.5

#     return world

# if __name__ == '__main__':
#     world = make_world(Wobbler)
#     world.mainloop()






##---------------------------------------------------------------------------------------------------------


                    ## ----------- 12/11/2024  ----------- ##

# Use Tkinter to write a basic web browser. It should have a Text widget where the 
# user can enter a URL and a Canvas to display the contents of the page. You can use 
# the urllib module to download files (see Exercise 14.6) and the HTMLParser module 
# to parse the HTML tags (see http: // docs. python. org/ 2/ library/ htmlparser. html ). 
# At a minimum your browser should handle plain text and hyperlinks. As a challenge 
# you 
# could handle background colors, text formatting tags and images. 



import tkinter as tk
from tkinter import ttk
from urllib import request
from html.parser import HTMLParser

class BasicWebBrowser:
    def __init__(self, root):
        self.root = root
        self.root.title("Basic Web Browser")

        # URL Entry Field
        self.url_entry = ttk.Entry(root, width=100)
        self.url_entry.pack(pady=5)

        # Go Button
        self.go_button = ttk.Button(root, text="Go", command=self.load_page)
        self.go_button.pack(pady=5)

        # Text widget to display webpage content
        self.text_display = tk.Text(root, wrap="word", width=100, height=35, bg="white", font=("Helvetica", 10))
        self.text_display.pack(padx=10, pady=10)

        # Configure the Text widget to display links in blue
        self.text_display.tag_configure("link", foreground="blue", underline=True)

        # Initialize HTML parser
        self.parser = MyHTMLParser(self.text_display)

    def load_page(self):
        url = self.url_entry.get()
        if not url.startswith("http"):
            url = "http://" + url  # Ensure URL starts with http:// or https://
        
        try:
            # Fetch the page content
            response = request.urlopen(url)
            page_content = response.read().decode('utf-8')
            self.text_display.delete(1.0, tk.END)  # Clear previous content
            self.parser.feed(page_content)  # Parse and display the new content
        except Exception as e:
            self.text_display.insert(tk.END, f"Error: {e}\n", "error")

class MyHTMLParser(HTMLParser):
    def __init__(self, text_display):
        super().__init__()
        self.text_display = text_display
        self.link_text = ""
        self.is_bold = False
        self.is_italic = False

    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr in attrs:
                if attr[0] == 'href':
                    self.link_text = f"Link: {attr[1]}"
        elif tag == 'b' or tag == 'strong':
            self.is_bold = True
        elif tag == 'i' or tag == 'em':
            self.is_italic = True

    def handle_endtag(self, tag):
        if tag == 'a':
            self.link_text = ""
        elif tag == 'b' or tag == 'strong':
            self.is_bold = False
        elif tag == 'i' or tag == 'em':
            self.is_italic = False

    def handle_data(self, data):
        font_style = ("Helvetica", 10, "")
        if self.is_bold and self.is_italic:
            font_style = ("Helvetica", 10, "bold italic")
        elif self.is_bold:
            font_style = ("Helvetica", 10, "bold")
        elif self.is_italic:
            font_style = ("Helvetica", 10, "italic")

        if self.link_text:
            self.text_display.insert(tk.END, self.link_text + "\n", "link")
            self.link_text = ""
        self.text_display.insert(tk.END, data, font_style)
        self.text_display.insert(tk.END, "\n")

if __name__ == "__main__":
    root = tk.Tk()
    browser = BasicWebBrowser(root)
    root.mainloop()
