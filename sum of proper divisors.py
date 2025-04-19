# 19/04/2025 sum of proper divisors under n
# I wrote this for Project Euler problems 21 and 23

def find_sum_of_proper_divisors(n):
  divisors_sum = 1 # all numbers shared the common divisor 1
  bound = int(n ** 0.5) # only have to check up to sqrt(n)

  for j in range(2, bound + 1):
      if i % j == 0:
          divisors_sum += j  # Add divisor j
          if j != i // j: # find the compliment divisor, make sure it is not a perfect square
              divisors_sum += i // j

n=100 # enter the number here
print(find_sum_of_proper_divisors(n))
