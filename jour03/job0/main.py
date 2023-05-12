# Ask to user ton enter an string
input_str = input("Please enter an string : ")

# We write the string in the file "output.txt"
with open("output.txt", "w") as f:
    f.write(input_str)
    
print("output.txt")
