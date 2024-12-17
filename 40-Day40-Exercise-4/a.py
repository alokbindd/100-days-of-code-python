import random
import string

def generate_random_chars(length=3):
    return ''.join(random.choices(string.ascii_letters, k=length))

def encode(word):
    if len(word) < 3:
        return word[::-1]
    else:
        first_letter = word[0]
        new_word = word[1:] + first_letter
        random_prefix = generate_random_chars()
        random_suffix = generate_random_chars()
        return random_prefix + new_word + random_suffix

def decode(word):
    if len(word) < 3:
        return word[::-1]
    else:
        core_word = word[3:-3]
        last_letter = core_word[-1]
        original_word = last_letter + core_word[:-1]
        return original_word

def main():
    choice = input("Choose option 1 to encode and 2 to decode: ")
    
    if choice == '1':
        text_to_encode = input("Enter text to encode: ")
        encoded_text = encode(text_to_encode)
        print(f"Encoded text: {encoded_text}")
    elif choice == '2':
        text_to_decode = input("Enter text to decode: ")
        decoded_text = decode(text_to_decode)
        print(f"Decoded text: {decoded_text}")
    else:
        print("Invalid input")

if __name__ == "__main__":
    main()
