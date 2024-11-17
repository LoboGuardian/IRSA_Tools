# from gtts import gTTS

nato_alphabet = {
    '1': 'One', '2': 'Two', '3': 'Three',
    '4': 'Four', '5': 'Five', '6': 'Six',
    '7': 'Seven', '8': 'Eight', '9': 'Nine',
    '0': 'Zero',
    'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie',
    'D': 'Delta', 'E': 'Echo', 'F': 'Foxtrot',
    'G': 'Golf', 'H': 'Hotel', 'I': 'India',
    'J': 'Juliet', 'K': 'Kilo', 'L': 'Lima',
    'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo',
    'S': 'Sierra', 'T': 'Tango', 'U': 'Uniform',
    'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray',
    'Y': 'Yankee', 'Z': 'Zulu'
}

# Morse code
# Letters
# 'A': '.-', 'B': '-...', 'C': '-.-.',
# 'D': '-..', 'E': '.', 'F': '..-.',
# 'G': '--.', 'H': '....', 'I': '..',
# 'J': '.---', 'K': '-.-', 'L': '.-..',
# 'M': '--', 'N': '-.', 'O': '---',
# 'P': '.--.', 'Q': '--.-', 'R': '.-.',
# 'S': '...', 'T': '-', 'U': '..-',
# 'V': '...-', 'W': '.--', 'X': '-..-',
# 'Y': '-.--', 'Z': '--..',
# Numbers
# '0': '-----', '1': '.----', '2': '..---',
# '3': '...--', '4': '....-', '5': '.....',
# '6': '-....', '7': '--...', '8': '---..',
# '9': '----.',


def nato_converter(text):
    """Converts text to NATO phonetic code."""
    words = text.upper().split()
    nato_words = []
    for word in words:
        nato_word = []
        for letter in word:
            nato_word.append(nato_alphabet.get(letter, letter))
        nato_words.append(' '.join(nato_word))
    return ' '.join(nato_words)


# Example usage:
# text = "Hello, World! I'm LR7010"
text = input("Insert your text ")
nato_code = nato_converter(text)
print(nato_code)
# Output: Hotel Echo Lima Lima O, Whiskey Oscar Romeo Letter Delta
