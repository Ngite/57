
#pop
student ={
    "name":"nikita",
    "department":"cse",
    "class":"third year"
}
student.pop("class")
print(student)

#copy
original_marks={'physics':60,'maths':80}
copied_marks=original_marks.copy()
print('original_marks:',original_marks)
print('copied_marks:',copied_marks)

#fromkey
d2=('a','b','c')
print(dict.fromkeys(d2,1))
print(d2)

#get
d3=('a','b','c')
print(d3.get('a'))
print(d3)
