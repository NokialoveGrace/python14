fruits = ("apple", "banana", "cherry")
print(fruits[0])
fruits = ("apple", "banana", "cherry", "orange", "kowi", "mrlon", "mango")
print(fruits[2:5])
print(fruits[2:5])
print(fruits[2:5])
#เพิ่มค่าใน
x = ("apple", "banana", "cherry")
y = list(x) #แปลงเป็นlistแล้วเก็บค่าเข้า y
y[1] = "kiwi"
x = tuple(y)#แปลงค่าlistเป็นtupleแล้วกลับมาเป็นค่าที่x
print(x)
#ลบค่าในtuple
x =  ("apple", "banana", "cherry")
y = list(x)
y.remove("apple")
x = tuple(y)
print(x)
#join
tuple1 = ("a", "b", "c")
tuple2 = (1, 2 ,3)
tuple3 = tuple1 + tuple2
print(tuple3)
x = range(3 ,6)
for n in x :
    print(n)
x = range(3, 20, 2)
for n in x:
    print("rangeแบบstep:",n)
    #นายอรรถสิทธิ์ ไทรทอง ม.6/14 เลขที่12