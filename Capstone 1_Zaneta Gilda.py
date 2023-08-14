from prettytable import PrettyTable

# DATA EMPLOYEE
Data = [
    [0, 'Keira', 'F', 35, 'Finance Manager', '6 January 2008'],
    [1, 'Theodore', 'M', 31, 'Human Resource Manager', '7 January 2010'],
    [2, 'James', 'M', 28, 'Marketing Manager', '8 January 2013'],
    [3, 'Serena', 'F', 26, 'Software Engineer', '9 January 2015'],
    [4, 'Nala', 'F', 23, 'Administrative Assistant', '10 January 2018']
]

# TO SHOW PRETTY TABLE
Table = PrettyTable()
# TO MAKE THE COLUMNS
Table.field_names = ['Employee ID', 'Nama', 'Gender', 'Usia', 'Role', 'Tanggal diterima']
# TO MAKE THE ROWS
for row in Data:
    Table.add_row(row)

#DEF FUNCTION  
def show_table():
    print(Table)

def add_data():
    employeeID = int(input('Input Employee ID : '))
    name = input('Input Name : ')
    gender = input('Input Gender (F/M) : ')
    age = int(input('Input Age : '))
    role = input('Input Role:')
    hiredate = input('Input Hire Date: ')
    new_row = [employeeID, name, gender, age, role, hiredate]
    Data.append(new_row)
    Table.add_row(new_row)
    print('Data telah berhasil ditambahkan')

def delete_data():
    index_to_delete = int(input("Masukkan index data yang ingin dihapus: "))
    if 0 <= index_to_delete < len(Data):
        Data.pop(index_to_delete)
        Table.clear_rows()
        for row in Data:
            Table.add_row(row)
        print("Data telah berhasil dihapus")

dataED = input('''
    EMPLOYEE DATABASE
      List Pilihan Menu:
      1. Menunjukkan tabel Employee Database Perusahaan
      2. Menambahkan data karyawan pada tabel 
      3. Menghapus data karyawan pada tabel
      4. Menghentikan program
    Input angka yang ingin diinput: ''')


while True:
    # INPUT MENU NUMBER

    if dataED == '1':
        show_table()
    elif dataED == '2':
        add_data()
        show_table()
    elif dataED == '3':
        delete_data()
        show_table()
    elif dataED == '4':
        break





