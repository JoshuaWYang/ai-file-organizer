# AI File Organizer

An AI-powered file management tool that automatically organizes images and videos using computer vision. The program uses Ollama Vision models to analyze media files, categorize them, and automatically sort them into organized folders.

## Features

- AI image classification using Ollama Vision models
- Automatically sorts images and videos into custom folders
- Extracts video frames for AI analysis
- Removes duplicate and older file versions
- Separates Topaz AI exports and MP3 files
- Manual file renaming utility
- Supports multiple media file formats

## How It Works

1. User selects a folder to organize
2. Program scans images and videos within the folder
3. AI analyzes media content and determines the correct category
4. Files are automatically moved into organized folders
5. Duplicate versions and unnecessary files can be removed

## Technologies Used

- Python
- Ollama API
- Qwen Vision Model
- OpenCV
- Regular Expressions
- File System Automation

## Installation

Clone the repository:

```bash
git clone https://github.com/JoshuaWYang/AI-File-Organizer.git
cd AI-File-Organizer
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Install Ollama:

https://ollama.com/

Download the Qwen Vision model:

```bash
ollama pull qwen2.5-vl
```

Make sure Ollama is running before starting the program.

## Usage

Run the program:

```bash
python main.py
```

Follow the prompts to select a folder and choose an organization option.

## Project Structure

```
AI-File-Organizer/
│
├── main.py                 # Program entry point
├── organizer.py            # Handles file organization
├── ai_analyzer.py          # AI image/video analysis
├── file_utils.py           # File management utilities
├── version_manager.py      # Duplicate and old version removal
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

## Future Improvements

- Add more customizable organization categories
- Add AI ability to make its own folders
- Support additional file types

## License

This project is for educational and personal use.
