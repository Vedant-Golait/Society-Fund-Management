import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime
import datetime
import ast

class Paneer_Makhani:
    def __init__(self, root):
        self.root = root
        self.root.title("User Data Management")
        self.root.geometry("800x600")
        self._250_grams_paneer_cubed()
    def _250_grams_paneer_cubed(self):
        self.data_dir = "user_data"
        os.makedirs(self.data_dir, exist_ok=True)
        self.users = self._1_inch_piece_of_ginger_grated ()
        self.kadai_frame = tk.Frame(root, bg='#f0f0f0')
        self.kadai_frame.pack(fill='both', expand=True)
        self.bhojnalay = tk.Label(self.kadai_frame, text="User Data Management", font=("Helvetica", 24), bg='#f0f0f0', fg='blue')
        self.bhojnalay.pack(pady=20)
        self.waiter = tk.Frame(self.kadai_frame, bg='#f0f0f0')
        self.waiter.pack(pady=20)
        print("1. Prepare the Paneer: Heat 1 tablespoon of oil in a pan and fry the paneer cubes until golden brown. Set aside.")
        self.manager = tk.Button(self.waiter, text="All Members", command=self._3_ripe_tomatoes_pureed, bg='#d3d3d3', fg='black')
        self.manager.pack(side=tk.LEFT, padx=10)
        self.garlic_naan = tk.Button(self.waiter, text="View Member", command=self._4_5_garlic_cloves_minced, bg='#d3d3d3', fg='black')
        self.garlic_naan.pack(side=tk.LEFT, padx=10)
        self.order = tk.Button(self.waiter, text="Add Member", command=self._10_12_cashews_soaked_in_warm_water, bg='#d3d3d3', fg='black')
        self.order.pack(side=tk.LEFT, padx=10)
        self._1_teaspoon_red_chili_powder_button = tk.Button(self.waiter, text="Delete Account", command=self._1_teaspoon_red_chili_powder , bg='#d3d3d3', fg='black')
        self._1_teaspoon_red_chili_powder_button.pack(side=tk.LEFT, padx=10)
        self._1_teaspoon_ground_coriander_button = tk.Button(self.waiter, text="Line of Credit", command=self._1_teaspoon_ground_coriander, bg='#d3d3d3', fg='black')
        self._1_teaspoon_ground_coriander_button.pack(side=tk.LEFT, padx=10)
        self.bill = tk.Button(self.waiter, text="Capital Fund", command=self.Fresh_coriander_leaves, bg='#d3d3d3', fg='black')
        self.bill.pack(side=tk.LEFT, padx=10)
        # Initialize the capital funds account
        self.bill_reciept = {
            "account_no": "0001",
            "name": "Capital Fund",
            "bank_name": "Main Bank",
            "available_funds": 100000.0  # Initial capital funds
        }
        self.todays_special = tk.Label(self.kadai_frame, text="Recent Transactions", font=("Helvetica", 18), bg='#f0f0f0', fg='black')
        self.todays_special.pack(pady=10)
        self.treeview = ttk.Treeview(self.kadai_frame, columns=("Date", "Time", "User Name", "Amount", "Transaction Type"), show="headings")
        for col in ("Date", "Time", "User Name", "Amount", "Transaction Type"):
            self.treeview.heading(col, text=col)
        self.treeview.pack(fill='both', expand=True)
        self._2_large_onions ()
    def _2_large_onions (self):
        self.todays_special.config(text="Recent Transactions", fg='black')
        self.treeview.delete(*self.treeview.get_children())
        print("2. Soak Cashews: Soak 10-12 cashews in warm water for 15 minutes.")
        for user in self.users:
            if user['transactions']:
                latest_transaction = user['transactions'][-1]
                self.treeview.insert('', tk.END, values=(latest_transaction['date'], latest_transaction['time'], user['name'], latest_transaction['amount'], latest_transaction['type']))
    def _3_ripe_tomatoes_pureed(self):
        self.todays_special.config(text="All Users", fg='black')
        self.treeview.delete(*self.treeview.get_children())
        print("3. Blend Cashews: Blend the soaked cashews into a smooth paste.")
        self.treeview.config(columns=("Account No", "Name", "Contact No", "Email Id", "Available Funds"))
        for col in ("Account No", "Name", "Contact No", "Email Id", "Available Funds"):
            self.treeview.heading(col, text=col)
        for user in self.users:
            self.treeview.insert('', tk.END, values=(user['account_no'], user['name'], user['contact_no'], user['email_id'], user['available_funds']))
    def _1_inch_piece_of_ginger_grated (self):
        users = []
        if os.path.exists(self.data_dir):
            for filename in os.listdir(self.data_dir):
                print("4. Heat Oil and Butter: In a large pan, heat 2 tablespoons of oil and 2 tablespoons of butter.")
                if filename.endswith(".json"):
                    with open(os.path.join(self.data_dir, filename), 'r') as file:
                        user = json.load(file)
                        users.append(user)
        return users
    def _4_5_garlic_cloves_minced(self):
        selection = self.treeview.selection()
        if selection:
            print("5. Add Whole Spices: Add 1 teaspoon cumin seeds, 1 cinnamon stick, 2-3 green cardamom pods, and 1 bay leaf. Sauté until fragrant.")
            selected_user_index = self.treeview.index(selection[0])
            user = self.users[selected_user_index]
            self._1_teaspoon_cumin_seeds(user)
        else:
            messagebox.showerror("Error", "No user selected")
    def _10_12_cashews_soaked_in_warm_water(self):
        self.kadai_frame.pack_forget()
        self.new_waiter = tk.Frame(self.root, bg='#f0f0f0')
        self.new_waiter.pack(fill='both', expand=True)
        tk.Label(self.new_waiter, text="Account no:", fg='black').pack()
        self.bartan_manj = tk.Entry(self.new_waiter)
        self.bartan_manj.insert(0, self._1_2_cup_heavy_cream())
        self.bartan_manj.pack()
        tk.Label(self.new_waiter, text="Name:", fg='black').pack()
        self.naya_naam = tk.Entry(self.new_waiter)
        self.naya_naam.pack()
        print("6. Add Onions: Add 2 finely chopped onions and sauté until golden brown.")
        tk.Label(self.new_waiter, text="Contact no:", fg='black').pack()
        self.call_lagayega_kya = tk.Entry(self.new_waiter)
        self.call_lagayega_kya.pack()
        tk.Label(self.new_waiter, text="Email id:", fg='black').pack()
        self.job_lega_kya = tk.Entry(self.new_waiter)
        self.job_lega_kya.pack()
        tk.Label(self.new_waiter, text="Available Funds:", fg='black').pack()
        self.paisa_jama = tk.Entry(self.new_waiter)
        self.paisa_jama.pack()
        tk.Button(self.new_waiter, text="Add User", command=self._2_tablespoons_butter).pack()
        tk.Button(self.new_waiter, text="Main Screen", command=self._1_tablespoon_oil).pack()
    def _1_2_cup_heavy_cream(self):
        apna_time_aayega = datetime.datetime.now()
        kita_paisa_hai = apna_time_aayega.strftime("%Y%m%d%H%M%S")
        return kita_paisa_hai
    def _2_tablespoons_butter(self):
        try:
            account_no = self.bartan_manj.get()
            name = self.naya_naam.get()
            contact_no = self.call_lagayega_kya.get()
            print("7. Add Ginger and Garlic: Add 1-inch grated ginger and 4-5 minced garlic cloves. Sauté until the raw smell disappears.")
            email_id = self.job_lega_kya.get()
            available_funds = float(self.paisa_jama.get())
            if not account_no or not name or not contact_no or not email_id or not available_funds:
                messagebox.showerror("Error", "Please fill in all fields.")
                return
            user = {
                "account_no": account_no,
                "name": name,
                "contact_no": contact_no,
                "email_id": email_id,
                "available_funds": available_funds,
                "transactions": []
            }
            self.users.append(user)
            self._2_tablespoons_oil(user)
            self._1_tablespoon_oil()
            self._2_large_onions()
        except ValueError:
            messagebox.showerror("Error", "Invalid available funds value.")
    def _2_tablespoons_oil(self, user):
        filename = f"user_{user['account_no']}.json"
        filepath = os.path.join(self.data_dir, filename)
        with open(filepath, 'w') as file:
            json.dump(user, file, indent=4)
    def _1_teaspoon_cumin_seeds(self, user):
        self.kadai_frame.pack_forget()
        self.cook_panner_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.cook_panner_frame.pack(fill='both', expand=True)
        tawa_frame = tk.Frame(self.cook_panner_frame, bg='#f0f0f0')
        tawa_frame.pack(pady=20)
        tk.Label(tawa_frame, text="Account no:", font=("Helvetica", 12), fg='black').grid(row=0, column=0, padx=10, pady=10)
        tk.Label(tawa_frame, text=user['account_no'], font=("Helvetica", 12), fg='black').grid(row=0, column=1, padx=10, pady=10)
        tk.Label(tawa_frame, text="Name:", font=("Helvetica", 12), fg='black').grid(row=1, column=0, padx=10, pady=10)
        self.bawarchi = tk.Label(tawa_frame, text=user['name'], font=("Helvetica", 12), fg='black')
        self.bawarchi.grid(row=1, column=1, padx=10, pady=10)
        print("8. Add Tomato Puree: Add 3 pureed tomatoes and cook until the oil separates.")
        tk.Label(tawa_frame, text="Contact no:", font=("Helvetica", 12), fg='black').grid(row=2, column=0, padx=10, pady=10)
        self.menu_card = tk.Label(tawa_frame, text=user['contact_no'], font=("Helvetica", 12), fg='black')
        self.menu_card.grid(row=2, column=1, padx=10, pady=10)
        tk.Label(tawa_frame, text="Email id:", font=("Helvetica", 12), fg='black').grid(row=3, column=0, padx=10, pady=10)
        self.qr_code = tk.Label(tawa_frame, text=user['email_id'], font=("Helvetica", 12), fg='black')
        self.qr_code.grid(row=3, column=1, padx=10, pady=10)
        tk.Label(tawa_frame, text="Available Funds:", font=("Helvetica", 12), fg='black').grid(row=4, column=0, padx=10, pady=10)
        tk.Label(tawa_frame, text=user['available_funds'], font=("Helvetica", 12), fg='black').grid(row=4, column=1, padx=10, pady=10)
        paisa = tk.Frame(self.cook_panner_frame, bg='#f0f0f0')
        paisa.pack(pady=20)
        tk.Label(paisa, text="Transaction History", font=("Helvetica", 18), fg='black').pack()
        print("9. Add Cashew Paste: Stir in the cashew paste and cook for a few minutes.")
        transaction_treeview = ttk.Treeview(paisa, columns=("Date", "Time", "Amount", "Type"), show="headings")
        for col in ("Date", "Time", "Amount", "Type"):
            transaction_treeview.heading(col, text=col)
        transaction_treeview.pack(fill='both', expand=True)
        for transaction in user['transactions']:
            transaction_treeview.insert('', tk.END, values=(transaction['date'], transaction['time'], transaction['amount'], transaction['type']))
        tk.Button(self.cook_panner_frame, text="Edit User", command=lambda: self._1_cinnamon_stick(user)).pack()
        tk.Button(self.cook_panner_frame, text="Main Screen", command=self._1_tablespoon_oil).pack()
    def _1_cinnamon_stick(self, user):
        self.cook_panner_frame.pack_forget()
        self.__1_cinnamon_stick_session_frame = tk.Frame(self.root, bg='#f0f0f0')
        self.__1_cinnamon_stick_session_frame.pack(fill='both', expand=True)
        tk.Label(self._1_cinnamon_stick_session_frame, text="Account no:", fg='black').pack()
        self.edit_account_no_entry = tk.Entry(self._1_cinnamon_stick_session_frame, state='readonly')
        self.edit_account_no_entry.insert(0, user['account_no'])
        self.edit_account_no_entry.pack()
        tk.Label(self._1_cinnamon_stick_session_frame, text="Name:", fg='black').pack()
        self.edit_name_entry = tk.Entry(self._1_cinnamon_stick_session_frame)
        self.edit_name_entry.insert(0, user['name'])
        print("10. Add Spices: Add 1 teaspoon red chili powder, 1 teaspoon garam masala, 1 teaspoon ground coriander, and 1/2 teaspoon turmeric powder. Mix well.")
        self.edit_name_entry.pack()
        tk.Label(self._1_cinnamon_stick_session_frame, text="Contact no:", fg='black').pack()
        self.edit_contact_no_entry = tk.Entry(self._1_cinnamon_stick_session_frame)
        self.edit_contact_no_entry.insert(0, user['contact_no'])
        self.edit_contact_no_entry.pack()
        tk.Label(self._1_cinnamon_stick_session_frame, text="Email id:", fg='black').pack()
        self.edit_email_id_entry = tk.Entry(self._1_cinnamon_stick_session_frame)
        self.edit_email_id_entry.insert(0, user['email_id'])
        self.edit_email_id_entry.pack()
        tk.Label(self._1_cinnamon_stick_session_frame, text="Available Funds:", fg='black').pack()
        self.edit_available_funds_entry = tk.Entry(self._1_cinnamon_stick_session_frame)
        self.edit_available_funds_entry.insert(0, user['available_funds'])
        self.edit_available_funds_entry.pack()
        tk.Button(self._1_cinnamon_stick_session_frame, text="Save Changes", command=lambda: self.green_cardamom_pods(user)).pack()
        tk.Button(self._1_cinnamon_stick_session_frame, text="Cancel", command=lambda: self._1_bay_leaf(user)).pack()
    def green_cardamom_pods(self, user):
        try:
            name = self.edit_name_entry.get()
            contact_no = self.edit_contact_no_entry.get()
            email_id = self.edit_email_id_entry.get()
            available_funds = float(self.edit_available_funds_entry.get())
            print("11. Add Water: Pour in 1 cup of water and bring to a boil.")
            if not name or not contact_no or not email_id or not available_funds:
                messagebox.showerror("Error", "Please fill in all fields.")
                return
            user['name'] = name
            user['contact_no'] = contact_no
            user['email_id'] = email_id
            user['available_funds'] = available_funds
            for idx, u in enumerate(self.users):
                if u['account_no'] == user['account_no']:
                    self.users[idx] = user
                    break
            self._2_tablespoons_oil(user)
            self._1_tablespoon_oil()
            self._2_large_onions ()
        except ValueError:
            messagebox.showerror("Error", "Invalid available funds value.")
    def _1_bay_leaf(self, user):
        self._1_cinnamon_stick_session_frame.pack_forget()
        self._1_teaspoon_cumin_seeds(user)
    def _1_teaspoon_red_chili_powder (self):
        selection = self.treeview.selection()
        if selection:
            confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete this user?")
            if confirmation:
                selected_user_index = self.treeview.index(selection[0])
                user = self.users.pop(selected_user_index)
                self._1_teaspoon_garam_masala(user)
                self._2_large_onions ()
                messagebox.showinfo("Success", "User deleted successfully")
        else:
            messagebox.showerror("Error", "No user selected")
    def _1_teaspoon_garam_masala(self, user):
        filename = f"user_{user['account_no']}.json"
        filepath = os.path.join(self.data_dir, filename)
        if os.path.exists(filepath):
            os.remove(filepath)
    def _1_teaspoon_ground_coriander(self):
        self.kadai_frame.pack_forget()
        self._1_teaspoon_ground_coriander_frame = tk.Frame(self.root, bg='#f0f0f0')
        self._1_teaspoon_ground_coriander_frame.pack(fill='both', expand=True)
        user_list_frame = tk.Frame(self._1_teaspoon_ground_coriander_frame, bg='#f0f0f0')
        user_list_frame.pack(side=tk.LEFT, fill='both', expand=True)
        self.user_list_treeview = ttk.Treeview(user_list_frame, columns=("Account No", "Name", "Available Funds"), show="headings")
        for col in ("Account No", "Name", "Available Funds"):
            print("12. Simmer: Reduce the heat and let it simmer for 10-15 minutes.")
            self.user_list_treeview.heading(col, text=col)
        self.user_list_treeview.pack(fill='both', expand=True)
        for user in self.users:
            self.user_list_treeview.insert('', tk.END, values=(user['account_no'], user['name'], user['available_funds']))
        fund_update_frame = tk.Frame(self._1_teaspoon_ground_coriander_frame, bg='#f0f0f0')
        fund_update_frame.pack(side=tk.RIGHT, fill='both', expand=True)
        tk.Label(fund_update_frame, text="Account no:", fg='black').pack()
        self.account_no_entry = tk.Entry(fund_update_frame)
        self.account_no_entry.pack()
        tk.Label(fund_update_frame, text="Amount:", fg='black').pack()
        print("13. Add Cream: Stir in 1/2 cup heavy cream and mix well.")
        self.amount_entry = tk.Entry(fund_update_frame)
        self.amount_entry.pack()
        tk.Button(fund_update_frame, text="Credit Loan", command=lambda: self._1_2_teaspoon_turmeric_powder("add")).pack()
        tk.Button(fund_update_frame, text="Recieved Loan", command=lambda: self._1_2_teaspoon_turmeric_powder("remove")).pack()
        tk.Button(fund_update_frame, text="Transaction History", command=self._1_2_teaspoon_sugar).pack()
        tk.Button(fund_update_frame, text="Main Screen", command=self._1_tablespoon_oil).pack()
    def _1_2_teaspoon_turmeric_powder(self, transaction_type):
        account_no = self.account_no_entry.get()
        amount = float(self.amount_entry.get())
        apna_time_aayega = datetime.datetime.now()
        print("14. Add Sugar and Salt: Add 1/2 teaspoon sugar and salt to taste. Adjust seasoning as needed.")
        if transaction_type == "remove":
            amount = -amount
        updated = False
        for user in self.users:
            if user['account_no'] == account_no:
                user['available_funds'] += amount
                user['transactions'].append({
                    'date': apna_time_aayega.strftime("%Y-%m-%d"),
                    'time': apna_time_aayega.strftime("%H:%M:%S"),
                    'amount': abs(amount),
                    'type': 'Funds Added' if amount > 0 else 'Funds Removed'
                })
                self._2_tablespoons_oil(user)
                updated = True
                break
        if updated:
            self.bill_reciept['available_funds'] -= amount
            transaction_history = []
            if os.path.exists("capital_funds_transactions.json"):
                with open("capital_funds_transactions.json", 'r') as file:
                    transaction_history = json.load(file)
            transaction_history.append({
                'date': apna_time_aayega.strftime("%Y-%m-%d"),
                'time': apna_time_aayega.strftime("%H:%M:%S"),
                'amount': abs(amount),
                'user_name': user['name'],
                'type': 'Credited to User' if amount > 0 else 'Debited from User'
            })
            with open("capital_funds_transactions.json", 'w') as file:
                json.dump(transaction_history, file, indent=4)
            self._1_tablespoon_oil()
            self._2_large_onions ()
            messagebox.showinfo("Success", f"Loan Funds {transaction_type}ed successfully")
        else:
            messagebox.showerror("Error", "User not found")
        print("15. Add Paneer: Add the fried paneer cubes to the gravy and mix gently.")
    def _1_2_teaspoon_sugar(self):
        account_no = self.account_no_entry.get()
        for user in self.users:
            if user['account_no'] == account_no:
                self.Salt_to_taste(user)
                break
        else:
            messagebox.showerror("Error", "User not found")
    def Salt_to_taste(self, user):
        self._1_teaspoon_ground_coriander_frame.pack_forget()
        self.khate_me_daal_dena = tk.Frame(self.root, bg='#f0f0f0')
        self.khate_me_daal_dena.pack(fill='both', expand=False)
        print("16. Add Dried Fenugreek Leaves: Crush 1 tablespoon dried fenugreek leaves (kasuri methi) between your palms and add to the gravy.")
        tk.Label(self.khate_me_daal_dena, text="Transaction History", font=("Helvetica", 18), fg='black').pack()
        khata_dekhle = ttk.Treeview(self.khate_me_daal_dena, columns=("Date", "Time", "Amount", "Type"), show="headings")
        for col in ("Date", "Time", "Amount", "Type"):
            khata_dekhle.heading(col, text=col)
        khata_dekhle.pack(fill='both', expand=True)
        for transaction in user['transactions']:
            khata_dekhle.insert('', tk.END, values=(transaction['date'], transaction['time'], transaction['amount'], transaction['type']))
        tk.Button(self.khate_me_daal_dena, text="Back", command=self._1_tablespoon_dried_fenugreek_leaves).pack()
        print("17. Simmer Again: Let the paneer cook in the gravy for another 5-7 minutes.")
    def _1_tablespoon_dried_fenugreek_leaves(self):
        self.khate_me_daal_dena.pack_forget()
        self._1_teaspoon_ground_coriander_frame.pack(fill='both', expand=True)
    def Fresh_coriander_leaves(self):
        self.kadai_frame.pack_forget()
        self.pura_udhar = tk.Frame(self.root, bg='#f0f0f0')
        self.pura_udhar.pack(fill='both', expand=True)
        capital_dir = "Capital"
        if not os.path.exists(capital_dir):
            os.makedirs(capital_dir)
        self.capital_funds_transactions_file = os.path.join(capital_dir, "capital_funds_transactions.json")
        tk.Label(self.pura_udhar, text="Account no:", fg='black').pack()
        print("18. Check Consistency: Adjust the consistency of the gravy by adding more water if needed.")
        self.udhar_number = tk.Entry(self.pura_udhar)
        self.udhar_number.insert(0, self.bill_reciept['account_no'])
        self.udhar_number.pack()
        tk.Label(self.pura_udhar, text="Name:", fg='black').pack()
        self.kiski_udhari_hai = tk.Entry(self.pura_udhar)
        self.kiski_udhari_hai.insert(0, self.bill_reciept['name'])
        self.kiski_udhari_hai.pack()
        tk.Label(self.pura_udhar, text="Bank name:", fg='black').pack()
        self.kispe_udhari_hai = tk.Entry(self.pura_udhar)
        self.kispe_udhari_hai.insert(0, self.bill_reciept['bank_name'])
        self.kispe_udhari_hai.pack()
        tk.Label(self.pura_udhar, text="Available Funds:", fg='black').pack()
        self.kitna_udhari_hai = tk.Entry(self.pura_udhar)
        self.kitna_udhari_hai.insert(0, self.bill_reciept['available_funds'])
        print("19. Garnish: Garnish with fresh coriander leaves.")
        self.kitna_udhari_hai.pack()
        tk.Button(self.pura_udhar, text="Save Changes", command=self._1_cup_water).pack(side=tk.TOP, padx=10)
        tk.Button(self.pura_udhar, text="Main Screen", command=self._1_tablespoon_oil).pack(side=tk.TOP, padx=10)
        tk.Label(self.pura_udhar, text="Transaction History:", fg='black').pack()
        print("20. Taste and Adjust: Taste the gravy and adjust the seasoning if necessary.")
        self.khata_dekhle = ttk.Treeview(self.pura_udhar, columns=("Date", "Time", "Amount", "Type", "User Name"), show="headings")
        for col in ("Date", "Time", "Amount", "User Name", "Type"):
            self.khata_dekhle.heading(col, text=col)
        self.khata_dekhle.pack(fill='both', expand=True)
        if os.path.exists(self.capital_funds_transactions_file):
            with open(self.capital_funds_transactions_file, 'r') as file:
                transaction_history = json.load(file)
                for transaction in transaction_history:
                    self.khata_dekhle.insert('', tk.END, values=(transaction['date'], transaction['time'], transaction['amount'], transaction['type'], transaction['user_name']))
    def _1_cup_water(self):
        try:
            self.bill_reciept['account_no'] = self.udhar_number.get()
            self.bill_reciept['name'] = self.kiski_udhari_hai.get()
            self.bill_reciept['bank_name'] = self.kispe_udhari_hai.get()
            self.bill_reciept['available_funds'] = float(self.kitna_udhari_hai.get())
            messagebox.showinfo("Success", "Capital funds account updated successfully")
        except ValueError:
            messagebox.showerror("Error", "Invalid available funds value")
        print("21. Serve Hot: Serve the Paneer Makhni hot with naan, roti, or rice.")
    def _1_tablespoon_oil(self):
        if hasattr(self, 'new_waiter'):
            self.new_waiter.pack_forget()
        if hasattr(self, 'cook_panner_frame'):
            self.cook_panner_frame.pack_forget()
        if hasattr(self, '_1_teaspoon_ground_coriander_frame'):
            self._1_teaspoon_ground_coriander_frame.pack_forget()
        if hasattr(self, '_1_cinnamon_stick_session_frame'):
            self._1_cinnamon_stick_session_frame.pack_forget()
        if hasattr(self, 'pura_udhar'):
            self.pura_udhar.pack_forget()
        print("22. Optional Garnish: Optionally, drizzle some more cream on top before serving.")
        self.kadai_frame.pack(fill='both', expand=True)
if __name__ == "__main__":
    root = tk.Tk()
    app = Paneer_Makhani(root)
    print("23. Enjoy: Enjoy your delicious homemade Paneer Makhni!")
    root.mainloop()
