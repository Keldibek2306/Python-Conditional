asosiy_narx = 100
yosh = int(input("Yoshingizni kiriting: "))
chegirma = 0

if yosh < 7:
    chegirma = 50
if yosh >= 7 and yosh <= 17:
    chegirma = 20
if yosh > 60:
    chegirma = 30

yakuniy_narx = asosiy_narx - (asosiy_narx * chegirma / 100)
print(f"Yakuniy chipta narxi: {yakuniy_narx} so'm")

