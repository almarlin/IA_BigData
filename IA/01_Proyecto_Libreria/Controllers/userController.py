from Model.User import User
import pandas as pd
import os

userPath = "./Data/biblioUsuarios.csv"

def get_user(dni):
    if os.path.getsize(userPath) > 0:
        users = pd.read_csv(userPath)

        userDf = users[users["dni"]== dni]       
        if userDf.empty:
            return False
        else:
            user = User()

            data = userDf.values.tolist()
            user.create(
                data[0][1],
                data[0][2],
                data[0][3],
                data[0][4],
                data[0][5],
                data[0][6],
                data[0][7]
            )
            user.id = data[0][0]
            return user

    else:
        return False    

def register_user(user):
    df = pd.DataFrame([user.to_dict()])
    if os.path.getsize(userPath) > 0:
        old = pd.read_csv(userPath)

        d = old[old["dni"] == user.dni]
        if d.empty:
            all = pd.concat([old, df], ignore_index=True)
            all.to_csv(userPath, sep=",", encoding="utf-8", index=False)
        else:
            return "Usuario ya registrado"
    else:
        df.to_csv(userPath, sep=",", encoding="utf-8", index=False)
    
    return "Usuario creado correctamente\n"

def down_user(user):
    df = pd.DataFrame([user.to_dict()])
    if os.path.getsize(userPath) > 0:
        old = pd.read_csv(userPath)

        d = old[old["dni"] == user.dni]
        if d.empty:
            return "El usuario ya esta dado de baja"  
        else:
            df = old[old["dni"]!= user.dni]
            # all = pd.concat([old, df], ignore_index=True)
            df.to_csv(userPath, sep=",", encoding="utf-8", index=False)
    else:
        return "No hay usuarios registrados\n"
    
    return "Usuario eliminado correctamente\n"

def save_user(user):
    userDf = pd.DataFrame([user.to_dict()])
    if os.path.getsize(userPath) > 0:
        old = pd.read_csv(userPath)
        userDf = userDf.astype(old.dtypes.to_dict())

        # Modificamos el dataframe
        old.update(old[["id"]].merge(userDf,'right'))

        # Se escribe en el fichero
        old.to_csv(userPath, sep=",", encoding="utf-8", index=False)
        

    return "Usuario actualizado correctamente\n"


def set_name_user(user,name):
    user.name = name
    return save_user(user)

def set_surname_user(user,surname):
    user.surname = surname
    return save_user(user)

def set_address_user(user,address):
    user.address = address
    return save_user(user)

def set_age_user(user,age):
    user.age = age
    return save_user(user)

def set_phone_user(user,phone):
    user.phone = phone
    return save_user(phone)

def list_user():
    if os.path.getsize(userPath) > 0:
        all = pd.read_csv(userPath)
        return all
    else:
        return "No hay usuarios registrados\n"