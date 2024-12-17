questions = [
  ["Which language was used to create Facebook?", "Python", "French", "JavaScript", "Php", "None", 4],
  ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Lisbon", "None", 3],
  ["What is the largest planet in our solar system?", "Earth", "Jupiter", "Mars", "Venus", "None", 2],
  ["What is the chemical symbol for water?", "H2O", "O2", "CO2", "N2", "None", 1],
  ["Who wrote 'To Kill a Mockingbird'?", "Harper Lee", "Mark Twain", "Jane Austen", "J.K. Rowling", "None", 1],
  ["Which element has the atomic number 1?", "Helium", "Hydrogen", "Oxygen", "Carbon", "None", 2],
  ["What is the currency of Japan?", "Dollar", "Euro", "Yen", "Won", "None", 3],
  ["Who painted the Mona Lisa?", "Vincent van Gogh", "Claude Monet", "Pablo Picasso", "Leonardo da Vinci", "None", 4],
  ["What is the hardest natural substance on Earth?", "Gold", "Iron", "Diamond", "Silver", "None", 3],
  ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Saturn", "None", 2],
  ["What is the square root of 64?", "6", "7", "8", "9", "None", 3],
  ["Which country is known as the Land of the Rising Sun?", "China", "Japan", "Thailand", "India", "None", 2],
  ["Who is known as the Father of Computers?", "Albert Einstein", "Charles Babbage", "Isaac Newton", "Nikola Tesla", "None", 2],
  ["What is the largest ocean on Earth?", "Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean", "None", 4],
  ["Who discovered penicillin?", "Marie Curie", "Alexander Fleming", "Louis Pasteur", "Gregor Mendel", "None", 2]
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,10000000]
money = 0

for i in range(0,len(questions)):
  question = questions[i]
  # print(question)
  print(f"Question for Rs. {levels[i]}")
  print(f"\n{question[0]}")
  print(f"1.{question[1]}        2.{question[2]}")
  print(f"3.{question[3]}        4.{question[4]}")
  reply = int(input("\nChoose between (1-4) or enter 0 to quit: \n"))
  if reply == 0:
    if i == 0:
      money = 0
    else:
      money = levels[i-1]
    break
  if reply == (question[-1]):
    print(f"Correct answer you won rs {levels[i]}\n")
    if i == 4:
      money = 10000
    elif i == 9:
      money == 320000
    elif i == 15:
      money = 10000000
  else:
      print(f"Incorrect answer you lost rs {levels[i]}")

print(f"You take home money rs {money}")