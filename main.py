import sqlite3




def show_table(name_for_show):
    connection = sqlite3.connect('horse_racing.db')
    cursor = connection.cursor()
    sql = "SELECT * FROM " + name_for_show
    cursor.execute(sql)
    for record in cursor:
        print(record)

    #print(cursor.fetchall())
    connection.close()

print("Добро пожаловать в приложение клуба любителей скачек «RamHorse»!")


def menu():
    print("-----------------------------------------------")
    print("Выберите опцию:")
    print("1. Посмотреть информацию о лошадях.")
    print("2. Посмотреть информацию о владельцах лошадей.")
    print("3. Посмотреть информацию о жокеях.")
    print("4. Посмотреть информацию о состязаниях.")
    print("5. Выход.")
    print("-----------------------------------------------")


while True:
    menu()
    choice = int(input("Введите ваш выбор: "))
    print("-----------------------------------------------")

    if choice == "1":
        print("Лошади:")
        show_table("horses")
    elif choice == "2":
        print("Владельцы:")
        show_table("owner")
    elif choice == "3":
        print("Жокеи:")
        show_table("rider")
    elif choice == "4":
        print("Состязания:")
        show_table("competition")
    elif choice == "5":
        break;
    else:
        print("Недействительное значение.")
