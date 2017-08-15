# List
# List store comma separated value in array fashion.It can store number, string or mix.
my_list = ['a', 'b', 'c']
my_list2 = [1, 2, 3, 4, 5]
my_list3 = [1, 2, 'a', 'b']
print(my_list)
print(my_list2)


# Using Index use the value of the list. Index generally started fron 0.

print(my_list[0])
print(my_list[:])
print(my_list[1:])
print(my_list[:-1])
print(my_list[:-2])

# print last 2 value
print(my_list2[-2:])

# reverse string
print(my_list3[::-1])


# Dictionary store key value pairs

d = {

    "Python": "programing",
    "English": "natural",
    "java": "programing",
    "French": "natural",
    "scala": "programing",
    "javascript": "programing"
}

print(d)
# adding new values in dictionary

d["dot net"] = "programing"
print(d)

# you also add numbers in dictionary
d["language known"] = 3
print(d)

print(d["Python"])
# access values from dictionary
print(d.keys())
print(d.values())
print(len(d))

# Loops and conditionals

my_list4 = ["Java", "Python","Ruby","Html"]
print(my_list4)

for item in  my_list4:
    print(item)

x = 10
if x > 5:
    print("I feel x is greater than five")

if x > 10 and x < 20:
    print("i fell no is greater than five and less than 20")

number_list = [1,2,3,4,5,6,7,8,9,10]
for number in number_list:
    print(number)
# one liner output
print([number for number in number_list])

# print the no is even

for no in number_list:
    if no%2 == 0:
        print(str(no) + ": is even")
    elif no == 7:
        print(str(no) + ": is best odd no")
    else:
        print(str(no) + ": is odd")


# function - one work want do more time

def my_function(something):
    return something

print(my_function("Hello this is Cool!"))

