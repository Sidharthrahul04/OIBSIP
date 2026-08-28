from services.qa_service import answer_question


questions = [
    "Who invented Python?",
    "What is artificial intelligence?",
    "What is the capital of France?"
]


for question in questions:

    print("\nQuestion:", question)

    answer = answer_question(question)

    print("Answer:", answer)