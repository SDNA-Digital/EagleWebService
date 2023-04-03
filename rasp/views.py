from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup
import re
import psycopg2 as pg
#import mysql.connector
#import pyodbc
import os
from django.conf import settings

def current_datetime(request, teste):

    html = "<html><body>Done! %s </body></html>" % teste

    listadelinks = []

    connection = pg.connect(user="postgres", password="3621", host="localhost", port="5432", database="DPP")
    curs = connection.cursor()
    curs.execute('SELECT*FROM normasite')

    listaDados = curs.fetchall()
    # connection = mysql.connector.connect(host = "localhost", user = "root", password = "0832", database ="testelei")
    # curs = connection.cursor()

    # connection = pyodbc.connect("Driver={SQL Server};""Server=Lucas;""Database=testelei;")
    # curs = connection.cursor()

    for link1 in listaDados:

        curs.execute(f'SELECT*FROM normasitesitepalavrachave where normasiteid = {link1[0]}')
        listaPalavraChave = curs.fetchall()
        response = requests.get(link1[1])
        content = response.content

        site = BeautifulSoup(content, 'html.parser')

        links = site.findAll(listaPalavraChave[0][4], class_=listaPalavraChave[0][2])

        for link in links:
            tipoNorma = re.match(listaPalavraChave[1][2], link.text)
            if tipoNorma:
                listadelinks.append(link.get_attribute_list('href')[0])

        for link_norma in listadelinks:
            response = requests.get(link_norma)

            content = response.content

            site = BeautifulSoup(content, 'html.parser')
            textoLei = site.find(listaPalavraChave[2][4], attrs={'class': listaPalavraChave[2][2]})
            nomeLei = textoLei.find(listaPalavraChave[3][4], attrs={'class': listaPalavraChave[3][2]})
            ementaLei = textoLei.find(listaPalavraChave[4][4], attrs={'class': listaPalavraChave[4][2]})
            dataPublicacao = site.find(listaPalavraChave[5][4], attrs={'class': listaPalavraChave[5][2]})
            vigorIndex = re.search(listaPalavraChave[6][2], textoLei.text)
            classificacaoindex = re.search(r'RESOLUÇÃO|PORTARIA', nomeLei.text).span()
            classificacao = nomeLei.text[classificacaoindex[0]:classificacaoindex[1]]
            conteudoLei = textoLei.find(string='').replaceWith(nomeLei)
            if vigorIndex == None:
                dataVigencia = ''
            else:
                vigorIndex = vigorIndex.span()
                textodata = textoLei.text[vigorIndex[0]:vigorIndex[1]]

                if textodata == "":
                    dataVigencia = dataPublicacao.text
                else:
                    if re.match(r'entra em vigor na data de sua publicação', textodata):
                        dataVigencia = dataPublicacao.text
                    else:
                        dataVigencia = textodata

            posicao_virgula = nomeLei.text.find(',')
            posicao_grau = nomeLei.text.find('º')
            posicao_primeiro_numero = posicao_grau + 2
            numero = nomeLei.text[posicao_primeiro_numero:posicao_virgula]

            print(numero)
            print(nomeLei.text)
            print(ementaLei.text)
            print(dataPublicacao.text)
            print(dataVigencia)
            print(classificacao)
            print(conteudoLei.text)

            curs.execute(
                "INSERT INTO norma (normanome, normanumero, normadescricaocurta, normainiciovigencia, normapublicadoem, normaurl, normaclassificacao, normatextodocumento, normadoc)VALUES (%s, %s, %s,%s, %s, %s, %s, %s, %s);",
                (nomeLei.text, numero, ementaLei.text, dataVigencia, dataPublicacao.text, link_norma, classificacao,
                 conteudoLei.text, True))

            # curs.execute(f"INSERT INTO norma (numerolei, nomelei, ementalei) VALUES ('{numero}', '{nomeLei.text}', '{ementaLei.text}');")

            connection.commit()
            x = r"C:\KBs\Eagle\NETFrameworkPostgreSQL003\Web\bin\aprc_fluxonormainicial.exe"
            os.startfile(x)

    curs.close()
    connection.close()


    return HttpResponse(html)

def HelloWorld(request):
    
    print(settings.DB_NAME)
    html = "<html><body><h1>Hello %s!</h1> <h3>Eagle WebService is Live!</h3></body></html>" % settings.DB_NAME
    connection = pg.connect(
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME
    )
    curs = connection.cursor()
    curs.execute('SELECT*FROM normasite')
    
    print(curs.fetchall())
    
    return HttpResponse(html)