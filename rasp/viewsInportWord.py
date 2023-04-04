from django.http import HttpResponse
import docx2txt
import psycopg2 as pg
#import sys
from django.conf import settings

def InportWord(request, caminho, id, tabela, campo, indice):

    html = "<html><body>inportword</body></html>"

    #arquivo_caminho = sys.argv[1]
    #id = sys.argv[2]
    #print(arquivo_caminho)
    result = docx2txt.process(caminho)
    print(result)
    conn = pg.connect(
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME
    )

    curs = conn.cursor()
    query = (f"""Update {tabela} set {campo} = ('{result}') where {indice} = {id}""")
    print(query)
    curs.execute(query)
    conn.commit()

    return HttpResponse(html)