import tkinter as tk

root = tk.Tk()
root.title("ログイン成功")

width = 350
height = 250

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x = (screen_width - width) // 2
y = (screen_height - height) // 2

root.geometry(f"{width}x{height}+{x}+{y}")

message = tk.Label(
    root,
    text="ポートフォリオは以上です \n\nご確認いただき\n\nありがとうございました",
    font=("TkDefaultFont", 10),
)
message.pack(pady=70)

button = tk.Button(root, text="終了", command=root.destroy)

button.pack()

root.mainloop()
