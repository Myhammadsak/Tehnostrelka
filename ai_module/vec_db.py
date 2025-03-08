from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance
from ai_module import embed_sentence, retriever, reranker_model

client = QdrantClient(host='127.0.0.1', port=6333)

COLLECTION_NAME = "assym_search"

# Функция для создания новой коллекции
def create_collection(collection_name: str):
    client.recreate_collection(collection_name=collection_name,
                               vectors_config=VectorParams(size=768, distance=Distance.COSINE))


# Функция поиска ближайшего вектора
def search_nearest(collection_name: str, text: str):
    vector = retriever.encode(text)
    return client.search(collection_name, vector)


# Функция для наполнения базы данных
def db_filling(collection_name: str):
    from tqdm import tqdm
    import pandas as pd

    df = pd.read_csv("films.csv")

    for i, payload in tqdm(df.iterrows()):
        # vector = embed_sentence(payload.iloc[3])
        vector = retriever.encode(payload.iloc[3])
        client.upsert(
            collection_name=collection_name,
            points=[
                {
                    'id': i,
                    'vector': vector.tolist(),
                    'payload': {
                        'title': payload.iloc[0],
                        'about': payload.iloc[3]
                        }
                }
            ]
        )


if __name__ == "__main__":
    from pprint import pprint
    
    # text = "Типы играют в огромные шахматы чтобы забрать философский камень"
    # text = "школьника укусил паук-мутант, когда они с классом были на экскурсии"
    text = "Богатый негр ищет себе водителя для поездки по америке, чтобы давать концерты"
    
    pprint(type(search_nearest(COLLECTION_NAME, text)[0]))


    # create_collection(COLLECTION_NAME)
    # db_filling(COLLECTION_NAME)



