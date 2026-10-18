#creating list to store 5 students names

names = ["amit","kapil","raju","ravi","karan"]

print(type(names))
print(names[0])
for n in names :
    print(n)



names=["amit","falguni","ashiravad","saurabbh"]
print(type(names))
print(names[0])
for n in names:
    print(n)
    


names=["amit","ravi","kapil","raju","ravi"]
#list slicing

print(names[0:4])
print(names[1:4])
print(names[:3])
print(names[2:])
print(names[::2])
print(names[::-1])

print("no of time ravi in list ",names.count('ravi'))
print("index of ravi in list ",names.index('ravi'))





course=[] #empty list
for i in range(3):
    c=input("enter the course name :")
    course.append(c)
print("courses ", course)


animal=[]  #empty list
for i in range(3):
    r = input("enter the animal name :")
    animal.append(r)
print(animal)    
   



product=[]
for i in range(3):
    p=input("enter product name :")
    pr=float(input("enter the price of product :"))
    stock=int(input("enter the stock :"))
    prod=(p,pr,stock)
    product.append(prod)
print("product details ",product)






student=[]
for i in range(3):
    n=input("enter the name here :")
    r=int(input("enter the roll no. here : "))
    c=input("enter the course :")
    m=int(input("enter the mobile number :"))
    e=input("enter the email :")
    stud=(n,r,c,m,e)
    student.append(stud)
print("student details :", student)



def gaandu(num):
    area= 3.14* num**2
    print(area)
radius=int(input("Enter radius"))
gaandu(radius)



emp = ["arun","amit"]
           
emp1= ["rohit","monalisa"]

emp.extend(emp1)
print("print emploees ",emp)

emp2=["aryan","falguni"]
emp.extend(emp2)
print("print employees ",emp)

emp.insert(1,"raghav")
print("after insert employees ",emp)

emp.remove("amit")
print("after remove employees ",emp)

result = emp.pop(1)
print("after pop employees ",emp)

print("index of monalisa",emp.index('monalisa'))
print("count of rohit",emp.count('rohit'))

emp.sort()
print("sort employees ",emp)

emp.reverse()
print("reverse of employees ",emp)



# 1. Student Marks Manager

# python


marks = [78, 85, 62, 90, 55]

print("All marks:", marks)
print("Highest mark:", max(marks))
print("Lowest mark:", min(marks))
print("Average:", sum(marks) / len(marks))

marks.append(88)          # add new mark
print("after append marks will ",marks)

marks.remove(55)          # remove a mark
print("after remove marks will :",marks)

marks.sort(reverse=True)  # sort descending
print("Updated marks:", marks)












