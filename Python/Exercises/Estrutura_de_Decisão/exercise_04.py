'''
4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

vowels = "AEIOU"

print("Digite uma letra: ")
while True:
    char = input().upper()
    if char.isnumeric() or len(char) > 1 or char ==  " ":
        print("Digite apenas uma letra.")
        continue
    message = "Foi uma vogal" if char in vowels else "Foi uma consoante"
    print(message)