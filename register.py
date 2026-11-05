import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib
import database

database.create_database()


def hash_password(password):
    encoded_password = password.encode()
    hashed_password = hashlib.sha256(encoded_password)
    password_hash = hashed_password.hexdigest()

    return password_hash


def register():
    email = email_entry.get()
    password = password_entry.get()
    if email == "":
        email_error.config(text="メールアドレスを入力して下さい")
    else:
        email_error.config(text="")

    if password == "":
        password_error.config(text="パスワードを入力して下さい")
    else:
        password_error.config(text="")

    if email == "" or password == "":
        return

    try:
        with sqlite3.connect("users.db") as connection:
            cursor = connection.cursor()

            password_hash = hash_password(password)

            cursor.execute(
                "INSERT INTO users (email,password) VALUES(?,?)", (email, password_hash)
            )

        messagebox.showinfo("登録完了", "登録が完了しました")

        root.destroy()

        import login_form

    except sqlite3.IntegrityError:
        tk.messagebox.showerror(
            "エラー", "このメールアドレスはすでに、登録されています"
        )


def open_loginform(event):
    root.destroy()
    import login_form


root = tk.Tk()
root.title("ユーザー登録")

width = 350
height = 250

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - width) // 2
y = (screen_height - height) // 2

root.geometry(f"{width}x{height}+{x}+{y}")

email_label = tk.Label(root, text="メールアドレス")
email_label.pack(pady=10)
email_entry = tk.Entry(root, width=40)
email_entry.pack(pady=(10, 5))
email_error = tk.Label(root, text="", fg="red")
email_error.pack()

password_label = tk.Label(root, text="パスワード")
password_label.pack()
password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack(pady=(5, 5))
password_error = tk.Label(root, text="", fg="red")
password_error.pack()

register_button = tk.Button(root, text="登録", cursor="hand2", command=register)
register_button.pack(pady=5)

back_button = tk.Label(
    root,
    text="ログイン画面へ戻る",
    fg="blue",
    cursor="hand2",
    font=("TkDefaultFont", 8),
)
back_button.pack(anchor="e", pady=(20, 10))
back_button.bind("<Button-1>", open_loginform)

root.mainloop()
