flag=True
from art import logo
print(logo)
while(flag):
    enc_dec = int(input("Enter 1 to encode\nEnter 2 to decode\nEnter any number to exit to exit\nEnter Choice"))
    if enc_dec == 1:
        print("You have chose to ENCODE")
        msg = input("Enter message to encode")
        shift = int(input("Enter by how many char you want to shift"))
        temp_list = []
        for i in range(len(msg)):
            act_val = ord(msg[i])
            temp_list.append(str(act_val+shift))
        enc_str = ""
        for j in temp_list:
            enc = chr(int(j))
            enc_str+=enc
        print(f"ENCODED MESSAGE IS\n{enc_str}")

    elif enc_dec == 2:
        print("You have chose to DECODE")
        msg = input("Enter message to decode")
        shift = int(input("Enter by how many char you want to shift"))
        temp_list = []
        for i in range(len(msg)):
            act_val = ord(msg[i])
            temp_list.append(str(act_val - shift))

        dec_str = ""
        for j in temp_list:
            enc = chr(int(j))
            dec_str += enc
        print(f"DECODED MESSAGE IS\n{dec_str}")

    else:
        flag = False
        print("Thanks for trying caesar's cipher")