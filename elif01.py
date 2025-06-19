ball = int(input("Ball kiriting (0-100): "))

if ball < 0 or ball > 100:
    print("Ball 0-100 oralig'ida bo'lishi kerak!")
elif ball >= 90:
    print("A (A'lo)")
elif ball >= 80:
    print("B (Yaxshi)")
elif ball >= 70:
    print("C (Qoniqarli)")
elif ball >= 60:
    print("D (Qoniqarsiz)")
else:
    print("F (Rad)")

