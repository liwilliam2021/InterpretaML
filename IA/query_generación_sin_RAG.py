import os
import sys
import openai
from IA.ejemplos.query_ejemplos import Q_EJEMPLOS
from datetime import datetime
import json

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)
from secret_key import API_KEY

USA_GPT4 = True
GPT_MODELO = "gpt-4" if USA_GPT4 else "gpt-3.5-turbo"
openai.api_key = API_KEY

def hacer_GPT_prompt_sin_RAG (tema, keywords):
    # TODO: WILL: improve prompt w/ GPT
    todo_ejemplos = '\n\n'.join (['Una consulta de ejemplo para el tema de ' + q[0] + ' es : ' + q[1] for q in Q_EJEMPLOS.items()])
    keyword_ejemplos = '' if not keywords else ('Asegúrese de incluir los siguientes hashtags y palabras clave en su consulta: ' + ','.join (keywords))
    system_prompt = f"""Quiero hacer un query con un algoritmo booleano para consultar Tweets sobre un tema específico. Quiero que el query contenga una amplia gama de puntos de vista, perspectivas, hashtags y datos demográficos.
    Puede usa estas operaciones booleanas AND, NOT, OR, (). En general, en lugar de frases exactas encerradas en "", debe usar NEAR/n como un operador de proximidad que incluye todos frases dentro de n palabras.
    Debes usar el regex *, (por ejemplo: aprobad*), si el final de una palabra es flexible. Debes usar ?, (por ejemplo: rid?culo), si la letra es flexible.
    Separe el query en secciones y etiquete cada una. Coloque las etiquetas entre <<< y >>>. 
    Prioriza la minimización de falsos positivos.Por ejemplo: si está buscando Tweets sobre migrantes, el frase (OR "extranjer?") es demasiado amplio porque hay empresas extranjeras, universidades extranjeras, etc. Trata ser específico.
    {keyword_ejemplos} Aquí hay unos ejemplos.
    \n""" +  todo_ejemplos
    user_prompt = f'Generas una consulta para el tema de {tema}.'

    prompt = [{
        "role": "system",
        "content": system_prompt
    }, {
        "role": "user",
        "content": user_prompt
    }]
    return prompt

def generar_primera_consulta (tema, keywords):
    """Generar la primera consulta con 'in-context learning' sin datos de Twitter"""
    print ('Generando la primera consulta')

    # Pregunta GPT con ejemplos
    result = openai.ChatCompletion.create(
                model=GPT_MODELO,
                messages= hacer_GPT_prompt_sin_RAG (tema, keywords),
                temperature=0.7
            )
    response = result['choices'][0]['message']['content']

    primer_comentario_idx = response.index ('<<<')
    primer_booleana_idx = response.index ('(')
    # Si hay un error aquí, es un problema de GPT
    consulta_inicio_idx = min (primer_comentario_idx, primer_booleana_idx)

    consulta = response[consulta_inicio_idx:]

    now = datetime.now()
    with open(f'IA/logs/q1{now}.json', "w") as outfile:
        json.dump(consulta, outfile)

    return consulta

