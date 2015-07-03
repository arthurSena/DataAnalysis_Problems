library(caret)
wbcd = read.csv("/home/arthur/Downloads/wisc_bc_data.csv")
wbcd_n = wbcd[-1] ## Exclui atributo de id
wbcd_train = wbcd_n[1:469,] ## Criando partição de treino
wbcd_test = wbcd_n[470:569,] ## Criando partição de teste
wbcd_train = wbcd_train[-1] ## Exclui variável alvo
wbcd_train_labels = wbcd[1:469, 1] ## Classes das instâncias de treino
wbcd_test_labels = wbcd[470:569, 1] ## Classes das instâncias de teste
fitControl = trainControl(method = "repeatedcv",number = 10,  repeats = 10) ## usa o método cross validation, com 10 folds (number), repetido 10 vezes para cada k(repeats=10)
knn_grid = expand.grid(k=c(1:20))
best_knn_model = train(wbcd_train, wbcd_train_labels,method="knn",preProcess=c("range"),tuneGrid=knn_grid,trControl=fitControl) ## método knn nos dados do breast cancer, normalizando os dados para a escala [0,1] (preProcess=c("range")), para cada k em knn_grid, tuneGrid=knn_grid, usando as amostras definidas em fitControl (trControl=fitControl)
plot(best_knn_model) ## Plota a acurácia do modelo para cada k em knn_grid
pred<-predict(best_knn_model, newdata = wbcd_test)


#---------------------------------------
# load the library
library(mlbench)
library(caret)
# load the dataset
data(PimaIndiansDiabetes)
# prepare training scheme
control <- trainControl(method="repeatedcv", number=10, repeats=3)
# train the LVQ model
set.seed(7)
modelLvq <- train(diabetes~., data=PimaIndiansDiabetes, method="lvq", trControl=control)
# train the GBM model
set.seed(7)
modelGbm <- train(diabetes~., data=PimaIndiansDiabetes, method="gbm", trControl=control, verbose=FALSE)
# train the SVM model
set.seed(7)
modelSvm <- train(diabetes~., data=PimaIndiansDiabetes, method="svmRadial", trControl=control)
# collect resamples
results <- resamples(list(LVQ=modelLvq, GBM=modelGbm, SVM=modelSvm))
# summarize the distributions
summary(results)
# boxplots of results
bwplot(results)
# dot plots of results
dotplot(results)