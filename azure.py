import os
import requests
import json

def analyze_text(text):
    """
    Envia um texto para a API do Azure Text Analytics e retorna a análise.
    """
    AZURE_ENDPOINT = "https://NomeDoSeuResource.cognitiveservices.azure.com/"
    AZURE_API_KEY = "SUA_KEY"
    AZURE_PATH = "text/analytics/v3.1/sentiment"
    
    url = AZURE_ENDPOINT + AZURE_PATH
    headers = {
        "Ocp-Apim-Subscription-Key": AZURE_API_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "documents": [
            {"id": "1", "language": "pt", "text": text}
        ]
    }
    
    response = requests.post(url, headers=headers, json=data)
    return response.json()

if __name__ == "__main__":
    with open("inputs/sentencas.txt", "r", encoding="utf-8") as file:
        text = file.read()
    
    result = analyze_text(text)
    print(json.dumps(result, indent=2, ensure_ascii=False))
