import statistics

data = [1,2,3,4,5,6,7,8,9,10]

mean = statistics.mean(data)
variance = statistics.variance(data)
stdev = statistics.stdev(data)


print(f"mean : {mean}")
print(f"variance : {variance}")
print(f"standard deviation: {stdev}")
