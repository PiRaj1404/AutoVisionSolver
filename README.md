# AutoVisionSolver

AutoVision Solver leverages advanced visual AI technology to transform image-based educational content into interactive, digital formats. It utilizes Google Cloud Vision for OCR, Google Translate for multilingual support, and generative AI to solve problems extracted from images. This solution is designed to enhance the accessibility and interactivity of educational materials, making it an invaluable tool in educational and problem-solving contexts.

## Features

- **Robust OCR Capabilities**: Integrates Google Cloud Vision to detect text within images.
- **Multilingual Support**: Utilizes Google Cloud Translate to ensure content accessibility across different languages.
- **Advanced Problem Solving**: Incorporates generative AI to interpret and solve detected problems, outputting results in a structured JSON format.
- **Data-Driven Insights**: Manages and utilizes structured JSON data for personalized education and analytics.

## Prerequisites

Before running this project, ensure you have the following:

- Python 3.8 or higher installed
- A Google Cloud account
- API keys for the Google Cloud Vision and Google's generative AI services
- Enabled APIs in the Google Cloud Console
- A gcpKeys.json file with your Google Cloud service account key

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/PiRaj1404/AutoVisionSolver.git
   cd AutoVisionSolver
   ```
   
2. Setup a virtual environment (recommended):
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows use venv\Scripts\activate
    ```
   
3. Install the required packages:
    ```
    pip install -r requirements.txt
    ```
   
4. Configure environment variables:
    - Create a .env file in the project root.
    - Add the following content:
    ```
    GOOGLE_API_KEY='your_api_key_here'
    ```

5. Set up Google Cloud credentials:

- Ensure the `gcpKeys.json` file is in the root or specify its path in your application.

## Running the application

You can run the application by running ```python app.py```

## Output

- **Structured JSON Output:** After processing, the results are stored in `outputData.json` within the project directory. This file contains structured JSON data organized per subject, detailing each problem's translated text, and the solution with steps.
- **Data Organization:** The JSON structure is segmented by subject, allowing for easy navigation and analysis of specific subjects. This detailed organization supports educational performance evaluations, identification of common difficulties, and personalization of learning paths.
- **Use Case for JSON Data:** This output file is essential for further analysis, offering insights for educational technology companies to adapt and enhance their services based on user interactions and performance. It enables data-driven decisions to improve educational tools and tailor learning experiences to individual needs.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your suggestions.

## License
Distributed under the MIT License. See LICENSE for more information.

## Contact
For questions or assistance, please contact Piyush at rajkarne@pdx.edu