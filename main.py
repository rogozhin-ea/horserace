import sqlite3
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


def show_table(name_for_show):
    connection = sqlite3.connect('horse_racing.db')
    cursor = connection.cursor()
    if name_for_show == "horses":
        sql = "SELECT * "
    sql = "SELECT DISTINCT competition.name, competition.date_and_time, competition.address, competition.hippodrome_name, competition_result.places, rider.Name, horses.Nickname, competition_result.driving_time from competition_result JOIN competition ON competition_result.id_competiton = competition.id JOIN competition_riders_horses ON competition_result.id_competiton = competition_riders_horses.id_competition JOIN horses_and_riders ON competition_result.id_riders = horses_and_riders.id_riders JOIN rider ON horses_and_riders.id_riders = rider.ID JOIN horses ON horses_and_riders.id_horses = horses.id ORDER BY competition.name"
    cursor.execute(sql)
    records = cursor.fetchall()
    for row in records:
        row_string = str(row).replace("(", "").replace(")", "").replace("'", "")
        print(row_string)
    connection.close()
    #Изменение 2

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
            gen_string = str(gen_record).replace("(", "").replace(")", "").replace("'", "").replace(",", "") + "     "

            age = "SELECT Age FROM horses where id = " + str(i)
            cursor.execute(age)
            age_record = cursor.fetchone()
            age_string = str(age_record).replace("(", "").replace(")", "").replace("'", "").replace(",", "")

            print(name_string, gen_string, age_string)

    connection.close()


def enter_riders():
    while True:
        host = "192.168.31.90"
        user = "postgres"
        password = "secret"
        db_name = "horse_riders"
        port = "5432"

        try:
            connection = psycopg2.connect(user=user, password=password, host=host, port=port)
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        except:
            print("Ошибка подключения")
            break;

        cursor = connection .cursor()
        cursor.execute(f"CREATE DATABASE {db_name};")
        print("База данных " + db_name + " успешно созданна" )

        connection.close()

        try:
            connection = psycopg2.connect(user=user, password=password, host=host, port=port, dbname=db_name)
            connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        except:
            print("Ошибка подключения")
            break;
        try:
            cursor = connection.cursor()
            cursor.execute("""CREATE TABLE riders (id SERIAL NOT NULL PRIMARY KEY, name CHARACTER VARYING(30),email CHARACTER VARYING(30),age INT);""")
        except:
            print("Ошибка создания таблицы")
            break;

        count_riders = input("Введите количество новых жокеев: ")

        for i in range(int(count_riders)):
            rider = input("Введите имя, email и возраст жокея: ").replace('"' , "'")
            cursor.execute(f"""INSERT INTO public.riders (name,email,age) VALUES ({rider});""")
            connection.commit()
            cursor.execute("""SELECT * FROM public.riders """)
            print(cursor.fetchall())

        connection.close()
        break;

def show_riders ():
    host = "192.168.31.90"
    user = "postgres"
    password = "secret"
    db_name = "horse_riders"
    port = "5432"

    try:
        connection = psycopg2.connect(user=user, password=password, host=host, port=port, dbname=db_name)
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    except:
        print("Ошибка подключения")

    cursor = connection.cursor()
    cursor.execute("""SELECT * FROM public.riders """)
    print(cursor.fetchall())

    connection.close()
print("Добро пожаловать в приложение клуба любителей  скачек «RamHorse»!")


def menu():
    print("-----------------------------------------------")
    print("Выберите опцию:")
    print("1. Посмотреть информацию о лошадях.")
    print("2. Посмотреть информацию о владельцах лошадей.")
    print("3. Посмотреть информацию о жокеях.")
    print("4. Посмотреть информацию о состязаниях.")
    print("5. Добавить информацию о жокеях")
    print("6. Выход.")
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
        print("Имя                                Адрес                                                         Возраст")
        show_norm_table(2)
    elif choice == 3:
        print("Жокеи:")
        show_riders()
    elif choice == 4:
        print("Состязания:")
        show_table("competition")
    elif choice == 5:
        print("Добавление информации о жокеях")
        enter_riders()
    elif choice == 6:
        break;
    else:
        print("Недействительное значение.")
