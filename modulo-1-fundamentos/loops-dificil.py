numbers = [1,2,3,4,5,6,7,8,9,10]
results = []
results2 = []
for n in numbers :
    results.append(2*n)
print(results)
results2 = [n*2 for n in numbers]
print(results2)
evens = [n for n in numbers if n%2==0]
print(evens)