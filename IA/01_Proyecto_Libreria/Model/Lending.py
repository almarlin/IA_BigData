import os
import pandas as pd

lendingPath = "./Data/biblioPrestamos.csv"

class Lending():
    
    def __init__(self):
        if os.path.exists(lendingPath) and os.path.getsize(lendingPath) > 0:
            lends = pd.read_csv(lendingPath)
            self.id = lends["id"].iloc[-1] + 1
        else:
            self.id = 1

    def create(self,id_user, id_book, start_date, end_date, return_date):
        self.id_user = id_user
        self.id_book = id_book
        self.start_date = start_date
        self.end_date = end_date
        self.return_date = return_date

        return self
    
    def to_dict(self):
        return {
            "id": self.id,
            "id_user": self.id_user,
            "id_book": self.id_book,
            "start_date": self.start_date,
            "end_date": self.end_date,
            "return_date": self.return_date
        }
