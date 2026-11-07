
from task2_chunks import make_chunks
from lab6_search import Retriever, show_hits
def compare_retrieval(docs, queries):
    records = make_chunks(docs, "sentence")
    for backend in ["tfidf", "embedding"]:
        engine = Retriever(records, backend)
        print("\nBackend:", backend)
        for query in queries:
            print("\nQuery:", query)
            hits = engine.search(query, k=3)
            show_hits(hits)
