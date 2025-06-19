email = input("Email manzilini kiriting: ")

tugash_yaxshi = email.endswith(".com") or email.endswith(".uz") or email.endswith(".net") or email.endswith(".org")

if "@" in email and tugash_yaxshi:
    print("Email qabul qilindi.")
else:
    print("Email noto'g'ri formatda.")

