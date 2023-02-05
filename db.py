import sqlite3

class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()
    
    def user_exists(self, user_id):#Проверка на наличие человека и его группы
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchmany(1)
            return bool(len(result))

    def check_group(self, user_id):#Проверка на наличие человека и его группы
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ? AND `group` = 'bebra'", (user_id,)).fetchmany(1)
            return bool(len(result))

    def get_name_group (self, user_id):
        with self.connection:
            result = self.cursor.execute("SELECT * FROM `users` WHERE `user_id` = ?", (user_id,)).fetchmany(1)
            for i in result:
                print(i[3])
            return i[3]

    def set_name_group(self, user_id, name_group):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `group` = ? WHERE `user_id` = ?", (name_group, user_id,))
    
    def add_user(self, user_id):
        with self.connection:
            return self.cursor.execute("INSERT INTO `users` (`user_id`) VALUES (?)", (user_id,))
    
    def set_active(self, user_id, active):
        with self.connection:
            return self.cursor.execute("UPDATE `users` SET `active` = ? WHERE `user_id` = ?", (active, user_id,))
    
    def get_users(self):
        with self.connection:
            return self.cursor.execute("SELECT `user_id`, `active` FROM `users`").fetchall()