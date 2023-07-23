import random

def getUserChoice():
    userChoice = input("Pilih salah satu diantara:\n[gunting, batu, kertas]\n=> ")
    print("="*35)
    userChoice = userChoice.lower()
    return userChoice

def getComputerChoice():
    choices = ["gunting", "batu", "kertas"]
    choiceIndex = random.randint(0,2)
    compChoice = choices[choiceIndex]
    return compChoice

def guntingBatuKertas():
    print("Permainan gunting, batu, kertas")
    print("="*35)
    computer = getComputerChoice() 
    player = getUserChoice()
    if player == computer:
        return print(f"anda SERI!\nanda : {player}\nkomputer : {computer}\n"+"="*35)
    elif player == "gunting" and computer == "kertas" or player == "batu" and computer == "gunting" or player == "kertas" and computer == "batu":
        return print(f"anda MENANG!\nanda : {player}\nkomputer : {computer}\n"+"="*35)
    else:
        return print(f"anda KALAH!\nanda : {player}\nkomputer : {computer}\n"+"="*35)
    
repeat = True
while repeat:
    guntingBatuKertas()
    repeat = input("Mau bermain lagi? [Ya/Tidak]\n=> ")
    if repeat == "Ya" or repeat == "ya":
        repeat = True
    elif repeat == "Tidak" or repeat == "tidak":
        print("Terimakasih telah bermain")
        repeat = False
    else:
        print("Input Invalid!")
        repeat = False