import random 
name = "Aaradhya"
question = "Am i the best ??"
answer = ""

random_number = random.randint(1,12)
print(random_number)

if random_number == 1:
  answer = "Yes - definitely "
elif random_number == 2:
  answer = "it is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy,try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you know"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very Doubtful"
elif random_number == 10:
  answer = "Why not?"
elif random_number == 11:
  answer = "come on man you are"
elif random_number == 12:
  answer = "shut up You are the BESTTTT"
elif name == "":
  print (question)
elif question == "":
  print ("Come on dont be shy ask your question here!")
else:
  answer = "ERROR 404"

print(name +" asks:" + question)  

print("Magic 8-Ball's answer:" + answer)


