from IA.palabra_clave_generación import generar_palabras_claves
from IA.query_generación_sin_RAG import generar_primera_consulta
from IA.simple_RAG import simple_RAG
from conseguir_dato.tweet_scraper import scrape
import asyncio

#### PROBLEMA POTENCIAL: possiblemente GPT no discute ningún tema problemático.

TEMA = 'El Derecho del aborto in Chile'
MAX_HASHTAGS = 8

# Genera la primera consulta sin datos de Twitter
primera_consulta = generar_primera_consulta(TEMA)

async def obtener_tweets_relevantes():
    # Genera potetential hashtags de este tema para Twitter
    hashtags = generar_palabras_claves(TEMA)
    print ('Usando Scraper')
    # Obtiene Tweets de las palabras clave candidatas
    tasks = [scrape(hashtag) for hashtag in hashtags[: MAX_HASHTAGS + 1]]
    return await asyncio.gather(*tasks)
    # TODO: WILL, generate more keywords from Tweets

# TODO: WILL: if you fine-tune instead of in-context learning, you can do one-shot RAG
resultas_scrape = asyncio.run(obtener_tweets_relevantes())
# Aplanar la lista 
tweets_relevantes = set([tweet for topic in resultas_scrape for tweet in topic])
texto_relevantes = '\n'.join([tweet[2] for tweet in tweets_relevantes])

# Mejorar la primera consulta on tweets relevantes
query = simple_RAG (TEMA, primera_consulta, texto_relevantes)

print (query)

# TODO: maybe do more cycles to get greater recall
