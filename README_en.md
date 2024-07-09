# AI Virtual Mate Web

## Introduction

**AI Virtual Mate Web** is a digital human chat software integrated with advanced artificial intelligence technology, providing a platform for users to interact with virtual characters through a web interface. Users can access the web locally or via a local area network to enjoy real-time voice interaction experiences. The software has rich personalized settings, including the virtual character's name, persona, language model selection, etc., and supports multiple voice synthesis engines and custom API integration.

## Open Source License

This project follows the **GPL-3.0** open source license, encouraging community members to freely use, modify, and distribute the code, while also requiring that derivative works distributed also follow the same open source license.

## Features

- **Multi-language Model Support**: Interfaces with a variety of pre-trained large language models, such as GPT-3.5, GPT-4, Gemini, etc.
- **Custom API Support**: Users can configure custom APIs according to their needs to achieve integration with specific large language models.
- **Multimodal Voice Synthesis**: Supports various voice synthesis engines such as Microsoft Cloud edge-tts, local pyttsx3, and GPT-SoVITS.
- **Real-time Voice Interaction**: Utilizing advanced voice recognition technology, users can communicate with the virtual mate in real time via voice.
- **Dynamic Web Interface**: A dynamic interaction interface provided by the Flet and Flask frameworks for the web server.
- **Live2D Character Display**: Integrated Live2D technology to display virtual character images, and change mouth shapes in real time according to the results of voice synthesis.

## System Requirements

- Operating System: Windows 10, Windows 11
- Python Version: It is recommended to use Python 3.10 or above
- Other Dependencies: See the `requirements.txt` file for details

## Installation Guide

### Clone the Project

```bash
git clone https://github.com/swordswind/ai_virtual_mate_web.git 
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage Instructions

### Launch the Application

Run the `main.py` script in the root directory of the project to launch the application (you need to fill in the image materials and place the Live2D model first):

```bash
python main.py
```

### Software Settings

- Click the "Software Settings" button at the bottom right of the launcher to enter the settings interface.
- Configure the name, persona, username, password, etc., of the virtual mate.
- Set the voice synthesis engine, speech rate, pitch, and various service port numbers.
- Click the "Save" button and restart the software to apply the changes.

### Voice Interaction

- In the main interface of the launcher, select "Enable" from the drop-down menu to activate the real-time voice interaction function.
- Voice input will automatically trigger a conversation with the virtual mate and display in real time in the launcher window.

### Conversation Interface

- Enter text messages in the conversation web page, click the "Send Message" button or press the Enter key to send.
- The response from the virtual mate will be displayed in the chat box.

### Character Display

- Click the "Open Character" button to open the Live2D character display page in the default browser.

### Export Chat History

- Click the "Export History" button at the bottom left of the conversation web page to export the current chat history as a text file.

### Clear Chat History

- Click the "Start New Conversation" button at the bottom left of the conversation web page to clear the current chat history and start a new conversation.

## Technology Stack

- **Python**: Main programming language.
- **Flask**: Web server framework for Live2D.
- **Flet**: Python library for building the conversation web interface.
- **Live2D**: Displaying virtual character images.
- **OpenAI**: Provides interfaces for pre-trained large language models.
- **Edge-TTS**: Microsoft's text-to-speech conversion service.
- **Pyttsx3**: Python's text-to-speech library.
- **Vosk**: Local speech recognition engine.

## Contribution Guide

We welcome and encourage community members to contribute code or suggestions for improvements to this project. Before submitting contributions, please read the standard contribution guide to understand how to correctly submit a pull request.

### How to Contribute

1. Fork this project to your GitHub account.
2. Clone your forked repository to your local machine.
3. Create a new branch, for example, `feature/your-feature`.
4. Make your changes on the new branch.
5. Commit your changes and push to your remote repository.
6. Create a Pull Request to the main branch of this project.

## Issue Feedback

If you encounter any issues during the use of the project, please submit an Issue in the [Issues](https://github.com/swordswind/ai_virtual_mate_web/issues) section.

## Contact Information

- Email: swordswind@qq.com
- Bilibili: [Fengying Jian Wind](https://space.bilibili.com/106439263)

## Version Information

- Current Version: v1.0

## Open Source Project Page

[AI Virtual Mate Web GitHub Page](https://github.com/swordswind/ai_virtual_mate_web) 

## Acknowledgements

Special thanks to all individuals and open source projects that support our project. Your support and contributions have made the AI Virtual Mate Web possible.
