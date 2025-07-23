print("Expert System for Career Path")
print("Select Subject As Follow")
print("Maths,Physics,Programing,Statistics,Chemistry,Circuits,Biology,AI Concept")
n=str(input("Enter Subject Name--->> "))
s=str(input("Enter Subject Name--->> "))
if(n=="Maths" and s=="Physics")or(n=="Physics" and s=="Maths"):
	print("Your Carrer Path---->>Mechanical Engineering")
elif(n=="Maths" and s=="Programing")or(n=="Programing" and s=="Maths"):
	print("Your Carrer Path---->>Computer Engineering")
elif(n=="Biology" and s=="Chemistry")or(n=="Chemistry" and s=="Biology"):
	print("Your Carrer Path---->>Biotechnology")
elif(n=="Maths" and s=="Circuits")or(n=="Circuits" and s=="Maths"):
	print("Your Carrer Path---->>Electronics Engineering")
elif(n=="Statistics" and s=="Programing")or(n=="Programing" and s=="Statistics"):
	print("Your Carrer Path---->>Artificial Intelligence & Data Science")
elif(n=="Ai Concept" and s=="Programing")or(n=="Programing" and s=="Ai Concept"):
	print("Your Carrer Path---->>Artificial Intelligence & Machine Learning")
else:
	print("Write The Subject Name From Above List")	
