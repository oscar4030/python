import random
counters = [0, 0, 0, 0, 0, 0]
for i in range(1000):
    value = random.randint(0, 5)
    counters[value] = counters[value] + 1
print("주사위가 1인 경우는 %s" %counters[0])
print("주사위가 2인 경우는 %s" %counters[1])
print("주사위가 3인 경우는 %s" %counters[2])
print("주사위가 4인 경우는 %s" %counters[3])
print("주사위가 5인 경우는 %s" %counters[4])
print("주사위가 6인 경우는 %s" %counters[5])
