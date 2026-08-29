import secrets
import string


def build_character_sets(
    use_uppercase,
    use_lowercase,
    use_numbers,
    use_symbols,
    exclude_ambiguous
):
    character_sets = []

    if use_uppercase:
        character_sets.append(string.ascii_uppercase)

    if use_lowercase:
        character_sets.append(string.ascii_lowercase)

    if use_numbers:
        character_sets.append(string.digits)

    if use_symbols:
        character_sets.append(string.punctuation)

    if exclude_ambiguous:
        ambiguous_characters = "0Ol1"

        character_sets = [
            "".join(
                character
                for character in character_set
                if character not in ambiguous_characters
            )
            for character_set in character_sets
        ]

    return character_sets


def generate_password(length, character_sets):
    password = []

    # Guarantee at least one character from every selected type
    for character_set in character_sets:
        password.append(secrets.choice(character_set))

    # Combine all selected character sets
    all_characters = "".join(character_sets)

    # Fill remaining positions
    for i in range(length - len(password)):
        password.append(secrets.choice(all_characters))

    # Securely shuffle password
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def calculate_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1

    if len(password) >= 12:
        score += 1

    if any(character.isupper() for character in password):
        score += 1

    if any(character.islower() for character in password):
        score += 1

    if any(character.isdigit() for character in password):
        score += 1

    if any(not character.isalnum() for character in password):
        score += 1

    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"