marks = float(input("enter marks (0-100): "))
if 0 <= marks <= 100:
   if marks >= 33:
    print("pass")
   else:
    print("fail")
else:
    print("invalid marks entered. please enter marks between 0 and 100.")
            