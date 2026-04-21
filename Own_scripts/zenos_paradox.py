from datetime import datetime as dt

start = dt.now()

print("Beginning with Zenos Paradox")

iterator = 0
sum = 0
init = 1

while sum < 1:
    halve = init/2
    sum += halve
    init = halve
    iterator += 1
    print(iterator,"=>",sum)

end = dt.now()

print(f"Program strated at {start} and ended at {end} total duration: {end-start}")