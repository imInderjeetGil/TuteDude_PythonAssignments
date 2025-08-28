data_1=input("Enter text to write to the file: ")
file=open("output.txt","r+")
file.write(data_1)

data_2=input("Enter additional text to append: ")
file.write("\n"+data_2)
file.seek(0)
print("Data successfully appended.\nFinal content of the output.txt:\n")
print(file.read())

