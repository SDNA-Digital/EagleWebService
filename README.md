<!--
    helpers -> funções onde não existe uso de serviço externo (Validação de CNPJ, Alguma regex ou algo do tipo)
    services -> Pasta onde as requests são feitas (Uma função onde recebe os parametros e faz a request para o local desejado)
    tools -> Faz o consumo dos services. Salva dados dentro das tabela. Trata os dados da ViewSet juntamente com o DB.
    assets -> Quando só a tool não for organização suficiente deve-se usar essa pasta ou criá-la
-->

# Welcome to Core!
[![Python](https://img.shields.io/badge/python-3.10-green)](https://www.python.org)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)
[![Service Port](https://img.shields.io/badge/Port-8000-yellow)]()

<p align="left">
    <img width=470 src="docs/images/darth-vader.gif">
</p>

## **Descrição do Projeto**
>
Esse projeto é destinado a montar um WebService, fornecendo serviços de raspagem de dados e outras interações de conteúdo relacionados ao DPP Eagle (Projeto da SDNA)
>

-------------------------------------------------------------------------------------------------------------------------------
## **Guias**
Aqui estão detalhadas o que é preciso para rodar o sistema localmente.

* **[Guia de Instalação](docs/readme/INSTALL.md)**
<!-- * **[Developing Guide](docs/readme/DEVELOP.md)**
* **[Deployment Guide](docs/readme/DEPLOY.md)**
* **[Postman Collection](docs/postman/postman_collection.json)** -->

-------------------------------------------------------------------------------------------------------------------------------
## **Links**

Os links abaixo funcionarão quando o app estiver rodando. Para autenticação básica do Django, por favor defina seu superuser local utilizando o seguinte comando: 
[createsuperuser](https://docs.djangoproject.com/en/2.2/intro/tutorial02/).

| Page                | Address                                                                                                                                  | Use                         | Authenticated |
|:--------------------|:-----------------------------------------------------------------------------------------------------------------------------------------|:----------------------------|:--------------|
| **Django Admin**        | [http://localhost:8000/admin](http://localhost:8000/admin)           | Django Admin                | Yes (Django)  |


-------------------------------------------------------------------------------------------------------------------------------
## **Guia de APIs e Endpoints**
| Page                | Endpoint `(Click to see the detailed description)`           | Short Description |
|:--------------------|:-----------------------------------|:--------------|
| **`Health`**         | **[api/health/](docs/routes_map/core/health/api_health.md)** | **Check the Application Health**  |
| **`Hello`**         | **[api/hello/](docs/routes_map/core/health/api_health.md)** | **Check the Application is running**  |
