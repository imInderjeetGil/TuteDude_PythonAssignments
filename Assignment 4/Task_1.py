try:
    file1=open("Sample.txt","r")
    reader=file1.read()
    print(reader)

except FileNotFoundError:
    print("The file 'sample.txt' was not found")
file1.close()