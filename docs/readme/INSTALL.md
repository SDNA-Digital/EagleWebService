
## **Prerequisites**
-  **Python 3.9**
-  **Postman**. Download [HERE](https://www.postman.com/downloads/)

-------------------------------------------------------------------------------------------------------------------------------

### **Configure o Projeto**

Variáveis de desenvolvimento:

* Essas **credenciais** (informações sensíveis) são armazenadas no arquivo `.env`.

Por favor copie (não renomeie) `.env.credentials` e cria seu arquivo `.env`.
Em seguida altere as variáveis conforme seu uso.


## **Instalação**
1. **Clone o Repositório.**
``` bash
$ cd /path/to/EagleWebService
$ git clone https://github.com/SDNA-Digital/EagleWebService.git
```
### **Run with VSCode**

1. Por favor, instale as seguintes extensões do VSCode:

* Python
* Django

### **Run locally**
2. No terminal crie um ambiente virtual e o ative:
``` bash
$ python -m venv env
$ source env/bin/activate
```

3. Instale os pacotes obrigatórios:
```
$ pip install -r requirements.txt
```

4.  Para rodar a aplicação:
``` bash
$ python manage.py runserver
```

## Uso
Para iniciar o uso do projeto, é possível criar um superuser utilizando o seguinte comando (**Não Obrigatório**):
```
    python3 manage.py createsuperuser
```