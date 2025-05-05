import json
from openai import OpenAI
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, "chat/index.html")



# Usar com chave API OpenAI

# client = OpenAI(api_key=settings.OPENAI_API_KEY)

#@csrf_exempt
# def responder(request):
#     if request.method == "POST":
#         dados = json.loads(request.body)
#         mensagem = dados.get("mensagem", "").lower()

#         prompt = f'"Você é um fã de counter-strike. Fale como se comunicasse diretamente para os outros fãs de forma descontraída e confiante, respondendo à mensagem de um torcedor: Torcedor: {mensagem} você:" '
        
#         resposta_ia = client.chat.completions.create(
#             model= "gpt-3.5-turbo",
#             messages=[
#                 {"role": "system", "content":"Você é um fã de counter-strike se comunicando com outros fãs"},
#                 {"role": "user", "content": mensagem}
#             ],
#             max_tokens = 100,
#             temperature = 0.8,
#         )
#         resposta = resposta_ia.choices[0].message.content.strip()

#         return JsonResponse({"resposta": resposta})

from .respostas import gerar_resposta

@csrf_exempt
def responder(request):
    if request.method == "POST":
        # Ignora a pergunta do usuário, apenas responde com uma frase aleatória
        resposta = gerar_resposta()
        return JsonResponse({"resposta": resposta})
    

def index(request):
    return render(request, "chat/index.html")

