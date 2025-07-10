import os
import time
import webbrowser
import random

def play_sound():
    try:
        os.system("mpv sound.mp3 --no-video > /dev/null 2>&1 &")
    except:
        pass

def animate_start():
    play_sound()
    for i in range(3):
        print("\033[1;32m[+] Loading Tool" + "." * (i + 1) + "\033[0m")
        time.sleep(1)
    os.system("clear")

def banner():
    os.system("clear")
    print("\033[1;31m=============================")
    print("     MOBILE CLONER PRO")
    print("=============================")
    print("TOLL OWNER: NEHAL DARK TRAP")
    print("YT: NEHAL DARK TRAP")
    print("INSTA: nehal_dark_trap")
    print("=============================\033[0m")

def open_link(url):
    try:
        os.system(f"xdg-open '{url}' > /dev/null 2>&1 &")
    except:
        webbrowser.open(url)

def subscription_lock():
    while True:
        banner()
        print("\033[1;32m1. Subscribe Channel")
        print("2. Already Subscribed\033[0m")
        print("\033[1;31m", end="")
        choice = input("Enter your choice (1/2): ")
        print("\033[0m", end="")

        if choice == "1":
            print("\n🔁 Opening YouTube Channel...")
            open_link("https://youtube.com/@nehal_dark_trap?si=CGE96-qu0BhVGHvi")
            print("📌 After subscribing, select 2 to continue.")
            time.sleep(2)
        elif choice == "2":
            print("✅ Subscription confirmed.")
            time.sleep(1)
            break
        else:
            print("❌ Invalid choice. Try again.")
            time.sleep(1)

def fake_cloning():
    os.makedirs("/sdcard/CLONED-DATA", exist_ok=True)
    banner()
    number = input("\033[1;33mEnter target number: \033[0m")
    print("\n\033[1;32m[•] Connecting to device", number)
    time.sleep(2)
    print("[•] Cloning Messages...")
    time.sleep(1)
    print("[•] Cloning Contacts...")
    time.sleep(1)
    print("[•] Cloning Call Logs...")
    time.sleep(1)
    print("[•] Cloning Gallery...")
    time.sleep(1)
    print("[•] Cloning Camera Access...")
    time.sleep(1)
    print("\033[1;32m[✓] Phone Cloned Successfully!\033[0m")
    with open("/sdcard/CLONED-DATA/clone_report.txt", "w") as f:
        f.write(f"Cloned Data from: {number}\n")
        f.write("✔️ Messages\n✔️ Contacts\n✔️ Gallery\n✔️ Call Logs\n✔️ Camera\n")
    print(f"\033[1;34m[+] Saved to: /sdcard/CLONED-DATA/clone_report.txt\033[0m")
    input("\nPress Enter to return to menu...")

def main_menu():
    while True:
        banner()
        print("\033[1;36m1. Join Telegram Group")
        print("2. Follow on Instagram")
        print("3. Clone a Phone")
        print("4. Exit\033[0m")
        choice = input("\nSelect an option (1-4): ")

        if choice == "1":
            open_link("https://t.me/darktrapchat")
        elif choice == "2":
            open_link("https://instagram.com/nehal_dark_trap")
        elif choice == "3":
            fake_cloning()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("❌ Invalid choice.")
            time.sleep(1)

if __name__ == "__main__":
    animate_start()
    subscription_lock()
    main_menu()
