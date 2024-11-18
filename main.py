from gtts import gTTS

nato_alphabet = {
    '1': 'One', '2': 'Two', '3': 'Three',
    '4': 'Four', '5': 'Five', '6': 'Six',
    '7': 'Seven', '8': 'Eight', '9': 'Nine',
    '0': 'Zero',
    # 'A': 'Alfa', 'B': 'Bravo',
    'A': ('Alfa', 'AHL-fah'),
    'B': ('Bravo', 'BRAH-voh'), 
    'C': 'Charlie',
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
    """Convert text to NATO phonetic code with pronunciation for TTS."""
    words = text.upper().split()
    nato_words_for_text = []
    nato_words_for_tts = []
    for word in words:
        nato_word_text = []
        nato_word_tts = []
        for letter in word:
            nato_letter = nato_alphabet.get(letter, (letter, letter))
            nato_word_text.append(nato_letter[0])  # Palabra para mostrar
            nato_word_tts.append(nato_letter[1])  # Pronunciación para TTS
        nato_words_for_text.append(' '.join(nato_word_text))
        nato_words_for_tts.append(' '.join(nato_word_tts))
    return ' '.join(nato_words_for_text), ' '.join(nato_words_for_tts)


# Ejemplo de uso:
text = input("Insert your text: ")
nato_text, nato_tts = nato_converter(text)
print("NATO code to display:", nato_text)

# Crear el archivo de audio con la pronunciación
tts = gTTS(text=nato_tts, lang='en')
tts.save("nato_code.mp3")
print("Audio file 'nato_code.mp3' created with pronunciation.")