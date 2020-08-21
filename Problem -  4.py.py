import time

ls = []
start = time.time()
for i in range(900,1000):
  for j in range(900,1000):
    num = str(i*j)
    if len(num)>5:
      if str(i*j)[::-1] == str(i*j)[0:len(num)]:
        ls.append(int(str(i*j)))
print(max(ls))

# 906609

end = time.time()
print("It took {} milliseconds to execute.".format((end-start)*1000))

# 46.08 milliseconds






  

