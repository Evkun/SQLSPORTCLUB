import tkinter as tk
from tkinter import ttk
import mysql.connector

# Функция для получения ФИО клиентов по ID зала
def get_clients_fio():
    client_id = entry_id.get()
    
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='7895123evg',
            database='gymsport'
        )
        cursor = connection.cursor()
        
        cursor.execute("""
            SELECT c.Name, c.SurName, c.Otchestvo, c.ID
            FROM persanal_data c
            INNER JOIN Sport h ON c.ID_ZAla = h.iD
            WHERE h.iD = %s
        """, (client_id,))
        
        results = cursor.fetchall()
        
        # Очистка предыдущих результатов
        for widget in tree.get_children():
            tree.delete(widget)

        if results:
            for result in results:
                tree.insert("", tk.END, values=result)
        else:
            label_no_results.config(text="Клиенты не найдены.")
        
    except mysql.connector.Error as e:
        label_error.config(text=f"Ошибка базы данных: {e}")
    finally:
        if connection:
            connection.close()

# Функция для получения счета клиента по его ID
def get_client_balance():
    client_id = entry_client_id.get()
    label_balance.config(text="")
    label_balancen.config(text="")
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='7895123evg',
            database='gymsport'
        )
        cursor = connection.cursor()
        
        cursor.execute("""
            SELECT schet
            FROM persanal_data
            WHERE ID = %s
        """, (client_id,))
        
        result = cursor.fetchone()
        
        if result:
            label_balance.config(text=f"Счет клиента: {result[0]}")
        else:
            label_balancen.config(text="Клиент не найден.")
        
    except mysql.connector.Error as e:
        label_balancen.config(text=f"Ошибка базы данных: {e}")
    finally:
        if connection:
            connection.close()

# Функция для изменения счета клиента
def update_client_balance():
    client_id = entry_client_id_update.get()
    new_balance = entry_new_balance.get()
    label_update_status.config(text="")
    label_update_statusn.config(text="")
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='7895123evg',
            database='gymsport'
        )
        cursor = connection.cursor()
        
        cursor.execute("""
            UPDATE persanal_data
            SET schet = %s
            WHERE ID = %s
        """, (new_balance, client_id))
        
        connection.commit()
        
        if cursor.rowcount > 0:
            label_update_status.config(text="Счет успешно обновлен.")
        else:
            label_update_statusn.config(text="Клиент не найден.")
        
    except mysql.connector.Error as e:
        label_update_statusn.config(text=f"Ошибка базы данных: {e}")
    finally:
        if connection:
            connection.close()

# Функция для получения зала клиента по его ID
# def get_client_gym():
#     client_id = entry_client_id_gym.get()
#     label_gymn.config(text="")
#     label_gym.config(text="")
#     try:
#         connection = mysql.connector.connect(
#             host='127.0.0.1',
#             user='root',
#             password='7895123evg',
#             database='gymsport'
#         )
#         cursor = connection.cursor()
        
#         cursor.execute("""
#             SELECT h.Name
#             FROM Sport h
#             INNER JOIN persanal_data c ON c.ID_ZAla = h.ID
#             WHERE c.ID= %s
#         """, (client_id,))
        
#         result = cursor.fetchone()
        
#         if result:
#             label_gym.config(text=f"Клиент занимается в зале: {result[0]}")
#         else:
#             label_gymn.config(text="Клиент не найден.")
#     except mysql.connector.Error as e:
#         label_gymn.config(text=f"Ошибка базы данных: {e}")
#     finally:
#         if connection:
#             connection.close()

# Создание основного окна
root = tk.Tk()
root.title("SPORTCLUB")

# Создание фрейма для элементов управления
frame = tk.Frame(root, bg='white', padx=20, pady=20)
frame.pack(expand=True, fill=tk.BOTH)

# Заголовок приложения
title_label = tk.Label(frame, text="Информация о клиентах", font=("Arial", 16, "bold"), bg='white')
title_label.pack(pady=3)

# Метка и поле ввода для ID зала
label_id = tk.Label(frame, text="Введите ID зала:", bg='white', font=("Arial", 12))
label_id.pack(pady=3)

entry_id = tk.Entry(frame, font=("Arial", 12))
entry_id.pack(pady=3)

# Кнопка для поиска клиентов по ID зала
button_search = tk.Button(frame, text="Найти клиентов по ID зала", command=get_clients_fio, bg='#4CAF50', fg='white', font=("Arial", 12))
button_search.pack(pady=3)

# Таблица для отображения результатов
columns = ("Имя", "Фамилия", "Отчество","ID")
tree = ttk.Treeview(frame, columns=columns, show='headings', height=5)
tree.heading("Имя", text="Имя")
tree.heading("Фамилия", text="Фамилия")
tree.heading("Отчество", text="Отчество")
tree.heading("ID", text="ID")
tree.pack(pady=10)

# Установка ширины колонок
tree.column("Имя", width=100)
tree.column("Фамилия", width=100)
tree.column("Отчество", width=100)
tree.column("ID", width=30)

# Метка для отображения отсутствия результатов
label_no_results = tk.Label(frame, text="", bg='white', font=("Arial", 12),fg='red')
label_no_results.pack(pady=3)

# Метка и поле ввода для ID клиента (счет)
label_client_id = tk.Label(frame, text="Введите ID клиента для получения счета:", bg='white', font=("Arial", 12))
label_client_id.pack(pady=3)

entry_client_id = tk.Entry(frame, font=("Arial", 12))
entry_client_id.pack(pady=3)

# Кнопка для получения счета клиента
button_balance = tk.Button(frame, text="Получить счет клиента", command=get_client_balance, bg='#2196F3', fg='white', font=("Arial", 12))
button_balance.pack(pady=3)



# Метка для отображения счета клиента
label_balance = tk.Label(frame, text="", bg='white', font=("Arial", 12),fg='#2196F3')
label_balance.pack(pady=3)
label_balancen = tk.Label(frame, text="", bg='white', font=("Arial", 12),fg='red')
label_balancen.pack(pady=3)

# # Метка и поле ввода для ID клиента (зал)
# label_client_id_gym = tk.Label(frame, text="Введите ID клиента для получения зала:", bg='white', font=("Arial", 12))
# label_client_id_gym.pack(pady=5)

# entry_client_id_gym = tk.Entry(frame, font=("Arial", 12))
# entry_client_id_gym.pack(pady=5)

# # Кнопка для получения зала клиента
# button_gym = tk.Button(frame, text="Получить зал клиента", command=get_client_gym, bg='#FF9800', fg='white', font=("Arial", 12))
# button_gym.pack(pady=10)

# # Метка для отображения зала клиента
# label_gym = tk.Label(frame, text="", bg='white', font=("Arial", 12),fg='#FF9800')
# label_gymn = tk.Label(frame, text="", bg='white', font=("Arial", 12),fg='red')
# label_gym.pack(pady=1)
# label_gymn.pack(pady=1)

# Метка и поле ввода для изменения счета клиента
label_client_id_update = tk.Label(frame, text="Введите ID клиента для изменения счета:", bg='white', font=("Arial", 12))
label_client_id_update.pack(pady=3)

entry_client_id_update = tk.Entry(frame, font=("Arial", 12))
entry_client_id_update.pack(pady=3)

label_new_balance = tk.Label(frame, text="Введите новый счет:", bg='white', font=("Arial", 12))
label_new_balance.pack(pady=3)

entry_new_balance = tk.Entry(frame, font=("Arial", 12))
entry_new_balance.pack(pady=3)

# Кнопка для изменения счета клиента
button_update_balance = tk.Button(frame, text="Изменить счет клиента", command=update_client_balance, bg='#FF5722', fg='white', font=("Arial", 12))
button_update_balance.pack(pady=3)

# Метка для отображения статуса обновления счета

label_update_status = tk.Label(frame, text="", bg='white', font=("Arial", 12), fg='green')
label_update_status.pack(pady=3)
label_update_statusn = tk.Label(frame, text="", bg='white', font=("Arial", 12), fg='red')
label_update_statusn.pack(pady=3)

# Метка для отображения ошибок базы данных
label_error = tk.Label(frame, text="", bg='white', font=("Arial", 12), fg='red')
label_error.pack(pady=3)

# Запуск главного цикла приложения
root.mainloop()
