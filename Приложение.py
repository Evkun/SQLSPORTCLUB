import tkinter as tk
from tkinter import messagebox, ttk
import mysql.connector

# Функция для получения ФИО клиентов по ID зала
def get_clients_fio():
    client_id = entry_id.get()
    
    try:
        # Подключаемся к базе данных MySQL
        connection = mysql.connector.connect(
            host='127.0.0.1',  # или IP-адрес вашего сервера
            user='root',  # ваше имя пользователя
            password='7895123evg',  # ваш пароль
            database='gymsport'  # имя вашей базы данных
        )
        cursor = connection.cursor()
        
        # Выполняем запрос для получения ФИО клиентов по ID зала
        cursor.execute("""
            SELECT c.Name, c.SurName, c.Otchestvo
            FROM persanal_data c
            INNER JOIN Sport h ON c.ID_ZAla = h.iD
            WHERE h.iD = %s
        """, (client_id,))
        
        results = cursor.fetchall()
        
        # Очищаем предыдущие данные из таблицы
        for row in tree.get_children():
            tree.delete(row)
        
        if results:
            # Заполняем таблицу новыми данными
            for result in results:
                tree.insert("", tk.END, values=result)
        else:
            messagebox.showerror("Ошибка", "Клиенты не найдены.")
        
    except mysql.connector.Error as e:
        messagebox.showerror("Ошибка", f"Ошибка базы данных: {e}")
    finally:
        if connection:
            connection.close()

# Создание основного окна
root = tk.Tk()
root.title("Поиск клиентов")

# Метка и поле ввода для ID зала
label_id = tk.Label(root, text="Введите ID зала:")
label_id.pack(pady=10)

entry_id = tk.Entry(root)
entry_id.pack(pady=10)

# Кнопка для поиска клиентов
button_search = tk.Button(root, text="Найти", command=get_clients_fio)
button_search.pack(pady=10)

# Создание таблицы для отображения результатов
columns = ("Имя", "Фамилия", "Отчество")
tree = ttk.Treeview(root, columns=columns, show='headings')
tree.heading("Имя", text="Имя")
tree.heading("Фамилия", text="Фамилия")
tree.heading("Отчество", text="Отчество")
tree.pack(pady=10)

# Установка ширины колонок
tree.column("Имя", width=100)
tree.column("Фамилия", width=100)
tree.column("Отчество", width=100)

# Запуск главного цикла приложения
root.mainloop()
