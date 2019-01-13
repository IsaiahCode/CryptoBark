from tkinter import *

bonelocker = {
    'a': 'wuff ',
    'b': 'woof ',
    'c': 'bowwow ',
    'd': 'howl ',
    'e': 'whine ',
    'f': 'ruff ',
    'g': 'grr ',
    'h': 'arf ',
    'i': 'yap ',
    'j': 'ar roof ',
    'k': 'raow ',
    'l': 'yelp ',
    'm': 'whimper ',
    'n': 'sniff ',
    'o': 'huff ',
    'p': 'growl ',
    'q': 'yip ',
    'r': 'groan ',
    's': 'bowbow ',
    't': 'rrr ',
    'u': 'pant ',
    'v': 'bay ',
    'w': 'scratch ',
    'x': 'fart ',
    'y': 'grunt ',
    'z': 'aroo ',
    ' ': 'bark '
}


# Barkryption Functions
def barkrypt():
    entered_text = textentry.get()  # This will collect the text from the text entry box

    cipher = ''
    for char in entered_text:
        cipher += bonelocker[char]

    output.delete(0.0, END)
    output.insert(END, cipher)


def debarkrypt():
    entered_text = textentry.get()  # This will collect the text from the text entry box

    for x, y in bonelocker.items():
        entered_text = entered_text.replace(y, x)

    output.delete(0.0, END)
    output.insert(END, entered_text)


# Exit function
def close_window():
    window.destroy()
    exit()


# main:
window = Tk()
window.title("CryptoBark")

# Photo
photo1 = PhotoImage(file="resources/Dogcrypto.png")
Label(window, image=photo1) .grid(row=0, column=0, sticky=N)

# Create Labels
Label(window, text="Enter a message you would like to barkrypt or debarkrypt:", fg="black", font="none 12 bold") .grid(row=1, column=0, sticky=W)
Label(window, text="Your secure message:", fg="black", font="none 12 bold") .grid(row=4, column=0, sticky=W)

# Create a text entry box
textentry = Entry(window, width=100, bg="white")
textentry.grid(row=2, column=0, padx=10, pady=10, sticky=W)

# Add some buttons
Button(window, text="Barkcrypt", width=10, command=barkrypt) .grid(row=3, column=0, padx=10, pady=10, sticky=W)
Button(window, text="Debarkrypt", width=10, command=debarkrypt) .grid(row=3, column=0, padx=10, pady=10, sticky=E)

# Create a text box
output = Text(window, width=75, height=6, wrap=WORD, background="white")
output.grid(row=5, column=0, padx=10, pady=10, sticky=W)

# Add exit button
Button(window, text="Exit", width=14, command=close_window) .grid(row=7, column=0, sticky=N)

# run the main loop
window.mainloop()
