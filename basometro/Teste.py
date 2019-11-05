from camaraPy.api_original.core import core, custom_exceptions
from camaraPy.api_original import proposicoes, deputados
import datetime
import pandas as pd
import csv


listona = [{"Tipo":"PEC","Numero":"2","Ano":"2015"},{"Tipo":"PLN","Numero":"2","Ano":"2019"},{"Tipo":"PDL","Numero":"3","Ano":"2019"},{"Tipo":"PLN","Numero":"4","Ano":"2019"},{"Tipo":"PEC","Numero":"6","Ano":"2019"},{"Tipo":"PEC","Numero":"34","Ano":"2019"},{"Tipo":"PLP","Numero":"55","Ano":"2019"},{"Tipo":"PEC","Numero":"70","Ano":"2011"},{"Tipo":"PDC","Numero":"379","Ano":"2016"},{"Tipo":"PLP","Numero":"441","Ano":"2017"},{"Tipo":"REQ","Numero":"482","Ano":"2019"},{"Tipo":"REQ","Numero":"829","Ano":"2019"},{"Tipo":"REQ","Numero":"844","Ano":"2019"},{"Tipo":"MPV","Numero":"852","Ano":"2018"},{"Tipo":"MPV","Numero":"861","Ano":"2018"},{"Tipo":"MPV","Numero":"863","Ano":"2018"},{"Tipo":"MPV","Numero":"866","Ano":"2018"},{"Tipo":"MPV","Numero":"867","Ano":"2018"},{"Tipo":"MPV","Numero":"870","Ano":"2019"},{"Tipo":"MPV","Numero":"871","Ano":"2019"},{"Tipo":"MPV","Numero":"879","Ano":"2019"},{"Tipo":"MPV","Numero":"881","Ano":"2019"},{"Tipo":"PL","Numero":"1292","Ano":"1995"},{"Tipo":"PL","Numero":"1321","Ano":"2019"},{"Tipo":"REQ","Numero":"1464","Ano":"2019"},{"Tipo":"REQ","Numero":"2070","Ano":"2019"},{"Tipo":"REQ","Numero":"2110","Ano":"2019"},{"Tipo":"REQ","Numero":"2144","Ano":"2019"},{"Tipo":"REQ","Numero":"2157","Ano":"2019"},{"Tipo":"REQ","Numero":"2234","Ano":"2019"},{"Tipo":"REQ","Numero":"2362","Ano":"2019"},{"Tipo":"REQ","Numero":"2381","Ano":"2019"},{"Tipo":"PL","Numero":"2724","Ano":"2015"},{"Tipo":"PL","Numero":"2787","Ano":"2019"},{"Tipo":"PL","Numero":"2788","Ano":"2019"},{"Tipo":"PL","Numero":"2999","Ano":"2019"},{"Tipo":"PL","Numero":"3715","Ano":"2019"},{"Tipo":"PL","Numero":"4121","Ano":"2019"},{"Tipo":"PL","Numero":"4742","Ano":"2001"},{"Tipo":"PL","Numero":"5029","Ano":"2019"},{"Tipo":"REQ","Numero":"7516","Ano":"2017"},{"Tipo":"PL","Numero":"7596","Ano":"2017"},{"Tipo":"PL","Numero":"8240","Ano":"2017"},{"Tipo":"PL","Numero":"10431","Ano":"2018"},{"Tipo":"PL","Numero":"10985","Ano":"2018"}]



file1 = open("MyFile.txt","a",encoding="UTF-8")
contador = 0

# Define parâmetros para a consulta

for i in listona:
    params = i

    # Acessa as votações da proposta
    votacoes = proposicoes.ObterVotacaoProposicao(params)
    dadosvotacoes = votacoes["proposicao"]["Votacoes"]["Votacao"]

    # Se os dados vêm na forma de lista, a proposição em questão
    # tem ao menos duas votações associadas à ela.
    if isinstance(dadosvotacoes, list):

        for votacao in dadosvotacoes:
            idVotacao = f"{votacao['@Data'].strip()}.{votacao['@Hora'].strip()}.{votacao['@codSessao'].strip()}".replace("/","-").replace(":",".")
            listaBancadas = votacao["orientacaoBancada"]["bancada"]

            for part in listaBancadas:
                orientacao = f"{idVotacao};{part['@Sigla']};{part['@orientacao']}\n"
                file1.write(orientacao)

    elif isinstance(dadosvotacoes, dict):
            idVotacao = f"{dadosvotacoes['@Data'].strip()}.{dadosvotacoes['@Hora'].strip()}.{dadosvotacoes['@codSessao'].strip()}".replace("/","-").replace(":",".")
            listaBancadas = dadosvotacoes["orientacaoBancada"]["bancada"]

            for part in listaBancadas:
                orientacao = f"{idVotacao};{part['@Sigla']};{part['@orientacao']}\n"
                file1.write(orientacao)

    contador = contador + 1
    print(f"Foi o projeto {contador}")