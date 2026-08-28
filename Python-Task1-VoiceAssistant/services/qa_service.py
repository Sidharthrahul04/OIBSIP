import re
import requests

from services.logger import logger


WIKIPEDIA_API_URL = "https://en.wikipedia.org/w/api.php"

HEADERS = {
    "User-Agent": "VoiceAssistant/1.0"
}


def clean_question(question):
    """
    Remove common question words so that the
    Wikipedia search focuses on the actual topic.
    """

    question = question.lower().strip()

    patterns = [
        r"^what is ",
        r"^what are ",
        r"^who is ",
        r"^who was ",
        r"^who invented ",
        r"^where is ",
        r"^when was ",
        r"^when did ",
        r"^why is ",
        r"^how does ",
        r"^how do ",
        r"^how is ",
        r"\?$"
    ]

    for pattern in patterns:
        question = re.sub(pattern, "", question)

    return question.strip()


def get_search_results(query):
    """
    Search Wikipedia and return multiple candidate pages.
    """

    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "utf8": 1,
        "srlimit": 5
    }

    response = requests.get(
        WIKIPEDIA_API_URL,
        params=params,
        headers=HEADERS,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    return (
        data
        .get("query", {})
        .get("search", [])
    )


def get_article_summary(title):
    """
    Retrieve the introduction of a Wikipedia article.
    """

    params = {
        "action": "query",
        "prop": "extracts",
        "exintro": 1,
        "explaintext": 1,
        "redirects": 1,
        "titles": title,
        "format": "json",
        "utf8": 1
    }

    response = requests.get(
        WIKIPEDIA_API_URL,
        params=params,
        headers=HEADERS,
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    pages = (
        data
        .get("query", {})
        .get("pages", {})
    )

    for page in pages.values():

        extract = page.get(
            "extract",
            ""
        ).strip()

        if extract:
            return extract

    return None


def shorten_answer(answer, max_length=500):
    """
    Keep the spoken response reasonably short.
    """

    if len(answer) <= max_length:
        return answer

    shortened = answer[:max_length]

    shortened = shortened.rsplit(
        " ",
        1
    )[0]

    return shortened + "..."


def answer_question(question):
    """
    Answer a general knowledge question using Wikipedia.
    """

    if not question or not question.strip():
        return "Please ask me a question."

    question = question.strip()

    try:

        # -------------------------------------------------
        # Prepare search query
        # -------------------------------------------------

        search_query = clean_question(question)

        if not search_query:
            search_query = question

        logger.info(
            f"Q&A question: {question}"
        )

        # -------------------------------------------------
        # Search Wikipedia
        # -------------------------------------------------

        search_results = get_search_results(
            search_query
        )

        if not search_results:

            logger.info(
                f"No Q&A results for: {question}"
            )

            return (
                "I couldn't find a reliable answer "
                "to that question."
            )

        # -------------------------------------------------
        # Try several candidate articles
        # -------------------------------------------------

        for result in search_results:

            title = result.get("title")

            if not title:
                continue

            summary = get_article_summary(
                title
            )

            if summary:

                answer = shorten_answer(
                    summary
                )

                logger.info(
                    f"Q&A answered using Wikipedia: {title}"
                )

                return answer

        return (
            "I found the topic, but I couldn't "
            "extract a useful answer."
        )

    # -----------------------------------------------------
    # HTTP error
    # -----------------------------------------------------

    except requests.exceptions.HTTPError as error:

        logger.error(
            f"Q&A HTTP error: {error}"
        )

        return (
            "The knowledge service returned "
            "an HTTP error."
        )

    # -----------------------------------------------------
    # Timeout
    # -----------------------------------------------------

    except requests.exceptions.Timeout:

        logger.error(
            "Q&A request timed out."
        )

        return (
            "The knowledge service took too long "
            "to respond."
        )

    # -----------------------------------------------------
    # Connection error
    # -----------------------------------------------------

    except requests.exceptions.ConnectionError as error:

        logger.error(
            f"Q&A connection error: {error}"
        )

        return (
            "I couldn't connect to the "
            "knowledge service."
        )

    # -----------------------------------------------------
    # Invalid response
    # -----------------------------------------------------

    except ValueError as error:

        logger.error(
            f"Invalid Q&A response: {error}"
        )

        return (
            "The knowledge service returned "
            "an invalid response."
        )

    # -----------------------------------------------------
    # Unexpected error
    # -----------------------------------------------------

    except Exception as error:

        logger.exception(
            f"Unexpected Q&A error: {error}"
        )

        return (
            "Something went wrong while "
            "answering your question."
        )