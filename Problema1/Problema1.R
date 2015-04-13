salariosTI <- read.csv("salarios-ti-refinado.csv")
salariosTI <- salariosTI[-1,]

#Os dados que eu considero incosistentes
temp <- salariosTI$Pos.Graduacao.ou.Certificacao == TRUE
temp <- salariosTI[temp,]
dados_inconsistentes <- temp[temp$Formaca == "Nao informou",]
nrow(dados_inconsistentes)/nrow(salariosTI)

#Melhor e estado e regiao para se trabalhar 
estados <- levels(salariosTI$UF)
estados_salario <- sapply(estados,function(estado){
  salario_estado <- salariosTI[salariosTI$UF == estado,]
  mean(salario_estado$Salario.Bruto)
}) 

estados_salario <- as.data.frame(estados_salario)
estados_salario <- cbind(Estados = rownames(estados_salario), estados_salario)
colnames(estados_salario)<- c("Estados","Media_Salarial")
estados_salario<-estados_salario[order(-estados_salario$Media_Salarial),]
rownames(estados_salario) <- NULL

regioes <- levels(salariosTI$Regiao)
regioes_salarios <- sapply(regioes, function(regiao){
   salario_regiao <- salariosTI[salariosTI$Regiao == regiao,]
   mean(salario_regiao$Salario.Bruto)
 })

regioes_salarios <- as.data.frame(regioes_salarios)
regioes_salarios <- cbind(Estados = rownames(regioes_salarios), regioes_salarios)
colnames(regioes_salarios)<- c("Regiao","Media_Salarial")
regioes_salarios<-regioes_salarios[order(-regioes_salarios$Media_Salarial),]
rownames(regioes_salarios) <- NULL

