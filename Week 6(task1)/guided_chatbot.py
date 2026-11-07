from lab6_search import Retriever
FAQ = [
    {"id":"faq:password", "question":"How do I reset my password?",
 "answer":"Use the recovery link on the login page.",
 "source":"it_help.txt"},
    {"id":"faq:submit", "question":"Where do I submit my assignment?",
 "answer":"Use the assignment upload page in the learning portal.",
 "source":"assessment.txt"},
    {"id":"faq:late", "question":"Can illness justify a late submission?",
 "answer":"Request an extension with medical evidence before the deadline.",
 "source":"handbook.txt"},
    {"id":"faq:library", "question":"How can I access library resources?",
     "answer":"Visit the university library portal.",
     "source":"library.txt"},

    {"id":"faq:help", "question":"How can I contact student support?",
     "answer":"Contact the student support department.",
     "source":"support.txt"}]
def build_bot(backend="tfidf"):
    records = [dict(r, text=r["question"]+" "+r["answer"]) for r in FAQ]
    return Retriever(records, backend)
def reply(engine, query):
    if not query.strip():
        return "Please enter a question."
    for r in FAQ:
        if query.strip().casefold() == r["question"].casefold():
            return r["answer"] + " [source: " + r["source"] + "]"
    hits = engine.search(query)
    if not hits:
        return "No matching FAQ. Please contact the help desk."
    lines = ["Possible matches; choose or rephrase your question:"]
    for r,score in hits:
        lines.append(r["question"] + f" (similarity {score:.3f})")
    return "\n".join(lines)
