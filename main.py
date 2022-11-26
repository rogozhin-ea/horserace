import sqlite3


def show_table(name_for_show):
    connection = sqlite3.connect('horse_racing.db')
    cursor = connection.cursor()
    sql = "SELECT * FROM " + name_for_show
    cursor.execute(sql)
    records = cursor.fetchall()
    for row in records:
        row_string = str(row).replace("(", "").replace(")", "").replace("'", "")
        print(row_string)

    connection.close()

def show_norm_table(option):
    connection = sqlite3.connect('horse_racing.db')
    cursor = connection.cursor()
    if option == 1:
        sql = "SELECT * FROM horses"
        cursor.execute(sql)
        records = cursor.fetchall()
        num = (len(records))
        for i in range(1, num):
            name = "SELECT Nickname FROM horses where id = " + str(i)
            cursor.execute(name)
            name_record = cursor.fetchone()
            name_string = str(name_record).replace("(", "").replace(")", "").replace("'", "").replace(",", "")
            if len(name_string) < 12:
                diff = 12 - len(name_string)
                for k in range(1, diff):
                    name_string = name_string + " "

            gender = "SELECT Gender FROM horses where id = " + str(i)
            cursor.execute(gender)
            gen_record = cursor.fetchone()
            gen_string = str(gen_record).replace("(", "").replace(")", "").replace("'", "").replace(",", "") + "    "

            age = "SELECT Age FROM horses where id = " + str(i)
            cursor.execute(age)
            age_record = cursor.fetchone()
            age_string = str(age_record).replace("(", "").replace(")", "").replace("'", "").replace(",", "")

            print(name_string, gen_string, age_string)


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

        if choice == 1:
            print("Лошади:")
            print("Имя         Пол         Возраст")
            show_norm_table(1)
        elif choice == 2:
            print("Владельцы:")
            show_table("owner")
        elif choice == 3:
            print("Жокеи:")
            show_table("rider")
        elif choice == 4:
            print("Состязания:")
            show_table("competition")
        elif choice == 5:
            break;
        else:
            print("Недействительное значение.")