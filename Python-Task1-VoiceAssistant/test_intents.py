from intents import detect_intent


test_commands = [
    "hello",
    "hey there",
    "could you tell me the current time",
    "what time is it right now",
    "what is today's date",
    "search Python decorators",
    "goodbye",
    "something completely random"
]


for command in test_commands:
    intent = detect_intent(command)
    print(f"{command} -> {intent}")