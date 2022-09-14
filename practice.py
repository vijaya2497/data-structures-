#Given a list, write a Python program to swap first and last element of the list.

"""
l = [3,4,5,6,8]
temp = l[0]
l[0] = l[-1]
l[-1] = temp
print(l)


l = [1,2,3,4,5]
l[0], l[-1] = l[-1], l[0]
print(l)


l = [1,2,3,4,5]
s, *m, e = l
l = e, *m , s
print(list(l))



# delete all elements from list

list1 *= 0


l = [1,2,3]
del l[1:]  deletes 2, 3
del l[:]    deletes all ele from list
print(l)



from collections import Counter

# declaring the list
l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]

# driver program
x = 3
d = Counter(l)
print('{} has occurred {} times'.format(x, d[x]))


# Sum of number digits in List
# using sum() + list comprehension
test_list = [12, 67, 98, 34]
l = list(map(lambda ele: sum(int(e) for e in str(ele)), test_list))
print(l)

#List Integer Summation : [3, 13, 17, 7]

from functools import reduce
test_list = [12, 67, 98, 34]
res = [reduce(lambda x, y : int(x) + int(y) , list(str(i))) for i in test_list]
print(res)


#multiply all numbers in list
from functools import reduce
l =  [1,2,3]
l1 = reduce(lambda x,y : x*y , l)
print(l1)

import math
l2 = math.prod(l)
print(l2)

# print even and odd  numbers in list
x = [2,5,6,8,3,9]
xe = [i for i in x if i%2 == 0]
xo = [i for i in x if i%2 != 0]
#print(xo)

xeve = list(filter(lambda x : x%2 == 0, x))
xodd = list(filter(lambda x: x%2 != 0, x))
print(xodd)

# count odd and even numbers in list
x = [2,5,6,8,3,9]
xel = len(list(filter(lambda x : x%2 == 0 , x)))
xol = len(list(filter(lambda x : x%2 != 0 , x)))
print(xel, xol)


# print positive and negative in list
x = [1, -1, 4, -5, 6 , -7]
xp = list(filter(lambda x : x > 0 , x))
xn = list(filter(lambda x : x < 0 , x))
print(xp, xn)


# removes elements from index 1 to 4
del list1[1:5]


# remove empty tuples from list
tuples = [(), ('ram','15','8'), (), ('laxman', 'sita'),
          ('krishna', 'akbar', '45'), ('',''),()]

#t = [ t for t in tuples if t]
#print(t)

t1 = list(filter(lambda x : len(x) > 0, tuples))
t1= list(filter(None, tuples))
print(t1)


l = [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
s = list(set(l))
print(s)

from collections import Counter

l1 = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]
d = Counter(l1)
print(d)

new_list = list([item for item in d if d[item] > 1])
print(new_list)


# Given a list, the task is to write a Python Program to square each odd number in a list using list comprehension.
data=[1,2,3,4,5,6,7]
s = [x*x for x in data if x %2 != 0]
print(s)



#  Given two lists, the task is to write a Python program to remove all the common elements of two lists.

a = [1, 2, 3, 4, 5]
b = [4, 5, 6, 7, 8,]

a, b = list(set(a) - set(b)), list(set(b) - set(a))
print(a,b)

a, b = list(set(a).difference(b)), list(set(b).difference(a))



# Get the indices of all occurrences of an element in a list
my_list = [1, 2, 3, 1, 5, 4]

indices = [ind for ind, ele in enumerate(my_list) if ele == 1]
print(indices)


# Given a list, the task is to write a Python Program to find the Index containing String.

l = ['sravan', 98, 'harsha', 'jyo', 78, 90]
#l1 = [ ind for ind, ele in enumerate(l) if type(ele) is str]
l1 = [l.index(i) for i in l if (type(i) is str)]
print(l1)



#  Convert list of dictionaries to dictionary of lists

data = [{'manoj': 'java', 'bobby': 'python'},
        {'manoj': 'php', 'bobby': 'java'},
        {'manoj': 'cloud', 'bobby': 'big-data'}]
print({key: [i[key] for i in data] for key in data[0]})


#Given two matrices, the task is to write a Python program to add elements to each row from initial matrix.
#input
l1 = [[4, 3, 5,], [1, 2, 3], [3, 7, 4]]
l2 = [[1, 3], [9, 3, 5, 7], [8]]
#output
[[4, 3, 5, 1, 3], [1, 2, 3, 9, 3, 5, 7], [3, 7, 4, 8]]

res = list(sub1 + sub2 for sub1, sub2 in zip(l1, l2))
print(res)



# Given a List of strings, the task is to write a Python program to sort list by the number present in the Strings. If no number is present, they will be taken to the front of the list.


#Input : test_list = [“gfg is 4”, “all no 1”, “geeks over 7 seas”, “and 100 planets”]
#Output : [‘all no 1’, ‘gfg is 4’, ‘geeks over 7 seas’, ‘and 100 planets’]
#Explanation : 1 < 4 < 7 < 100, numbers in strings deciding order.

l = ["gfg is 4", "all no 1", "geeks over 7 seas", "and 100 planets"]
def num_sort(strn):
    l =  [ele for ele in strn.split() if ele.isdigit()]
    if len(l) > 0:
        return int(l[0])
    return -1
l.sort(key=num_sort)
print(l)



# Get word frequency in percentage

test_list = ["Gfg is best for geeks", "All love Gfg", "Gfg is best for CS", "For CS geeks Gfg is best"]

#Output : {‘Gfg’: 0.21052631578947367, ‘is’: 0.15789473684210525, ‘best’: 0.15789473684210525, ‘for’: 0.10526315789473684, ‘geeks’: 0.10526315789473684, ‘All’: 0.05263157894736842, ‘love’: 0.05263157894736842, ‘CS’: 0.10526315789473684, ‘For’: 0.05263157894736842}

from collections import Counter

c = Counter(" ".join(ele for ele in test_list).split())
res = {key: val / sum(c.values()) for key, val in c.items()}
print(res)


# Python Program to Construct n*m Matrix from List


#Input : test_list = [6, 3, 7, 2, 6, 8, 4, 3, 9, 2, 1, 3], n, m = 3, 5
#Output : “Matrix Not Possible”
#Explanation : List has 12 elements and 3*5 is 15, hence Matrix not possible.

#Input : test_list = [6, 3, 7, 2, 6, 8], n, m = 2, 3
#Output : [[6, 3, 7], [2, 6, 8]]
#Explanation : List converted to 2*3 matrix.
test_list = [6, 3, 7, 2, 6, 8]
n,m = 2,3
k = 0
res = []
if n*m != len(test_list):
    print("matrix not possible")
else:
    for idx in range(0, n):
        sub = []
        for jdx in range(0, m):
            sub.append(test_list[k])
            k += 1
        res.append(sub)
print(res)


# Given a Matrix, the task is to write python program to reverse every Kth row. Where, K is some span value.

test_list = [[5, 3, 2], [8, 6, 3], [3, 5, 2], [3, 6], [3, 7, 4], [2, 9]]
k = 4
#Output: [[5, 3, 2], [8, 6, 3], [3, 5, 2], [6, 3], [3, 7, 4], [2, 9]]
#Explanation: Every 4th row is reversed.

s = [ele[ ::-1] if (ind+1)%4 == 0 else ele for ind, ele in enumerate(test_list)]
print(s)

# Program to extract Dictionaries with given Key from a list of dictionaries
test_list = [{'gfg' : 2, 'is' : 8, 'good' : 3}, {'gfg' : 1, 'for' : 10, 'geeks' : 9}, {'love' : 3, 'gfgs' : 4}]
key = "good"
#Output : [{‘gfg’: 2, ‘is’: 8, ‘good’: 3}]
s = [ele for ele in test_list if key in ele.keys() ]
print(s)

#given a list, the task is to write a Python program to replace the grouping of the consecutive elements with a product of the frequency and Item.
test_list = [3, 3, 3, 3, 6, 7, 5, 5, 5, 8, 8, 6, 6, 6, 6, 6, 1, 1, 1, 2, 2]
#Output : [12, 6, 7, 15, 16, 30, 3, 4]
#Explanation : 3 occurs 4 times in consecution hence, 3*4 = 12, the result.
from itertools import groupby
res = [sum(group) for k, group in groupby(test_list)]
print(res)



#Given a list of numbers, the task is to write a Python program to remove all numbers with repetitive digits.


test_list = [4252, 6578, 3421, 6545, 6676]

#Output : test_list = [6578, 3421]

#Explanation : 4252 has 2 occurrences of 2 hence removed. Similar case for all other removed.

#s = [sub for sub in test_list if len(set(str(sub))) == len(str(sub))]
import re
regex = re.compile(r"(\d).*\1")
res = [sub for sub in test_list if not regex.search(str(sub))]
print(res)


#Given a string list, our task is to write a Python Program to check all strings are disjoint from one another.
#Output : True
#Explanation : No string character repeat in other strings.
test_list = ["gfg", "is", "bet"]
concats = ''.join(test_list)
res = len(concats) == len(set(concats))
print(res)



# Given a List, our task is to write a Python program to reverse a range in the list.
test_list = [6, 3, 1, 8, 9, 2, 10, 12, 7, 4, 11]
start, end = 3, 9

#Output : [6, 3, 1, 7, 12, 10, 2, 9, 8, 4, 11]

#Explanation : 8, 9, 2, 10, 12, 7 are reversed in list to 7, 12, 10, 2, 9, 8.

test_list[start:end] = test_list[start:end][ :: -1]
print(test_list)



#Given a string S, the task is to print permutations of all words in a sentence.

#Examples:

#Input: S = “sky is blue”
#Output:
#sky is blue
#sky blue is
#is sky blue
#is blue sky
#blue sky is
#blue is sky

from itertools import permutations
sentence = "sky is blue"
lis = sentence.split()
permute = permutations(lis)
for i in permute:
    permutelist = list(i)
    s = " ".join(permutelist)
    print(s)



#Uncommon elements in Lists of List

test_list1 = [ [1, 2], [3, 4], [5, 6] ]
test_list2 = [ [3, 4], [5, 7], [1, 2] ]


res_set = set(map(tuple, test_list1)) ^ set(map(tuple, test_list2))
res_list = list(map(list, res_set))
print(res_list)


# reverse row sort
test_list = [[4, 1, 6], [7, 8], [4, 10, 8]]
res = [sorted(sub, reverse = True) for sub in test_list]
print(res)


# Test if List contains elements in Range
# using all()

# Initializing loop
test_list = [4, 5, 6, 7, 3, 9]

i, j = 3, 10

res = all(ele >= i and ele < j for ele in test_list)


# Python – Extract words starting with K in String List
test_list = ["Gfg is good for learning", "Gfg is for geeks", "I love G4G"]
K = 'l'
#Output : [‘learning’, ‘love’]

l1 = [ele for temp in test_list for ele in temp.split() if ele[0].lower() == K.lower()]
print(l1)



# Split String of list on K character
test_list = ['Gfg is best', 'for Geeks', 'Preparing']
k = ' '
l = k.join(test_list).split(k)
print(l)




# Function to locate the occurrence of the string x in the string s.
Input:
s = GeeksForGeeks, x = Fr
Output: -1


Input:
s = GeeksForGeeks, x = For
Output: 5
Explanation: For is present as substring
in GeeksForGeeks from index 5 (0 based
indexing).


def strstr(s, x):
    # code here

    if s.find(x) != -1:

        return s.find(x)
    else:
        return -1


#1. Write a function in python to read the content from a text file
#line by line and display the same on screen.


def read():
    filename = 'test.txt'
    with open(filename, "r") as f:
        data = f.readlines()
        for line in data:
            print(line)

    f.close()

read()

#Write a function in python to count the number of lines from a text file "test.txt"
#which is not starting with an alphabet "T".

def count():
    c = 0
    with open("test.txt", "r") as f:
        data = f.readlines()
    for line in data:
        if line[0] != 'T':
           c += 1
    return c
print(count())



#Write a function in Python to count and display the total number of words in a text file

def wordcount():
    with open("test.txt", "r") as f:
        data = f.read()
        words = data.split()
        return len(words)



print(wordcount())


# Write a function in Python to read lines from a text file "test.txt".
# Your function should find and display the number of occurrence of the word "the".


def occurrence():
    c = 0
    with open("test.txt", "r") as f:
        data = f.read()
        words = data.split()
        for line in words:
            if line == 'the' or line == 'The':
                c += 1
    return c


print(occurrance())



#  Write a Python program to read first n lines of a file


def read(n):
    filename = 'test.txt'
    with open(filename, "r") as f:
        data = f.read()
    lines = data.split("\n")


    f.close()
    return print(lines[n:])


def adread(n):
    from itertools import islice
    filename = 'test.txt'
    with open(filename, "r") as f:
        for line in islice(f, n):
            print(line)


adread(2)



# Write a Python program to read last n lines of a file

def adread(n):
    from itertools import islice
    filename = 'test.txt'
    with open(filename, "r") as f:
        data = f.readlines()
    res = data[ -n: ]
    for line in res:
        print(line)
adread(2)


# Write a python program to find the longest words.

def longword():
    filename = 'test.txt'
    with open(filename, "r") as f:
        data = f.read().split()
    c = len(max(data, key=len))

    return [word for word in data if len(word) == c]

print(longword())



#Write a Python program to count the number of lines in a text file.

def num():
    filename = 'test.txt'
    with open(filename, "r") as f:
        data = f.readlines()
    return print(len(data))

num()


# Write a Python program to get the file size of a plain file.


def file_size(fname):
    import os
    size = os.stat(fname).st_size
    return size


print("File size in bytes of a plain file: ", file_size("test.txt"))



# Write a Python program to copy the contents of a file to another file .

from shutil import copyfile
copyfile('test.txt', 'test2.txt')



filename = "test.txt"
with open(filename, "r") as f:
    data = f.read().splitlines()
print(data)



# Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
import string, os
if not os.path.exists("letters"):
   os.makedirs("letters")
for letter in string.ascii_uppercase:
   with open(letter + ".txt", "w") as f:
       f.writelines(letter)


#Python program to get Current Time

from datetime import *
import pytz

india_tz = pytz.timezone('Asia/Kolkata')
datetime_india = datetime.now(india_tz)
print("INDIA time:", datetime_INDIA.strftime("%H:%M:%S"))



from datetime import datetime

now_method = datetime.now()
currentTime = now_method.strftime("%H:%M:%S")
print("Current Time =", currentTime)


import time
Time = time.localtime()

currentTime = time.strftime("%H:%M:%S", Time)
print(currentTime)



# flashcards  https://www.geeksforgeeks.org/python-program-to-build-flashcard-using-class-in-python/

class flashcard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning

    def __str__(self):
        return self.word + self.meaning

flash = []
print("welcome to flashcard application")

while(True):
    word = input("enter name")
    meaning = input("enter meaning")
    flash.append(flashcard(word, meaning))
    n = int(input("enter 0 to continue"))
    if n:
        break
print("\nyour flashcards")
for i in flash:
     print(">", i)



# https://www.geeksforgeeks.org/student-management-system-in-python/

class student:
    def __init__(self, name, rollno, marks1, marks2):
        self.name = name
        self.rollno = rollno
        self.marks1 = marks1
        self.marks2 = marks2

    def accept(self, name, rollno, marks1, marks2):

        std = student(name, rollno, marks1, marks2)
        l.append(std)


    def display(self):
        for i in l:
            print("Name:" , i.name)
            print("rollno:", i.rollno)
            print("marks1:", i.marks1)
            print("marks2:", i.marks2)

    def search(self, rollno):
        for i in l:
            if i.rollno == rollno:
                break
            else:
                print("student not found")
        #print('name : {}, rollno: {} marks1: {} marks2: {}'. format(i.name, i.rollno,  i.marks1 , i.marks2))
        return i

    def update(self, old_roll_num, new_roll_num):
        i = obj.search(old_roll_num)
        i.rollno = new_roll_num

    def delete(self, rollno):
        i = obj.search(rollno)
        l.remove(i)








l = []
obj = student('', 0, 0, 0)
#print("enter student details")
#name = input("enter name")
#rollno = input("enter rollno")
#marks1 = int(input("enter marks1"))
#marks2 = int(input("enter marks2"))
obj.accept("vijaya", 23, 100, 100)
#obj.display()
#obj.search(23)
#obj.update(23, 45)
#obj.display()
obj.delete(23)
obj.display()





def countSpecialElements(matrix):
    nRows = len(matrix)
    nCount = 0

    for row in matrix:
        for indexCol, element in enumerate(row):

            if element == min(row) or element == max(row):
                if row.count(element) > 1:
                    return -1
                nCount = nCount + 1

            else:
                listColumn = []

                for indexRow in range(0, nRows):
                    listColumn.append(matrix[indexRow][indexCol])


                if element == min(listColumn) or element == max(listColumn):
                    if listColumn.count(element) > 1:
                        return -1
                    nCount = nCount + 1

    return nCount


if __name__ == '__main__':
    nCount = countSpecialElements([[1, 3, 4], [5, 2, 9], [8, 7, 6]])
    print(nCount)



"""
















