
balans = 5000
summa = input("Yechmoqchi bo'lgan summani kiriting: ")

if summa.isdigit():
    summa = int(summa)
    if summa < 0:
        print("Manfiy summa kiritib bo'lmaydi.")
    if summa >= 0 and summa <= balans:
        print(f"Pul yechildi. Qolgan balans: {balans - summa} so'm")
    if summa > balans:
        print(f"Mablag' yetarli emas. Sizning balansingiz: {balans} so'm")
else:
    print("Faqat son kiriting.")
