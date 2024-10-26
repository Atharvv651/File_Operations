with open("file.txt", "r") as file:
    print(f"READ MODE \n {file.read()}")
file.close()

print("\n \n")
with open("file.txt", "a") as file:
    print("APPEND MODE")

    with open("file.txt", "r") as file1:
        print(f"Original: {file1.read()}")
    file1.close()

    file.write("This is a new line")
file.close()

print("\n")
with open("file.txt", "r") as file:
    print(f"New: {file.read()}")
file.close()

print("\n \n")
with open("file.txt", "w") as file:
    print("WRITE MODE")

    with open("file.txt", "r") as file1:
        print(f"Original: {file1.read()}")
    file1.close()

    file.write("This is a new line")
file.close()

print("\n")
with open("file.txt", "r") as file:
    print(f"New: {file.read()}")
file.close()
