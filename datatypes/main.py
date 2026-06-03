# what is data types
# two types of data types
# 1. primitive data types
# 2. non-primitive data types

# 1. primitive data types: int,float,complex,bool,str,None

# name ='admin'
# print(type(name))
# print(dir(name))
# print(id(name))

# name ='admin'
# print(name[2])
# course="we are learning python"
# print(course[2:6])
# print(course.upper())
# print(course.capitalize())
# print(course.title())
# print(course.split())

# RAm rAi
# Ram Rai

# list -> collection of items which are ordered and changeable

# users=['ram','shyam','hari']
# users[0]='laxmi'
# print(users)
# print(users[5])

# data=[
#     [12,34,56,87,89],
#     [23,[[[45]],800],67,78,90]
# ]

# print(data[0][0])

# data=['ram']

# print(dir(data))

# 'append', 'clear', 'copy', 'count', 'extend',
# 'index', 'insert', 'pop', 'remove', 'reverse', 'sort'

# data=[]
# data.append('ram')
# data.append('shyam')
# print(data)

# data=['ram','sita','Shyam','anil','laxmi']
# data.insert(0,'hari')
# data.pop(1)
# data.remove('sita')
# data.sort()
# data.sort(reverse=True)
# print(data)
# data1=['hari','gita']
# data.append(data1)
# data.extend(data1)
# print(data)

# data =('ram','shyam','hari')
# data[0]='laxmi'
# print(dir(data))

# data =('ram','shyam','hari')
# data =list(data)
# data[0]='laxmi'
# data = tuple(data)
# print(dir(data))


# data ={'ram','sita','ram','laxmi'}
# print(data)

# data=['ram',20]

# data={
#     'name':'ram',
#     'age':20,
#     'course':'python',
#     'address':{
#         'city':'kathmandu',
#         'country':'nepal'
#     }
# }
# print(data['address']['city'])

# data=[
#     {
#         'name':"sophia",
#         'country':[
#             {
#                 'name':'nepal',
#             }
#         ]
#     }
# ]

# print(data[0]['name'],data[0]['country'][0]['name'])

data={
    'name':'ram',
    'age':20,
    'course':'python'
}
# print(data['names'])
print(data.get('names','key not found'))
print("we are learning python")

# print(dir(data))
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 
# 'popitem', 'setdefault', 'update', 'values'

# python operators
# 1. arithmetic operators: +, -, *, /, //, %, **
# 2. assignment operators: =, +=, -=, *=, /=, //=
# 3. comparison operators: ==, !=, >, <, >=, <=
# 4. logical operators: and, or, not
# 5. bitwise operators: &, |, ^, ~, <<, >>
# 6. membership operators: in, not in
# 7. identity operators: is, is not