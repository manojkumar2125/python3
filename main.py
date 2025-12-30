name = input("Enter the name: ");
age = int(input("Enter the age: "))
print("Hello" + name +", you are " + str(age) + " years old");

a = 20;
b =30;

a,b =b,a 
print(a, b)

if(age<=18):
    print("Major")
elif(age>18):
    print("Minor")
else:
    print("Not Valid age")

print(float(age))


list = [1,2,3,4,5]
for i in range(len(list)):
    print(list[i])


n =5
sum =""

for i in range(1,n):
    sum +=(str(i))
    print(sum)

print(name[::-1])
