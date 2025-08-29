student_dict={"Aman":90,"Harsh":60,"Inder":80,"Devesh":0,"Gourav":10}
try:
    st_name=input("Enter the student's name: ")
    print(f"{st_name}'s marks:",student_dict[st_name])
except KeyError:
    print("Student not found")