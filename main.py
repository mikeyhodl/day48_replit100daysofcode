# f = open("file1.txt", "a+")
# whatText = input("> ")
# f.write(f"{whatText}\n")
# f.close()

# f = open("saved.txt", "a+")
# whatText = input("> ")
# f.write(f"{whatText}\n")
# whatText = input("> ")
# f.write(f"{whatText}\n")
# f.close()


# f = open("savedFoal.txt", "a+")
# whatText = input("> ")
# f.write(f"{whatText}\n")
# whatText = input("> ")
# f.write(f"{whatText}\n")
# f.close()


import os, time

while True:
  print("                 HIGH SCORE TABLE")
  print()
  name = input("INITIALS > ").upper()
  score = input("SCORE > ")
  print()

  f = open("high.score", "a+")
  f.write(f"{name} {score}\n")
  f.close()

  print("ADDED")
  time.sleep(1)
  os.system("clear")