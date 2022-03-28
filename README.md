# Bootcamp de python da Enacom

Código fonte para o bootcamp de Python da Enacom

## Requisitos mínimos:

Ambiente testado

- Ambiente Python - 3.9.7
- Sistema operacional: Ubuntu 20.04

## Ambiente virtual 

1. Criar o ambiente virtual:

```
$ python -m venv btc_python
```

2. Ativar o ambiente virtual

```
$ . btc_python/bin/activate
```

3. Instalar as bibliotecas necessárias para o ambiente funcionar

```
$ pip install -r requirements.txt
```

4. Para executar, utilize o seguinte comando:

```
$ uvicorn main:app --reload
```