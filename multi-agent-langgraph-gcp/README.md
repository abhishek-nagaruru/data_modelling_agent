# Multi-Agent LangGraph GCP

## Overview
This project implements a multi-agent solution using LangGraph, integrated with Google Cloud Platform (GCP) and Gemini. The system is designed to facilitate agent-based interactions and graph-based data management.

## Project Structure
```
multi-agent-langgraph-gcp
├── src
│   ├── agents
│   │   └── __init__.py
│   ├── graph
│   │   └── __init__.py
│   ├── gcp
│   │   └── __init__.py
│   ├── gemini
│   │   └── __init__.py
│   └── main.py
├── requirements.txt
└── README.md
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd multi-agent-langgraph-gcp
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Configure Google Cloud Platform:
   - Set up your GCP project and enable necessary APIs.
   - Authenticate using your service account or user credentials.

5. Configure Gemini integration:
   - Obtain your Gemini API keys and set them in the environment variables or configuration files.

## Usage
To run the application, execute the following command:
```
python src/main.py
```

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.