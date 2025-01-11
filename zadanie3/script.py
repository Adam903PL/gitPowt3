import csv

def main():
    with open("zadanie3/users.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Login", "Password"])
        while True:
            login = input("Enter login (or 'q' to quit): ")
            if login.lower() == 'q':
                break
            password = input("Enter password: ")
            writer.writerow([login, password])

if __name__ == "__main__":
    main()
