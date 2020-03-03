
import os

#roster.txt and script should be in different location than student submissions
os.chdir('path\\to\\student\\submissions\\folder')

roster_array = open("path\\to\\roster.txt").read().splitlines()
print(roster_array)

for file in os.listdir():
    complete_file_name, file_ext = os.path.splitext(file)
    placeholder = complete_file_name.split("_")
    student_name = placeholder[0]
    if student_name not in roster_array:
        print("%s not in roster, deleting file" % (student_name))
        os.remove(file)
 
