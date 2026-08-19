#one list
courses=['History','Math','Physics','Compsci']
#切片
print(courses)
print(len(courses))  
print(courses[0])
print(courses[-1])
print(courses[0:2])
print(courses[2:])
print(courses[:2])
#append method
courses.append('Art')
print(courses)
#insert method
courses.insert(1,'English')
print(courses)
courses_2=['Chinese','Education']
#extend method(添加了一整个list.courses_2,并不能提取单独的元素出来)
courses.insert(0,courses_2)
print(courses)
#能提取每一个元素
courses.extend(courses_2)
print(courses)
#remove method
courses.remove(courses_2)
print(courses)
#pop method(删掉最后一个元素)
courses.pop()
poped=courses.pop()
print(poped)
print(courses)
#reverse method颠倒清单
courses.reverse()
print(courses)
#sort method排序方法
nums=[1,3,2,5,4]
nums.sort()
print(nums)
#descending order
nums.sort(reverse=True)
print(nums)
# sorted function
sorted_courses=sorted(courses)
print(sorted_courses)
#min max sum
print(min(nums),max(nums),sum(nums))
#index method索引
print(courses.index('Art'))
#Ture or False
print('PE' in courses)
#loop循环
for item in courses:
    print(item)