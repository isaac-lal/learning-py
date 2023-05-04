# freeCodeCamp.org: Learn Python - Full Course for Beginners [Tutorial] (3:21:28)

# employee_file = open("employees.txt", "a") # appends onto existing text in file
employee_file = open("employees1.txt", "w")

employee_file.write("Isaac - Software Engineer")
employee_file.write("\nKelly - Customer Service") # adds new line onto the file with the text

# You can also use writing files to make html code and code a website
employee_file.close()