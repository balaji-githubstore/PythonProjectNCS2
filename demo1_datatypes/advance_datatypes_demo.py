

colors = ['red', 'green', 'yellow', 'pink']

print(type(colors))

print(colors)
print(colors[0])

list_size = len(colors)
print(list_size)

colors.append('blue')
colors.append('white')
print(colors)
print(colors[4])

colors.remove('yellow')

print(colors)

colors.insert(1, 'orange')
print(colors)

colors.append('red')

print(colors)

print(colors.count('blue'))

print(len(colors))

# will start at 10:55 AM IST

fruits = ['banana', 'mango', 'orange']
print(fruits)
# remove the item at index 1 and returns it
removed_item = fruits.pop(1)
print(removed_item)
print(fruits)
fruits.append('pineapple')
print(fruits)
fruits.insert(2, 'JackFruit')
print(fruits)

signal = ('red', 'green', 'yellow')
print(signal[0])

appium_dic = {
    'platformName': 'android',
    'deviceName': 'redmi k20',
    'browserName': 'chrome',
    'deviceId':909983
}

print(appium_dic)
print(appium_dic['deviceName'])


student_record={
    'studentId':1001,
    'studentName':'John',
    'percentage':72.7,
    'mailId':'john@gmail.com',
    'marks':[55,98,56,89,88]
}

print(student_record['studentId'])

print(student_record['marks'])

print(student_record['marks'][1])

item_count=len(student_record['marks'])
print(item_count)



