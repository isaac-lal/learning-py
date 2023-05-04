# freeCodeCamp.org: Learn Python - Full Course for Beginners [Tutorial] (3:12:41)

'''
r = read (read the file, but not edit)
w = write (write in the file and modify it)
a = append (add to the end of the file, but not modify existing contents)
r+ = read and write (read and write inside the file)
'''

personal_file = open("personal-file.txt", "r") # not running but code still works

for skill in personal_file.readlines():
    print(skill)

print("------------------")

print(personal_file.readable()) # prints a boolean if the file is readable, r = true and w = false
print(personal_file.read())
print(personal_file.readline()) # prints first line
print(personal_file.readline()) # prints second line
print(personal_file.readlines()[1]) # prints all lines and putting it inside an array

personal_file = close()