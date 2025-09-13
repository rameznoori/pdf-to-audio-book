
# PDF to Audio Book using Python

This Python script reads the text from a selected PDF file and converts it to speech using text-to-speech synthesis. The program uses the `PyPDF2` library to extract text from each page of the PDF and `pyttsx3` for offline text-to-speech conversion. It provides a simple file dialog to choose the PDF, then sequentially reads out the entire document aloud.
## Features

- Open and read any user-selected PDF file
- Extract text from all pages of the PDF using PyPDF2
- Convert the extracted text to speech with pyttsx3
- Offline, no internet connection required for speech synthesis
- Simple GUI file picker dialog to select PDF file

## Getting Started / Installation

- Install Python 3.x if not installed.
- Install required Python packages via pip:

    ```
    pip install pyttsx3 PyPDF2
    ```
- Run the Python script. A file picker will prompt you to select the PDF file to read.
## Usage Instructions

- Run the script.
- A file dialog will open; select the PDF file you want to convert to speech.
- The program will read the entire PDF aloud, page by page.
- To stop, terminate the script execution.
## Technologies Used

- Python 3.x
- PyPDF2 for PDF text extraction
- pyttsx3 for text-to-speech conversion (offline)
- tkinter for file dialog GUI
## File Structure

```
/
├── script.py          # Main Python script for PDF to speech functionality
└── README.md             # This documentation file
```
## Customization

- You may customize voice rate, volume, and voice properties in the pyttsx3 initialization (`player = pyttsx3.init()`).
- Extend the script to add GUI controls for play, pause, stop, or select reading range.
- Integrate error handling for unreadable PDFs or empty pages.
## Limitations

- Works best with text-based PDFs, not scanned image PDFs.
- No pause or stop button; speech runs until the PDF is fully read.
- No support for selecting specific pages or partial reading.
- The quality and voice depend on the local text-to-speech engine installed on the system.
## Future Improvements

- Add a GUI interface with controls to pause, resume, and jump between pages.
- Support for scanned PDFs using OCR integration.
- Option to save speech output as audio file.
- Add language and voice selection features.
- Improve error handling and user feedback.
## Contributing

Contributions are always welcome! To contribute:

- Fork the repository.
- Make feature branches for your improvements.
- Submit pull requests with clear descriptions.
## License


This project is open-source and available under the MIT License.
## Acknowledgements

- PyPDF2 and pyttsx3 developers for their powerful libraries.
- Python community for continuous support and resources.
- Tutorials and sample projects that helped build this tool.