#a a recursive function to sum of natural numbers up to n
list = []
for x in range(1,100):
    if 0 == x and 100 == x :
        list.append(str(x))
print(",".join(list))

#removing element in index 2 

numbers = [1,3,5,7,9]
numbers.remove([2])
print(numbers)

#updating the dictionary
student_info = {
     'name' : 'Alice',
      'age' : 20,
     'grade' : 'A'
}
student_info.update({'age': 25})

#adding anew key value
student_info = {
     'name' : 'Alice',
      'age' : 20,
    'grade' : 'A'
}
student_info['city'] = 'New York'
print(student_info)


#value greater than 5
original_dic = {'a':3,'b':8,'c':2,"d":7}

for b, d in original_dic.value():
    print(b, d)
