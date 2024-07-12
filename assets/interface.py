# from ttkbootstrap import Window, Frame, Checkbutton, Entry, END, Text, Button, Label
# import tkinter as tk
# from tkinter import messagebox
# import datetime
# import threading

# from assets.jmsRequests import *

# class RELATORIO_JMS():
#     def __init__(self, authToken, accessLevel, name, userId) -> None:
#         self.authToken = authToken
#         self.accessLevel = accessLevel
#         self.name = name
#         self.userId = userId

#         self.consultaBipagemCheck = None

#         def on_closing(): # Função para finalizar todo o sistema
#             import sys
#             sys.exit()

#         #configurações do root
#         self.root = Window(themename='solar') #tema pronto
#         self.root.geometry('1000x700') #dimensionamento da janela
#         self.root.place_window_center() #força janela a abrir no centro da tela
#         self.root.title(f"Relatórios JMS") #titulo da janela principal
#         self.root.resizable(False, False) #bloqueia o ajuste de tamanho da janela por parte do usuario
#         self.root.protocol("WM_DELETE_WINDOW", on_closing) # Caso o usuário clique no X ele finaliza todo o sistema
#         #conteudo do Root
#         self.Frames() # chama os frames
#         self.entradas() # chama as caixas de entrada 'input'
    

#         # CHECKBOX RELATÓRIOS
#         self.consultaBipagemCheck = tk.IntVar()
#         self.Cria_check('Consulta de Bipagem', 'normal', self.consultaBipagemCheck, self.accessLevel,8 ) # chama os checkbuttons
        
#         #loop principal
#         self.root.mainloop()
    
#     #cria os frames
#     def Frames(self):
#         self.frame_checkbox = Frame(self.root, border=3, relief='raised')
#         self.frame_checkbox.place(relx=0.01, rely=0.01, relwidth=0.30, relheight=0.98)
        
#         self.frame_textbox = Frame(self.root, border=3, relief='raised')
#         self.frame_textbox.place(relx=0.33, rely=0.11, relwidth=0.65, relheight=0.879)
    
#     #cria as os inputs para o usuário
#     def entradas(self):
#         self.entry1 = Label(self.root, font='verdana, 12', text = f"Usuário:{self.name} \tID: {self.userId}")
#         self.entry1.place(relx=0.33, rely=0.01, relwidth=0.65, relheight=0.04)
#         # self.Placeholder(self.entry1, self.authToken)
        
#         self.entry2 = Entry(self.root,style='success', font='verdana, 12')
#         self.entry2.place(relx=0.48, rely=0.059, relwidth=0.1)
#         self.Placeholder(self.entry2, "2024-12-31")
        
#         self.entry3 = Entry(self.root,style='success', font='verdana, 12')
#         self.entry3.place(relx=0.7, rely=0.059, relwidth=0.1)
#         self.Placeholder(self.entry3, "2024-12-31")

#         self.textBox = Text(self.frame_textbox, font='verdana, 12', height = 31)
#         self.textBox.pack(fill = tk.BOTH)

#         self.searchButton = Button(self.frame_textbox, text = "Pesquisar", command = lambda: threading.Thread(target = self.search).start())
#         self.searchButton.pack()

#     #cria os chechbuttons
#     def Cria_check(self, TEXTO:str, STATUS:str, checkVar, useraccessLevel, minaccessLevel:int):
#         def on_checkbutton_toggle():
#             if checkVar.get() == 1:
#                 print(f"is checked")
#             else:
#                 print(f"is unchecked")

#         self.bt1 = Checkbutton(self.frame_checkbox, text=TEXTO.upper(), variable = checkVar, state=STATUS, bootstyle='success-round-toggle', command = on_checkbutton_toggle)
#         if useraccessLevel >= minaccessLevel:
#             self.bt1.pack(padx=10, pady=2, side='top')
    
#     #cria e trata os placeholders (texto das entradas)
#     def Placeholder(self, entry, placeholder_text):
#         entry.insert(0, placeholder_text)
#         entry.config(foreground='grey')
        
#         entry.bind("<FocusIn>", lambda event, placeholder=placeholder_text: self.FocusIn(event, entry, placeholder))
#         entry.bind("<FocusOut>", lambda event, placeholder=placeholder_text: self.FocusOut(event, entry, placeholder_text))
            
#     def FocusIn(self, event, entry, placeholder):
#         if entry.get() == placeholder:
#             entry.delete(0, END)
#             entry.config(foreground='white')
            
#     def FocusOut(self, event, entry, placeholder):  
#         if entry.get() == "":
#             entry.delete(0, END)
#             entry.insert(0, placeholder)
#             entry.config(foreground='grey')



#     # FUNÇÃO QUE PESQUISA TODOS OS RELATÓRIO COM BASE NAS CHECKBOX MARCADAS
#     def search(self):

#         check = 0

#         idList = self.textBox.get("1.0", tk.END).strip().split("\n")

#         if self.entry2.get() != "":
#             startDate = self.entry2.get()
#         else:
#             startDate = datetime.datetime.today().strftime("%Y-%m-%d")

#         if self.entry3.get() != "":
#             endtDate = self.entry2.get()
#         else:
#             endtDate = datetime.datetime.today().strftime("%Y-%m-%d")


#         if self.consultaBipagemCheck.get() == 1:
#             check += self.consultaBipagemCheck.get()
#             jmsRequests(self.authToken).runConsultaBipagens(idList, startDate, endtDate)

#         if check > 0:
#             messagebox.askokcancel(title = "Pronto", message = "Consolidação finalizada!")
        
        


# # RELATORIO_JMS()


from ttkbootstrap import Window, Frame, Checkbutton, Entry, END, Text, Button, Label, Progressbar
import tkinter as tk
from tkinter import messagebox
import datetime
import threading

from assets.jmsRequests import *

class RELATORIO_JMS():
    def __init__(self, authToken, accessLevel, name, userId) -> None:
        self.authToken = authToken
        self.accessLevel = accessLevel
        self.name = name
        self.userId = userId

        self.consultaBipagemCheck = None

        def on_closing(): # Função para finalizar todo o sistema
            import sys
            sys.exit()

        #configurações do root
        self.root = Window(themename='vapor') #tema pronto
        self.root.geometry('1000x700') #dimensionamento da janela
        self.root.place_window_center() #força janela a abrir no centro da tela
        self.root.title(f"Relatórios JMS") #titulo da janela principal
        self.root.resizable(False, False) #bloqueia o ajuste de tamanho da janela por parte do usuario
        self.root.protocol("WM_DELETE_WINDOW", on_closing) # Caso o usuário clique no X ele finaliza todo o sistema
        #conteudo do Root
        self.Frames() # chama os frames
        self.entradas() # chama as caixas de entrada 'input'
    

        # CHECKBOX RELATÓRIOS
        self.consultaBipagemCheck = tk.IntVar()
        self.Cria_check('Consulta de Bipagem', 'normal', self.consultaBipagemCheck, self.accessLevel,1 ) # chama os checkbuttons
        self.ultimoBeep = tk.IntVar()
        self.Cria_check('Ultima Bipagem', 'normal', self.ultimoBeep, self.accessLevel,1 ) # chama os checkbuttons
        
        #loop principal
        self.root.mainloop()
    
    #cria os frames
    def Frames(self):
        self.frame_checkbox = Frame(self.root, border=3, relief='raised')
        self.frame_checkbox.place(relx=0.01, rely=0.01, relwidth=0.30, relheight=0.98)
        
        self.frame_textbox = Frame(self.root, border=3, relief='raised')
        self.frame_textbox.place(relx=0.33, rely=0.11, relwidth=0.65, relheight=0.879)
    
    #cria as os inputs para o usuário
    def entradas(self):
        self.entry1 = Label(self.root, font='verdana, 12', text = f"Usuário:{self.name} \tID: {self.userId}")
        self.entry1.place(relx=0.33, rely=0.01, relwidth=0.65, relheight=0.04)
        # self.Placeholder(self.entry1, self.authToken)
        
        self.entry2 = Entry(self.root,style='success', font='verdana, 12')
        # self.entry2.place(relx=0.48, rely=0.059, relwidth=0.1)
        self.Placeholder(self.entry2, "2024-12-31")
        
        self.entry3 = Entry(self.root,style='success', font='verdana, 12')
        # self.entry3.place(relx=0.7, rely=0.059, relwidth=0.1)
        self.Placeholder(self.entry3, "2024-12-31")

        self.textBox = Text(self.frame_textbox, font='verdana, 12', height = 31)
        self.textBox.pack(fill = tk.BOTH)

        self.searchButton = Button(self.frame_textbox, text = "Pesquisar", command = self.start_search)
        self.searchButton.pack(side = tk.BOTTOM)

        self.contador = Label(self.frame_textbox, text = f"")
    
    def start_search(self):
        # Substitui o botão de pesquisa por uma barra de progresso
        self.searchButton.pack_forget()
        self.progress = Progressbar(self.frame_textbox, mode='indeterminate')
        self.progress.pack()
        self.progress.start()

        # Inicia a pesquisa em uma nova thread
        threading.Thread(target=self.search).start()

    #cria os chechbuttons
    def Cria_check(self, TEXTO:str, STATUS:str, checkVar, useraccessLevel, minaccessLevel:int):
        def on_checkbutton_toggle():
            if checkVar.get() == 1:
                print(f"is checked")
            else:
                print(f"is unchecked")

        self.bt1 = Checkbutton(self.frame_checkbox, text=TEXTO.upper(), variable = checkVar, state=STATUS, bootstyle='success-round-toggle', command = on_checkbutton_toggle)
        if useraccessLevel >= minaccessLevel:
            self.bt1.pack(padx=10, pady=2, side='top')
    
    #cria e trata os placeholders (texto das entradas)
    def Placeholder(self, entry, placeholder_text):
        entry.insert(0, placeholder_text)
        entry.config(foreground='grey')
        
        entry.bind("<FocusIn>", lambda event, placeholder=placeholder_text: self.FocusIn(event, entry, placeholder))
        entry.bind("<FocusOut>", lambda event, placeholder=placeholder_text: self.FocusOut(event, entry, placeholder_text))
            
    def FocusIn(self, event, entry, placeholder):
        if entry.get() == placeholder:
            entry.delete(0, END)
            entry.config(foreground='white')
            
    def FocusOut(self, event, entry, placeholder):  
        if entry.get() == "":
            entry.delete(0, END)
            entry.insert(0, placeholder)
            entry.config(foreground='grey')

    # FUNÇÃO QUE PESQUISA TODOS OS RELATÓRIO COM BASE NAS CHECKBOX MARCADAS
    def search(self):
        self.contador.pack(side = tk.BOTTOM)
        threads = []
        check = 0

        idList = self.textBox.get("1.0", tk.END).strip().split("\n")

        if self.entry2.get() != "":
            startDate = self.entry2.get()
        else:
            startDate = datetime.datetime.today().strftime("%Y-%m-%d")

        if self.entry3.get() != "":
            endDate = self.entry2.get()
        else:
            endDate = datetime.datetime.today().strftime("%Y-%m-%d")

        if self.consultaBipagemCheck.get() == 1:
            check += self.consultaBipagemCheck.get()
            beepCheck = beepCheckJMS(self.authToken)
            beepCheckThread = threading.Thread(target = beepCheck.runBeepCheck, args = (idList, startDate, endDate, self.contador))
            threads.append(beepCheckThread)

        if self.ultimoBeep.get() == 1:
            check += self.ultimoBeep.get()
            lastScan = lastScanJMS(self.authToken)
            lastScanThread = threading.Thread(target = lastScan.runLastScan, args = (idList, self.accessLevel, self.contador))
            threads.append(lastScanThread)

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        # Para a barra de progresso e traz o botão de volta
        self.progress.stop()
        self.progress.pack_forget()
        self.searchButton.pack()

        if check > 0:
            messagebox.askokcancel(title = "Pronto", message = "Consolidação finalizada!")
            self.contador.pack_forget()
        
# RELATORIO_JMS()
