def change():
    expense = 23.75
    money = 100
    print(f"Ingresar gasto:\n{expense}\nDinero recibido\n{money}\n")
    resto=money-expense
    decimal=int((resto-int(resto))*100)
    print(f"Vuelto\n\nPesos:\n{int(resto)}\nCentavos:\n{decimal}")
