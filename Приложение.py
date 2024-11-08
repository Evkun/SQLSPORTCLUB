import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Функция для получения ФИО клиента по ID
def get_client_fio():
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
        
        # Выполняем запрос для получения ФИО клиента по ID
        cursor.execute("""
            SELECT c.Name, c.SurName, c.Otchestvo
            FROM persanal_data c
            INNER JOIN Sport h ON c.ID_ZAla = h.iD
            WHERE h.iD = %s
        """, (client_id,))
        
        result = cursor.fetchone()
        
        if result:
            full_name = f"{result[0]} {result[1]} {result[2]}"
            label_result.config(text=full_name)
        else:
            messagebox.showerror("Ошибка", "Клиент не найден.")
        
    except mysql.connector.Error as e:
        messagebox.showerror("Ошибка", f"Ошибка базы данных: {e}")
    finally:
        if connection:
            connection.close()

# Создание основного окна
root = tk.Tk()
root.title("Поиск клиента")

# Метка и поле ввода для ID клиента
label_id = tk.Label(root, text="Введите ID зала:")
label_id.pack(pady=10)

entry_id = tk.Entry(root)
entry_id.pack(pady=10)

# Кнопка для поиска клиента
button_search = tk.Button(root, text="Найти", command=get_client_fio)
button_search.pack(pady=10)

# Метка для вывода результата
label_result = tk.Label(root, text="")
label_result.pack(pady=10)

# Запуск главного цикла приложения
root.mainloop()
