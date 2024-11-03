import socket
import numpy as np
import json
import time

testArray = []
testpathArray = []

# 첫 번째 반복문
for i in range(1, 200):
    for j in range(1, 200):
        testArray.append(0.01 * i)
        testArray.append(0.01 * j)
        testArray.append(0.0)
        

# 두 번째 반복문
for i in range(1, 200):
    for j in range(1, 100):
        testArray.append(0.01 * i)
        testArray.append(0.0)
        testArray.append(0.01 * j)

# 세 번째 반복문
for i in range(1, 100):
    for j in range(1, 200):
        testArray.append(0.0)
        testArray.append(0.01 * j)
        testArray.append(0.01 * i)

for i in range(1, 200):
    for j in range(1, 100):
        testArray.append(0.01 * i)
        testArray.append(2.0)
        testArray.append(0.01 * j)

for i in range(1, 100):
    for j in range(1, 200):
        testArray.append(2.0)
        testArray.append(0.01 * j)
        testArray.append(0.01 * i)

# 네 번째 반복문
for i in range(1, 21):
    testpathArray.append(0.5)
    testpathArray.append(0.5 + 0.025 * i)
    testpathArray.append(0.5)