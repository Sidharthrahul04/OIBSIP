from intents import detect_intent


test_commands = [

    # Greetings
    "hello",
    "hey there",
    "good morning",

    # Time
    "what time is it",
    "tell me the current time",
    "do you know the time",

    # Date
    "what is today's date",
    "tell me today's date",
    "what is the current date",

    # Weather
    "what's the weather in kochi",
    "how's the weather in dubai",
    "tell me the weather in bangalore",
    "what is the temperature in delhi",
    "what's mumbai weather like",

    # Search
    "search Python decorators",
    "search for Python decorators",
    "look up machine learning",
    "google Python functions",

    # Reminder
    "remind me in 10 seconds to check my assignment",
    "remind me in 5 minutes to drink water",
    "remind me in 2 hours to study",

    # Email
    "send an email",
    "send email",
    "compose an email",
    "write an email",

    # Exit
    "goodbye",
    "quit",
    "exit",

    # Unknown
    "play some music",
    "open calculator",
    "what is the meaning of life"
]


for command in test_commands:

    result = detect_intent(command)

    print("\nCommand:", command)
    print("Intent:", result["intent"])
    print("Entities:", result["entities"])