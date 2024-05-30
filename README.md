# Text to Speech Configurator

## Overview
The Text to Speech Configurator is a Python application that converts text into speech with customizable settings. It features a graphical user interface (GUI) built using Tkinter and utilizes the pyttsx3 library for text-to-speech conversion. This project provides users with the ability to adjust volume, speech rate, and select different voices for a personalized listening experience.

## Features
- **Text Input**: Users can input or paste text into the provided text box.
- **Volume Control**: Adjust the volume of the speech output using a slider.
- **Rate Control**: Set the speech rate in words per minute (wpm) using a slider.
- **Voice Selection**: Choose from available voices installed on the system.
- **Speak Button**: Trigger the text-to-speech conversion with a click of a button.

## How to Use
1. Clone the repository:
   ```
   git clone https://github.com/Rakshitgupta9/Text-to-Speech-Configurator.git
   ```
2. Navigate to the project directory:
   ```
   cd Text-to-Speech-Configurator
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the application:
   ```
   python main.py
   ```

## Example Code Explanation
The main.py file contains the Python code for the Text to Speech Configurator application. Here's a brief explanation of the code:
- The application uses Tkinter for the GUI and pyttsx3 for text-to-speech conversion.
- It initializes the pyttsx3 engine and retrieves available voices.
- The GUI elements such as text box, sliders for volume and rate control, and dropdown menu for voice selection are created.
- The speak_text function is defined to handle text-to-speech conversion with user-defined settings.
- The main application window is created using Tkinter, and the event loop is started.

## Requirements
- Python 3.x
- Tkinter library (included with standard Python installations)
- pyttsx3 library (installable via pip)

## Images
### GUI
![image](https://github.com/Rakshitgupta9/Text-to-Speech-Configurator/assets/95240061/18e85fcd-cb33-41c9-9413-478331c9b577)

### Voice Option
![image](https://github.com/Rakshitgupta9/Text-to-Speech-Configurator/assets/95240061/5553d319-c944-4311-813a-da3f1c00637f)

### Sample
![image](https://github.com/Rakshitgupta9/Text-to-Speech-Configurator/assets/95240061/3b6a05c4-1f62-43ca-bffa-87efed8857b3)


## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [pyttsx3](https://pypi.org/project/pyttsx3/)
- [tkinter](https://docs.python.org/3/library/tkinter.html)

