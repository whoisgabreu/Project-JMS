from turtle import color
from ttkbootstrap import Window, Frame, Radiobutton, Entry, END, Text, Button, Label, Progressbar, Scrollbar
import tkinter as tk
from tkinter import messagebox
import datetime
import threading

from assets.jmsRequests import *
from assets.imgPOD import *

class RELATORIO_JMS():
    def __init__(self, authToken, accessLevel, name, userId, userLimit:int, userLimitPod:int) -> None:
        self.authToken = authToken
        self.accessLevel = accessLevel
        self.name = name
        self.userId = userId
        self.userLimit = userLimit
        self.userLimitPod = userLimitPod

        self.consultaBipagemCheck = None

        def on_closing(): # Função para finalizar todo o sistema
            import sys
            sys.exit()

        #configurações do root
        self.root = Window(themename='vapor') #tema pronto
        self.root.geometry('1000x700') #dimensionamento da janela
        self.root.place_window_center() #força janela a abrir no centro da tela
        self.root.title(f"Pesquisa IDs") #titulo da janela principal
        self.root.resizable(False, False) #bloqueia o ajuste de tamanho da janela por parte do usuario
        self.root.protocol("WM_DELETE_WINDOW", on_closing) # Caso o usuário clique no X ele finaliza todo o sistema
        #conteudo do Root
        self.Frames() # chama os frames
        self.entradas() # chama as caixas de entrada 'input'
    
        # MEU NOMINO
        self.Label = Label(self.root,text = "Developed by Gabriel Lucas de Ângelus.", font = "verdana 7")
        self.Label.place(relx=0.77, rely=0.073, relwidth=1, relheight=0.035)

        self.selectedReport = tk.StringVar()
        # CHECKBOX RELATÓRIOS
        self.Cria_radio('Consulta de Bipagem', 'consulta_bipagem', self.selectedReport, self.accessLevel,4 ) # chama os checkbuttons
        self.Cria_radio('Ultima Bipagem', 'ultima_bipagem', self.selectedReport, self.accessLevel,4 ) # chama os checkbuttons
        self.Cria_radio('POD', 'POD', self.selectedReport, self.accessLevel,1 ) # chama os checkbuttons
        
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
        self.entry1 = Label(self.root, font='verdana, 12', text = f"Usuário: {self.name} \n\nID: {self.userId}")
        self.entry1.place(relx=0.33, rely=0.00, relwidth=0.65, relheight=0.10)
        # self.Placeholder(self.entry1, self.authToken)
        
        self.entry2 = Entry(self.root,style='success', font='verdana, 12')
        # self.entry2.place(relx=0.48, rely=0.059, relwidth=0.1)
        self.Placeholder(self.entry2, "2024-12-31")
        
        self.entry3 = Entry(self.root,style='success', font='verdana, 12')
        # self.entry3.place(relx=0.7, rely=0.059, relwidth=0.1)
        self.Placeholder(self.entry3, "2024-12-31")

        # self.textBox = Text(self.frame_textbox, font='verdana, 12', height = 31)
        # self.textBox.pack(fill = tk.BOTH)

        # Adicionando TextBox com Scrollbar
        self.scrollbar = Scrollbar(self.frame_textbox, style = "success")
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.textBox = Text(self.frame_textbox, font='verdana, 12', height=31, yscrollcommand=self.scrollbar.set)
        self.textBox.pack(fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.textBox.yview)
        

        self.searchButton = Button(self.frame_textbox, text = "Pesquisar", command = self.start_search)
        self.searchButton.pack(side = tk.BOTTOM, fill = tk.BOTH, expand = True)

        self.contador = Label(self.frame_textbox, text = f"")
    
    def start_search(self):

        idList = self.textBox.get("1.0", tk.END).strip().split("\n")

        if len(idList) > self.userLimit and self.selectedReport.get() != "POD":
            messagebox.showinfo(title = "Limite excedido!", message = f"Pesquise apenas {self.userLimit} pedidos. Você inseriu {len(idList)}.")
            return
        elif len(idList) > self.userLimitPod and self.selectedReport.get() == "POD":
            messagebox.showinfo(title = "Limite excedido!", message = f"Pesquise apenas {self.userLimitPod} pedidos. Você inseriu {len(idList)}.")
            return

        # Substitui o botão de pesquisa por uma barra de progresso
        self.searchButton.pack_forget()
        self.progress = Progressbar(self.frame_textbox, mode='determinate')
        self.progress.pack(fill = tk.X)
        self.progress.start()

        # Inicia a pesquisa em uma nova thread
        threading.Thread(target=self.search).start()

    #cria os chechbuttons
    def Cria_radio(self, texto:str, valor, variable, useraccessLevel, minaccessLevel:int):
        def on_radiobutton_toggle():
            # print(f"{valor} selected")
            pass

        self.radio = Radiobutton(self.frame_checkbox, text=texto.upper(), variable=variable, value=valor, command=on_radiobutton_toggle)
        if useraccessLevel >= minaccessLevel:
            self.radio.pack(padx=10, pady=5, side="top", anchor = "w")
    
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
        threads = []

        idList = self.textBox.get("1.0", tk.END).strip().split("\n")
        # print(len(idList))
        self.contador.pack(side = tk.BOTTOM)


        selectedReport = self.selectedReport.get()

        if selectedReport == 'consulta_bipagem':

            if self.entry2.get() != "":
                startDate = self.entry2.get()
            else:
                startDate = datetime.datetime.today().strftime("%Y-%m-%d")

            if self.entry3.get() != "":
                endDate = self.entry2.get()
            else:
                endDate = datetime.datetime.today().strftime("%Y-%m-%d")
                
            beepCheck = beepCheckJMS(self.authToken)
            beepCheckThread = threading.Thread(target=beepCheck.runBeepCheck, args=(idList, startDate, endDate, self.contador, self.progress))
            threads.append(beepCheckThread)

        elif selectedReport == 'ultima_bipagem':
            lastScan = lastScanJMS(self.authToken)
            lastScanThread = threading.Thread(target=lastScan.runLastScan, args=(idList, self.accessLevel, self.contador, self.progress))
            threads.append(lastScanThread)

        elif selectedReport == 'POD':
            baixarPOD = imgPOD(self.authToken)
            podThread = threading.Thread(target = baixarPOD.start, args = (idList, self.contador, self.progress))
            threads.append(podThread)

        for t in threads:
            t.start()

        for t in threads:
            t.join()

        self.progress.stop()

        if selectedReport:
            messagebox.askokcancel(title = "Pronto", message = "Finalizado!")
        # Para a barra de progresso e traz o botão de volta
            self.progress.pack_forget()
            self.contador.pack_forget()
            self.searchButton.pack(side = tk.BOTTOM, fill = tk.BOTH, expand = True)
        
# RELATORIO_JMS()