from dotenv import load_dotenv

load_dotenv()

from services.qa_service import answer_question


questions = [
    "Who invented Python?",
    "When was Python first released?",
    "What is the capital of France?",
    "Who was the Premier League champion in 2025?",
    "Who was the Premier League champion in 2026?",
    "What is artificial intelligence?"
]


for question in questions:

    print("\nQuestion:", question)

    answer = answer_question(question)

    print("Answer:", answer)