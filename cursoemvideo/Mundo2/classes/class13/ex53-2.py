#palindromo detector
is_palindrome = True

word = input("Informe uma palavra: ")
letter_position = len(word) - 1

# cleaning the spaces of the sentence
word = word.upper().strip().replace(" ", "")
print("new word: ",word)

inverse_word = []

for letter in word:
    inverse_word.append(word[letter_position])
    letter_position -= 1

letter_position = 0

for letter in word:
    if not word[letter_position] == inverse_word[letter_position]:
        is_palindrome = False
        break

print(inverse_word)

answer = "A palvra é um palíndromo." if is_palindrome else "A palavra não é um palíndromo."
print(answer)