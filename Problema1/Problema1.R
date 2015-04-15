salariosTI <- read.csv("salarios-ti-refinado.csv")
salariosTI <- salariosTI[-1,]

#Melhor e estado e regiao para se trabalhar 
estados <- levels(salariosTI$UF)
estados_salario <- sapply(estados,function(estado){
  salario_estado <- salariosTI[salariosTI$UF == estado,]
  median(salario_estado$Salario.Bruto)
}) 

estados_salario <- as.data.frame(estados_salario)
estados_salario <- cbind(Estados = rownames(estados_salario), estados_salario)
colnames(estados_salario)<- c("Estados","Media_Salarial")
estados_salario<-estados_salario[order(-estados_salario$Media_Salarial),]
rownames(estados_salario) <- NULL

regioes <- levels(salariosTI$Regiao)
regioes_salarios <- sapply(regioes, function(regiao){
   salario_regiao <- salariosTI[salariosTI$Regiao == regiao,]
   median(salario_regiao$Salario.Bruto)
 })

regioes_salarios <- as.data.frame(regioes_salarios)
regioes_salarios <- cbind(Estados = rownames(regioes_salarios), regioes_salarios)
colnames(regioes_salarios)<- c("Regiao","Media_Salarial")
regioes_salarios<-regioes_salarios[order(-regioes_salarios$Media_Salarial),]
rownames(regioes_salarios) <- NULL

regioes <- levels(salariosTI$Regiao)
regioes_salariosAlto <- sapply(regioes, function(regiao){
  salario_regiao <- salariosTI[salariosTI$Regiao == regiao,]
  salario_regiao <- salario_regiao[salario_regiao$Salario.Bruto > quantile(salariosTI$Salario.Bruto,0.50),]
  median(salario_regiao$Salario.Bruto)
})

regioes_salariosBaixo <- sapply(regioes, function(regiao){
  salario_regiao <- salariosTI[salariosTI$Regiao == regiao,]
  salario_regiao <- salario_regiao[salario_regiao$Salario.Bruto <= quantile(salariosTI$Salario.Bruto,0.50),]
  median(salario_regiao$Salario.Bruto)
})

  
regioes_salarioDiferenca <- regioes_salariosAlto - regioes_salariosBaixo

regioes_salarioDiferenca <- as.data.frame(regioes_salarioDiferenca)
regioes_salarioDiferenca <- cbind(Regioes = rownames(regioes_salarioDiferenca), regioes_salarioDiferenca)
colnames(regioes_salarioDiferenca)<- c("Regiao","Diferenca")
regioes_salarioDiferenca<-regioes_salarioDiferenca[order(-regioes_salarioDiferenca$Diferenca),]
rownames(regioes_salarioDiferenca) <- NULL

salarios_altos_baixos <- cbind(regioes_salariosAlto,regioes_salariosBaixo)
barplot(t(salarios_altos_baixos),beside = TRUE,ylim = c(0,6000),main = "Diferenca entre Salários Altos e Baixos")
