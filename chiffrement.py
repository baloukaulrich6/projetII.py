# chriffrement de cesar Encryption
alphabet = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
'u', 'v', 'w', 'x', 'y', 'z']



def cesar(start_test, shift_amount, cipher_direction):
    end_text = ""
# TODO-2: what if the user enters a shift that is greater than the number of letters in the alphabel.?
    if shift >= 26 :
       shift_amount = shift % 26

    if cipher_direction == "decode":
        shift_amount *= -1

    for char in start_test:
# TODO-3: what happens if the user enter a number/symbol/space.?
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char

    print(f"le text {cipher_direction}d est {end_text}")

# TODO 4 : can you figure out a way to ask the user if they want to restart the cipher program?
shoul_continu = True
while shoul_continu:
    direction = input("type 'encode' to encrypt, type 'decode' to decrypt\n")
    text = input("entre de message:\n").lower()
    shift = int(input("nombre de deplacement:\n"))

    cesar(start_test= text,shift_amount= shift, cipher_direction=direction)
    result = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if result =='no':
        shoul_continu = False
        print("GOOD BYE!")













# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#       position = alphabet.index(letter)
#       new_position = position + shift_amount
#       new_letter = alphabet[new_position]
#       cipher_text += new_letter
#   print(f"le texte encode est {cipher_text}")
#
#
# def decrypt(ciphe_text, shift_amount):
#     new_plain_text = ""
#     for letter in ciphe_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         new_letter = alphabet[new_position]
#         new_plain_text += new_letter
#     print(f"le texte decode est {new_plain_text}")



# if direction == "encode":
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#     decrypt(ciphe_text=text, shift_amount=shift)