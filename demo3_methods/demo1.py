def area_of_circle(radius):
    result = 3.14 * radius * radius
    return result


def area_of_triangle(base, height):
    return (base * height) / 2


print("*" * 50)

output = area_of_circle(10)
print(output)

output = area_of_circle(20)
print(output)

output = area_of_triangle(1, 25)
print(output)
