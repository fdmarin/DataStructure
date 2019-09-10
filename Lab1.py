# Federico Marin (ID: 88736754)
# Lab 1 option B
# 9/9/2019


import hashlib


def hash_with_sha256(str):
    hash_object = hashlib.sha256(str.encode('utf-8'))
    hex_dig = hash_object.hexdigest()
    return hex_dig


# check method allows the file to be read and to retrieve all information from text file necessary to make program
# compile. also stores information read from text file into variables for further manipulation.
def check(s):
    # try/catch was not necessary as file was hard coded in but inserted just to practice
    try:
        file = open("password_file.txt", "r")
        read = file.readlines()

    except:
        print("file read error")

    for line in read:
        arr = line.split(",")
        user = arr[0]
        salt_value = arr[1]
        hashedpassfromarr = arr[2].replace('\n', '')
        newhash = concatinate(s, salt_value)  # we store the concatinated password in newhash
        newhash = hash_with_sha256(newhash)  # newhash is updated by calling the hash method on the concatinated password

        # if statement just checks if the hashed password we created is the same as the one in the txt file.
        if newhash == hashedpassfromarr:
            print(user + " password is: " + s)
        file.close()


def concatinate(s, salt):  # this method allows the generated password (EX: 000) to be added with the salt value
    return s + salt


# method where passwords are generated for all instances.
def password_generator(s, n):
    # if checks if length of the generated password is at the correct and desired length (n). if so calls method check
    if len(s) == n:
        check(s)
        return
    # for allows the passwords to generate using numbers 0 - 9. i will increase with every iteration. recursive call
    for i in range(10):
        password_generator(s + str(i), n)

# for loop in main allows the length of the password to be set without hard coding it in, range method allows #'s 3-7
# to be used
def main():
    for n in range(3, 8):
        password_generator("", n)
    hex_dig = hash_with_sha256('This is how you hash a string with sha256')
    print(hex_dig)


main()
