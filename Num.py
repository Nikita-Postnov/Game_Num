import random
import tkinter as tk
from tkinter import messagebox

def guess_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    def check_guess():
        nonlocal attempts
        user_guess = int(entry.get())
        attempts += 1

        if user_guess == secret_number:
            messagebox.showinfo("Результат", f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток!")
            root.destroy()
        elif user_guess < secret_number:
            messagebox.showinfo("Результат", "Загаданное число больше вашей догадки. Попробуйте еще раз.")
        else:
            messagebox.showinfo("Результат", "Загаданное число меньше вашей догадки. Попробуйте еще раз.")
        entry.delete(0, tk.END)

    root = tk.Tk()
    root.title("Угадай число")
    root.geometry("300x150")

    label = tk.Label(root, text="Я загадал число от 1 до 100. Попробуйте угадать!")
    label.pack(pady=10)

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text="Проверить", command=check_guess)
    button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    guess_number()
