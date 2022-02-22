name = "hello world"
print(type(name))
print(name)
print(name.upper())
print(name.lower())


num1 = "$120,500,000"
num2 = "$520,000"

# remove $ and , from num1 and num2
num1 = num1.replace("$", "").replace(",", "")
num2 = num2.replace("$", "").replace(",", "")
print(num1)
print(num2)

# below code covert to numeric type if it is a proper number
num1 = int(num1)
num2 = float(num2)
print(num1 + num2)

mail_id = "balaji@ncs.com"

print(mail_id[0])
print(mail_id[5])
print(mail_id[0:6])
print(mail_id[1:])
print(mail_id[6:])
print(mail_id[:6])


ls=mail_id.split("@")
print(ls)

print(ls[0])

text="Specify the start index and the end index"

ls=text.split(" ")
print(ls)

print(4**3)