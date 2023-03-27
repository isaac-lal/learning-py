# freeCodeCamp.org: Learn Python - Full Course for Beginners [Tutorial] (2:07:19)

# Dictionaries store information in key value pairs

month_convert = { # can also be numbers (Jan = 1, Feb = 2, etc.)
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December", 
}

print(month_convert["Nov"])
print(month_convert["Jan"])
print(month_convert.get("Luv")) # returns none if no value matches