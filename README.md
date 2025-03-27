# Simple Voice Assistant

This is a simple voice assistant created as an exploratory project to test the functionality of `pyttsx3` for text-to-speech synthesis and `SpeechRecognition` for speech-to-text conversion. The assistant can execute basic commands like opening websites, searching Wikipedia, telling jokes, and retrieving stock prices.

## Installation

1. Clone this repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Run the assistant:
   ```sh
   python voice_assistant.py
   ```

## Dependencies
The project relies on the following Python packages:
- `pyttsx3` - Text-to-speech conversion
- `SpeechRecognition` - Speech-to-text processing
- `pywhatkit` - Web search and YouTube integration
- `yfinance` - Stock market data retrieval
- `pyjokes` - Joke generation
- `wikipedia-api` - Wikipedia search

Make sure these packages are installed before running the assistant.

## License
This project is for public use and is not licensed under any specific terms. You are free to use and modify it as needed.

## Disclaimer
This assistant is a basic implementation for learning purposes. It is not optimized for production use and may not handle complex voice commands efficiently.

