# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode
import string
import random

def encode(words):
    nwords = []
    for word in words:
        if (len(word)<=3):
            nwords.append(word[::-1])
        else:
            r1 = ''.join(random.choices(string.ascii_letters,k=3))
            r2 = ''.join(random.choices(string.ascii_letters,k=3))
            t = r1 + word[1:]+word[0] + r2
            nwords.append(t)
    return " ".join(nwords)

def decode(words):
    nwords = []
    for word in words:
        if (len(word)>3):
            b = word[3:-3]
            # print(b) 
            t = b[-1]+b[0:-1]
            nwords.append(t) 
        else:
            nwords.append(word[::-1])
    return " ".join(nwords)

def main():
    while True:
        msg = input("Enter the message:")
        choice = input("Choose 'e' for encoding and 'd' for decoding or q to quit:").lower()
        words = msg.split()

        if choice == 'e':
            encoded_msg = encode(words)
            print("Encoded message: ",encoded_msg)
        elif choice == 'd':
            decoded_msg = decode(words)
            print("Decoded message: ",decoded_msg)
        elif choice == 'q':
            print("Good bye")
            break
        else:
            print("Invalid choice. Please choose 'e' for encoding or 'd' for decoding.")

if __name__ == "__main__":
    main()


# print(words)

# a = input("choose option 1 to encode and 2 decode:")
# try:
#     if (int(a) == 1):
#         a = input("Enter text to encode:")
#         a.split()
#         encode(a)
#     else:
#         decode(input("Enter text to decode:"))
#         pass
# except ValueError as e:
#     print("Invalid input")