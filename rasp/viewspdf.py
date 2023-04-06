import io
from django.http import HttpResponse
import psycopg2 as pg
from django.conf import settings
import requests
from PyPDF2 import PdfReader

def Inportpdf(request, caminho, id, tabela, campo, indice):
    html = "<html><body>Done!</body></html>"
    r = requests.get(caminho, stream=True)
    f = io.BytesIO(r.content)
    
    reader = PdfReader(f)
    texto = ''
    for pagina in reader.pages:
        texto += pagina.extract_text()
    
    conn = pg.connect(
        user=settings.DB_USER,
        password=settings.DB_PASSWORD,
        host=settings.DB_HOST,
        port=settings.DB_PORT,
        database=settings.DB_NAME
    )
    
    curs = conn.cursor()
    query = (f"""Update {tabela} set {campo} = ('{texto}') where {indice} = {id}""")
    
    print(query)
    curs.execute(query)
    conn.commit()
    return HttpResponse(html)