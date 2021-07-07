from pm4py.objects.conversion.log import converter as log_converter
import pandas as pd
import pm4py
from pm4py.objects.log.util import dataframe_utils

entrada = open("entrada.txt", "r")
linhas = entrada.readlines()
contador = 0
for linha in linhas:
    if contador == 0:
        linha = linha.rstrip('\n')
        variavel1 = linha
    elif contador == 1:
        linha = linha.rstrip('\n')
        variavel2 = linha
    elif contador == 2:
        linha = linha.rstrip('\n')
        variavel3 = linha
    contador+=1
entrada.close()

pd.set_option('max_columns', None)

logCsv = pd.read_csv('Production_Data.csv', sep=',')
logCsv = dataframe_utils.convert_timestamp_columns_in_df(logCsv)

logCsv = pm4py.format_dataframe(logCsv, case_id=f'{variavel1}', activity_key=f'{variavel2}', timestamp_key=f'{variavel3}')
logCsv = log_converter.apply(logCsv)

from pm4py.algo.discovery.heuristics import algorithm as heuristics_miner
net, im, fm = heuristics_miner.apply(logCsv, parameters={heuristics_miner.Variants.CLASSIC.value.Parameters.DEPENDENCY_THRESH: 0.99})

from pm4py.visualization.petri_net import visualizer as pn_visualizer
gviz = pn_visualizer.apply(net, im, fm)
pn_visualizer.view(gviz)