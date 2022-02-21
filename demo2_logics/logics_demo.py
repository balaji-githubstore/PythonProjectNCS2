num = 9

if num > 0:
    print("Positive number")
    print("*" * 50)
elif num == 0:
    print("It is zero!!!")
    print("*" * 50)
else:
    print("Negative number")
    print("*" * 50)

browser_name = "CH"

# 1.	Declare the browsername and intialize with either ch or ff or edge or ie
# 2.	Write the if condition to launch the browser name based on the variable declared

if browser_name == "ch" or browser_name == "CH":
    print("Launch Chrome")
elif browser_name == "ff":
    print("Launch firefox")
elif browser_name == "edge":
    print("Launch edge")
else:
    print("Launch ie")

# numbers=[98,-99,89]
#
# if numbers[2]>0:
#     print("posiiiiitive")

page_number = 280

if page_number >= 100:
    if page_number <= 200:
        print("yes, it's between 100 and 200!!")

if page_number >= 100 and page_number <= 200:
    print("yes, it's between 100 and 200!!")
else:
    print("no, it's not between 100 and 200!!")

if 100 <= page_number <= 200:
    print("yes, it's between 100 and 200!!")
else:
    print("no, it's not between 100 and 200!!")
