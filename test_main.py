import unittest
from main import show_norm_table, show_table, auth, inf_menu


class TestMain(unittest.TestCase):
    def test_show_norm_table_horse(self):
        self.assertEqual(show_norm_table(1), ('Сильвер', 'Мужской', '4'))

    def test_show_norm_table_owner(self):
        self.assertEqual(show_norm_table(2), ('Кудряшов Святослав Андреевич      ', 'Ивановская область город Наро-Фоминск пер. 1905 года 99      ', '27'))

    def test_show_norm_table_rider(self):
        self.assertEqual(show_norm_table(3), ('Беляев Давид Егорович        ', 'Ульяновская область город Солнечногорск наб. 1905 года 75    ', '33      ', '68'))

    def test_show_norm_table_fail(self):
        self.assertEqual(show_norm_table(5), 'Недействительное значение.')

    def test_show_table(self):
        self.assertEqual(show_table("competition"), 'Success')

    def test_auth_success(self):
        self.assertEqual(auth("test", "test"), 1)

    def test_auth_fail(self):
        self.assertEqual(auth("tessdt", "tt"), 0)

    def test_inf_menu_fail(self):
        self.assertEqual(inf_menu(4), 'Fail')

    if __name__ == "__main__":
        unittest.main()