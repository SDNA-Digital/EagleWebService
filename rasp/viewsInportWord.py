from django.http import HttpResponse
import docx2txt
import psycopg2 as pg
from django.conf import settings
import requests
import os

def InportWord(request, caminho, id, tabela, campo, indice):

    html = "<html><body>inportword</body></html>"
    
    save_link(caminho,"./tmp/temporary.docx")
    
    result = docx2txt.process('./tmp/temporary.docx')
    
    os.remove(os.path.join('./tmp/', "temporary.docx"))

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

def save_link(book_link, book_name):
    the_book = requests.get(book_link, stream=True)
    with open(book_name, 'wb') as f:
      for chunk in the_book.iter_content(1024 * 1024 * 2):  # 2 MB chunks
        f.write(chunk)