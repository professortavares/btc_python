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


Referências:
- What is REST https://restfulapi.net/

- Richardson Maturity Model
https://martinfowler.com/articles/richardsonMaturityModel.html

- Markdown https://www.markdownguide.org/cheat-sheet/

- Criando ambientes virtual em python https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments



# Desafio do dia:

Modifique o API TODO-LIST para que:
1. Crie um teste de unidade de modo que uma tarefa não possa retroceder no status, ou seja, apenas são permitidas as seguintes mudanças (todo-> doing, doing->done)
1. Crie um teste de unidade, de modo que apenas seja possível excluir uma tarefa caso ela esteja no status ‘done’
1. Cada tarefa possua o status de conclusão (todo, doing e done)
1. Crie um atributo para indicar o momento em que uma tarefa mudou de status (todo-> doing, doing->done)
