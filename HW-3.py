name1 = input("Please tell me first player: ")
name2 = input("Please tell me second player: ")

print(f"Wecome to the our Hangman Game {name1} and {name2}")

word = input(f"{name1}, please enter the word you want to play with {name2}:")


print(f"{name2}, you have the right to enter 4 letters. Can you enter 4 letters")

p1 = input("Letter 1: ")
p2 = input("Letter 2: ")
p3 = input("Letter 3: ")
p4 = input("Letter 4: ")

i = 0
j = len(word)

while i<j:
    if (word[i] == p1):
        if (word[i] == p2):
           if (word[i] == p3):
               if (word[i] == p4):
                     print(f"{i + 1}. letter is:", word[i])
                     i = i+1
           print(f"{i + 1}. letter is:", word[i])
        print(f"{i + 1}. letter is:", word[i])
    print(f"{i + 1}. letter is:", word[i])

    if (word[i] == p2):
      if (word[i] == p3):
        if (word[i] == p4):
            print(f"{i + 1}. letter is:", word[i])
            i = i + 1
      print(f"{i + 1}. letter is:", word[i])
    print(f"{i + 1}. letter is:", word[i])

    if (word[i] == p3):
      if (word[i] == p4):
        print(f"{i + 1}. letter is:", word[i])
        i = i + 1
print(f"{i + 1}. letter is:", word[i])

if (word[i] == p4):
    print(f"{i + 1}. letter is:", word[i])
    i = i + 1

k = 0;
while k <= 2:
    guess = input("Enter your guess:")
    if (guess == word):
        print(f"Congratulations {name2}, you won this game")
        k = k+1
while k == 3:
    print(f"Sorry {name2}, you lost this game")