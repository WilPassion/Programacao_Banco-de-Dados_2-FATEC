# instalando biblioteca

!pip install neo4j

# importando biblioteca - permite que você crie uma sessão ou conexão com um banco de dados Neo4
from neo4j import GraphDatabase

# credenciais - conectando ao BD
uri = "neo4j+s://93************ses.neo4j.io"
user = "neo4j"
password = "HtXWbhWsHO************fSlWPNz-gzS6QKUo"

driver = GraphDatabase.driver(uri, auth=(user, password))

"""**Arquivo - Mundo1**"""

# criando node Seleção
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Selecao {nome:'Brasil',cor:'Verde',cor:'Amarelo'})"))

'''

Abrindo uma Sessão:

- with driver.session() as session:: Abre uma sessão no banco de dados Neo4j. Isso permite que você execute operações no banco de dados.
Escrevendo uma Transação:

- session.write_transaction(...): Inicia uma transação de escrita no banco de dados. Isso é necessário para realizar operações que modificam o banco de dados, como a exclusão de relacionamentos.
Executando um Comando Cypher:

-lambda tx: tx.run(...): Uma função lambda que executa um comando Cypher dentro da transação.'''

# criando node Seleção
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Selecao {nome:'Argentina', cor: 'Azul', cor: 'Branco'})"))

# criando node Seleção
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Selecao {nome:'Uruguai', cor: 'Azul', cor: 'Branco'})"))

# criando node Seleção
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Selecao {nome:'Franca', cor: 'Azul', cor: 'Branco', cor:'Vermelho'})"))

# criando node Seleção
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Selecao {nome:'Espanha', cor: 'Amarelo', cor: 'Vermelho'})"))

# criando node Seleção
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Selecao {nome:'Alemanha', cor: 'Amarelo', cor: 'Vermelho', cor:'Preto'})"))

# criando node Seleção
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Selecao {nome:'Inglaterra', cor: 'Vermelho', cor: 'Branco'})"))

# criando node Seleção
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Selecao {nome:'Italia', cor: 'Verde', cor: 'Vermelho', cor: 'Branco'})"))

# criando node Seleção
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Selecao {nome:'Estados Unidos', cor: 'Azul', cor: 'Vermelho', cor:'Branco'})"))

# criando node Seleção
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Selecao {nome:'Japao', cor: 'Vermelho', cor: 'Branco'})"))

# criando node Seleção
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Selecao {nome:'Nigeria', cor: 'Verde', cor: 'Branco'})"))

# criando node Seleção
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Selecao {cor: 'Vermelho', cor: 'Branco', nome:'Canada'})"))

# criando node Seleção
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Selecao {cor: 'Amarelo', cor: 'Vermelho', cor:'Azul', nome:'Colombia'})"))

# criando node Continente - América do Sul
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Continente {nome:'America do Sul'})"))

# criando node Continente - América do Norte
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Continente {nome:'America do Norte'})"))

# criando node Continente - América Central
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Continente {nome:'America Central'})"))

# criando node Continente - Europa
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Continente {nome:'Europa'})"))

# criando node Continente - Africa
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Continente {nome:'Africa'})"))

# criando node Continente - Ásia
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Continente {nome:'Asia'})"))

# criando node Continente - Oceania
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Continente {nome:'Oceania'})"))

# criando node Continente - Antartida
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE ( :Continente {nome:'Antardida'})"))

# consultando resultado inserção nodes
q1 = "MATCH (x) RETURN x"

# abrir seção para executar consulta
with driver.session() as session:
  result = session.run(q1)

  # processa resultados
  for record in result:
    node = record["x"]
    print(node)

# consulta labels "Seleção" com cor = 'Vermelho' OR 'Branco'
q1 = "MATCH (n:Selecao), (y:Selecao) WHERE n.cor = 'Vermelho' OR y.cor = 'Branco' RETURN n, y"

# abrir seção para executar consulta
with driver.session() as session:
    result = session.run(q1)

    # processa resultados
    for record in result:
        node_n = record["n"]
        node_y = record["y"]
        print(f"Node n: {node_n}\nNode y: {node_y}")

# consulta labels "Seleção" com cor = 'Vermelho' AND 'Branco'
q1 = "MATCH (n:Selecao), (y:Selecao) WHERE n.cor = 'Vermelho' AND y.cor = 'Branco' RETURN n, y"

# abrir seção para executar consulta
with driver.session() as session:
    result = session.run(q1)

    # processa resultados
    for record in result:
        node_n = record["n"]
        node_y = record["y"]
        print(f"Node n: {node_n}\nNode y: {node_y}")

# deletando nodes
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (n) DETACH DELETE n"))

# consultando nodes - confirmando delete
q1 = "MATCH (x) RETURN x"

# abrir seção para executar consulta
with driver.session() as session:
  result = session.run(q1)

  # processa resultados
  for record in result:
    node = record["x"]
    print(node)

"""**Arquivo - Mundo2**"""

# add node Selecao
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Selecao {nome: 'Brasil', cores: ['Verde', 'Amarelo']})"))

# add node Selecao
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Selecao {nome: 'Argentina', cores: ['Azul', 'Branco']})"))

# add node Selecao
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Selecao {nome: 'Uruguai', cores: ['Azul', 'Branco']})"))

# add node Selecao
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Selecao {nome: 'Franca', cores: ['Azul', 'Branco', 'Vermelho']})"))

# add node Selecao
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Selecao {nome: 'Espanha', cores: ['Amarelo', 'Vermelho']})"))

# add node Selecao
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Selecao {nome: 'Alemanha', cores: ['Amarelo', 'Vermelho', 'Preto']})"))

# add node Selecao
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Selecao {nome: 'Inglaterra', cores: ['Vermelho', 'Branco']})"))

# add node Selecao
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Selecao {nome: 'Italia', cores: ['Verde', 'Vermelho', 'Branco']})"))

# add node Selecao
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Selecao {nome: 'Estados Unidos', cores: ['Azul', 'Vermelho', 'Branco']})"))

# add node Selecao
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Selecao {nome: 'Japao', cores: ['Vermelho', 'Branco']})"))

# add node Selecao
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Selecao {nome: 'Nigeria', cores: ['Verde', 'Branco']})"))

# add node Selecao
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Selecao {nome: 'Canada', cores: ['Vermelho', 'Branco']})"))

# add node Selecao
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Selecao {nome: 'Colombia', cores: ['Amarelo', 'Vermelho', 'Azul']})"))

# add node Continente
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Continente {nome: 'America do Sul'})"))

# add node Continente
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Continente {nome: 'America do Norte'})"))

# add node Continente
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Continente {nome: 'America Central'})"))

# add node Continente
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Continente {nome: 'Europa'})"))

# add node Continente
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Continente {nome: 'Africa'})"))

# add node Continente
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Continente {nome: 'Asia'})"))

# add node Continente
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Continente {nome: 'Oceania'})"))

# add node Continente
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (:Continente {nome: 'Antartida'})"))

# node com label 'Selecao' e propriedades "Branco" e "Vermelho"
q1 = "MATCH (s:Selecao) WHERE ALL(cor IN ['Branco', 'Vermelho'] WHERE cor IN s.cores) RETURN s"

# abrir seção para consulta e executá-la
with driver.session() as session:
    result = session.run(q1)

    # processa resultados
    for record in result:
        node = record["s"]
        print(node)

# node com label 'Selecao' e propriedades "Roxo" AND (WHERE ALL) "Vermelho"
q1 = "MATCH (s:Selecao) WHERE ALL(cor IN ['Roxo', 'Vermelho'] WHERE cor IN s.cores) RETURN s"

# abrir seção para consulta e executá-la
with driver.session() as session:
    result = session.run(q1)

    # processa resultados
    for record in result:
        node = record["s"]
        print(node)

# SEM SAÍDA ---> WHERE ALL = AND

# WHERE ANY = OR - Retornar Selecao e propriedades "Roxo" OU "Vermelhor"
q1 = "MATCH (s:Selecao) WHERE ANY (cor IN ['Roxo', 'Vermelho'] WHERE cor IN s.cores) RETURN s"

# Abrir uma sessão e executar a consulta
with driver.session() as session:
    result = session.run(q1)

    # Processar os resultados
    for record in result:
        node = record["s"]
        print(node)

"""**Criando Relacionamentos**"""

# consulta labels "Selecao" "Continente", cujo nome seja "Colombia" e "América do Sul"
q1 = "MATCH (p:Selecao), (c:Continente) WHERE p.nome = 'Colombia' AND c.nome = 'America do Sul' RETURN p, c"

# abrir seção para consulta
with driver.session() as session:
  result = session.run(q1)

  # processar resultados
  for record in result:
    node_n = record["p"]
    node_y = record["c"]
    print(f"Node n: {node_n}\nNode y: {node_y}")

# criando Relacionemnto entre Colómbia e América do Sul
with driver.session() as session:
  session.write_transaction(lambda tx: tx.run("MATCH (p:Selecao), (c:Continente) WHERE p.nome = 'Colombia' AND c.nome = 'America do Sul' CREATE (p)-[r:Pertence]->(c) RETURN p, c, r"))

# Verifica relacionamento criado
q1 = "MATCH (p:Selecao)-[r:Pertence]->(c:Continente) WHERE p.nome = 'Colombia' AND c.nome = 'America do Sul' RETURN p, r, c"

# abrir seção para consulta
with driver.session() as session:
    result = session.run(q1)

    # processar resultados
    for record in result:
        node_p = record["p"]
        relationship_r = record["r"]
        node_c = record["c"]

        # print
        print(f"Node p: {node_p}")
        print(f"Relationship r: {relationship_r}")
        print(f"Node c: {node_c}")
        print()

# criando relacionamento - 'America do Sul' x 'Colombia'
with driver.session() as session:
  session.write_transaction(lambda tx: tx.run("MATCH (p:Selecao), (c:Continente) WHERE p.nome = 'Colombia' AND c.nome = 'America do Sul' CREATE (p)<-[r:Contem]-(c) RETURN p, c, r"))

# Verifica relacionamento criado - Contem
q1 = "MATCH (p:Selecao)-[r:Pertence]->(c:Continente) WHERE p.nome = 'Colombia' AND c.nome = 'America do Sul' RETURN p, r, c"

# abrir seção para consulta
with driver.session() as session:
    result = session.run(q1)

    # processar resultados
    for record in result:
        node_p = record["p"]
        relationship_r = record["r"]
        node_c = record["c"]

        # print
        print(f"Node p: {node_p}")
        print(f"Relationship r: {relationship_r}")
        print(f"Node c: {node_c}")
        print()

# consultando resultado inserção nodes
q1 = "MATCH (x) RETURN x"

# abrir seção para executar consulta
with driver.session() as session:
  result = session.run(q1)

  # processa resultados
  for record in result:
    node = record["x"]
    print(node)

# Busca node 'Colombia' e o node 'America do Sul'
q1 = "MATCH (n:Selecao), (c:Continente) WHERE n.nome = 'Colombia' AND c.nome = 'America do Sul' RETURN n, c"

# abrir seção para consulta
with driver.session() as session:
    result = session.run(q1)

    # processar resultados
    for record in result:
        node_n = record["n"]  # Mudou de node_p para node_n
        node_c = record["c"]

        # print
        print(f"Node n: {node_n}")
        print(f"Node c: {node_c}")

# Verifica relacionamento criado - Contem
q1 = "MATCH (p:Selecao)-[r:Pertence]->(c:Continente) WHERE p.nome = 'Colombia' AND c.nome = 'America do Sul' RETURN p, r, c"

# abrir seção para consulta
with driver.session() as session:
    result = session.run(q1)

    # processar resultados
    for record in result:
        node_p = record["p"]
        relationship_r = record["r"]
        node_c = record["c"]

        # print
        print(f"Node p: {node_p}")
        print(f"Relationship r: {relationship_r}")
        print(f"Node c: {node_c}")
        print()

"""**Arquivo - Mundo3 (Criando Relacionamentos)**"""

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Colombia' AND c.nome = 'America do Sul' CREATE (p)<-[r:Contem]-(c) RETURN p, c, r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Brasil' AND c.nome = 'America do Sul' CREATE (p)-[r:Pertence]->(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Argentina' AND c.nome = 'America do Sul' CREATE (p)-[r:Pertence]->(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Uruguai' AND c.nome = 'America do Sul' CREATE (p)-[r:Pertence]->(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Franca' AND c.nome = 'Europa' CREATE (p)-[r:Pertence]->(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Espanha' AND c.nome = 'Europa' CREATE (p)-[r:Pertence]->(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Alemanha' AND c.nome = 'Europa' CREATE (p)-[r:Pertence]->(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Inglaterra' AND c.nome = 'Europa' CREATE (p)-[r:Pertence]->(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Italia' AND c.nome = 'Europa' CREATE (p)-[r:Pertence]->(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Colombia' AND c.nome = 'America do Sul' CREATE (p)-[r:Pertence]->(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Estados Unidos' AND c.nome = 'America do Norte' CREATE (p)-[r:Pertence]->(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Japao' AND c.nome = 'Asia' CREATE (p)-[r:Pertence]->(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Nigeria' AND c.nome = 'Africa' CREATE (p)-[r:Pertence]->(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Canada' AND c.nome = 'America do Norte' CREATE (p)-[r:Pertence]->(c) RETURN p,c,r"))

"""**Arquivo - Mundo4**"""

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Colombia' and c.nome = 'America do Sul' CREATE (p)<-[r:Contem]-(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Brasil' and c.nome = 'America do Sul' CREATE (p)<-[r:Contem]-(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Argentina' and c.nome = 'America do Sul' CREATE (p)<-[r:Contem]-(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Uruguai' and c.nome = 'America do Sul' CREATE (p)<-[r:Contem]-(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Franca' and c.nome = 'Europa' CREATE (p)<-[r:Contem]-(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Espanha' and c.nome = 'Europa' CREATE (p)<-[r:Contem]-(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Alemanha' and c.nome = 'Europa' CREATE (p)<-[r:Contem]-(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Inglaterra' and c.nome = 'Europa' CREATE (p)<-[r:Contem]-(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Italia' and c.nome = 'Europa' CREATE (p)<-[r:Contem]-(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Colombia' and c.nome = 'America do Sul' CREATE (p)<-[r:Contem]-(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Estados Unidos' and c.nome = 'America do Norte' CREATE (p)<-[r:Contem]-(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Estados Unidos' and c.nome = 'America do Norte' CREATE (p)<-[r:Contem]-(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Japao' and c.nome = 'Asia' CREATE (p)<-[r:Contem]-(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Nigeria' and c.nome = 'Africa' CREATE (p)<-[r:Contem]-(c) RETURN p,c,r"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (p: Selecao), (c:Continente) WHERE p.nome = 'Canada' and c.nome = 'America do Norte' CREATE (p)<-[r:Contem]-(c) RETURN p,c,r"))

# consultando resultado inserção nodes
q1 = "MATCH (x) RETURN x"

# abrir seção para executar consulta
with driver.session() as session:
  result = session.run(q1)

  # processa resultados
  for record in result:
    node = record["x"]
    print(node)

# verifica todos relacionamentos criados
q1 = """
MATCH (p:Selecao)-[r:Pertence]->(c:Continente)
RETURN p, c, r
UNION
MATCH (p:Selecao)<-[r:Contem]-(c:Continente)
RETURN p, c, r
"""

# abrir seção para consulta
with driver.session() as session:
    result = session.run(q1)

    # processar resultados
    for record in result:
        node_p = record["p"]
        relationship_r = record["r"]
        node_c = record["c"]

        # print
        print(f"Node p: {node_p}")
        print(f"Relationship r: {relationship_r}")
        print(f"Node c: {node_c}")
        print()

# contando relacionamentos
q1 = '''MATCH (p:Selecao)-[r:Pertence]->(c:Continente)
RETURN p, c, r
UNION
MATCH (c:Continente)-[r:Contem]->(p:Selecao)
RETURN p, c, r'''

# Abrir uma sessão e executar a consulta
with driver.session() as session:
    result = session.run(q1)

    # Processar os resultados
    count = 0
    for record in result:
        node_p = record["p"]
        node_c = record["c"]
        relationship_r = record["r"]

        count += 1

# saída - 31
print(f"Total de itens retornados: {count}")

# consultando nodes
q1 = '''MATCH (p: Selecao), (c: Continente)
WHERE p.nome = 'Colombia'
AND c.nome = 'America do Sul'
RETURN p, c'''

# Abrir uma sessão e executar a consulta
with driver.session() as session:
    result = session.run(q1)

    # Processar os resultados
    for record in result:
        node_p = record["p"]
        node_c = record["c"]

        # Imprimir cada nó
        print(f"Node p: {node_p}")
        print(f"Node c: {node_c}")

# excluindo excesso de relacionamentos
with driver.session() as session:
    session.write_transaction(
        lambda tx: tx.run(
            """
            MATCH (s:Selecao)-[r:Pertence]->(c:Continente)
            WHERE s.nome = 'Colombia' AND c.nome = 'America do Sul'
            DELETE r
            RETURN s, c
            """
        )
    )

# excluindo excesso de relacionamentos - parte oposta aos do bloco acima
with driver.session() as session:
    session.write_transaction(
        lambda tx: tx.run(
            """
            MATCH (s:Selecao)<-[r:Contem]-(c:Continente)
            WHERE s.nome = 'Colombia' AND c.nome = 'America do Sul'
            DELETE r
            RETURN s, c
            """
        )
    )

# printando relacionamentos
q1 = """
MATCH (p:Selecao)-[r:Pertence]->(c:Continente)
RETURN p, c, r
UNION
MATCH (p:Selecao)<-[r:Contem]-(c:Continente)
RETURN p, c, r
"""

# abrir seção para consulta
with driver.session() as session:
    result = session.run(q1)

    # processar resultados
    for record in result:
        node_p = record["p"]
        relationship_r = record["r"]
        node_c = record["c"]

        # print
        print(f"Node p: {node_p}")
        print(f"Relationship r: {relationship_r}")
        print(f"Node c: {node_c}")
        print()

# contando relacionamentos
q1 = '''MATCH (p:Selecao)-[r:Pertence]->(c:Continente)
RETURN p, c, r
UNION
MATCH (c:Continente)-[r:Contem]->(p:Selecao)
RETURN p, c, r'''

# Abrir uma sessão e executar a consulta
with driver.session() as session:
    result = session.run(q1)

    # Processar os resultados
    count = 0
    for record in result:
        node_p = record["p"]
        node_c = record["c"]
        relationship_r = record["r"]

        count += 1

# saída --> 2 relacionamentos excluídos - 25
print(f"Total de itens retornados: {count}")

# Criando relacionamento 'Contem' e 'Pertence' de Colombia - America do Sul
# [r:Pertence]
with driver.session() as session:
    session.write_transaction(
        lambda tx: tx.run(
            '''
            MATCH (s:Selecao), (c:Continente)
            WHERE s.nome = 'Colombia'
            AND c.nome = 'America do Sul'
            CREATE (s)-[r:Pertence]->(c)
            RETURN s, c, r
            '''
        )
    )

# Criando relacionamento 'Contem' e 'Pertence' de Colombia - America do Sul
# [r:Contem] --> lado oposto
with driver.session() as session:
    session.write_transaction(
        lambda tx: tx.run(
            '''
            MATCH (s:Selecao), (c:Continente)
            WHERE s.nome = 'Colombia'
            AND c.nome = 'America do Sul'
            CREATE (s)<-[r:Contem]-(c)
            RETURN s, c, r
            '''
        )
    )

# consulta aos nodes
q1 = "MATCH (n) RETURN n"

#abrindo seção
with driver.session() as session:
    result = session.run(q1)

    # processar result
    for record in result:
        node = record["n"]
        print(node)

# removendo nodes (outliers) - America Central, Antartida e Oceania

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (c:Continente {nome: 'Antartida'}) DETACH DELETE c"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (c:Continente {nome: 'America Central'}) DETACH DELETE c"))

with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (c:Continente {nome: 'Oceania'}) DETACH DELETE c"))

# checando remoção dos nodes
# consulta final aos nodes
q1 = "MATCH (n) RETURN n"

#abrindo seção
with driver.session() as session:
    result = session.run(q1)

    # processar result
    for record in result:
        node = record["n"]
        print(node)

# printando relacionamentos
q1 = """
MATCH (p:Selecao)-[r:Pertence]->(c:Continente)
RETURN p, c, r
UNION
MATCH (p:Selecao)<-[r:Contem]-(c:Continente)
RETURN p, c, r
"""

# abrir seção para consulta
with driver.session() as session:
    result = session.run(q1)

    # processar resultados
    for record in result:
        node_p = record["p"]
        relationship_r = record["r"]
        node_c = record["c"]

        # print
        print(f"Node p: {node_p}")
        print(f"Relationship r: {relationship_r}")
        print(f"Node c: {node_c}")
        print()

# criando node
with driver.session() as session:
    session.write_transaction(
        lambda tx: tx.run(
            "CREATE (:Selecao {nome: 'Portugal', cores: ['Verde', 'Vermelho', 'Amarelo', 'Branco', 'Azul']})"
        )
    )

# checando node criado
q1 = "MATCH (n) RETURN n"

#abrindo seção
with driver.session() as session:
    result = session.run(q1)

    # processar result
    for record in result:
        node = record["n"]
        print(node)

# Criando relacionamento:
# Europa CONTEM Portugal
# Portugal PERTENCE a Europa
with driver.session() as session:
    session.write_transaction(
        lambda tx: tx.run(
            "MATCH (s:Selecao), (c:Continente) WHERE s.nome = 'Portugal' AND c.nome = 'Europa' CREATE (s)-[r:Pertence]->(c) RETURN s, c, r"
        )
    )

# Criando o relacionamento do outro lado
with driver.session() as session:
    session.write_transaction(
        lambda tx: tx.run(
            "MATCH (s:Selecao), (c:Continente) WHERE s.nome = 'Europa' CREATE (s)<-[r:Contem]-(c) RETURN s, c, r"
        )
    )

# checando node
q1 = "MATCH (n) RETURN n"

#abrindo seção
with driver.session() as session:
    result = session.run(q1)

    # processar result
    for record in result:
        node = record["n"]
        print(node)

# printando relacionamentos
q1 = """
MATCH (p:Selecao)-[r:Pertence]->(c:Continente)
RETURN p, c, r
UNION
MATCH (p:Selecao)<-[r:Contem]-(c:Continente)
RETURN p, c, r
"""

# abrir seção para consulta
with driver.session() as session:
    result = session.run(q1)

    # processar resultados
    for record in result:
        node_p = record["p"]
        relationship_r = record["r"]
        node_c = record["c"]

        # print
        print(f"Node p: {node_p}")
        print(f"Relationship r: {relationship_r}")
        print(f"Node c: {node_c}")
        print()

# criando node
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("CREATE (Terra {nome: 'Terra'})"))

# estabelecendo relacionamento
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (m:Terra), (c:Continente) WHERE c.nome <> 'Terra' CREATE (m)-[:CONTÉM]->(c)"))

# pritando relacionamentos criados acima
q1 = "MATCH (n)-[r]-(m) RETURN n, r, m"

#abrindo seção
with driver.session() as session:
    result = session.run(q1)

    # processar result
    for record in result:
        node.n = record["n"]
        node.m = record["m"]
        relationship_r = record["r"]

        # print
        print(f"Node n: {node.n}")
        print(f"Relationship r: {relationship_r}")
        print(f"Node m: {node.m}")
        print()

q1 = "MATCH (n) RETURN n"

#abrindo seção
with driver.session() as session:
    result = session.run(q1)

    # processar result
    for record in result:
        node = record["n"]
        print(node)

# deletando relação Terra
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (:Terra)-[r]-() DELETE r"))

# Deletando node - Terra
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (m:Terra) DELETE m"))

q1 = "MATCH (n) RETURN n"

#abrindo seção
with driver.session() as session:
    result = session.run(q1)

    # processar result
    for record in result:
        node = record["n"]
        print(node)

# apagando tudo
with driver.session() as session:
    session.write_transaction(lambda tx: tx.run("MATCH (n) DETACH DELETE (n)"))

driver.close()