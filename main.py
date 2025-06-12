word = input("Enter a word: ")

vowels = "aeiouAEIOU"

vowel_count = 0

for char in word:
    if char in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)
