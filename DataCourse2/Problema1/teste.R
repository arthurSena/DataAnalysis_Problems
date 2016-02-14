#O grafico abaixo eh referente a questao 3 usando apenas ggplot
#      qplot(x = factor(Departamento), y = Porcentagem, data=alunos_situacao_disciplina, geom="bar", fill=Situacao, stat='identity')  + theme(text = element_text(size=9),axis.text.x = element_text(angle = 45, hjust = 1))

porcentagem_acima_media <- por_aluno %>% mutate(AcimaMedia = CRA >=7) %>% group_by(Periodo_Ingresso, AcimaMedia) %>%  summarise(Qtd = n()) 

temp <- porcentagem_acima_media %>% group_by(Periodo_Ingresso) %>% mutate(TotalAlunos = sum(Qtd)) %>% group_by(AcimaMedia, add = T) %>% mutate(Porcentagem=round(100*Qtd/TotalAlunos,2))

temp$AcimaMedia <- revalue(factor(temp$AcimaMedia), c("FALSE"="ABAIXO_MEDIA", "TRUE"="ACIMA_MEDIA"))

ggplot(porcentagem_acima_media, aes(Periodo_Ingresso, Qtd)) +   
  geom_bar(aes(fill = AcimaMedia), position = "dodge", stat="identity")

p <- ggplot(porcentagem_acima_media, aes(x=Periodo_Ingresso, y=Qtd, group=AcimaMedia))
p + geom_line()

hPlot(x = "Periodo_Ingresso", y = "Porcentagem", group = "AcimaMedia", data = temp)