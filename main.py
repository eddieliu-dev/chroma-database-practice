import chromadb
import uuid

client = chromadb.CloudClient(
    api_key='ck-HdWFV3R2VLngyLL8NQ3dpf4FCzUu65DJxs71YgVAuYGU',
    tenant='57dca400-ce03-4b94-849c-87be7cb2a8b0',
    database='Test'
)

# client.delete_collection(name="news")
# collection = client.create_collection(name = "news")
collection = client.get_or_create_collection(name="news")

with open("documents_dup_part_1_part_1", "r", encoding="utf-8") as file:
    news: list[str] = file.read().splitlines()

# collection.add(
#     ids=[str(uuid.uuid4()) for _ in news],
#     documents=news,
#     metadatas=[{"line": line} for line in range(len(news))]
# )

# print(collection.peek())

results = collection.query(
    query_texts=[
        "有没有体育相关的新闻?"
    ],
    n_results=5
)

for i, query_results in enumerate(results["documents"]):
    print(f"\nQuery {i}")
    print("\n".join((query_results)))