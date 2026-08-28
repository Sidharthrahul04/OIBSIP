from intents import detect_intent


test_commands = [
    "send an email",
    "send email",
    "compose an email",
    "write an email"
]


for command in test_commands:

    result = detect_intent(command)

    print(f"\nCommand: {command}")
    print(f"Intent: {result['intent']}")
    print(f"Entities: {result['entities']}")