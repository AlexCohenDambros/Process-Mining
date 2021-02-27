import pandas as pd
from datetime import datetime
import os.path

listas = {}
dici = {}


def inicial():
    print("\n#####################ENTRADA DO LOG#######################")
    print("Entre com o nome da tabela o qual está o Log\n")
    LoopEntr = True
    while LoopEntr:
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

        def abrir():
            global listas
            dadosLog = open(rf"C:\Users\Micro\Desktop\ProjetoPIBIC\{arqEntr}.txt", "r")
            abrir = dadosLog.read()
            listas = eval(abrir)
            dadosLog.close()

        def write():
            dadosLog = open(rf"C:\Users\Micro\Desktop\ProjetoPIBIC\{arqEntr}.txt", "w+")
            dadosLog.write(str(listas))
            dadosLog.close()

        if os.path.isfile(rf"C:\Users\Micro\Desktop\ProjetoPIBIC\{entrada}.xlsx"):
            print("\nArquivo xlsx carregado com sucesso!!!")
        else:
            print("\nO arquivo (xlsx) não foi localizado")
            inicial()
            break

        if os.path.isfile(rf"C:\Users\Micro\Desktop\ProjetoPIBIC\{arqEntr}.txt"):
            print("\nArquivo txt carregado com sucesso!!!")
        else:
            print("\nO arquivo (txt) não foi localizado e foi criado um novo com esse nome!!!!!\n")
            write()

        log = pd.read_excel(rf"C:\Users\Micro\Desktop\ProjetoPIBIC\{entrada}.xlsx", sheet_name="LogTeste", header=0)

        log["StartTime"] = pd.to_datetime(log.StartTime)

        log.sort_values(["ID", "StartTime"], inplace=True)  # ORDENANDO A HORA E O ID

        LoopEntr = False

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
        inicio = log["ID"].min()
        fim = log["ID"].max()
        LoopID = True
        while LoopID:
            if inicio <= fim:
                print("=========================================================================")
                logFs = log[log.ID == inicio]
                lista = logFs["Activity"].unique()

                timeA = pd.Timestamp(logFs["StartTime"].min())
                timeB = pd.Timestamp(logFs["EndTime"].max())
                timeF = timeB - timeA

                timestampT = datetime.timestamp(timeA)
                timestampT2 = datetime.timestamp(timeB)
                timestampF = timestampT2 - timestampT

                DataFrameDif = {"Diferença": []}
                newDataFrame = pd.DataFrame(DataFrameDif)

                newDataFrame["Diferença"] = (timeB - logFs["StartTime"])

                time_delta_series = newDataFrame["Diferença"]

                converted_series = time_delta_series.apply(get_seconds)
                converted_series = converted_series / 60

                print(logFs)

                print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
                print("Tempo inicial: ", timeA)
                print("Tempo final: ", timeB)
                print("O tempo total de execução deste produto foi de: ", timeF)
                print("Total:", timestampF / 60, "minutos")

                result = converted_series / logFs["Product"]

                Estado = ''
                i = 0
                for c in lista:
                    Estado += c
                    try:
                        listas[f'{Estado}'].append(result.iloc[i])
                    except KeyError:
                        listas[f'{Estado}'] = []
                        listas[f'{Estado}'].append(result.iloc[i])

                    Estado += "-"

                    write()
                    i += 1

            else:
                break

            inicio += 1
        print("=========================================================================")
        print("                          FIM DA EXECUÇÃO!")

    def excel():
        listaLog = log["Activity"].unique()
        listaLog.sort()

        incre = 0
        for x in listaLog:
            dici[x] = incre
            incre += 1

        colunas = list(listaLog) + ['Estado', 'Ocorrido', 'Previsão', 'Resultado']
        DataFrameTable = pd.DataFrame(columns=colunas)

        inicio = log["ID"].min()
        fim = log["ID"].max()
        LoopID = True
        while LoopID:
            if inicio <= fim:
                logFs = log[log.ID == inicio]
                lista = logFs["Activity"].unique()
                DataFrameDif = {"Diferença": []}
                newDataFrame = pd.DataFrame(DataFrameDif)
                timeB = pd.Timestamp(logFs["EndTime"].max())
                newDataFrame["Diferença"] = (timeB - logFs["StartTime"])
                time_delta_series = newDataFrame["Diferença"]
                converted_series = time_delta_series.apply(get_seconds)
                converted_series = converted_series / 60
                listaPrevi = converted_series.unique()

                Estado = ''
                i = 0
                for c in lista:
                    Estado += c

                    Previ2 = listas[f'{Estado}']
                    Media = (sum(Previ2) / len(Previ2))
                    result = ((listaPrevi[i] - Media) / listaPrevi[i])

                    try:
                        lAtividades = Estado.split("-")
                    except KeyError:
                        lAtividades = Estado.split(" ")

                    l_output = [0 for y in range(0, len(dici))]
                    for y in lAtividades:
                        l_output[dici[y]] = l_output[dici[y]] + 1

                    novalista = [l_output + [Estado, listaPrevi[i], Media, result]]

                    Df2 = pd.DataFrame(novalista, columns=colunas)
                    DataFrameTable = DataFrameTable.append(Df2, ignore_index=True)

                    Estado += "-"
                    i += 1

            else:
                break
            inicio += 1

        print("\nArquivo gerado com sucesso!")
        writer = pd.ExcelWriter(rf"C:\Users\Micro\Desktop\ProjetoPIBIC\saida.xlsx")
        DataFrameTable.to_excel(writer, sheet_name="Sheet1")
        writer.save()

    menu()

inicial()
