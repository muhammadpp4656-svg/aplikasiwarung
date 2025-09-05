import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from kivy.lang import Builder
from kivy.clock import Clock
from datetime import datetime

from database import Database

# Muat file KV
kv_file = Builder.load_file('finance_app.kv')

class FinanceApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db = Database()

    def build(self):
        return kv_file

    def on_start(self):
        self.update_dashboard()
        self.update_debt_list()
    
    def on_pause(self):
        return True

    def update_dashboard(self):
        transactions = self.db.get_all_transactions()
        total_income = 0
        total_expense = 0
        for transaction in transactions:
            if transaction[1] == 'Pemasukan':
                total_income += transaction[2]
            else:
                total_expense += transaction[2]
        
        balance = total_income - total_expense
        
        self.root.ids.total_income_label.text = f'Total Pemasukan: Rp.{total_income:,.0f}'
        self.root.ids.total_expense_label.text = f'Total Pengeluaran: Rp.{total_expense:,.0f}'
        self.root.ids.balance_label.text = f'Saldo: Rp.{balance:,.0f}'

    def update_debt_list(self):
        debt_list_widget = self.root.ids.debt_list
        debt_list_widget.clear_widgets()
        
        debts = self.db.get_all_debts()
        for debt in debts:
            row = BoxLayout(size_hint_y=None, height=80, padding=[10, 0, 10, 0])
            row.id = str(debt[0])
            row.add_widget(Label(text=f'{debt[1]}\n[color=808080]{debt[4]}[/color]', markup=True, halign='left', size_hint_x=0.5))
            row.add_widget(Label(text=f'Rp.{debt[2]:,.0f}', halign='right', size_hint_x=0.3))
            btn = Button(text='Lunas', size_hint_x=0.2)
            btn.bind(on_release=lambda x, d_id=debt[0]: self.mark_debt_paid(d_id))
            row.add_widget(btn)
            debt_list_widget.add_widget(row)

    def add_transaction(self):
        trans_type = self.root.ids.transaction_type_spinner.text
        amount_text = self.root.ids.amount_input.text
        desc = self.root.ids.desc_input.text
        
        if trans_type != 'Pilih' and amount_text.isdigit():
            amount = float(amount_text)
            date_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.db.add_transaction(trans_type, amount, desc, date_str)
            
            self.root.ids.amount_input.text = ''
            self.root.ids.desc_input.text = ''
            self.root.ids.transaction_type_spinner.text = 'Pilih'
            self.update_dashboard()

    def add_debt(self):
        person = self.root.ids.debt_person_input.text
        amount_text = self.root.ids.debt_amount_input.text
        
        if person and amount_text.isdigit():
            amount = float(amount_text)
            date_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.db.add_debt(person, amount, date_str)
            
            self.root.ids.debt_person_input.text = ''
            self.root.ids.debt_amount_input.text = ''
            self.update_debt_list()

    def mark_debt_paid(self, debt_id):
        self.db.mark_debt_as_paid(debt_id)
        self.update_debt_list()

    # Fungsi untuk menangani fokus keyboard
    def keyboard_open(self, instance):
        instance.keyboard.show_keyboard()
        instance.keyboard.on_key_down = self.key_down_handler
        
    def key_down_handler(self, keyboard, keycode, text, modifiers):
        pass

if __name__ == '__main__':
    FinanceApp().run()