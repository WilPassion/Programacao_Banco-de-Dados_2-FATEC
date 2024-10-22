                                                   MONGO DB COMPASS e SHELL

### **CREATE:**

* Criando coleção:

              Linha de comando --> db.createCollection("Big Data Para Negócios")

<img align="center" src="https://github.com/WilPassion/Programacao_Banco-de-Dados_2-FATEC/blob/main/MongoDB/img_Compass/criandoColecao.PNG" alt="criandoColecao" width="1000">  

-----------------------------------------

* Inserindo um documento:

              Linha de comando --> db.BigDataParaNegócios.insertOne({"Unidade":"Taboão da Serra"})
  
<img align="center" src="https://github.com/WilPassion/Programacao_Banco-de-Dados_2-FATEC/blob/main/MongoDB/img_Compass/insertDocsCompass1.PNG" alt="insertumdocumento" width="1000">  

<img align="center" src="https://github.com/WilPassion/Programacao_Banco-de-Dados_2-FATEC/blob/main/MongoDB/img_Compass/insertDocsCompass2.PNG" alt="insertumdocumento" width="1000"> 

<img align="center" src="https://github.com/WilPassion/Programacao_Banco-de-Dados_2-FATEC/blob/main/MongoDB/img_Compass/insertDocsCompass3.PNG" alt="insertumdocumento" width="1000"> 

* Inserindo muitos documentos:

              db.BigDataParaNegócios.insertMany([{"Unidade":"Jundiaí"},{"Unidade": "São Roque"}])

              -----------------------------------------


              db.BigDataParaNegocios.insertMany([
            
                  {"Unidade":"Santos", "Semestre":"1", "Anos":"2024"},
                  {"Unidade":"São Caetano do Sul","Curso":"Segurança da Informação"}
            
              ])
              -----------------------------------------

              db.BigDataParaNegocios.insertMany([
              {
                "Unidade:": "Jundiai"
              },
              {
                "Unidade": "São Roque"
              }
             ])




<img align="center" src="https://github.com/WilPassion/Programacao_Banco-de-Dados_2-FATEC/blob/main/MongoDB/img_Compass/insertManyDocsCompass1.PNG" alt="insertMuitosdocumentos" width="1000"> 

<img align="center" src="https://github.com/WilPassion/Programacao_Banco-de-Dados_2-FATEC/blob/main/MongoDB/img_Compass/insertManyDocsCompass2.PNG" alt="insertMuitosdocumentos" width="1000"> 

**Observações:**

• O _id é reservado para uso como chave primária  
• Nome dos campos não poder conter caractere NULL  
• Restrição de tamanho de documentos BSON = 16MB

-----------------------------------------

**Importando arquivos CSV/JSON:** 

img import
img

-----------------------------------------
### **READ:** 

**Aplicando filtros:** 


>• Filter – Utilizado para especificar qual >será a condição que os documentos devem atender para serem retornados na busca.
>
>• Sort – Especifica a ordem de classificação dos documentos retornados. 
>
>• Project – Especifica quais campos serão ou não retornados na consulta.
>
>• LIMIT – Especifica o máximo de linhas a serem retornados.
>
>• Project – Especifica quais campos serão ou não retornados na consulta.  

**Aplicando filtros (Chave e Valor) - Filter:**  

imgfilter1


**Aplicando filtros (Ordenação Ano Desc.) - Sort:**  

sort1

• Consulta por Ordenação Ano Cresc. -> Sort = {"Ano ": 1}  

• Consulta por Ordenação Ano Cresc. -> Sort = {"Ano ": 1}  

--------------------------------------

• Consulta/Printa sem o número do ID -> Project = { _id: 0 }  
  

**Aplicando filtro OR:** 

• Sintaxe -> {[$or:{"Valor1"}, {"Valor2"}]}

{$or:[{"Ano:":"2024"},{"Unidade": "São Caetano do Sul"}]}

**Aplicando filtro AND:**

• Sintaxe -> {[$and:{"Valor1"}, {"Valor2"}]}

{$and:[{"Curso": "Segurança da Informação"},{"Unidade": "São Caetano do Sul"}]}

**Aplicando filtro IN:**

• Considere uma coleção de documentos representando produtos, com campos como nome e categoria. Se você quiser encontrar todos os produtos que são da categoria "Eletrônicos" ou "Brinquedos", você pode usar o filtro IN da seguinte forma:

{ categoria: { $in: ["Eletrônicos", "Brinquedos"] } }

{"Ano": {$in: [2023,2028]}}

**Aplicando filtro GT (Greater Than):**

• Imagine que você tenha uma coleção de produtos com os campos nome e preço. Se você quiser encontrar todos os produtos com preço superior a 100 reais, você usaria a seguinte consulta:

{ campo: { $gt: valor } }
{ preço: { $gt: 100 } }

Nota - O uso das aspas no campo é opcional:

{"Ano": {$gt: 2024}} ou {Ano: {$gt: 2024}}

**Aplicando filtro LT (Lower Than):**

{Ano: {$lt: 2028}}  


{$and: [
	{Ano: {$lt: 2028}},
	{Ano: {$gt: 2020}}
]}

ou...

{$and: [ {Ano: {$lt: 2028}}, {Ano: {$gt: 2020}} ] }

**Aplicando filtro LTE (Less Than OR Equal):**

• Sintaxe -> { campo: { $lte: valor } }

{ preço: { $lte: 100 } }

• Para encontrar documentos que satisfaçam pelo menos uma das condições:

{
  $or: [
    {preço: {$lte: 50}},
    {categoria: "Eletronicos"}
  ]
}

**No SHELL:****************************

sintaxe_img

• Retorna todos docs da coleção -> db.BigDataParaNegocios.find()

**Aplicando filtros (Chave e Valor) - Filter:**  

db.BigDataParaNegocios.find({"Unidade:","Ipiranga"})

• Traz os resultados da consulta apenas com o campo apontado (Semestre): 

db.BigDataParaNegocios.find({}, {"Semestre":4})

find_chave_vazia

**Aplicando filtros (Ordenação Ano Desc.) - Sort:**  

sort1

                        • Consulta por Ordenação Ano Cresc. -> Sort = {"Ano ": 1}  


                        • Consulta por Ordenação Ano Cresc. -> Sort = {"Ano ": 1}  

--------------------------------------

• Consulta/Printa sem o número do ID:

                        db{ {"Unidade": "4"}, "_id": 0}
  

**Aplicando filtro OR:** 

• Sintaxe -> {[$or:{"Valor1"}, {"Valor2"}]}

{$or:[{"Ano:":"2024"},{"Unidade": "São Caetano do Sul"}]}

**Aplicando filtro AND:**

• Sintaxe -> {[$and:{"Valor1"}, {"Valor2"}]}

{$and:[{"Curso": "Segurança da Informação"},{"Unidade": "São Caetano do Sul"}]}

**Aplicando filtro IN:** ++++++

• Considere uma coleção de documentos representando produtos, com campos como nome e categoria. Se você quiser encontrar todos os produtos que são da categoria "Eletrônicos" ou "Brinquedos", você pode usar o filtro IN da seguinte forma:

{"Ano": {$in: [2023,2028]}}

**Aplicando filtro GT (Greater Than):**

• Imagine que você tenha uma coleção de produtos com os campos nome e preço. Se você quiser encontrar todos os produtos com preço superior a 100 reais, você usaria a seguinte consulta:

{ campo: { $gt: valor } }
{ preço: { $gt: 100 } }

Nota - O uso das aspas no campo é opcional:

{"Ano": {$gt: 2024}} ou {Ano: {$gt: 2024}}

**Aplicando filtro LT (Lower Than):**

{Ano: {$lt: 2028}}  


{$and: [
	{Ano: {$lt: 2028}},
	{Ano: {$gt: 2020}}
]}

ou...

{$and: [ {Ano: {$lt: 2028}}, {Ano: {$gt: 2020}} ] }

**Aplicando filtro LTE (Less Than OR Equal):**
-----------------------------------------
### **UPDATE:**

-----------------------------------------
### **DELETE:**
