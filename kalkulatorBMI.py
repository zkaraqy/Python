def kalkulatorBMI():
    jenisKelamin = input("Jenis Kelamin [Pria/Wanita] :\n=> ")
    jenisKelamin = jenisKelamin.capitalize()
    if jenisKelamin == "Pria" or jenisKelamin == "Wanita":
        None
    else:
        print("Mohon masukkan jenis kelamin yang benar sesuai pilihan")
        kalkulatorBMI()

    usia = int(input("Usia :\n=> "))
    if usia < 18:
        result = print("Kalkulator hanya untuk 18 tahun ke atas")
        return result and None
    
    beratBadan = float(input("Berat Badan (kg) :\n=> "))
    tinggiBadan = int(input("Tinggi Badan (cm) :\n=> "))

    meter = tinggiBadan/100
    calcBMI = beratBadan/meter**2
    if calcBMI < 18.5:
        result = print(
            f"Hasil BMI < 18.5\n=> {calcBMI}\nBerat Badan Kurang\nAnda kekurangan berat badan"
        )
        return result
    elif 18.5 <= calcBMI < 22.9:
        result = print(
            f"Hasil BMI diantara 18.5 dan 22.9\n=> {calcBMI}\nNormal\nAnda memiliki berat badan ideal.\nGood job!!"
        )
        return result
    else:
        result = print(
            f"Hasil BMI lebih dari 25\n=> {calcBMI}\nObesitas\nAnda berada dalam kategori obesitas"
        )
        return result
    
repeat = True 
while repeat:
    kalkulatorBMI()
    repeat = input("Ulang? [Ya/Tidak]\n=> ")
    if repeat == "Ya" or repeat == "ya":
        repeat = True
    elif repeat == "Tidak" or repeat == "tidak":
        repeat = False
    else:
        print("Input Invalid!")
        repeat = False