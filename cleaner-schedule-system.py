print("=== CLEANERS SCHEDULE SYSTEM ===")

admin_user = "Admin"
admin_pass = "Admin123"
admin_security_answer = "Admin123"

accounts = {}                
logged_in_user = None        

mwf_schedule = [
    ["Monday", "8:00 AM - 10:00 AM", "Classroom Cleaning"],
    ["Wednesday", "9:00 AM - 11:00 AM", "Library Cleaning"],
    ["Friday", "1:00 PM - 3:00 PM", "Restroom Cleaning"]
]

tts_schedule = [
    ["Tuesday", "8:30 AM - 10:30 AM", "Restroom Cleaning"],
    ["Thursday", "10:00 AM - 12:00 PM", "Hallway Maintenance"],
    ["Saturday", "7:30 AM - 9:30 AM", "Garden Cleaning"]
]

while True:
    if not logged_in_user:

        print("\nMAIN MENU:")
        print("1. Cleaner Register")
        print("2. Cleaner Login")
        print("3. Admin Login")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            print("\n=== REGISTER CLEANER ===")

            while True:
                username = input("Enter cleaner username: ")

                if username == "":
                    print("⚠ Username cannot be empty.")
                elif not username.isalpha():
                    print("⚠ Username must contain letters only.")
                else:
                    break

            if username in accounts:
                print("⚠ Username already registered.")
            else:
                accounts[username] = {"schedule": None}
                print(f"✅ Cleaner '{username}' registered successfully.")
                print("⚠ No schedule assigned yet. Admin must assign schedule.")

        elif choice == "2":
            username = input("Enter username: ")

            if username in accounts:
                logged_in_user = username
                print(f"\n✅ Welcome, {username}!")

                while logged_in_user:
                    print("\n=== CLEANER MENU ===")
                    print("1. View Schedule")
                    print("2. Log Out")

                    sub = input("Enter choice: ")

                    if sub == "1":
                        sched_type = accounts[logged_in_user]["schedule"]

                        if sched_type is None:
                            print("⛔ No schedule assigned yet. Please wait for admin.")
                        else:
                            print("\n=== YOUR SCHEDULE ===")
                            print("{:<10} {:<20} {:<30}".format("DAY", "TIME", "AREA"))
                            print("-" * 60)

                            if sched_type == "MWF":
                                for d, t, a in mwf_schedule:
                                    print("{:<10} {:<20} {:<30}".format(d, t, a))

                            elif sched_type == "TTS":
                                for d, t, a in tts_schedule:
                                    print("{:<10} {:<20} {:<30}".format(d, t, a))

                    elif sub == "2":
                        print(f"👋 Goodbye, {logged_in_user}!")
                        logged_in_user = None
                    
                    else:
                        print("❌ Invalid choice.")

            else:
                print("❌ Username not found. Please register first.")

        elif choice == "3":
            print("\n=== ADMIN LOGIN ===")

            u = input("Admin username: ")
            p = input("Admin password: ")

            if u == admin_user and p == admin_pass:
                print("🔐 Admin access granted.")
                logged_in_user = "ADMIN"

            else:
                print("❌ Incorrect login.")
                print("1. Try Again")
                print("2. Forgot Password")
                
                opt = input("Enter choice: ")

                if opt == "2":
                    print("\n=== RESET ADMIN PASSWORD ===")
                    answer = input("Enter Admin Key: ")

                    if answer == admin_security_answer:
                        print("✔ Correct! Set your new password.")
                        new_pass = input("Enter new admin password: ")

                        if new_pass == "":
                            print("❌ Password cannot be empty.")
                        else:
                            admin_pass = new_pass
                            print("✅ Admin password successfully reset!")
                    else:
                        print("❌ Incorrect admin key.")
                else:
                    print("Returning to main menu...")

            while logged_in_user == "ADMIN":
                print("\n=== ADMIN MENU ===")
                print("1. View All Cleaners")
                print("2. Assign Schedule")
                print("3. View Cleaners' Schedules")
                print("4. Log Out")

                admin_choice = input("Enter choice: ")

                if admin_choice == "1":
                    print("\n=== CLEANERS LIST ===")
                    if not accounts:
                        print("No cleaners registered.")
                    else:
                        for user, data in accounts.items():
                            sched = data["schedule"]
                            if sched is None:
                                sched = "❌ No schedule yet"
                            print(f"- {user} : {sched}")

                elif admin_choice == "2":
                    name = input("Enter cleaner username: ")

                    if name not in accounts:
                        print("❌ Cleaner not found.")
                    else:
                        print("\nChoose schedule type:")
                        print("1. MWF")
                        print("2. TTS")

                        sched_input = input("Enter choice: ")

                        if sched_input == "1":
                            accounts[name]["schedule"] = "MWF"
                            print(f"✅ {name}'s schedule set to MWF.")
                        elif sched_input == "2":
                            accounts[name]["schedule"] = "TTS"
                            print(f"✅ {name}'s schedule set to TTS.")
                        else:
                            print("❌ Invalid schedule type.")

                elif admin_choice == "3":
                    print("\n=== CLEANERS' ASSIGNED SCHEDULES ===")

                    if not accounts:
                        print("No cleaners registered.")
                    else:
                        for user, data in accounts.items():
                            sched = data["schedule"]

                            if sched == "MWF":
                                print(f"\n📌 {user} — MWF SCHEDULE")
                                print("{:<10} {:<20} {:<30}".format("DAY", "TIME", "AREA"))
                                print("-" * 60)
                                for d, t, a in mwf_schedule:
                                    print("{:<10} {:<20} {:<30}".format(d, t, a))

                            elif sched == "TTS":
                                print(f"\n📌 {user} — TTS SCHEDULE")
                                print("{:<10} {:<20} {:<30}".format("DAY", "TIME", "AREA"))
                                print("-" * 60)
                                for d, t, a in tts_schedule:
                                    print("{:<10} {:<20} {:<30}".format(d, t, a))

                            else:
                                print(f"\n📌 {user} — ❌ No schedule assigned")

                elif admin_choice == "4":
                    print("👋 Admin logged out.")
                    logged_in_user = None

                else:
                    print("❌ Invalid choice.")

        elif choice == "4":
            print("👋 Thank you for using the system!")
            break

        else:
            print("❌ Invalid choice. Try again.")
