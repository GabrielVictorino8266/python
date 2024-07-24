#palindromo detector
is_palindromo = True

word = input("Informe uma palavra: ")
letter_position = 0

# cleaning the spaces of the sentence
word = word.upper().strip().replace(" ", "")
print("new word: ",word)

inverse_word = word[::-1]

for letter in word:
    if not word[letter_position] == inverse_word[letter_position]:
        is_palindromo = False
        break

answer = "A palvra é um palíndromo." if is_palindromo else "A palavra não é um palíndromo."
print(answer)