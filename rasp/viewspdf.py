import tika
import fitz
import psycopg2
from django.http import HttpResponse
from django.conf import settings

def Inportpdf(request, caminho, id, tabela, campo, indice):
    html = "<html><body>Done! %s </body></html>"

    import tika
    import psycopg2
    from tika import parser
    from django.http import HttpResponse
    raw = parser.from_file(caminho)
    dados = raw['content']
    print(dados)
    # conn = psycopg2.connect(
    #     host="localhost",
    #     database="DPP",
    #     user="postgres",
    #     password="3621"
    # )
    conn = pg.connect(
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME
    )
    curs = conn.cursor()
    query = (f"""Update {tabela} set {campo} = ('{dados}') where {indice} = {id}""")
    print(query)
    curs.execute(query)
    conn.commit()

    return HttpResponse(html)