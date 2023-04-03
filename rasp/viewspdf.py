import tika
import fitz
import psycopg2
from django.http import HttpResponse

def Inportpdf(request, caminho, id, tabela, campo, indice):
    html = "<html><body>Done! %s </body></html>"

    import tika
    import psycopg2
    from tika import parser
    from django.http import HttpResponse
    raw = parser.from_file(caminho)
    dados = raw['content']
    print(dados)
    conn = psycopg2.connect(
        host="localhost",
        database="DPP",
        user="postgres",
        password="3621"
    )
    curs = conn.cursor()
    query = (f"""Update {tabela} set {campo} = ('{dados}') where {indice} = {id}""")
    print(query)
    curs.execute(query)
    conn.commit()

    return HttpResponse(html)