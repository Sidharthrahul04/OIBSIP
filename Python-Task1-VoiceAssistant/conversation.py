class ConversationState:
    """
    Stores temporary information about the current
    multi-step conversation.
    """

    def __init__(self):
        self.reset()

    def reset(self):
        # Current conversation mode
        self.mode = None

        # -------------------------
        # Email state
        # -------------------------

        self.recipient = None
        self.subject = None
        self.message = None
        self.awaiting_confirmation = False

        # -------------------------
        # Weather state
        # -------------------------

        self.weather_city = None

    # =====================================================
    # EMAIL
    # =====================================================

    def start_email(self):
        """Start a new email conversation."""

        self.reset()

        self.mode = "EMAIL"

    def is_email_active(self):
        """Check whether an email conversation is active."""

        return self.mode == "EMAIL"

    # =====================================================
    # WEATHER
    # =====================================================

    def start_weather(self):
        """Start a weather conversation."""

        self.mode = "WEATHER"

        self.weather_city = None

    def is_weather_active(self):
        """Check whether the assistant is waiting for a city."""

        return (
            self.mode == "WEATHER"
            and self.weather_city is None
        )

    # =====================================================
    # GENERAL
    # =====================================================

    def clear(self):
        """Clear the current conversation."""

        self.reset()