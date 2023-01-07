import sqlite3
#import psycopg2
#from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def input_auth():
    print("-----------------------------------------------")
    login = str(input("Введите логин: "))
    password = str(input("Введите пароль: "))
    print("-----------------------------------------------")
    flag = auth(login, password)
    return flag


def auth(login, password):
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()
    sql = f"SELECT * FROM users WHERE login = '{login}' AND password = '{password}'"
    cursor.execute(str(sql))
    logpass = cursor.fetchall()
    if len(logpass) != 0:
        fl_auth = 1
        print("Авторизация выполнена успешно")
        return fl_auth
    else:
        fl_auth = 0
        print("Авторизация не удалась")
        return fl_auth


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

    elif option == 2:
        sql = "SELECT * FROM owner"
        cursor.execute(sql)
        records = cursor.fetchall()
        num = (len(records))
        for i in range(1, num):
            name = "SELECT Name FROM owner where id = " + str(i)
            cursor.execute(name)
            name_record = cursor.fetchone()
            name_string = str(name_record).replace("(", "").replace(")", "").replace("'", "").replace(",", "")
            if len(name_string) < 35:
                diff = 35 - len(name_string)
                for k in range(1, diff):
                    name_string = name_string + " "

            address = "SELECT Address FROM owner where id = " + str(i)
            cursor.execute(address)
            address_record = cursor.fetchone()
            address_string = str(address_record).replace("(", "").replace(")", "").replace("'", "").replace(",", "")
            if len(address_string) < 62:
                diff = 62 - len(address_string)
                for k in range(1, diff):
                    address_string = address_string + " "

            age = "SELECT Age FROM owner where id = " + str(i)
            cursor.execute(age)
            age_record = cursor.fetchone()
            age_string = str(age_record).replace("(", "").replace(")", "").replace("'", "").replace(",", "")

            print(name_string, address_string, age_string)

    elif option == 3:
        sql = "SELECT * FROM rider"
        cursor.execute(sql)
        records = cursor.fetchall()
        num = (len(records))
        for i in range(1, num):
            name = "SELECT Name FROM rider where id = " + str(i)
            cursor.execute(name)
            name_record = cursor.fetchone()
            name_string = str(name_record).replace("(", "").replace(")", "").replace("'", "").replace(",", "")
            if len(name_string) < 30:
                diff = 30 - len(name_string)
                for k in range(1, diff):
                    name_string = name_string + " "

            address = "SELECT Address FROM rider where id = " + str(i)
            cursor.execute(address)
            address_record = cursor.fetchone()
            address_string = str(address_record).replace("(", "").replace(")", "").replace("'", "").replace(",", "")
            if len(address_string) < 62:
                diff = 62 - len(address_string)
                for k in range(1, diff):
                    address_string = address_string + " "

            age = "SELECT Age FROM rider where id = " + str(i)
            cursor.execute(age)
            age_record = cursor.fetchone()
            age_string = str(age_record).replace("(", "").replace(")", "").replace("'", "").replace(",", "") + "      "

            rating = "SELECT rating FROM rider where id = " + str(i)
            cursor.execute(rating)
            rating_record = cursor.fetchone()
            rating_string = str(rating_record).replace("(", "").replace(")", "").replace("'", "").replace(",", "")

            print(name_string, address_string, age_string, rating_string)

    elif option == 4:
        connection = sqlite3.connect('horse_racing.db')
        cursor = connection.cursor()
        sql = "SELECT DISTINCT competition.name, competition.date_and_time, competition.address, competition.hippodrome_name, competition_result.places, rider.Name, horses.Nickname, competition_result.driving_time from competition_result JOIN competition ON competition_result.id_competiton = competition.id JOIN competition_riders_horses ON competition_result.id_competiton = competition_riders_horses.id_competition JOIN horses_and_riders ON competition_result.id_riders = horses_and_riders.id_riders JOIN rider ON horses_and_riders.id_riders = rider.ID JOIN horses ON horses_and_riders.id_horses = horses.id ORDER BY competition.name"
        cursor.execute(sql)
        records = cursor.fetchall()
        for row in records:
            row_string = str(row).replace("(", "").replace(")", "").replace("'", "")
            print(row_string)
        connection.close()
        return 'Success'

    else:
        msg = "Недействительное значение."
        print(msg)
        return msg

    connection.close()


def enter_table(db_name):
    if db_name == 'horse':
        h_name = input("Введите кличку: ")
        h_gen = input("Введите пол: ")
        h_age = input("Введите возраст: ")
        h_owner = input("Введите id владельца: ")
        connection = sqlite3.connect('horse_racing.db')
        cursor = connection.cursor()
        sql = f"INSERT INTO horses (Nickname, Gender, Age, id_owner) VALUES ('{h_name}', '{h_gen}', '{h_age}', '{h_owner}');"
        cursor.execute(sql)
        connection.commit()
        cursor.execute("SELECT * FROM horses")
        print(cursor.fetchall())
        connection.close()
        return 'Success'

    elif db_name == 'owner':
        o_name = input("Введите ФИО: ")
        o_address = input("Введите адрес: ")
        o_age = input("Введите возраст: ")
        connection = sqlite3.connect('horse_racing.db')
        cursor = connection.cursor()
        sql = f"INSERT INTO owner (name, address, age) VALUES ('{o_name}', '{o_address}', '{o_age}');"
        cursor.execute(sql)
        connection.commit()
        cursor.execute("SELECT * FROM owner")
        print(cursor.fetchall())
        connection.close()
        return 'Success'

    elif db_name == 'rider':
        r_name = input("Введите ФИО: ")
        r_address = input("Введите адрес: ")
        r_age = input("Введите возраст: ")
        r_rating = input("Введите рейтинг: ")
        connection = sqlite3.connect('horse_racing.db')
        cursor = connection.cursor()
        sql = f"INSERT INTO rider (Name, Address, Age, rating) VALUES ('{r_name}', '{r_address}', '{r_age}', '{r_rating}');"
        cursor.execute(sql)
        connection.commit()
        cursor.execute("SELECT * FROM rider")
        print(cursor.fetchall())
        connection.close()
        return 'Success'

    elif db_name == 'competition':
        c_name = input("Введите название соревнований: ")
        c_date = input("Введите дату: ")
        c_hyp = input("Введите название ипподрома: ")
        c_address = input("Введите адрес: ")
        connection = sqlite3.connect('horse_racing.db')
        cursor = connection.cursor()
        sql = f"INSERT INTO competition (name, date_and_time, hippodrome_name, address) VALUES ('{c_name}', '{c_date}', '{c_hyp}', '{c_address}');"
        cursor.execute(sql)
        connection.commit()
        cursor.execute("SELECT * FROM competition")
        print(cursor.fetchall())
        connection.close()
        return 'Success'

    else:
        print("Недействительное значение")


print("Добро пожаловать в приложение клуба любителей скачек «RamHorse»!")


def menu():
    print("-----------------------------------------------")
    print("Выберите опцию:")
    print("1. Посмотреть информацию о лошадях.")
    print("2. Посмотреть информацию о владельцах лошадей.")
    print("3. Посмотреть информацию о жокеях.")
    print("4. Посмотреть информацию о состязаниях.")
    print("5. Добавить информацию о лошадях")
    print("6. Добавить информацию о владельцах лошадей")
    print("7. Добавить информацию о жокеях")
    print("8. Добавить информацию о состязаниях")
    print("9. Выход.")
    print("-----------------------------------------------")

def inf_menu(fl_auth):
    if fl_auth != 1:
        if fl_auth != 0:
            return "Fail"
    if fl_auth != 0:
        if fl_auth != 1:
            return "Fail"
    while True:
        menu()
        choice = input("Введите ваш выбор: ")
        print("-----------------------------------------------")

        if choice == "1":
            print("Лошади:")
            print("Имя         Пол         Возраст")
            show_norm_table(1)
        elif choice == "2":
            print("Владельцы:")
            print("Имя                                Адрес                                                         Возраст")
            show_norm_table(2)
        elif choice == "3":
            print("Имя                           Адрес                                                         Возраст  Рейтинг")
            show_norm_table(3)
        elif choice == "4":
            print("Состязания:")
            show_norm_table(4)
        elif choice == "5":
            if fl_auth == 1:
                enter_table('horse')
            else:
                print("Для продолжения необходимо авторизоваться")
        elif choice == "6":
            if fl_auth == 1:
                enter_table('owner')
            else:
                print("Для продолжения необходимо авторизоваться")
        elif choice == "7":
            if fl_auth == 1:
                enter_table('rider')
            else:
                print("Для продолжения необходимо авторизоваться")
        elif choice == "8":
            if fl_auth == 1:
                enter_table('competition')
            else:
                print("Для продолжения необходимо авторизоваться")
        elif choice == "9":
            break;
        else:
            print("Недействительное значение.")


def start_menu():
    authorized = 0
    while True:
        print("-----------------------------------------------")
        print("Выберите опцию:")
        print("1. Авторизоваться")
        print("2. Открыть меню")
        print("3. Выйти")
        print("-----------------------------------------------")
        choice = input("Введите ваш выбор: ")
        if choice == "1":
            authorized = input_auth()
        elif choice == "2":
            inf_menu(authorized)
        elif choice == "3":
            break;
        else:
            print("Недействительное значение.")


start_menu()