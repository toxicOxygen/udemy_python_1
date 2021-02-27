from urllib import request
import json
import random

def getQuestion():
  url = "https://opentdb.com/api.php?amount=1"
  data = request.urlopen(url).read().decode()
  jsonData = json.loads(data)
  return jsonData['results'][0]

def mixOptions(correct, incorrect):
  n = random.randint(0,len(incorrect))

  if n >= 3:
    incorrect.append(correct)
  else:
    incorrect.insert(n, correct)
  return n,incorrect

def formatQuestion(question):
  m = question.replace("&quot;",'"')
  return m

while True:
  obj = getQuestion()
  correct_answer = obj.get('correct_answer')
  incorrect_answers = obj.get('incorrect_answers')
  question = formatQuestion(obj.get('question'))

  ans, options = mixOptions(correct_answer,incorrect_answers)
  
  print(question)
  for i in range(len(options)):
    print(f'{chr(ord("A") + i)}) {options[i]}')
  
  userChoice = input("A or B or C or D >> ")
  userChoice = userChoice.upper()
  userAnswer = options[ord(userChoice) - ord("A")]
  
  if userAnswer == correct_answer:
    print("that's right")
  else:
    print(f"that's incorrect, right answer is {correct_answer}")
  
  print('\n press enter to continue or "quit" to end game')

  terminate = input(">> ").lower()
  if terminate == "quit":
    break

