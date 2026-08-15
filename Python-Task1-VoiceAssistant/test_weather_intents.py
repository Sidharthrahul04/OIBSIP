from intents import detect_intent


test_commands = [
    "what's the weather in kochi",
    "what is the weather in bangalore",
    "tell me the temperature in delhi",
    "what's the weather at mumbai",
    "hello",
    "what time is it"
]


for command in test_commands:
    result = detect_intent(command)

    print(f"\nCommand: {command}")
    print(f"Intent: {result['intent']}")
    print(f"Entities: {result['entities']}")