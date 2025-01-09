import os
import pandas as pd
from Model.Lending import Lending
from datetime import date, timedelta

lendPath = "./Data/biblioPrestamos.csv"


def get_lend(id_user,id_book):
    if os.path.getsize(lendPath) > 0:

        lends = pd.read_csv(lendPath)

        find = lends[(lends["id_user"] == id_user) & (lends["id_book"] == id_book)]
        if find.empty:
            return False
        else:
            lendList = find.values.tolist()
            lend = Lending()

            lend.id = lendList[0][0]
            lend.id_user = lendList[0][1]
            lend.id_book = lendList[0][2]
            lend.start_date = lendList[0][3]
            lend.end_date = lendList[0][4]
            lend.return_date = lendList[0][5]

            return lend
            

    return False

def save_lend(lend):
    lendDf = pd.DataFrame([lend.to_dict()])
    if os.path.getsize(lendPath) > 0:
        old = pd.read_csv(lendPath)
        lendDf = lendDf.astype(old.dtypes.to_dict())

        # Modificamos el dataframe
        old.update(old[["id"]].merge(lendDf,'right'))

        # Se escribe en el fichero
        old.to_csv(lendPath, sep=",", encoding="utf-8", index=False)
    else:
        lendDf.to_csv(lendPath, sep=",", encoding="utf-8", index=False)

    return "Préstamos actualizados correctamente\n"

def lend_book_to_user(book,user):
    
    id_user = user.id
    id_book = book.id
    old = get_lend(id_user,id_book)
    if old:
        if old.return_date != date(1,1,1).strftime("%Y-%m-%d"):
            return "Este usuario ya tiene prestado este libro\n"
    else:

        start_date = date.today()
        end_date = start_date + timedelta(days=14)
        return_date =date(1,1,1)

        lend = Lending()
        lend.create(id_user,id_book,start_date,end_date,return_date)
        save_lend(lend)

        return "Préstamo realizado correctamente\n"

def return_book(book,user):
    lend = get_lend(user.id,book.id)
    if lend:

        if lend.return_date == date(1,1,1).strftime("%Y-%m-%d"):
            lend.return_date = date.today().strftime("%Y-%m-%d")
            save_lend(lend)
    else:
        return "No hay préstamos pendientes para este usuario con este libro\n"

    return "Libro devuelto correctamente\n"

def get_all_lends_user(user):
    if os.path.size(lendPath) > 0:

        lends = pd.read_csv(lendPath)

    find = lends[lends["id_user"] == user.id]
    if find.empty:
        return False
    else:

        return find
            
def get_pending_lends(*user):
    if os.path.getsize(lendPath) > 0:

        lends = pd.read_csv(lendPath)
    if user:
        find = lends[(lends["id_user"] == user[0].id) & (lends["return_date"] != date(1,1,1).strftime("%Y-%m-%d"))]
        if find.empty:
            return False
        else:

            return find
    else:
        find = lends[lends["return_date"] != date(1,1,1).strftime("%Y-%m-%d")]
        if find.empty:
            return False
        else:

            return find    
