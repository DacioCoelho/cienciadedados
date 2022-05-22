"""

Predição = Previsão
Uma das coisas mais im portantes na predição é saber se queremos prefer um problema de alvo númerico ou de classificação.
    Momento de prever o futuro, com base nos dados e modelos
        A modelagem é muito importante, mas ela não é um fim em si msmo! Buscar o modelo ideal não pode ser seu foco
    Modelagem preditiva
        Análise preditiva - Segue a estrutura:
                                    Entrada, Saída e Alvo
            Os problemas de predição são divididos em: Regressão e Classificação
                Regressão: Alvo numérico
                    Pode ser linear com o objetivo de reduzir a diferença entre os pontos observados e os pontos
                    que o modelo prevê.
                    Metodo utilizado para encontrar essafunção linear é pelos mínimos quadrados.


    Como avalair nosso modelo preditivo?
        Coeficiente de determinação pode ser expresso de 0 a 1

    Classificação: alvo é uma categoria
        O alvo é uma categoria, um exemplo é a classificação se o e-mail é ou não Spam
        O alvo podem ser várias categorias e o modelo faz uma separação entre as classes do problema.
        Regressão logistica:
            Não se usa uma regressão linear, mas sim uma regressão logística.
            Um algoritmo muito utilziado em problemas de regressão logistica é a K-NN
                k-NN faz a classificação para cada ponto ao analisar os pontos vizinhos.
        Underfitting
        Overfitting
     Para avalair modelos classificatórios:
        ROC (Receiver Operating Characteristic) - Varia de 0 a 1
        Podemos avalaiar as taxas de erros e acertos em cada situação.

"""