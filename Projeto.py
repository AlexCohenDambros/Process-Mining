import pandas as pd
from datetime import datetime
import os.path

listas = {}
dici = {}


def inicial():

    def abrir():  # ABRIR TXT
        global listas
        dadosLog = open(rf"C:\Users\alex-\Desktop\ProjetoPIBIC\{arqEntr}.txt", "r")
        abrir = dadosLog.read()
        listas = eval(abrir)
        dadosLog.close()

    def write():  # ESCREVER TXT
        dadosLog = open(rf"C:\Users\alex-\Desktop\ProjetoPIBIC\{arqEntr}.txt", "w+")
        dadosLog.write(str(listas))
        dadosLog.close()

    LoopEntr = True
    while LoopEntr:
        print("\n#####################ENTRADA DO LOG#######################")
        print("Entre com o nome da tabela o qual está o Log\n")
        try:
            entrada = input("Entrada: ")
        except:
            print("Você digitou algo que não podia, tente novamente!!!")
            break

        try:
            print("\nEntre com o nome do arquivo de dados desejados sobre o respectivo Log\n")
            arqEntr = input("Entrada: ")
        except:
            print("Você digitou algo que não podia, tente novamente!!!")

        # Arquivo xlsx ou csv
        if os.path.isfile(rf"C:\Users\alex-\Desktop\ProjetoPIBIC\{entrada}.xlsx"):
            print("\nArquivo xlsx carregado com sucesso!!!")
        elif os.path.isfile(rf"C:\Users\alex-\Desktop\ProjetoPIBIC\{entrada}.csv"):
            print("\nArquivo csv carregado com sucesso!!!")
        else:
            print("\nO arquivo (xlsx) ou (csv) não foi localizado")
            inicial()
            break

        # Arquivo txt Abrir ou criar
        if os.path.isfile(rf"C:\Users\alex-\Desktop\ProjetoPIBIC\{arqEntr}.txt"):
            print("\nArquivo txt carregado com sucesso!!!")
        else:
            print("\nO arquivo (txt) não foi localizado e foi criado um novo com esse nome!!!!!\n")
            write()

        # log carregar
        try:
            log = pd.read_excel(rf"C:\Users\alex-\Desktop\ProjetoPIBIC\{entrada}.xlsx", header=0, sep=",")
        except:
            log = pd.read_csv(rf"C:\Users\alex-\Desktop\ProjetoPIBIC\{entrada}.csv", header=0, sep=",")

        if log.empty:
            print("\nEste LOG está vazio!!! Tente Inserir outro LOG!!")
            inicial()
            break

        log = log.rename(columns={'Case ID': 'CaseID'})
        log = log.rename(columns={'Start Timestamp': 'StartTimestamp'})
        log = log.rename(columns={'Qty Completed': 'QtyCompleted'})

        log["Start Timestamp"] = pd.to_datetime(log.StartTimestamp)
        log.sort_values(["CaseID", "StartTimestamp"], inplace=True)  # ORDENANDO A HORA E O ID

        listaLog = log["Activity"].unique()
        listaLog.sort()

        incre = 0
        for x in listaLog:
            dici[x] = incre
            incre += 1

        log.loc[log.QtyCompleted == 0, 'QtyCompleted'] = 1
        LoopEntr = False

    def get_days(time_delta):
        return time_delta.days

    def get_seconds(time_delta):
        return time_delta.seconds

    def menu():

        LoopM = True
        while LoopM:

            print("\n#################### MENU ########################")
            print("1 - CALCULAR\n"
                  "2 - PREVER\n"
                  "3 - EXCEL\n"
                  "4 - SAIR")

            try:
                escolhaMenu = int(input("Digite o número desejado: "))
            except:
                print("Você digitou algo que não podia, tente novamente!!!")
                break

            if escolhaMenu == 1:
                calcular()

            elif escolhaMenu == 2:
                prever()

            elif escolhaMenu == 3:
                excel()
            elif escolhaMenu == 4:
                break
            else:
                print("Voce digitou um número invalido, tente novamente!! ")
                LoopM = True

    def prever():

        abrir()
        print("\nSeja bem vindo ao previsão de tempo!!")
        LoopPrevi = True
        while LoopPrevi:
            try:
                print("\nDigite qual o último estado em que a maquina esteve!!!")
                entradaPrev = input("entrada: ")

            except:
                print("\nVoce digitou algo invalido, tente novamente!! ")
                break

            entradaPrev = entradaPrev.upper()

            try:
                Previ = listas[f'{entradaPrev}']
            except:
                print("\nSua entrada não foi localizada tente novamente mais tarde!!!")
                break

            if len(Previ) == 0:
                print("\nEste estado está vazio!! Não possue nenhum termo!! Tente novamente mais tarde!!!")
                break

            Media = (sum(Previ) / len(Previ))
            print(f"\nA previsão de tempo é aproximadamente {Media}")

            print("\nDeseja continuar? (sim = 1 / nao = 2)")

            try:
                decide = int(input("Entrada: "))

            except:
                print("\nVoce digitou algo que nao podia, será desiginado ao menu como medida de segurança!")
                break

            if decide == 1:
                LoopPrevi = True
            elif decide == 2:
                break

    def calcular():
        try:
            log["CaseID"] = pd.to_numeric(log["CaseID"].str[5:])
        except:
            print("")

        casos = log["CaseID"].unique()
        inicio = log["CaseID"].min()
        fim = log["CaseID"].max()

        LoopID = True
        while LoopID:
            if inicio == fim:
                break
            elif inicio not in casos:
                inicio += 1
                continue
            elif inicio <= fim:

                logFs = log[log.CaseID == inicio]
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

                converted_seriesD = time_delta_series.apply(get_days)
                converted_seriesD = converted_seriesD * 1440

                converted_seriesS = time_delta_series.apply(get_seconds)
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
                    if Product not in listas:
                        listas[f'{Product}'] = {}

                    for c in lista:
                        NumberEstado += str(dici[c])
                        try:
                            listas[f'{Product}'][f'{NumberEstado}'].append(result.iloc[i])
                        except KeyError:
                            listas[f'{Product}'][f'{NumberEstado}'] = []
                            listas[f'{Product}'][f'{NumberEstado}'].append(result.iloc[i])

                        NumberEstado += "-"

                        write()
                        i += 1

            else:
                break
            inicio += 1

        print("=========================================================================")
        print("                          FIM DA EXECUÇÃO!")

    def excel():
        abrir()
        print(dici)

        Looptxt = True
        while Looptxt:
            if len(listas) == 0:
                print("\nO dicionário inserido está vazio!!"
                      "Insira outro ou tente carregar os dados na opção '1' do Menu!!!")
                try:
                    escolher = int(
                        input("\nInsire a opção 1 para inserir um novo arquivo, ou 2 para carregar os dados do Log: "))
                    if escolher == 1:
                        inicial()
                        break

                    elif escolher == 2:
                        calcular()
                        break

                    else:
                        print("Você digitou algo inválido!!!!!")
                        break
                except:
                    print("Digite apenas números inteiros!!")
                    Looptxt = True
            else:
                try:
                    log["CaseID"] = pd.to_numeric(log["CaseID"].str[5:])
                except:
                    print("")

                casos = log["CaseID"].unique()

                colunas = list(listaLog) + ['Estado', 'Ocorrido', 'Previsão', 'Resultado']
                DataFrameTable = pd.DataFrame(columns=colunas)

                inicio = log["CaseID"].min()
                fim = log["CaseID"].max()
                LoopID = True
                while LoopID:
                    if inicio == fim:
                        break
                    elif inicio not in casos:
                        inicio += 1
                        continue
                    elif inicio <= fim:

                        logFs = log[log.CaseID == inicio]
                        lista = logFs["Activity"].unique()
                        listaP = logFs["Part Desc."].unique()

                        timeB = pd.Timestamp(logFs["Complete Timestamp"].max())

                        DataFrameDif = {"Diferença": []}
                        newDataFrame = pd.DataFrame(DataFrameDif)

                        newDataFrame["Diferença"] = (timeB - pd.to_datetime(logFs["StartTimestamp"]))

                        time_delta_series = newDataFrame["Diferença"]

                        converted_seriesD = time_delta_series.apply(get_days)
                        converted_seriesD = converted_seriesD * 1440

                        converted_seriesS = time_delta_series.apply(get_seconds)
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
                                    MediaEx = sum(listas[f'{Product}'][f'{NumberEstado}']) / len(listas[f'{Product}'][f'{NumberEstado}'])
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
                                DataFrameTable = DataFrameTable.append(Df2, ignore_index=True)

                                Estado += "/"
                                NumberEstado += '-'

                                i += 1

                    else:
                        break
                    inicio += 1

                print("\nArquivo gerado com sucesso!")
                writer = pd.ExcelWriter(rf"C:\Users\alex-\Desktop\ProjetoPIBIC\SaidaFinal.xlsx")
                DataFrameTable.to_excel(writer, sheet_name="Sheet1")
                writer.save()
                Looptxt = False

    menu()


inicial()
