# AI-Powered Resume Content Generator

This Python script generates resume content based on a given job title using the AIML API. It creates a resume summary, extracts optimized keywords, and generates role objectives tailored to the specified job title.

## Features

- Generates a professional resume summary
- Extracts ATS-optimized keywords
- Creates role-specific objectives
- Handles API rate limiting with exponential backoff

## Prerequisites

Before running this script, make sure you have the following installed:

- Python 3.6+
- pip (Python package installer)

## Installation

1. Clone this repository or download the script.

2. Install the required packages:

pip install python-dotenv

pip install openai

pip install tenacity



3. Create a `.env` file in the same directory as the script and add your AIML API token:

## Usage

Run the script from the command line:

python index.py

When prompted, enter the job title for which you want to generate resume content.

The script will output a JSON-formatted string containing:
- A resume summary
- Optimized keywords
- Role objectives

## Configuration

- The script uses the `mistralai/Mistral-7B-Instruct-v0.2` model by default. You can change this in the `generate_ai_content` function if needed.
- The maximum number of tokens for each API call is set to 256. Adjust the `max_tokens` parameter in `generate_ai_content` if you need longer responses.
- The retry mechanism is set to attempt 3 times with exponential backoff. Modify the `@retry` decorator parameters if you need different retry behavior.

## Error Handling

The script includes basic error handling and will print error messages if it fails to generate content. It uses a retry mechanism to handle temporary failures or rate limiting issues.

## Contributing

Feel free to fork this repository and submit pull requests with any enhancements.

## Disclaimer

This script interacts with an external API. Make sure you comply with the API's terms of service and have the necessary permissions to use it.
