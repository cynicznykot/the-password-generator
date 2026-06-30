import tkinter as tk
from tkinter import ttk
from generator import build_character_pool, generate_password


def main():
    # Create a window
    root = tk.Tk()
    root.title("Your Personal Password Generator")
    root.geometry("800x700")

    # Create variables
    length_var = tk.IntVar(value=16)
    use_letters = tk.BooleanVar(value=True)
    use_digits = tk.BooleanVar(value=True)
    use_symbols = tk.BooleanVar(value=True)
    password_var = tk.StringVar(value="")

    def on_generate():
        # Retrieving values
        length = length_var.get()
        letters = use_letters.get()
        digits = use_digits.get()
        symbols = use_symbols.get()

        # Type checking
        if not (letters or digits or symbols):
            password_var.set("⚠️ Select at least one character type.")
            return

        # Func generated password
        pool = build_character_pool(letters, digits, symbols)
        password = generate_password(length, pool)
        # Final result
        password_var.set(password)


    # ---- INTERFACE ELEMENTS ----
    # Length mark
    Label_length = tk.Label(root, text="Length Password:", font=("Arial", 12))
    Label_length.pack(pady=5)

    # Slider
    scale = tk.Scale(root, from_=15, to=64, orient="horizontal", variable=length_var, length=400)
    scale.pack(pady=5)

    # Checkboxes
    check_letters = tk.Checkbutton(root, text="Check Letters", variable=use_letters)
    check_letters.pack(pady=5)

    check_digits = tk.Checkbutton(root, text="Check Digits", variable=use_digits)
    check_digits.pack(pady=5)

    check_symbols = tk.Checkbutton(root, text="Check Symbols", variable=use_symbols)
    check_symbols.pack(pady=5)

    # Button
    button = tk.Button(root, text="Generate Password", command=on_generate)
    button.pack(pady=5)

    # Password field
    entry = tk.Entry(root, textvariable=password_var, width=50)
    entry.pack()

    # Launch window
    root.mainloop()


if __name__ == "__main__":
    main()