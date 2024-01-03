mark = float(input("Enter your obtained marks: "))

if (mark>100 or mark<0):
  print("Invalid Input")
elif mark>=80:
  print("A+")
elif mark>=70:
  print("A")
elif mark>=60:
  print("A-")
elif mark>=50:
  print("B")
elif mark>=40:
  print("C")
elif mark>=33:
  print("D")
else:
  print("Fail")
