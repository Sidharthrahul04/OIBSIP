from intents import detect_intent


test_commands = [
    "remind me in 10 seconds to check my assignment",
    "remind me in 5 minutes to submit my project",
    "remind me in 2 hours to attend the meeting",
    "remind me 10 seconds to check my assignment"
]


for command in test_commands:
    result = detect_intent(command)

    print(f"\nCommand: {command}")
    print(f"Intent: {result['intent']}")
    print(f"Entities: {result['entities']}")