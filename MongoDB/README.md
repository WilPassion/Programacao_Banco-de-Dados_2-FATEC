                                                   MONGO DB COMPASS

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

<img align="center" src="https://github.com/WilPassion/Programacao_Banco-de-Dados_2-FATEC/blob/main/MongoDB/img_Compass/insertManyDocsCompass1.PNG" alt="insertMuitosdocumentos" width="1000"> 

<img align="center" src="https://github.com/WilPassion/Programacao_Banco-de-Dados_2-FATEC/blob/main/MongoDB/img_Compass/insertManyDocsCompass2.PNG" alt="insertMuitosdocumentos" width="1000"> 

**Observações:**

• O _id é reservado para uso como chave primária  
• Nome dos campos não poder conter caractere NULL  
• Restrição de tamanho de documentos BSON = 16MB

-----------------------------------------
### **READ:**

-----------------------------------------
### **UPDATE:**

-----------------------------------------
### **DELETE:**
