##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk


# main window
root = tk.Tk()

root.wm_geometry("300x200")
root.title("athorization")

frame_login = tk.Frame(root)
frame_login.grid(sticky = "news", row = 0, column = 0)
user_int =""
def test():
    user_int = ent_passowrd.get()
    auth_lable = tk.Label(frame_auth, text = "password: " + user_int)
    auth_lable.pack()
    frame_auth.tkraise()
    print("yes")

lbl_username = tk.Label(frame_login, text="Username:", font = "Courier")
ent_username = tk.Entry(frame_login, bd=3)
lbl_username.pack(pady=10)
ent_username.pack(pady=5)
lbl_password = tk.Label(frame_login, text = "password:", font = "Courier")
ent_passowrd = tk.Entry(frame_login, bd=3, show = "汉")
lbl_password.pack(padx=10)
ent_passowrd.pack(pady=10)
button = tk.Button(frame_login, text="Login", command = test)
button.pack()


frame_auth = tk.Frame(root)
frame_auth.grid(sticky = "news", row = 0, column = 0)

frame_login.tkraise()


root.mainloop()