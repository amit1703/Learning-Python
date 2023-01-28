def blackjack(a,b,c):
    # טענת כניסה: מקבלת 3 מספרים שמהווים 3 קלפים במשחק בלאקגק
    # טענת יציאה: מחזירה את הסכום שלהם או את המילה bust אם עבר 21
     if sum([a,b,c]) <= 21:
         return sum(a,b,c)
     elif sum(a,b,c) <= 31 and 11 in [a,b,c]:
         return sum([a,b,c]) -10
     else:
         return "Bust"