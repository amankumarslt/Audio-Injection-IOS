# Appium iOS Audio Injection Test

This project demonstrates Appium automation testing for iOS audio injection capabilities using LambdaTest cloud platform.

## Prerequisites

- Python 3.11 or higher
- pip (Python package installer)

## Setup Instructions

### 1. Activate Virtual Environment

If you haven't created a virtual environment yet, create one:

```bash
python3 -m venv venv
```

Activate the virtual environment:

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

### 2. Install Dependencies

Install the required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

This will install:
- Appium-Python-Client
- pytest
- requests

## Running Tests

Execute the iOS audio injection test:

```bash
pytest tests/test_ios.py
```

## Project Structure

```
.
├── conftest.py          # Pytest configuration and driver fixture setup
├── pytest.ini          # Pytest configuration file
├── requirements.txt     # Python dependencies
├── tests/
│   └── test_ios.py     # iOS audio injection test
└── audio/
    └── harvard.wav     # Audio file for injection testing
```

## Test Details

The test (`tests/test_ios.py`) performs the following actions:
- Injects audio into the iOS app session
- Clicks the microphone button to start recording
- Stops the recording
- Navigates to the Recordings tab
- Plays back the recorded audio

## Notes

- Make sure your LambdaTest credentials are configured in `conftest.py`
- The test uses LambdaTest's cloud platform for iOS device testing
- Audio injection is enabled via the `enableAudioInjection` capability
