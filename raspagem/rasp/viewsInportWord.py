from django.http import HttpResponse
import docx2txt
import psycopg2
#import sys

def InportWord(request, caminho, id, tabela, campo, indice):

    html = "<html><body>inportword</body></html>"

    #arquivo_caminho = sys.argv[1]
    #id = sys.argv[2]
    #print(arquivo_caminho)
    result = docx2txt.process(caminho)
    print(result)
    conn = psycopg2.connect(
        host="localhost",
        database="DPP",
        user="postgres",
        password="3621"
    )

    curs = conn.cursor()
    query = (f"""Update {tabela} set {campo} = ('{result}') where {indice} = {id}""")
    print(query)
    curs.execute(query)
    conn.commit()

    return HttpResponse(html)