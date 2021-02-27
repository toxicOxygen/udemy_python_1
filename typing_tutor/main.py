import time
import matplotlib.pyplot as plt
import random

words = [
  'elephant',
  'terminator',
  'government',
  'parliament',
  'mathematics',
  'scenario',
]

n = random.randint(0,60) // 10
count = 0
mistakes = []
timeTaken = []

while count <= 5:
  count += 1
  start = time.time()
  print(f'type the word "{words[n]}"')
  word = input(">> : ")
  end = time.time()
  timeTaken.append(round(end -  start, 4))
  word = word.strip()

  msCount = 0
  for c in range(len(word.lower())):
    if word[c] != words[n][c]:
      msCount += 1
  mistakes.append(msCount)

print(mistakes)
print(timeTaken)

