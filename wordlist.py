import random

words = []
counter = 0
answ = "s"
word = 0

while answ == "s":
    answ = str.lower(input("Você quer gerar uma wordlist? (S/N): "))
    if answ != "s":
        print("Você decidiu não fazer uma wordlist... o script parou!")
        break
    print("Para parar de entrar com palavras digite -0")
    while word != "-0":
        counter += 1
        word = input("Digite uma palavra: ")
        if word == "-0":
            print("Você escolheu parar de entrar palavras")
            break
        else:
            words.append(word)
    passwords = int(input("Quantas palavras personalizadas você quer?: "))
    dig = int(input("Quantos caracteres você quer?: "))
    wordlist = []
    list1 = []
    list2 = []
    list1 = words
    list2 = words
    words.sort
    list1.sort(reverse=True)
    list2.reverse
    for w in range(passwords):
        word = random.choice(words)+random.choice(list1)
        while len(word) < dig:
            word += random.choice(list2)
        wordlist.append(word)
    file = open("words.txt", "w")
    for i in wordlist:
        file.write(i)
        file.write("\n")
        file.close
