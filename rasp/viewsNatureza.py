from django.http import HttpResponse
import pandas as pd
import pyodbc

def import_natureza_atividade(request):
  html = "<html><body>Natureza de atividade importada</body></html>"
  

  tipos_grupos = {
      "Familia": 1,
      "GrandeGrupo": 2,
      "Ocupacao": 3,
      "PerfiOcupacional": 4,
      "Sinonimo": 5,
      "SubGrupoPrincipal": 6,
      "SubGrupo": 7,
  }

  DadosCon = ("Driver={SQL SERVER};" "Server=lucas\sqlexpress;" "Database=EagleV2;" "Trusted_connection = yes;")
  # DadosCon = ("Driver={SQL SERVER};" "Server=lucas\sqlexpress;" "Database=Teste_Scrapper;" "Trusted_connection = yes;")
  Con = pyodbc.connect(DadosCon)
  cursor = Con.cursor()
  print("Conexão Bem Sucedida")

  def InserirGrupo(grupo, tipo):
      for row in range(0,len(grupo)):
          codigo = grupo['CODIGO'][row]
          titulo = str(grupo['TITULO'][row]).strip().capitalize()

          query = f"""
              select NaturezaAtividadeDescricao from NaturezaAtividade
              where NaturezaAtividadeDescricao = '{titulo}'
              and NaturezaAtividadeTipo = '{tipo}'
          """

          cursor.execute(query)
          resultados = cursor.fetchall()
          
          encontrado = False

          for x in resultados:
              print('Bingo! Name: ' + titulo)
              encontrado = True

          if not encontrado:
              query = f"""INSERT INTO NaturezaAtividade(NaturezaAtividadeDescricao, NaturezaAtividadeAtivo, NaturezaAtividadeCodigo, NaturezaAtividadeTipo)
                  VALUES
                  ('{titulo}', 'A', '{codigo}', '{tipo}')"""
              cursor.execute(query)
              cursor.commit()

  file_names = [
      "Familia",
      "GrandeGrupo",
      "Ocupacao",
      # "PerfiOcupacional",
      "Sinonimo",
      "SubGrupoPrincipal",
      "SubGrupo"
  ]

  for name in file_names:
      uri = f"C:\\model\\ESTRUTURACBO\\{name}.csv"
      grupo = pd.read_csv(uri, sep= ";", encoding='latin-1')
      print("\n---------- "+ name +" ----------\n")

      InserirGrupo(grupo=grupo, tipo=tipos_grupos[name])
    
  return HttpResponse(html)
  