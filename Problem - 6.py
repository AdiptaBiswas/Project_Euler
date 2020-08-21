import time

# Square of Sum
def sq_o_sm(n):
  start = time.time()
  sum_10 = 55
  for i in range(1,n//10):
    new_sum = int(str(i)+"00")+55
    sum_10+=new_sum
  square_of_sum = sum_10**2
  return square_of_sum,start
square_of_sum,time_tkn = sq_o_sm(100)
print("Time taken: {} milliseconds".format((time.time()-time_tkn)*1000))
print(square_of_sum)

# Sum of Square
def sm_o_sq(n):
  start = time.time()
  sum_Sq = 385
  for j in range(11,n+1):
    sum_Sq+=j**2
  return sum_Sq,start
Sum_of_square, time_taken = sm_o_sq(100)
print("Time taken: {} milliseconds".format((time.time()-time_taken)*1000))
print(Sum_of_square)

# Difference
print(square_of_sum - Sum_of_square)

# 25164150



