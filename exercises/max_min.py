def count(array1):
    len1=0

    for x in array1:
        len1+=1

    return(len1)

 

def average(array1):
    sum=0

    for i in range(len(array1)):
        sum =sum+array1[i]

    return(sum/count(array1))

 

def min1(array1):
    min=array1[0]

    for i in range(len(array1)):
        if(min > array1[i]):
            min=array1[i]

    return(min)

 

def max1(array1):
    max=array1[0]
    
    for i in range(len(array1)):
        if(max<array1[i]):
            max=array1[i]

    return(max)

#data sets
B=[ 50, 9, 76, 39, 70, 54]
T=[120, 195, 82, 100]
N=[114, 110, 111, 100, 90, 80, 100]

print("----B------")

print("count:", count(B))

print("average:",average(B))

print("minimum:",min1(B))

print("maximum:",max1(B))

print("------T------")

print("count:", count(T))

print("average:",average(T))

print("minimum:",min1(T))

print("maximum:",max1(T))

print("------N------")

print("count:", count(N))

print("average:",average(N))

print("minimum:",min1(N))

print("maximum:",max1(N))

