def getCelcius():
    try:
        inputCelcius = input("Derajat Celcius: ")     
        celcius = int(inputCelcius)
        return celcius
    except ValueError:
        print("Invalid input! Mohon masukkan derajat Celcius yang benar")
        return getCelcius()

def getFahrenheit():
    try:
        inputFahrenheit = input("Derajat Fahrenheit: ")
        fahrenheit = int(inputFahrenheit)
        return fahrenheit
    except ValueError:
        print("Invalid input! Mohon masukkan derajat Fahrenheit yang benar")
        return getFahrenheit()

def getKelvin():
    try:
        inputKelvin = input("Derajat Kelvin: ")
        kelvin = int(inputKelvin)
        return kelvin
    except ValueError:
        print("Invalid input! Mohon masukkan derajat Kelvin yang benar")
        return getKelvin()

def getReamur():
    try:
        inputReamur = input("Derajat Reamur: ")
        reamur = int(inputReamur)
        return reamur
    except ValueError:
        print("Invalid input! Mohon masukkan derajat Reamur yang benar")
        return getReamur()
    
def konversiSuhu():
    print("Program Konversi Suhu")
    print("="*25)
    print("1. Celcius ke Fahrenheit\n2. Celcius ke Reamur\n3. Celcius ke Kelvin")
    print("4. Fahrenheit ke Celcius\n5. Fahrenheit ke Reamur\n6. Fahrenheit ke Kelvin")
    print("7. Reamur ke Celcius\n8. Reamur ke Fahrenheit\n9. Reamur ke Kelvin")
    print("10. Kelvin ke Celcius\n11. Kelvin ke Fahrenheit\n12. Kelvin ke Reamur")
    print("13. Keluar")
    print("="*25)
    pilihan = input("Pilih konversi sesuai dengan nomor opsi:\n=> ")
    if pilihan == "1":
        C = getCelcius()
        F = (9/5)*C+32
        return print(f"Hasil = {F}°F")
    elif pilihan == "2":
        C = getCelcius()
        R = (4/5)*C
        return print(f"Hasil = {R}°R") 
    elif pilihan == "3":
        C = getCelcius()
        K = C+273
        return print(f"Hasil = {K} K") 
    elif pilihan == "4":
        F = getFahrenheit()
        C = 5/9*(F-32)
        return print(f"Hasil = {C}°C") 
    elif pilihan == "5":
        F = getFahrenheit()
        R = 4/9*(F-32)
        return print(f"Hasil = {R}°R")
    elif pilihan == "6":
        F = getFahrenheit()
        K = 5/9*(F-32)+273
        return print(f"Hasil = {K} K")
    elif pilihan == "7":
        R = getReamur()
        C = (5/4)*R
        return print(f"Hasil = {C}°C") 
    elif pilihan == "8":
        R = getReamur()
        F = (9/4)*R+32
        return print(f"Hasil = {F}°F")
    elif pilihan == "9":
        R = getReamur()
        K = (5/4)*R+273
        return print(f"Hasil = {K} K") 
    elif pilihan == "10":
        K = getKelvin()
        C = K -273
        return print(f"Hasil = {C}°C")
    elif pilihan == "11":
        K = getKelvin()
        F = 9/5*(K-273)+32
        return print(f"Hasil = {F}°F")
    elif pilihan == "12":
        K = getKelvin()
        R = 4/5*(K-273)
        return print(f"Hasil = {R}°R")
    elif pilihan == "13":
        repeat = False
        return repeat
    else:
        print("Input Invalid! Coba lagi")
        return konversiSuhu()

repeat = True
while repeat:
    konversiSuhu()
    print("="*25)
    repeat = input("Ulang? [Ya/Tidak]\n=> ")
    if repeat == "Ya" or repeat == "ya":
        repeat = True
    elif repeat == "Tidak" or repeat == "tidak":
        repeat = False
    else:
        print("Input Invalid!")
        repeat = False