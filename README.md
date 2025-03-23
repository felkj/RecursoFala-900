# Azure Text Analysis

Este projeto tem como objetivo demonstrar o uso da API do **Azure Cognitive Services** para análise de texto, incluindo identificação de sentimentos, extração de entidades e palavras-chave. A intenção era realizar a integração direta com a API do Azure, mas devido a dificuldades no acesso à conta trial, optamos por simular os resultados esperados.

## 📌 Estrutura do Projeto
- `inputs/sentencas.txt` → Arquivo de texto com frases para análise.
- `azure.py` → Script que enviaria os textos para a API do Azure.
- `README.md` → Documentação e explicação do projeto.

## 🚀 Como Funcionaria
Caso fosse possível acessar a API, o processo seguiria estas etapas:
1. O script lê as frases do arquivo `inputs/example.txt`.
2. Envia os textos para a API do **Azure Text Analytics**.
3. A API retorna insights sobre sentimentos, entidades e palavras-chave.
4. Os resultados são exibidos no terminal em formato JSON.

## 🔍 Exemplo Simulado de Resultados
Dado o seguinte texto de entrada:
```txt
Estou muito feliz com este projeto!
O filme foi excelente, adorei cada cena.
Não gostei da comida do restaurante.
```

O retorno esperado da API seria algo assim:
```json
{
  "documents": [
    {
      "id": "1",
      "sentiment": "positive",
      "confidenceScores": {"positive": 0.99, "neutral": 0.01, "negative": 0.00},
      "keyPhrases": ["projeto"]
    },
    {
      "id": "2",
      "sentiment": "positive",
      "confidenceScores": {"positive": 0.95, "neutral": 0.04, "negative": 0.01},
      "keyPhrases": ["filme", "cena"]
    },
    {
      "id": "3",
      "sentiment": "negative",
      "confidenceScores": {"positive": 0.02, "neutral": 0.10, "negative": 0.88},
      "keyPhrases": ["comida", "restaurante"]
    }
  ]
}
```

## 📢 Conclusão
Apesar das limitações de acesso ao serviço, este projeto ainda pode servir como referência para quem deseja explorar **análise de sentimentos e NLP com a API do Azure**. Caso o acesso seja liberado no futuro, bastará substituir as credenciais e executar o script normalmente. 

---
🔗 **Dicas para continuar o aprendizado:**
- [Documentação oficial do Azure Text Analytics](https://learn.microsoft.com/en-us/azure/cognitive-services/language-service/)
- [Exemplos práticos no GitHub da Microsoft](https://github.com/Azure-Samples)
