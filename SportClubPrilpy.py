import tkinter as tk
from tkinter import ttk
import mysql.connector
import subprocess
from tkinter import messagebox
def open_app2():
    subprocess.Popen(['python', 'C://Users//Евгений//Desktop//+Client.py'])

class GymApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gym Client Management")
        self.root.configure(bg="#f0f0f0")
        
        open_button = tk.Button(root, text="Добавить или удалить клиента", command=open_app2, bg="#4CAF50", fg="white")
        open_button.pack(pady=20)

        self.frame_search = tk.Frame(root, bg="#ffffff", bd=5, relief=tk.GROOVE)
        self.frame_search.pack(pady=10, padx=20)

        self.frame_balance = tk.Frame(root, bg="#ffffff", bd=5, relief=tk.GROOVE)
        self.frame_balance.pack(pady=10, padx=20)

        self.frame_update = tk.Frame(root, bg="#ffffff", bd=5, relief=tk.GROOVE)
        self.frame_update.pack(pady=10, padx=20)
        
        self.frame_spisanie = tk.Frame(root, bg="#ffffff", bd=5, relief=tk.GROOVE)
        self.frame_spisanie.pack(pady=10, padx=20)

        tk.Label(self.frame_search, text="ID зала:", bg="#ffffff").grid(row=0, column=0)
        self.entry_id = tk.Entry(self.frame_search)
        self.entry_id.grid(row=0, column=1)

        self.button_search = tk.Button(self.frame_search, text="Поиск клиентов", command=self.get_clients_fio, bg="#2196F3", fg="white")
        self.button_search.grid(row=0, column=2)

        self.tree = ttk.Treeview(root, columns=("Name", "SurName", "Otchestvo", "ID"), show='headings')
        self.tree.heading("Name", text="Имя")
        self.tree.heading("SurName", text="Фамилия")
        self.tree.heading("Otchestvo", text="Отчество")
        self.tree.heading("ID", text="ID")
        self.tree.pack(pady=10)

        self.label_no_results = tk.Label(root, text="", bg="#f0f0f0")
        self.label_no_results.pack()

        tk.Label(self.frame_balance, text="ID клиента:", bg="#ffffff").grid(row=0, column=0)
        self.entry_client_id = tk.Entry(self.frame_balance)
        self.entry_client_id.grid(row=0, column=1)

        self.button_balance = tk.Button(self.frame_balance, text="Получить счет", command=self.get_client_balance, bg="#2196F3", fg="white")
        self.button_balance.grid(row=0, column=2)

        self.label_balance = tk.Label(self.frame_balance, text="", bg="#ffffff")
        self.label_balance.grid(row=1, columnspan=3)

        tk.Label(self.frame_update, text="ID клиента:", bg="#ffffff").grid(row=0, column=0)
        self.entry_client_id_update = tk.Entry(self.frame_update)
        self.entry_client_id_update.grid(row=0, column=1)

        tk.Label(self.frame_update, text="Новый баланс:", bg="#ffffff").grid(row=1, column=0)
        self.entry_new_balance = tk.Entry(self.frame_update)
        self.entry_new_balance.grid(row=1, column=1)

        self.button_update = tk.Button(self.frame_update, text="Обновить счет", command=self.update_client_balance, bg="#4CAF50", fg="white")
        self.button_update.grid(row=2, columnspan=2)

        self.label_update_status = tk.Label(self.frame_update, text="", bg="#ffffff")
        self.label_update_status.grid(row=3, columnspan=2)
        
        tk.Label(self.frame_spisanie, text="ID клиента:", bg="#ffffff").grid(row=0, column=0)
        self.entry_frame_spisanie = tk.Entry(self.frame_spisanie)
        self.entry_frame_spisanie.grid(row=0, column=1)
        self.button1 = tk.Button(self.frame_spisanie, text="Покупка одного занятия", command=self.Spisanie1,bg="#4CAF50", fg="white")
        self.button1.grid (row=1, column=1)  
        self.button2 = tk.Button(self.frame_spisanie, text="Покупка абонемента на месяц", command=self.Spisanie2,bg="#B8860B", fg="white")
        self.button2.grid (row=1, column=2)
        self.button3 = tk.Button(self.frame_spisanie, text="Покупка абонемента на год", command=self.Spisanie3,bg="Red", fg="white")
        self.button3.grid (row=1, column=3)
        self.label_spisanie_status= tk.Label(self.frame_spisanie, text="", bg="#ffffff")
        self.label_spisanie_status.grid(row=3, columnspan=2)
    def Spisanie1(self):
        client_id=self.entry_frame_spisanie.get()
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
            SET schet = 
                
                CASE 
                    WHEN ID_ZAla =1 THEN schet-1500
                    WHEN ID_ZAla =2 THEN schet-1000
                    WHEN ID_ZAla =3 THEN schet-500
                    WHEN ID_ZAla =4 THEN schet-800
                    ELSE schet
                END
            WHERE ID = %s
            """, ([client_id]))
            connection.commit()
            
            if cursor.rowcount > 0:
                self.label_spisanie_status.config(text="Счет успешно обновлен.")
            else:
                self.label_spisanie_status.config(text="Клиент не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        except mysql.connector.Error as e:
            self.label_no_results.config(text=f"Ошибка базы данных: {e}")
        
        finally:
            if connection:
                connection.close()
        
    def Spisanie2(self):
        client_id=self.entry_frame_spisanie.get()
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
            SET schet = 
                
                CASE 
                    WHEN ID_ZAla =1 THEN schet-10000
                    WHEN ID_ZAla =2 THEN schet-8000
                    WHEN ID_ZAla =3 THEN schet-3500
                    WHEN ID_ZAla =4 THEN schet-6500
                    ELSE schet
                END
            WHERE ID = %s
            """, ([client_id]))
            connection.commit()
            
            if cursor.rowcount > 0:
                self.label_spisanie_status.config(text="Счет успешно обновлен.")
            else:
                self.label_spisanie_status.config(text="Клиент не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        except mysql.connector.Error as e:
            self.label_no_results.config(text=f"Ошибка базы данных: {e}")
        
        finally:
            if connection:
                connection.close()
        

    def Spisanie3(self):
        client_id=self.entry_frame_spisanie.get()
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
            SET schet = 
                
                CASE 
                    WHEN ID_ZAla =1 THEN schet-21000
                    WHEN ID_ZAla =2 THEN schet-16000
                    WHEN ID_ZAla =3 THEN schet-10000
                    WHEN ID_ZAla =4 THEN schet-14000
                    ELSE schet
                END
            WHERE ID = %s
            """, ([client_id]))
            connection.commit()
            
            if cursor.rowcount > 0:
                self.label_spisanie_status.config(text="Счет успешно обновлен.")
            else:
                self.label_spisanie_status.config(text="Клиент не найден.")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
        except mysql.connector.Error as e:
            self.label_no_results.config(text=f"Ошибка базы данных: {e}")
        
        finally:
            if connection:
                connection.close()
             
    
    
       

    def get_clients_fio(self):
        client_id = self.entry_id.get()
        
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
            """, ([client_id]))
            
            results = cursor.fetchall()
            
            # Очистка предыдущих результатов
            for widget in self.tree.get_children():
                self.tree.delete(widget)

            if results:
                for result in results:
                    self.tree.insert("", tk.END, values=result)
            else:
                self.label_no_results.config(text="Клиенты не найдены.")
            
            # Анимация появления результатов
            self.animate_treeview()

        except mysql.connector.Error as e:
            self.label_no_results.config(text=f"Ошибка базы данных: {e}")
        
        finally:
            if connection:
                connection.close()

    def animate_treeview(self):
        # Простая анимация для выделения новых данных
        for item in self.tree.get_children():
            self.tree.item(item, tags=('highlight',))
        
        self.tree.tag_configure('highlight', background='yellow')
        
        # Убираем подсветку через 2 секунды
        self.root.after(2000, lambda: [self.tree.item(item, tags='') for item in self.tree.get_children()])

    def get_client_balance(self):
        client_id = self.entry_client_id.get()
        
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
                self.label_balance.config(text=f"Счет клиента: {result[0]}")
            else:
                self.label_balance.config(text="Клиент не найден.")
        
        except mysql.connector.Error as e:
            self.label_balance.config(text=f"Ошибка базы данных: {e}")
        
        finally:
            if connection:
                connection.close()

    def update_client_balance(self):
        client_id = self.entry_client_id_update.get()
        new_balance = self.entry_new_balance.get()
        
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
                self.label_update_status.config(text="Счет успешно обновлен.")
            else:
                self.label_update_status.config(text="Клиент не найден.")
        
        except mysql.connector.Error as e:
            self.label_update_status.config(text=f"Ошибка базы данных: {e}")
        
        finally:
            if connection:
                connection.close()
        

if __name__ == "__main__":
    root = tk.Tk()
    app = GymApp(root)
    root.mainloop()

    
    
    
