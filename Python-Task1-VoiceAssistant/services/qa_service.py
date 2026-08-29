import os

from google import genai
from dotenv import load_dotenv

from services.logger import logger


# =========================================================
# LOAD ENVIRONMENT VARIABLES
# =========================================================

load_dotenv()


# =========================================================
# GEMINI CLIENT
# =========================================================

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    logger.error("GEMINI_API_KEY is missing.")

    client = None

else:
    client = genai.Client(
        api_key=api_key
    )


# =========================================================
# QUESTION ANSWERING
# =========================================================

def answer_question(question):
    """
    Answer a general knowledge question using Gemini.
    """

    if not question or not question.strip():

        return "Please ask me a question."

    if client is None:

        return (
            "The question answering service "
            "is not configured."
        )

    question = question.strip()

    try:

        prompt = f"""
You are the question-answering component of a
Python voice assistant.

Answer the user's question directly.

Important rules:

1. Answer the EXACT question.
2. Do not provide an unrelated article summary.
3. Keep the answer short because it will be spoken aloud.
4. Prefer one to three sentences.
5. If the user asks WHO, give the person, team, or organization.
6. If the user asks WHEN, give the relevant date or year.
7. If the user asks WHERE, give the relevant location.
8. If the user asks WHICH TEAM, clearly name the team.
9. If the question asks about a specific year, pay attention to that year.
10. Do not repeat the question.
11. Do not use markdown.
12. Do not say "According to Wikipedia".
13. Do not explain your reasoning.
14. If the question is ambiguous, briefly explain the ambiguity.

User question:

{question}
"""

        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        answer = response.text.strip()

        if not answer:

            logger.warning(
                f"Gemini returned an empty answer: {question}"
            )

            return (
                "I couldn't find a useful answer "
                "to that question."
            )

        logger.info(
            f"Q&A answered using Gemini: {question}"
        )

        return answer

    except Exception as error:

        logger.exception(
            f"Gemini Q&A error: {error}"
        )

        print(
            "Gemini Q&A error:",
            error
        )

        return (
            "I couldn't get an answer right now. "
            "Please try again."
        )