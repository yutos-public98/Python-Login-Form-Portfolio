import tkinter as tk
import database
import auth

database.create_database()

root = tk.Tk()
root.title("ログイン画面")
width = 350
height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - width) // 2
y = (screen_height - height) // 2

root.geometry(f"{width}x{height}+{x}+{y}")


def open_register(event):
    root.destroy()
    import register


def login():
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

    status_label.config(text="認証中", fg="black")

    root.after(1000, authenticate, email, password)


def authenticate(email, password):
    result = auth.authenticate_user(email, password)

    if result:
        status_label.config(text="認証成功", fg="blue")
        root.after(1000, open_loginsuccess)
    else:
        status_label.config(text="認証失敗", fg="red")


def open_loginsuccess():
    root.destroy()
    import login_success


label = tk.Label(root, text=" メールアドレス")
label.pack(
    pady=(10, 5),
)
email_entry = tk.Entry(root, width=40)
email_entry.pack(pady=(5, 5))
email_error = tk.Label(root, text="", fg="red")
email_error.pack()

password_label = tk.Label(root, text="パスワード")
password_label.pack(pady=(5, 5))
password_entry = tk.Entry(root, width=40, show="*")
password_entry.pack(pady=(5, 5))
password_error = tk.Label(root, text="", fg="red")
password_error.pack()

login_button = tk.Button(
    root,
    text="ログイン",
    cursor="hand2",
    command=login,
)
login_button.pack(pady=(5, 5))

status_label = tk.Label(root, text="")
status_label.pack()

register_link = tk.Label(
    root,
    text="新規登録はこちら",
    fg="blue",
    cursor="hand2",
    font=("TkDefaultFont", 8, "underline"),
)
register_link.pack(anchor="e", pady=(5, 5))
register_link.bind("<Button-1>", open_register)

label = tk.Label(
    root,
    text=" メールアドレスはデフォルトで、test1@example.com\n\nパスワードは1234\n\nを登録してあります",
)
label.pack(
    pady=(10, 5),
)

root.mainloop()
