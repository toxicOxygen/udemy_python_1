import random

colors = ['red','orange','yellow','green','blue','white','violet','indigo','pink','black']

n = random.randint(0,99) % 10
print("i am thinking of a color")
print('it could any of these colors',colors)

while True:

  user = input("What color is it ? : ")

  if user.lower() == colors[n].lower():
    print("you're right")
    cont = input("do u wanna play again, y/N\t")

    if cont.lower()[0] == 'y':
      n = random.randint(0,99) % 10
      print("i am thinking of a color")
      print('it could any of these colors',colors)
      continue
    else:
      break
  else:
    print("wrong answer try again")