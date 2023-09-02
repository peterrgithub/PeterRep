print("Hello world")
print("Python calculator")
first_number = 2
second_number = 8
sum_of_numbers = first_number + second_number
print(first_number)
print(second_number)
print(sum_of_numbers)
multiplication_of_numbers = first_number * second_number
print(multiplication_of_numbers)
division_of_numbers = second_number / first_number
print(division_of_numbers)
subtraction_of_numbers = second_number - first_number
print(subtraction_of_numbers)
name = "Menace"
print(name)

#shifting to string concatenation
first_number = "2"
second_number = "8"

#3.0 shifting to data structures (lists)
list_of_numbers = [2, 4, 6, 8]
print(list_of_numbers)
print(list_of_numbers[1])
print(list_of_numbers[1], list_of_numbers[3])
print(list_of_numbers[1] + list_of_numbers[3])

#addition of lists
list1 = [2, 4, 6]
list2 = [8, 10, 12]
print(list1[2] + list2[1])


#subtraction of lists elements between lists
list1 = [2, 4, 6]
list2 = [8, 10, 12]
print(list1[2] - list2[1])

#multiplication of lists elements between lists
list1 = [2, 4, 6]
list2 = [8, 10, 12]
print(list1[2] * list2[1])

#addition of multiple lists
list1 = [2, 4, 6]
list2 = [8, 10, 12]
print(list1 + list2)

#addition of multiple lists
list1.append (9)
print(list1)

#deleting elements of lists
list1.pop (3)       #NB: when deleting the elements of a list, the index is written without squared brackets 
print(list1)

#Manipulation of Lists
#The input is case sensitive; programmer has to create notice asking user to type their name in lowercase!
celebrities = ["davido", "wizkid", "ayrastarr"]
name = input ("What is your name?: ")
if name in celebrities:
    print("Access granted!")
else:
    print("Access denied!") #QUESTION: Why is input case sensitive? How can sensitivity be deactivated?

#Instructors login
usernames = ["jennifer", "halleluyah", "silvareal"]
passwords = [0, 1, 2]
username = input ("Write instructor name: ")
password = int(input("Write instructor password: "))
if username in usernames:
    if password in passwords:    
        print("login successful!")
    else:
        print("Invalid username or passpword")
    


#django_instructors = ["jennifer", "halleluyah", "silvareal"]
#name = input ("What is your name?: ")
#Index options must be enclosed in squared brackets for syntaxt to be correct.
#if name == (django_instructors[0], django_instructors[1], django_instructors[2]): #Does't work with indices?
 #   print("Access granted!")
#else:
 #   print("Access denied!")
