from tkinter import *
import tkinter.messagebox as tm
import hashlib
from tkinter import filedialog
import pandas as pd
from datetime import datetime
from tkinter.filedialog import askopenfilename
import tkinter as tk

# Dicionarios
login = {}
dici = {}
listas = {}

def register():
    while True:
        print("=================================")
        nome = input('Insira o nome: ')
        senha = input("Digite uma senha: ")
        if len(senha) != 4:
            print("Sua senha tem que ter 4 caracteres")
            break
        senha = hashlib.md5(senha.encode('utf-8')).hexdigest()

        f = open("senhasgravadas.txt", "a+")
        f.write(nome + " " + senha + "\n")
        f.close()
        print("Conta cadastrada!!")
        break


class Login:
    def abrir(self):
        global listas
        lc = True
        while lc:
            lce = False
            if self.openfile != "":
                try:
                    dadosLog = open(f"{self.openfile}", "r")
                    abrir = dadosLog.read()
                    listas = eval(abrir)
                    dadosLog.close()
                    tm.showinfo("Login info", "Arquivo carregado com sucesso!")
                except:
                    dadosLog = open(f"{self.openfile}", "w+")
                    dadosLog.write(str(listas))
                    dadosLog.close()
                    lce = True
            else:
                tm.showerror("Open File", "Erro na seleção de um arquivo!! Tente novamente!!")
            lc = lce

    def writer(self):
        try:
            dadosLog = open(f"{self.savefile.name}", "w+")
            dadosLog.write(str(listas))
            dadosLog.close()
            tm.showinfo("Save File","Arquivo salvo com sucesso!!")
        except:
            tm.showerror("Save File", "Erro na seleção de um arquivo!! Tente novamente!!")

    def savelog(self):
        try:
            writer = pd.ExcelWriter(f"{self.savelogEx.name}")
            self.DataFrameTable.to_excel(writer, sheet_name="Sheet1")
            writer.save()
            tm.showinfo("Save File", "Arquivo salvo com sucesso!!")
        except:
            tm.showerror("Save Log", "Erro na hora de salvar o xlsx, por favor Tente novamente!!")

    def abriLog(self):
        logW = True
        while logW:
            try:
                try:
                    self.log = pd.read_excel(f"{self.openfileLOG}", header=0, sep=",")
                    tm.showinfo("Open Log", "Arquivo aberto com Sucesso!!! (xlsx)")
                except:
                    self.log = pd.read_csv(f"{self.openfileLOG}", header=0, sep=",")
                    tm.showinfo("Open Log", "Arquivo aberto com Sucesso!!! (csv)")

                self.log = self.log.rename(columns={'Case ID': 'CaseID'})
                self.log = self.log.rename(columns={'Start Timestamp': 'StartTimestamp'})
                self.log = self.log.rename(columns={'Qty Completed': 'QtyCompleted'})

                self.log["Start Timestamp"] = pd.to_datetime(self.log.StartTimestamp)
                self.log.sort_values(["CaseID", "StartTimestamp"], inplace=True)  # ORDENANDO A HORA E O ID

                self.listaLog = self.log["Activity"].unique()
                self.listaLog.sort()

                incre = 0
                for x in self.listaLog:
                    dici[x] = incre
                    incre += 1

                self.log.loc[self.log.QtyCompleted == 0, 'QtyCompleted'] = 1
                # log[log["QtyCompleted"] == 0]
            except:
                tm.showerror("Log ERRO", "Voce não possui um log selecionado!! Selecione um arquivo no Menu")

            logW = False

    def open_file(self):
        self.openfile = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        self.abrir()



    def save_file(self):
        response = tm.askyesno("Save", "Deseja salvar agora?")

        if response == True:
            self.savefile = filedialog.asksaveasfile(defaultextension="txt", filetypes=[("Text Files", "*.txt"),
                                                                                        ("All Files", "*.*")])
            self.writer()

    def saveLogExport(self):
        responseLog = tm.askyesno("Save Log", "Voce ja carregou os dados no item 3 do menu?")

        if responseLog == True:
            self.savelogEx = filedialog.asksaveasfile(defaultextension="xlsx", filetypes=[("Excel Files", "*.xlsx"),
                                                                                            ("All Files", "*.*")])
            self.savelog()

        else:
            responseItem3 = tm.askyesno("Execute Log", "Voce deseja carregar os dados agora?")

            if responseItem3 == True:
                self.excel()

    def saveLogExportItem3(self):
        responseLog = tm.askyesno("Save Log", "Deseja salvar agora?")
        if responseLog == True:
            self.savelogEx = filedialog.asksaveasfile(defaultextension="xlsx", filetypes=[("Excel Files", "*.xlsx"),
                                                                                            ("All Files", "*.*")])
            self.savelog()

    def Log(self):
        self.openfileLOG = askopenfilename(filetypes=[("*.xlsx","*.csv"), ("All Files", "*.*")])
        self.abriLog()

    def check_login(self):
        usuario = self.nome.get()
        senha = self.senha.get()
        senha = hashlib.md5(senha.encode('utf-8')).hexdigest()

        f = open("senhasgravadas.txt", "r")
        fr = f.read().splitlines()
        for l in fr:
            (key, valor) = l.split(" ")
            login[key] = valor

        if usuario in login:
            if login[usuario] == senha:
                tm.showinfo("Login info", "Welcome: " + usuario)
                self.InsertLog()

            else:
                tm.showerror("Login error", "Authentication Error")
        else:
            tm.showerror("Login error", "Authentication Error")

    def __init__(self):
        self.master = Tk()
        self.var1 = tk.IntVar()

        self.master.geometry('854x480+300+200')
        self.master.title("Process Mining")
        self.master.iconbitmap(rf"C:\Users\alex-\Desktop\ProjetoPIBIC\ico.ico")
        self.master.resizable(False, False)

        self.master.config(bg='powder blue')
        self.fontePadrao = ("Arial", "12")

        # TEXT (LOGIN DO USUARIO)
        self.titulo = Label(font="Arial 30 bold", text="Login do Usuário")
        self.titulo["font"] = ("Arial", "30", "bold")
        self.titulo.place(x=280, y=20)

        # NAME
        self.nomeLabel = Label(text="Username", font=self.fontePadrao)
        self.nomeLabel.place(x=200, y=120)

        self.nome = Entry(bg="lightgray")
        self.nome["width"] = 50
        self.nome["font"] = self.fontePadrao
        self.nome.place(x=200, y=150)

        # SENHA
        self.senhaLabel = Label(text="Password", font=self.fontePadrao)
        self.senhaLabel.place(x=200, y=200)

        self.senha = Entry(bg="lightgray")
        self.senha["width"] = 50
        self.senha["font"] = self.fontePadrao
        self.senha["show"] = "*"
        self.senha.place(x=200, y=230)

        # BUTTON
        self.autenticar = Button()
        self.autenticar["text"] = "Autenticar"
        self.autenticar["font"] = ("Arial", "15")
        self.autenticar["width"] = 25
        self.autenticar["height"] = 3
        self.autenticar["command"] = self.check_login
        self.autenticar.place(x=200, y=300)

        # BUTTON SAIR
        self.sair = Button()
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Arial", "16")
        self.sair["pady"] = 23
        self.sair["padx"] = 30
        self.sair["command"] = self.sair.quit
        self.sair.place(x=520, y=300)

        self.master.mainloop()

    def InsertLog(self):
        self.master.destroy()

        self.menu = Tk()
        self.menu.title("Process Mining")
        self.menu.geometry('854x480+300+200')
        self.menu.resizable(False, False)
        self.menu.iconbitmap(rf"C:\Users\alex-\Desktop\ProjetoPIBIC\ico.ico")

        # BUTTON OPEN LOG
        self.OpenLog = Button()
        self.OpenLog["text"] = "Open Log"
        self.OpenLog["font"] = ("Arial", "15")
        self.OpenLog["width"] = 10
        self.OpenLog["height"] = 2
        self.OpenLog["command"] = self.Log
        self.OpenLog.place(x=20, y=100)

        # BUTTON OPEN TXT
        self.Opentxt = Button()
        self.Opentxt["text"] = "Open File"
        self.Opentxt["font"] = ("Arial", "15")
        self.Opentxt["width"] = 10
        self.Opentxt["height"] = 2
        self.Opentxt["command"] = self.open_file
        self.Opentxt.place(x=20, y=180)

        # BUTTON SAVE TXT
        self.savetxt = Button()
        self.savetxt["text"] = "Save File"
        self.savetxt["font"] = ("Arial", "15")
        self.savetxt["width"] = 10
        self.savetxt["height"] = 2
        self.savetxt["command"] = self.save_file
        self.savetxt.place(x=20, y=260)

        # BUTTON EXPORT OUTPUT
        self.export = Button()
        self.export["text"] = "Export Output"
        self.export["font"] = ("Arial", "14")
        self.export["width"] = 10
        self.export["height"] = 2
        self.export["command"] = self.saveLogExport
        self.export.place(x=20, y=340)

        # TITULO
        self.menuLabel = Label(text="MENU", font="Aril 30 bold")
        self.menuLabel.place(x=400, y=20)

        # BUTTON1 MENU CALULAR
        self.calcu = Button()
        self.calcu["text"] = "1 - CALCULAR"
        self.calcu["font"] = ("Arial", "14")
        self.calcu["width"] = 25
        self.calcu["height"] = 2
        self.calcu["command"] = self.calcular
        self.calcu.place(x=320, y=120)

        # BUTTON2 MENU PREVER EM UM ESTADO COM UM PRODUTO
        self.prev = Button()
        self.prev["text"] = "2 - PREVER"
        self.prev["font"] = ("Arial", "14")
        self.prev["width"] = 25
        self.prev["height"] = 2
        self.prev["command"] = self.prever
        self.prev.place(x=320, y=200)

        # BUTTON3 MENU EXCEL CALCULO
        self.exc = Button()
        self.exc["text"] = "3 - EXCEL"
        self.exc["font"] = ("Arial", "14")
        self.exc["width"] = 25
        self.exc["height"] = 2
        self.exc["command"] = self.excel
        self.exc.place(x=320, y=280)

    def get_days(self,time_delta):
        return time_delta.days

    def get_seconds(self,time_delta):
        return time_delta.seconds


    def prever(self):
        self.preveJan = Toplevel()
        self.preveJan.title("Prever")
        self.preveJan.configure(background='lightblue')
        self.preveJan.geometry('854x480+300+200')
        self.preveJan.iconbitmap(rf"C:\Users\alex-\Desktop\ProjetoPIBIC\ico.ico")
        self.preveJan.resizable(False, False)
        # de onde veio a janela
        self.preveJan.transient(self.menu)
        self.preveJan.focus_force()
        self.preveJan.grab_set()

        # INSERIR NOME DO PRODUTO
        self.proLabel = Label(self.preveJan, text="Insira o nome do Produto", font="Arial 20 bold")
        self.proLabel.place(x=200, y=100)

        self.pro = Entry(self.preveJan, bg="lightgray")
        self.pro["width"] = 50
        self.pro["font"] = self.fontePadrao
        self.pro.place(x=200, y=150)

        # INSERIR NOME DA MÁQUINA
        self.maqLabel = Label(self.preveJan, text="Insira o(s) Estado(s)", font="Arial 20 bold")
        self.maqLabel.place(x=200, y=200)

        self.maq = Entry(self.preveJan, bg="lightgray")
        self.maq["width"] = 50
        self.maq["font"] = self.fontePadrao
        self.maq.place(x=200, y=250)

        # BUTTON PREVER
        self.bt = Button(self.preveJan)
        self.bt["text"] = "PREVER"
        self.bt["font"] = ("Arial", "14")
        self.bt["width"] = 25
        self.bt["height"] = 2
        self.bt["command"] = self.preverCalculo
        self.bt.place(x=300, y=300)

    def preverCalculo(self):
        global listas, Previ

        LoopPrevi = True
        while LoopPrevi:
            lce = False
            try:
                self.abrir()
            except:
                tm.showerror("Open File", "Voce não possui um arquivo selecionado!! Selecione um arquivo no Menu")
                break

            maq = self.maq.get()
            pro = self.pro.get()
            try:
                Previ = listas[f'{pro}'][f'{maq}']
            except:
                tm.showerror("Prever Erro", "Sua entrada não foi localizada tente novamente!!!")
                break


            if len(Previ) == 0:
                tm.showerror("Prever Erro", "Este estado está vazio!! Não possue nenhum termo!!!")
                break

            Media = (sum(Previ) / len(Previ))
            tm.showinfo("Prever info",
                        f"A media do estado inserido, presente do produto: {pro} foi de: " + str(Media))
            LoopPrevi = lce

    def calcular(self):

        LoopPreviCal = True
        while LoopPreviCal:
            try:
                self.abriLog()
            except:
                tm.showerror("Log ERRO", "Voce não possui um log selecionado!! Selecione um arquivo no Menu")
                break
            try:
                self.abrir()
            except:
                tm.showerror("Open File", "Voce não possui um arquivo selecionado!! Selecione um arquivo no Menu")
                break
            try:
                self.log["CaseID"] = pd.to_numeric(self.log["CaseID"].str[5:])
            except:
                print("")

            try:
                casos = self.log["CaseID"].unique()
                inicio = self.log["CaseID"].min()
                fim = self.log["CaseID"].max()
            except:
                break

            LoopID = True
            while LoopID:
                if inicio == fim:
                    break
                elif inicio not in casos:
                    inicio += 1
                    continue
                elif inicio <= fim:

                    logFs = self.log[self.log.CaseID == inicio]
                    lista = logFs["Activity"].unique()
                    listaP = logFs["Part Desc."].unique()

                    timeA = pd.Timestamp(logFs["StartTimestamp"].min())
                    timeB = pd.Timestamp(logFs["Complete Timestamp"].max())
                    timeF = timeB - timeA

                    timestampT = datetime.timestamp(timeA)
                    timestampT2 = datetime.timestamp(timeB)
                    timestampF = timestampT2 - timestampT

                    DataFrameDif = {"Diferença": []}
                    newDataFrame = pd.DataFrame(DataFrameDif)

                    newDataFrame["Diferença"] = (timeB - pd.to_datetime(logFs["StartTimestamp"]))

                    time_delta_series = newDataFrame["Diferença"]

                    converted_seriesD = time_delta_series.apply(self.get_days)
                    converted_seriesD = converted_seriesD * 1440

                    converted_seriesS = time_delta_series.apply(self.get_seconds)
                    converted_seriesS = converted_seriesS / 60

                    converted_seriesF = converted_seriesD + converted_seriesS

                    print(logFs)

                    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                    print("Tempo inicial: ", timeA)
                    print("Tempo final: ", timeB)
                    print("O tempo total de execução deste produto foi de: ", timeF)
                    print("Total:", timestampF / 60, "minutos")

                    result = converted_seriesF / logFs["QtyCompleted"]

                    NumberEstado = ''
                    i = 0

                    for p in listaP:
                        Product = p
                        if Product in listas:
                            print("Já Existe este produto")
                        else:
                            listas[f'{Product}'] = {}
                            print("Produto criado")
                        for c in lista:
                            NumberEstado += str(dici[c])
                            try:
                                listas[f'{Product}'][f'{NumberEstado}'].append(result.iloc[i])
                            except KeyError:
                                listas[f'{Product}'][f'{NumberEstado}'] = []
                                listas[f'{Product}'][f'{NumberEstado}'].append(result.iloc[i])

                            NumberEstado += "-"
                            i += 1

                else:
                    break
                inicio += 1

            print("=========================================================================")
            print("                          FIM DA EXECUÇÃO!")

            LoopPreviCal = False


            try:
                self.save_file()
            except:
                tm.showerror("Save File", "Ocorreu algum problema na hora de salvar, tente novamente!!")


    def excel(self):
        global listas

        LoopPreviEx = True
        while LoopPreviEx:
            try:
                self.abriLog()
            except:
                tm.showerror("Log ERRO", "Voce não possui um log selecionado!! Selecione um arquivo no Menu")
                break
            try:
                self.abrir()
            except:
                tm.showerror("Open File", "Voce não possui um arquivo selecionado!! Selecione um arquivo no Menu")
                break

            print(dici)

            Looptxt = True
            while Looptxt:
                if len(listas) == 0:
                    tm.showerror("Dici", "O dicionário inserido está vazio!! Insira outro ou tente carregar os dados "
                                         "na opção '1 - Calcular' do Menu!!!")
                    break
                else:
                    try:
                        self.log["CaseID"] = pd.to_numeric(self.log["CaseID"].str[5:])
                    except:
                        print("")

                    casos = self.log["CaseID"].unique()

                    colunas = list(self.listaLog) + ['Estado', 'Ocorrido', 'Previsão', 'Resultado']
                    self.DataFrameTable = pd.DataFrame(columns=colunas)

                    inicio = self.log["CaseID"].min()
                    fim = self.log["CaseID"].max()
                    LoopID = True
                    while LoopID:
                        if inicio == fim:
                            break
                        elif inicio not in casos:
                            inicio += 1
                            continue
                        elif inicio <= fim:

                            logFs = self.log[self.log.CaseID == inicio]
                            lista = logFs["Activity"].unique()
                            listaP = logFs["Part Desc."].unique()

                            timeB = pd.Timestamp(logFs["Complete Timestamp"].max())

                            DataFrameDif = {"Diferença": []}
                            newDataFrame = pd.DataFrame(DataFrameDif)

                            newDataFrame["Diferença"] = (timeB - pd.to_datetime(logFs["StartTimestamp"]))

                            time_delta_series = newDataFrame["Diferença"]

                            converted_seriesD = time_delta_series.apply(self.get_days)
                            converted_seriesD = converted_seriesD * 1440

                            converted_seriesS = time_delta_series.apply(self.get_seconds)
                            converted_seriesS = converted_seriesS / 60

                            converted_seriesF = converted_seriesD + converted_seriesS

                            listaPrevi = converted_seriesF.unique()

                            Estado = ''
                            NumberEstado = ''
                            i = 0

                            for p in listaP:
                                Product = p
                                for c in lista:
                                    Estado += c
                                    NumberEstado += str(dici[c])

                                    try:
                                        MediaEx = sum(listas[f'{Product}'][f'{NumberEstado}']) / len(
                                            listas[f'{Product}'][f'{NumberEstado}'])
                                    except:
                                        break

                                    try:
                                        result = ((listaPrevi[i] - MediaEx) / listaPrevi[i])
                                    except:
                                        result = 0

                                    try:
                                        lAtividades = Estado.split("/")
                                    except KeyError:
                                        lAtividades = Estado.split("  ")

                                    l_output = [0 for y in range(0, len(dici))]
                                    for y in lAtividades:
                                        l_output[dici[y]] = l_output[dici[y]] + 1

                                    try:
                                        novalista = [l_output + [NumberEstado, listaPrevi[i], MediaEx, result]]
                                        print(novalista)
                                    except:
                                        print("Erro")

                                    Df2 = pd.DataFrame(novalista, columns=colunas)
                                    self.DataFrameTable = self.DataFrameTable.append(Df2, ignore_index=True)

                                    Estado += "/"
                                    NumberEstado += '-'

                                    i += 1

                        else:
                            break
                        inicio += 1

                    try:
                        self.saveLogExportItem3()
                    except:
                        tm.showerror("Save Log", "Ocorreu algum problema na hora de salvar o log, tente novamente!!")
                    Looptxt = False
            LoopPreviEx = False


lp = Login()
