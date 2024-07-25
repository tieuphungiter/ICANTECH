"""
Đề bài: Python program to filter prime numbers
Link: https://www.w3resource.com/python-exercises/filter/python-filter-exercise-7.php
"""
NguyenTo = []
for i in range(101):
  NguyenTo.append(True)
  
def Sang():
  NguyenTo[0] = False
  NguyenTo[1] = False
  for i in range(2, 101):
    if NguyenTo[i]:
      for j in range(i*i, 101, i):
        NguyenTo[j] = False
Sang()

def isPrime(n):
  return NguyenTo[n]

Ar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print(Ar)
Ar2 = list(filter(isPrime, Ar))
print(Ar2)
