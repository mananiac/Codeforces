num = int(input())
for _ in range(num):
    string=""
    word = input()
    if len(word) < 11:
        print(word)
    else:
        string = word[0] + str((len(word)-2)) + word[len(word)-1]
        print(string)