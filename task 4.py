import math
cookies = int(input("How many cookies are being produced?")) #asks the user how many cookies are being produced.
if cookies < 200:
    print ("There is a minimum of 200.") #if the user puts a number under 200, lets the user know there is a minimum of 200 cookies.
    cookies = int(input("How many cookies are being produced?"))
boxes =math.floor (cookies/12) #calculates how many boxes are required depending on the amount of cookies.
print ("The number of boxes you need is ", boxes)
crates =math.floor (boxes/20) #calculates how many crates are required depending on the amount of boxes.
print ("The number of crates you need is ", crates)
singles = cookies%12 #calculates the number of left over (single) cookies there are.
print ("The number of singles cookies you have is ", singles)
boxes = cookies%240 #calculates the remainder cookies that can't fit in a crate and must go in a box.
boxes =math.floor (boxes/12)
total_value = crates*80 + boxes*5 + singles*0.50 #calculates the total value including crates, boxes and singles.
print ("The total value is ", total_value)

