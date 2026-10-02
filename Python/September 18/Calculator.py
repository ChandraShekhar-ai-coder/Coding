af = float(input("What's Your first No. "))
aa = int(input("What do You want\n1. Sum\n2. Subtract\n3. Multiply\n4. Division\n5. Exponent\n6. Square root\n7. Cube Root\n\nEnter choice (1-7): "))
if aa == 6:
 print("First No. Square Root",af**(1/2))
if aa==7:
 print("First No. Cube Root",af**(1/3))

else:
 ag= float(input("What is Your Second No. "))
  # Combined into one single string with correct \n formatting

 if aa == 1:
  print(af+ag)
 if aa == 2:
  print(af-ag)
 if aa == 3:
  print(af*ag)
 if aa == 4:
  print(af/ag)
 if aa == 5:
  print(af**ag)

 else:
  print("404 Pleas e Smile")
