import requests
from tkinter import messagebox
import sys

class authenticateUser:

    def check(self, userId:str):
        self.userId = userId

        result = requests.get(url = f"https://prjeto-jms-default-rtdb.firebaseio.com/{self.userId}/.json")
        if result.status_code == 200:
            try:
                if result.json().get("active",False) == False:
                    messagebox.askokcancel(message = f"{self.userId} bloqueado! Entre em contato com o Desenvolvedor.")

                elif result.json().get("active",False) == True:
                    return (result.json().get("name",None), result.json().get("accessLevel",None), result.json().get("userLimit",None), result.json().get("userLimitPod",None))

                else:
                    messagebox.askokcancel(message = f"{self.userId} não cadastrado! Entre em contato com o Desenvolvedor.")
                
            except: pass
                