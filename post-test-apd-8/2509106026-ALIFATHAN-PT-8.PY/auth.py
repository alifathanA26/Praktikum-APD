from tools import clear, pause
from admin_menu import menu_admin
from user_menu import menu_user

# Data user
users = {
    "maba": {"password": "026", "role": "user"},
    "admin": {"password": "111", "role": "admin"}
}

def login():
    clear()
    print("== LOGIN ==")
    username = input("Username: ")
    password = input("Password: ")

    if username in users and password == users[username]["password"]:
        print("Login berhasil!")
        pause()
        if users[username]["role"] == "admin":
            menu_admin()
        else:
            menu_user()
    else:
        print("Username atau password salah!")
        pause()
