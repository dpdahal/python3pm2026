# loop
# for -> list, tuple, set, dict, string
# while -> condition
# nested loop

# i=1 
# while i<=10:
#     print(i,end=" ")
#     i+=1


# i=10
# while i>=1:
#     print(i,end=" ")
#     i-=1

# i=1 
# total =0
# while i<=10:
#     if i%2==0:
#         print(i,end=" ")
#     total+=i
#     i+=1

# print("\nTotal:",total)


# numbers=[12,56,76,67,87,70,70,67]

# data=[
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]
# ]

# result =[12,14,16]
# for n in numbers:
#     print(n,end=" ")

# for i in range(1,11):
#     print(i,end=" ")


# x=0
# while x<len(numbers):
#     print(numbers[x],end=" ")
#     x+=1



users=[]
num =int(input("Enter number of users: "))
x=1
while x<=num:
    name = input("Enter name: ")
    users.append(name)
    x+=1


print("Users:",users)