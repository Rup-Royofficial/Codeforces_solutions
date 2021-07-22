def isInAlphabeticalOrder(word):
    for i in range(len(word) - 1):
        if word[i] > word[i + 1]:
            return "NO"
    return "YES"

for j in range(int(input())):
    count = int(input())
    word = input()
    pin_words = isInAlphabeticalOrder(word)
    print(pin_words)
