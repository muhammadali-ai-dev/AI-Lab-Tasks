from sklearn.feature_extraction.text import TfidfVectorizer

class Retriever:
    def __init__(self, records, backend="tfidf"):
        self.records = records
        self.vectorizer = TfidfVectorizer()
        texts = [r["text"] for r in records]
        self.matrix = self.vectorizer.fit_transform(texts)

    def search(self, query, k=3):
        if not query.strip():
            return []

        q = self.vectorizer.transform([query])

        if q.nnz == 0:
            return []

        scores = (q @ self.matrix.T).toarray()[0]
        ranked = sorted(
            range(len(scores)),
            key=lambda i: -scores[i]
        )

        return [
            (self.records[i], float(scores[i]))
            for i in ranked[:k]
        ]
