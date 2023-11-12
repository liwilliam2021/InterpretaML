from IA.palabra_clave_generación import generar_palabras_claves
from IA.query_generación_sin_RAG import generar_primera_consulta
from IA.simple_RAG import simple_RAG
from conseguir_dato.tweet_scraper import scrape
import asyncio
import sys

#### PROBLEMA POTENCIAL: possiblemente GPT no discute ningún tema problemático.

MAX_HASHTAGS = 8

asunto = None
ubicación = None
keywords = None
if (len(sys.argv) == 1):
    print ('Usando el tema predeterminado')
    asunto = 'El Derecho del aborto'
    ubicación = "Chile"    
elif (len(sys.argv) in [3,4]):
    print ('El tema es recibido...')
    asunto = sys.argv[1]
    ubicación = sys.argv[2]
    if (len(sys.argv) == 4):
        keywords = sys.argv[3].split(',')
else:
    raise ValueError ('Error: proporcione el problema y la ubicación por separado y entre comillas. \n Por ejemplo: python3 generar_query.py "El Derecho del aborto" "Chile"')

tema = f'{asunto} en {ubicación}'

# Genera la primera consulta sin datos de Twitter
primera_consulta = generar_primera_consulta(tema, keywords)

async def obtener_tweets_relevantes():
    # Genera potetential hashtags de este tema para Twitter
    hashtags = generar_palabras_claves(tema)
    if (keywords):
        hashtags = keywords + hashtags # TODO: make set
    print ('Usando Scraper')
    # Obtiene Tweets de las palabras clave candidatas
    tasks = [scrape(hashtag, ubicación) for hashtag in hashtags[: MAX_HASHTAGS + 1]]
    return await asyncio.gather(*tasks)
    # TODO: WILL, generate more keywords from Tweets + filter for false positives w/ GPT

# TODO: WILL: if you fine-tune instead of in-context learning, you can do one-shot RAG
resultas_scrape = asyncio.run(obtener_tweets_relevantes())
# Aplanar la lista 
tweets_relevantes = set([tweet for topic in resultas_scrape for tweet in topic])
texto_relevantes = '\n'.join([tweet[2] for tweet in tweets_relevantes])

# Mejorar la primera consulta on tweets relevantes
query = simple_RAG (tema, primera_consulta, texto_relevantes)

print (query)

# TODO: WILL: maybe do more cycles to get greater recall
