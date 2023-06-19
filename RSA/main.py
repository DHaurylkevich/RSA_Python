from tkinter import *
from tkinter import messagebox
from cryptography import encrypt, decrypt, generate_key_pair
from key import *

def exit_program():
    window.destroy()

def new_keys():
    private_key,public_key = generate_key_pair()
    messagebox.showinfo("Private key", private_key)
    messagebox.showinfo("Public_key", public_key)

def encrypt_message():
    message = message_entry.get()
    encrypted_message = encrypt(message, public_key)
    with open('crypto.txt', "w") as file:
        file.write(encrypted_message)
    messagebox.showinfo("Wiadomość zaszyfrowana", encrypted_message)

def decrypt_message_on_file():
    with open('crypto.txt', "r") as file:
        encrypted_message = file.read()    
    decrypted_message = decrypt(encrypted_message, private_key)
    messagebox.showinfo("Wiadomość deszyfrowana", decrypted_message)

def decrypt_message():
    encrypted_message = message_entry.get()    
    decrypted_message = decrypt(encrypted_message, private_key)
    messagebox.showinfo("Wiadomość deszyfrowana", decrypted_message)

def read_private_key():
    private_key = read_to_file('private_key.pem')
    messagebox.showinfo("Private key", private_key)

def read_public_key():
    public_key = read_to_file('public_key.pem')
    messagebox.showinfo("Public_key", public_key)

window = Tk()
window.title("RSA")

window.geometry('400x300')
frame = Frame(
   window, 
   padx = 10, 
   pady = 10 
)
frame.pack(expand=True)

message_label = Label(window, text="Wiadomość:")
message_label.pack()

message_entry = Entry(window)
message_entry.pack()

encrypt_button = Button(window, text="Szyfrowanie", command= encrypt_message)
encrypt_button.pack()

decrypt_button = Button(window, text="Deszyfrowanie", command= decrypt_message)
decrypt_button.pack()

decrypt_button = Button(window, text="Deszyfrowanie z pliku", command= decrypt_message_on_file)
decrypt_button.pack()

public_key_button = Button(window, text="Klucz publiczny", command= read_public_key)
public_key_button.pack()

private_key_button = Button(window, text="Klucz prywatny", command= read_private_key)
private_key_button.pack()

new_key_button = Button(window, text="Generowanie nowych kluczy", command= new_keys)
new_key_button.pack()

exit_button = Button(window, text="Exit", command=exit_program)
exit_button.pack()

window.mainloop()