import json
import os

from services.logger import logger


COMMAND_FILE = os.path.join(
    "config",
    "custom_commands.json"
)


def load_custom_commands():
    """
    Load custom commands from the JSON configuration file.

    Returns:
        list: List of configured custom commands.
    """

    try:

        if not os.path.exists(COMMAND_FILE):

            logger.warning(
                "Custom command configuration file not found."
            )

            return []

        with open(
            COMMAND_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        commands = data.get(
            "commands",
            []
        )

        logger.info(
            f"Loaded {len(commands)} custom commands."
        )

        return commands

    except json.JSONDecodeError as error:

        logger.error(
            f"Invalid custom command JSON: {error}"
        )

        return []

    except OSError as error:

        logger.error(
            f"Could not read custom commands: {error}"
        )

        return []

    except Exception as error:

        logger.exception(
            f"Unexpected custom command error: {error}"
        )

        return []


def find_custom_command(command):
    """
    Find a custom command matching the user's input.

    Args:
        command (str): User's spoken command.

    Returns:
        dict or None: Matching command configuration.
    """

    command = command.lower().strip()

    commands = load_custom_commands()

    for custom_command in commands:

        name = custom_command.get(
            "name",
            ""
        ).lower().strip()

        if command == name:

            logger.info(
                f"Custom command matched: {name}"
            )

            return custom_command

    return None