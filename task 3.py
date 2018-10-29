course_taken = int(input("how many courses are you taking?"))
course_mark = 0
for x in range(0, course_taken):
    if course_taken > 0:
        course_mark = course_mark + float(input("what is your mark for this course?")) #this code represents the amount of times the program is gonna ask the user what mark they have in their course.
divide = course_mark/course_taken #this calculates the students average based on their course mark and number of courses taken.
print(divide)
if divide >= 79.5:
    print ("Congratulations! You have received the Principals award.") #congratulates the user on receiving the principals award.
if divide <= 79.5:
    print ("I'm sorry, your average doesn't qualify for the Principals award.") #lets the user know they don't qualify for the principals award.