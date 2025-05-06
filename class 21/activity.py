student={'name':'bob','age':'10','height':'1.99'}
print(student)
student['gender']="male"
print(student,"n")
print("after deleting height: ")
student.pop('height')
print(student)
print("after delete last item")
student.popitem()
print(student)

