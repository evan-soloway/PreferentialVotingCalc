from Program import Program

perameter = input("Perameters: ")
print()

try:
     program = Program(perameter)
     program.main()
     
except Exception as error:
     print(error)


