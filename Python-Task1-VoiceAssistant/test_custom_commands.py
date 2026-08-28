from services.command_service import (
    load_custom_commands,
    find_custom_command
)


print("Loaded commands:")

commands = load_custom_commands()

for command in commands:
    print(command)


test_commands = [
    "open github",
    "open linkedin",
    "open google",
    "open youtube"
]


print("\nTesting commands:")

for command in test_commands:

    result = find_custom_command(command)

    print(
        f"{command} -> {result}"
    )