import array as arr

stud_list = arr.array('i', [])

n = int(input("Enter number of students: "))
print("Enter Roll no. of students who attend training program in random order: ")

for i in range (0, n):
  ele = int(input())
  stud_list.append(ele)

def lin_search(key, a):
  global n
  for i in range (0, n):
    if (a[i] == key):
      print("Student is in the training program.")
  else:
    print("Student is not in the training program.")

def sen_search(key, a):
  global n
  last = a[n - 1]
  a[n - 1] = key
  i = 0
  while (a[i] != key):
    i += 1
  a[n - 1] = last
  
  if (i < n-1 or a[n - 1] == key):
    print("Student is in the training program.")
  else:
    print("Student is not in the training program.")

def fib_search(key, a):
  tmp = sorted(a)
  fib = arr.array('i', [])
  global n
  fib.append(0)
  fib.append(1)

  for i in range (2,n+1):
    fib.append(fib[i-2] + fib[i-1])
  

  offset = -1
  k = n

  while (i in (0,n)):
    i = min(offset + fib[k-2], n+1)

    if tmp[i] == key:
      print("Student is in the training program.")
      break
    elif key > tmp[i]:
      offset = i
      k = k-1
    elif key < tmp[i]:
      k = k-2
  else:
    print("Student is not in the training program.")

def bin_search(key, a):
  temp = sorted(a)
  min = 0
  max = len(a) - 1
  mid = 0
  while (min <= max):
    mid = (min + max) // 2
    if (temp[mid] < key):
      min = mid + 1
    elif (temp[mid] > key):
      max = mid - 1
    else:
      print("Student is in the training program.")
      break
  else:
    print("Student is not in the training program.")

key = int(input("Enter Roll no. of student to search for: "))
print("Linear Search: ")
lin_search(key, stud_list)
print("Sentinel Search: ")
sen_search(key, stud_list)
print("Binary Search: ")
bin_search(key, stud_list)
print("Fibonacci Search: ")
fib_search(key, stud_list)
