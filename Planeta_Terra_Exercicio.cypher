// CRIANDO NODES - SELEÇÃO

// Criar a seleção Brasil com as cores Verde e Amarelo
CREATE (:Selecao {nome: 'Brasil', cor: 'Verde', cor: 'Amarelo'})

// Criar a seleção Argentina com as cores Azul e Branco
CREATE (:Selecao {nome: 'Argentina', cor: 'Azul', cor: 'Branco'})

// Criar a seleção Uruguai com as cores Azul e Branco
CREATE (:Selecao {nome: 'Uruguai', cor: 'Azul', cor: 'Branco'})

// Criar a seleção França com as cores Azul, Branco e Vermelho
CREATE (:Selecao {nome: 'Franca', cor: 'Azul', cor: 'Branco', cor: 'Vermelho'})

// Criar a seleção Espanha com as cores Amarelo e Vermelho
CREATE (:Selecao {nome: 'Espanha', cor: 'Amarelo', cor: 'Vermelho'})

// Criar a seleção Alemanha com as cores Amarelo, Vermelho e Preto
CREATE (:Selecao {nome: 'Alemanha', cor: 'Amarelo', cor: 'Vermelho', cor: 'Preto'})

// Criar a seleção Inglaterra com as cores Vermelho e Branco
CREATE (:Selecao {nome: 'Inglaterra', cor: 'Vermelho', cor: 'Branco'})

// Criar a seleção Itália com as cores Verde, Vermelho e Branco
CREATE (:Selecao {nome: 'Italia', cor: 'Verde', cor: 'Vermelho', cor: 'Branco'})

// Criar a seleção Estados Unidos com as cores Azul, Vermelho e Branco
CREATE (:Selecao {nome: 'Estados Unidos', cor: 'Azul', cor: 'Vermelho', cor: 'Branco'})

// Criar a seleção Japão com as cores Vermelho e Branco
CREATE (:Selecao {nome: 'Japao', cor: 'Vermelho', cor: 'Branco'})

// Criar a seleção Nigéria com as cores Verde e Branco
CREATE (:Selecao {nome: 'Nigeria', cor: 'Verde', cor: 'Branco'})

// Criar a seleção Canadá com as cores Vermelho e Branco
CREATE (:Selecao {nome: 'Canada', cor: 'Vermelho', cor: 'Branco'})

// Criar a seleção Colômbia com as cores Amarelo, Vermelho e Azul
CREATE (:Selecao {nome: 'Colombia', cor: 'Amarelo', cor: 'Vermelho', cor: 'Azul'})

// criando nodes - CONTINENTE

// Criar o continente América do Sul
CREATE (:Continente {nome: 'America do Sul'})

// Criar o continente América do Norte
CREATE (:Continente {nome: 'America do Norte'})

// Criar o continente América Central
CREATE (:Continente {nome: 'America Central'})

// Criar o continente Europa
CREATE (:Continente {nome: 'Europa'})

// Criar o continente África
CREATE (:Continente {nome: 'Africa'})

// Criar o continente Ásia
CREATE (:Continente {nome: 'Asia'})

// Criar o continente Oceania
CREATE (:Continente {nome: 'Oceania'})

// Criar o continente Antártida
CREATE (:Continente {nome: 'Antartida'})

/////////////////////////////////////////////////////////////////////////////////// 

// consultando nodes criados
MATCH (n) RETURN n

/////////////////////////////////////////////////////////////////////////////////// 

// consulta labels "Seleção" com cor = 'Vermelho' OR 'Branco'
MATCH (n:Selecao), (y:Selecao) 
WHERE n.cor = 'Vermelho' OR y.cor = 'Branco' RETURN n, y

// consulta labels "Seleção" com cor = 'Vermelho' AND 'Branco'
MATCH (n:Selecao), (y:Selecao) 
WHERE n.cor = 'Vermelho' AND y.cor = 'Branco'
RETURN n, y

/////////////////////////////////////////////////////////////////////////////////// 

// deletando nodes - DETACH 
MATCH (n) DETACH DELETE n

// consultando nodes - confirmando delete
MATCH (x) RETURN x

/////////////////////////////////////////////////////////////////////////////////// 

// add node - SELEÇÃO
CREATE (:Selecao {nome: 'Brasil', cores: ['Verde', 'Amarelo']})

// add node - SELEÇÃO
CREATE (:Selecao {nome: 'Argentina', cores: ['Azul', 'Branco']})

// add node - SELEÇÃO
CREATE (:Selecao {nome: 'Uruguai', cores: ['Azul', 'Branco']})

// add node - SELEÇÃO
CREATE (:Selecao {nome: 'Franca', cores: ['Azul', 'Branco', 'Vermelho']})

// add node - SELEÇÃO
CREATE (:Selecao {nome: 'Espanha', cores: ['Amarelo', 'Vermelho']})

// add node - SELEÇÃO
CREATE (:Selecao {nome: 'Alemanha', cores: ['Amarelo', 'Vermelho', 'Preto']})

// add node - SELEÇÃO
CREATE (:Selecao {nome: 'Inglaterra', cores: ['Vermelho', 'Branco']})

// add node - SELEÇÃO
CREATE (:Selecao {nome: 'Italia', cores: ['Verde', 'Vermelho', 'Branco']})

// add node - SELEÇÃO
CREATE (:Selecao {nome: 'Estados Unidos', cores: ['Azul', 'Vermelho', 'Branco']})

// add node - SELEÇÃO
CREATE (:Selecao {nome: 'Japao', cores: ['Vermelho', 'Branco']})

// add node - SELEÇÃO
CREATE (:Selecao {nome: 'Nigeria', cores: ['Verde', 'Branco']})

// add node - SELEÇÃO
CREATE (:Selecao {nome: 'Canada', cores: ['Vermelho', 'Branco']})

// add node - SELEÇÃO
CREATE (:Selecao {nome: 'Colombia', cores: ['Amarelo', 'Vermelho', 'Azul']});

// add node - CONTINENTE
CREATE (:Continente {nome: 'America do Sul'})

// add node - CONTINENTE
CREATE (:Continente {nome: 'America do Norte'})

// add node - CONTINENTE
CREATE (:Continente {nome: 'America Central'})

// add node - CONTINENTE
CREATE (:Continente {nome: 'Europa'})

// add node - CONTINENTE
CREATE (:Continente {nome: 'Africa'})

// add node - CONTINENTE
CREATE (:Continente {nome: 'Asia'})

// add node - CONTINENTE
CREATE (:Continente {nome: 'Oceania'})

// add node - CONTINENTE
CREATE (:Continente {nome: 'Antartida'})

/////////////////////////////////////////////////////////////////////////////////// 

// node com label 'Selecao' e propriedades "Branco" e "Vermelho"
MATCH (s:Selecao) 
WHERE ALL(cor IN ['Branco', 'Vermelho'] 
WHERE cor IN s.cores) 
RETURN s

// node com label 'Selecao' e propriedades "Roxo" AND (WHERE ALL) "Vermelho"
MATCH (s:Selecao) WHERE ALL(cor IN ['Roxo', 'Vermelho'] WHERE cor IN s.cores) RETURN s

// WHERE ANY = OR - Retornar Selecao e propriedades "Roxo" OU "Vermelho"
MATCH (s:Selecao) WHERE ANY (cor IN ['Roxo', 'Vermelho'] WHERE cor IN s.cores) RETURN s

// consulta labels "Selecao" "Continente", cujo nome seja "Colombia" e "América do Sul"
MATCH (p:Selecao), (c:Continente) WHERE p.nome = 'Colombia' AND c.nome = 'America do Sul' RETURN p, c

/////////////////////////////////////////////////////////////////////////////////// 

// criando Relacionemnto entre Colómbia e América do Sul;
MATCH (p:Selecao), (c:Continente) WHERE p.nome = 'Colombia' AND c.nome = 'America do Sul' CREATE (p)-[r:Pertence]->(c) RETURN p, c, r

// Verifica relacionamento criado
MATCH (p:Selecao)-[r:Pertence]->(c:Continente) WHERE p.nome = 'Colombia' AND c.nome = 'America do Sul' RETURN p, r, c

// Verifica relacionamento criado - PERTENCE
MATCH (p:Selecao)-[r:Pertence]->(c:Continente) WHERE p.nome = 'Colombia' AND c.nome = 'America do Sul' RETURN p, r, c

/////////////////////////////////////////////////////////////////////////////////// 

// consultando resultado inserção nodes
MATCH (x) RETURN x;

// Busca node 'Colombia' e o node 'America do Sul'
MATCH (n:Selecao), (c:Continente) 
WHERE n.nome = 'Colombia' AND c.nome = 'America do Sul' 
RETURN n, c

// Verifica relacionamento criado - PERTENCE
MATCH (p:Selecao)-[r:Pertence]->(c:Continente) 
WHERE p.nome = 'Colombia' AND c.nome = 'America do Sul' 
RETURN p, r, c

/////////////////////////////////////////////////////////////////////////////////// 

// RELACIONAMENTOS - País -> PERTENCE -> Continente

MATCH (p: Selecao), (c:Continente) 
WHERE p.nome = 'Colombia' AND c.nome = 'America do Sul' 
CREATE (p)<-[r:Contem]-(c) 
RETURN p, c, r


MATCH (p: Selecao), (c:Continente) 
WHERE p.nome = 'Brasil' and c.nome = 'America do Sul' 
CREATE (p)-[r:Pertence]->(c) 
RETURN p,c,r

MATCH (p: Selecao), (c:Continente) 
WHERE p.nome = 'Argentina' AND c.nome = 'America do Sul' 
CREATE (p)-[r:Pertence]->(c) 
RETURN p,c,r

MATCH (p: Selecao), (c:Continente) 
WHERE p.nome = 'Uruguai' and c.nome = 'America do Sul' 
CREATE (p)-[r:Pertence]->(c) 
RETURN p,c,r

MATCH (p: Selecao), (c:Continente) 
WHERE p.nome = 'Franca' AND c.nome = 'Europa' 
CREATE (p)-[r:Pertence]->(c) 
RETURN p,c,r

MATCH (p: Selecao), (c:Continente) 
WHERE p.nome = 'Espanha' AND c.nome = 'Europa' 
CREATE (p)-[r:Pertence]->(c) 
RETURN p,c,r

MATCH (p: Selecao), (c:Continente) 
WHERE p.nome = 'Alemanha' AND c.nome = 'Europa' 
CREATE (p)-[r:Pertence]->(c) 
RETURN p,c,r

MATCH (p: Selecao), (c:Continente) 
WHERE p.nome = 'Inglaterra' AND c.nome = 'Europa' 
CREATE (p)-[r:Pertence]->(c) 
RETURN p,c,r

MATCH (p: Selecao), (c:Continente) 
WHERE p.nome = 'Italia' AND c.nome = 'Europa' 
CREATE (p)-[r:Pertence]->(c) 
RETURN p,c,r

MATCH (p: Selecao), (c:Continente) 
WHERE p.nome = 'Colombia' AND c.nome = 'America do Sul' 
CREATE (p)-[r:Pertence]->(c) 
RETURN p,c,r

MATCH (p: Selecao), (c:Continente) 
WHERE p.nome = 'Estados Unidos' AND c.nome = 'America do Norte' 
CREATE (p)-[r:Pertence]->(c) 
RETURN p,c,r

MATCH (p: Selecao), (c:Continente) 
WHERE p.nome = 'Japao' AND c.nome = 'Asia' 
CREATE (p)-[r:Pertence]->(c) 
RETURN p,c,r

MATCH (p: Selecao), (c:Continente) 
WHERE p.nome = 'Nigeria' AND c.nome = 'Africa' 
CREATE (p)-[r:Pertence]->(c) 
RETURN p,c,r

MATCH (p: Selecao), (c:Continente) 
WHERE p.nome = 'Canada' AND c.nome = 'America do Norte' 
CREATE (p)-[r:Pertence]->(c) 
RETURN p,c,r

/////////////////////////////////////////////////////////////////////////////////// 

// Checando relacionamentos
MATCH (p:Selecao)-[r:Pertence]->(c:Continente)
RETURN p, c, r
UNION
MATCH (p:Selecao)<-[r:Contem]-(c:Continente)
RETURN p, c, r

// consultando nodes - 'Colombia' e 'America do Sul'
MATCH (p: Selecao), (c: Continente)
WHERE p.nome = 'Colombia'
AND c.nome = 'America do Sul'
RETURN p, c

/////////////////////////////////////////////////////////////////////////////////// 

// excluindo excesso de relacionamentos
MATCH (s:Selecao)-[r:Pertence]->(c:Continente)
WHERE s.nome = 'Colombia' AND c.nome = 'America do Sul'
DELETE r
RETURN s, c

// excluindo excesso de relacionamentos - parte oposta aos do bloco acima
MATCH (s:Selecao)<-[r:Contem]-(c:Continente)
WHERE s.nome = 'Colombia' AND c.nome = 'America do Sul'
DELETE r
RETURN s, c

// printando relacionamentos
MATCH (p:Selecao)-[r:Pertence]->(c:Continente)
RETURN p, c, r
UNION
MATCH (p:Selecao)<-[r:Contem]-(c:Continente)
RETURN p, c, r

// contando relacionamentos
MATCH (p:Selecao)-[r:Pertence]->(c:Continente)
RETURN p, c, r
UNION
MATCH (c:Continente)-[r:Contem]->(p:Selecao)
RETURN p, c, r

/////////////////////////////////////////////////////////////////////////////////// 

// Criando relacionamento 'Contem' e 'Pertence' de Colombia - America do Sul
// [r:Pertence]
MATCH (s:Selecao), (c:Continente)
WHERE s.nome = 'Colombia' AND c.nome = 'America do Sul'
CREATE (s)-[r:Pertence]->(c)
RETURN s, c, r

// Criando relacionamento 'Contem' e 'Pertence' de Colombia - America do Sul
// [r:Contem] --> lado oposto
MATCH (s:Selecao), (c:Continente)
WHERE s.nome = 'Colombia' AND c.nome = 'America do Sul'
CREATE (s)<-[r:Contem]-(c)
RETURN s, c, r

// consulta aos nodes
MATCH (n) RETURN n

/////////////////////////////////////////////////////////////////////////////////// 

// removendo nodes (outliers) - America Central, Antartida e Oceania
MATCH (c:Continente {nome: 'Antartida'}) DETACH DELETE c
MATCH (c:Continente {nome: 'America Central'}) DETACH DELETE c;
MATCH (c:Continente {nome: 'Oceania'}) DETACH DELETE c;

# checando remoção dos nodes
# consulta final aos nodes
MATCH (n) RETURN n

/////////////////////////////////////////////////////////////////////////////////// 

// criando node - Seleção
REATE (:Selecao {nome: 'Portugal', cores: ['Verde', 'Vermelho', 'Amarelo', 'Branco', 'Azul']})

// checando node criado
MATCH (n) RETURN n

// Criando relacionamento:
// Europa CONTEM Portugal
// Portugal PERTENCE a Europa
MATCH (s:Selecao), (c:Continente) WHERE s.nome = 'Portugal' AND c.nome = 'Europa' 
CREATE (s)-[r:Pertence]->(c)
RETURN s, c, r

// Criando o relacionamento do outro lado
MATCH (s:Selecao), (c:Continente) WHERE s.nome = 'Europa' CREATE (s)<-[r:Contem]-(c) RETURN s, c, r

// printando relacionamentos
MATCH (p:Selecao)-[r:Pertence]->(c:Continente)
RETURN p, c, r
UNION
MATCH (p:Selecao)<-[r:Contem]-(c:Continente)
RETURN p, c, r

/////////////////////////////////////////////////////////////////////////////////// 

// criando node - TERRA
CREATE (Terra {nome: 'Terra'})

// estabelecendo relacionamento
MATCH (m:Terra), (c:Continente) WHERE c.nome <> 'Terra' CREATE (m)-[:CONTÉM]->(c)

// pritando relacionamentos criados acima
MATCH (n)-[r]-(m) RETURN n, r, m

// consulta resultado
MATCH (n) RETURN n

/////////////////////////////////////////////////////////////////////////////////// 

// deletando relação Terra
MATCH (:Terra)-[r]-() DELETE r

// Deletando node - Terra
MATCH (m:Terra) DELETE m

// consulta resultado
MATCH (n) RETURN n

// apagando tudo
MATCH (n) DETACH DELETE (n)