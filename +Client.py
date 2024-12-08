import tkinter as tk
from tkinter import messagebox
import mysql.connector
from mysql.connector import Error
import subprocess

class DatabaseApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Добавление данных в базу")
        self.master.configure(bg="#f0f0f0")  # Цвет фона

        self.frame_update = tk.Frame(self.master, bg="#ffffff", bd=5, relief=tk.GROOVE)
        self.frame_update.pack(padx=20, pady=20)

        # Поля ввода
        tk.Label(self.frame_update, text="Фамилия:", bg="#ffffff").grid(row=0, column=0, sticky='w', padx=5, pady=5)
        self.surnameNew = tk.Entry(self.frame_update)
        self.surnameNew.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.frame_update, text="Имя:", bg="#ffffff").grid(row=1, column=0, sticky='w', padx=5, pady=5)
        self.NameNew = tk.Entry(self.frame_update)
        self.NameNew.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.frame_update, text="Отчество:", bg="#ffffff").grid(row=2, column=0, sticky='w', padx=5, pady=5)
        self.otcgestvoNew = tk.Entry(self.frame_update)
        self.otcgestvoNew.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.frame_update, text="Счёт:", bg="#ffffff").grid(row=3, column=0, sticky='w', padx=5, pady=5)
        self.schetNew = tk.Entry(self.frame_update)
        self.schetNew.grid(row=3, column=1, padx=5, pady=5)

        tk.Label(self.frame_update, text="Id Зала:", bg="#ffffff").grid(row=4, column=0, sticky='w', padx=5, pady=5)
        self.id_zalaNew = tk.Entry(self.frame_update)
        self.id_zalaNew.grid(row=4, column=1, padx=5, pady=5)

        # Поле для отображения ID клиента
        tk.Label(self.frame_update, text="ID клиента:", bg="#ffffff").grid(row=5, column=0, sticky='w', padx=5, pady=5)
        self.IDNew = tk.Entry(self.frame_update)
        self.IDNew.grid(row=5, column=1, padx=5, pady=5)
        self.IDNew.config(state='readonly')  # Делаем поле только для чтения

        # Кнопка добавления данных
        self.add_button = tk.Button(self.frame_update, text="Добавить данные", command=self.add_data, bg="#4CAF50", fg="white")
        self.add_button.grid(row=6, columnspan=2, pady=(10, 0))

        # Генерируем ID клиента при инициализации
        self.generate_client_id()

        # Поле для ввода ID клиента для удаления
        tk.Label(self.master, text="ID клиента для удаления:", bg="#f0f0f0").pack(pady=(20, 0))
        self.entry_delete_id = tk.Entry(self.master)
        self.entry_delete_id.pack(pady=(0, 10))

        # Кнопка для удаления клиента
        delete_button = tk.Button(self.master, text="Удалить клиента", command=self.delete_data, bg="#f44336", fg="white")
        delete_button.pack(pady=(0, 20))

    def generate_client_id(self):
        new_id = 1  # Пример значения
        self.IDNew.config(state='normal')
        self.IDNew.delete(0, tk.END)
        self.IDNew.insert(0, new_id)
        self.IDNew.config(state='readonly')

    def add_data(self):
        
        messagebox.showinfo("Информация", "Данные успешно добавлены!")

    def delete_data(self):
        
        messagebox.showinfo("Информация", "Данные успешно удалены!")
    def connect_to_database(self):
        """Создает соединение с базой данных MySQL."""
        try:
            connection = mysql.connector.connect(
                host='127.0.0.1',  
                database='gymsport',  
                user='root',  
                password='7895123evg'  
            )
            if connection.is_connected():
                print("Успешное подключение к базе данных")
                return connection
        except Error as e:
            print(f"Ошибка при подключении к MySQL: {e}")
            return None

    def generate_client_id(self):
        """Генерирует новый ID клиента."""
        connection = self.connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                cursor.execute("SELECT MAX(ID) FROM persanal_data")  
                max_id = cursor.fetchone()[0]
                new_id = max_id + 1 if max_id is not None else 1  
                self.IDNew.config(state='normal')  
                self.IDNew.delete(0, tk.END)   
                self.IDNew.insert(0, new_id) 
                self.IDNew.config(state='readonly')  
            except Error as e:
                messagebox.showerror("Ошибка", f"Ошибка при получении максимального ID: {e}")
                print(f"Ошибка при получении максимального ID: {e}")
            finally:
                connection.close()

    def insert_data(self, connection):
        """Добавляет новые данные в таблицу."""
        
        name = self.NameNew.get()
        surname = self.surnameNew.get()
        otcgestvo = self.otcgestvoNew.get()
        schet = self.schetNew.get()
        id_zala=self.id_zalaNew.get()
        ID = self.IDNew.get()

        try:
            cursor = connection.cursor()
            query = """INSERT INTO persanal_data (ID,Name, SurName, Otchestvo, schet, ID_ZAla)
                       VALUES (%s,%s, %s, %s, %s, %s)"""
            cursor.execute(query, (ID,name, surname, otcgestvo, schet, id_zala))
            connection.commit()
            messagebox.showinfo("Успех", "Данные успешно добавлены")
            print("Данные успешно добавлены")
            self.generate_client_id()  # Генерируем новый ID после успешного добавления
        except Error as e:
            messagebox.showerror("Ошибка", f"Ошибка при добавлении данных: {e}")
            print(f"Ошибка при добавлении данных: {e}")

    def add_data(self):
        """Обрабатывает добавление данных в базу."""
        connection = self.connect_to_database()
        if connection:
            self.insert_data(connection)
            connection.close()
    def connect_to_database(self):
        """Подключается к базе данных."""
        try:
            connection = mysql.connector.connect(
                host='127.0.0.1',  
                database='gymsport',  
                user='root',  
                password='7895123evg'  
            )
            return connection
        except Error as e:
            messagebox.showerror("Ошибка подключения", f"Ошибка: {e}")
            return None

    def delete_data(self):
        """Удаляет данные из базы по ID."""
        client_id = self.entry_delete_id.get()

        if not client_id.isdigit():
            messagebox.showerror("Ошибка", "Введите корректный ID клиента.")
            return

        connection = self.connect_to_database()
        if connection:
            try:
                cursor = connection.cursor()
                query = "DELETE FROM persanal_data WHERE ID = %s"
                cursor.execute(query, (int(client_id),))
                connection.commit()

                if cursor.rowcount > 0:
                    messagebox.showinfo("Успех", f"Клиент с ID {client_id} успешно удален.")
                    print(f"Клиент с ID {client_id} успешно удален.")
                else:
                    messagebox.showwarning("Предупреждение", f"Клиент с ID {client_id} не найден.")
                    print(f"Клиент с ID {client_id} не найден.")

            except Error as e:
                messagebox.showerror("Ошибка", f"Ошибка при удалении данных: {e}")
                print(f"Ошибка при удалении данных: {e}")
            finally:
                cursor.close()
                connection.close()
if __name__ == "__main__":
    root = tk.Tk()
    app = DatabaseApp(root)
    root.mainloop()
