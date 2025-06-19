soat = int(input("Soatni kiriting (0-23): "))

if soat < 0 or soat > 23:
    print("Soat 0-23 oralig'ida bo'lishi kerak!")
elif soat >= 5 and soat <= 11:
    print("Ertalab")
elif soat >= 12 and soat <= 17:
    print("Kunduzi")
elif soat >= 18 and soat <= 21:
    print("Kechqurun")
else:
    print("Tun")

