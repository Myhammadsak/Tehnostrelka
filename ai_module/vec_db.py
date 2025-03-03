from qdrant_client import QdrantClient
from qdrant_client.http.models import VectorParams, Distance
from ai_module import embed_sentence

# Инициализация клиента Qdrant
client = QdrantClient(host='127.0.0.1', port=6333)

COLLECTION_NAME = "test_collection"

def create_collection(collection_name):
    client.recreate_collection(collection_name=collection_name,
                               vectors_config=VectorParams(size=768, distance=Distance.COSINE))

if __name__ == "__main__":

    create_collection(COLLECTION_NAME)

    films = [("Название", "описание")]

    for i, payload in enumerate(films):
        vector = embed_sentence(payload[1])
        client.upsert(
            collection_name=COLLECTION_NAME,
            points=[
                {
                    'id': i,
                    'vector': vector.tolist(),
                    'payload': {
                        'title': payload[0],
                        'about': payload[1]
                        }
                }
            ]
        )

    print("Тексты успешно векторизованы и записаны в Qdrant.")
