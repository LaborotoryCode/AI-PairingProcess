from sentence_transformers import SentenceTransformer, SimilarityFunction
model = SentenceTransformer("msmarco-distilbert-cos-v5", similarity_fn_name=SimilarityFunction.COSINE)

print("Started")

mentors = [
    """
    I will provide strict guidance every step of the way.
    """
]

mentees = [
    """
    I want to be be helped and given very specific instructions.
    """,

    """
    I want to be given freedom to learn as I go.
    """
]

results = []

mentor_embeddings = model.encode(mentors[0])

for i in range(len(mentees)):
    mentee_embeddings = model.encode(mentees[i])
    similarities = model.similarity(mentor_embeddings, mentee_embeddings)
    results.append(round(similarities.item(), 8))

print(results)
