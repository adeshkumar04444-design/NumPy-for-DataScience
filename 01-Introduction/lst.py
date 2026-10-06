# Why NumPy array is better than python list. and what's the need.

# Problem: Suppose a scientist wanted to find out the average temperature of millions of cities around the world.

# A Python list is a traditional method that consumes more memory and time to handle large amounts of data.

tempreatures = [32.5, 31.8, 33.0, 35.2, 36.6]

total = 0
for temp in tempreatures:
    total += temp

average = total/len(tempreatures)
print(average)
