letter = input("Enter a letter: ")
vowel = ["a", "e", "i", "o", "u"]

if letter.lower() in vowel:
    print("Vowel")
elif letter.lower() not in vowel:
  print("Consonant")
