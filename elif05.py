vazn = float(input("Vazningizni kiriting (kg): "))
boy = float(input("Bo'yingizni kiriting (m): "))

if vazn <= 0 or vazn > 500 or boy <= 0 or boy < 0.5 or boy > 3.0:
    print("Noto'g'ri ma'lumot. Vazn 1-500 kg, bo'y 0.5-3.0 m oralig'ida bo'lishi kerak.")
else:
    bmi = vazn / (boy ** 2)
    print(f"BMI: {round(bmi, 2)}")

    if bmi < 18.5:
        print("Kam vazn")
    elif bmi < 25:
        print("Normal vazn")
    elif bmi < 30:
        print("Ortiqcha vazn")
    else:
        print("Semizlik")

