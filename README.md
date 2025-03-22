# ATS Resume Tracker

## Overview
The **ATS Resume Tracker** is an AI-powered tool designed to automate and optimize the resume screening process. Built as part of the **Alumni Connect Platform**, this system leverages **GPT-based AI** to analyze resumes and match them with job postings efficiently. It provides recruiters and job seekers with a seamless and intelligent job-matching experience.

## Features
- **Automated Resume Parsing**: Extracts key details such as skills, experience, education, and certifications.
- **Job Matching**: Uses AI-driven algorithms to match resumes with job descriptions.
- **Scoring System**: Assigns a compatibility score based on keyword relevance, job requirements, and ATS ranking techniques.
- **Dashboard & Insights**: Provides recruiters with real-time analytics and candidate ranking.
- **Interactive Feedback**: Offers candidates suggestions to improve their resumes for better ATS performance.
- **Integration with Alumni Connect Platform**: Allows seamless job postings and applications within the ecosystem.

## Tech Stack
- **Frontend**: React.js
- **Backend**: Supabase
- **AI Processing**: Google Generative AI, GPT
- **Parsing Libraries**: PyPDF2, python-docx
- **Development Tools**: Streamlit, Python-dotenv

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/ats-resume-tracker.git
   cd ats-resume-tracker
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables in `.env`:
   ```sh
   SUPABASE_URL=your_supabase_url
   SUPABASE_KEY=your_supabase_key
   GPT_API_KEY=your_gpt_api_key
   ```
4. Run the application:
   ```sh
   streamlit run app.py
   ```

## Usage
1. Upload a resume in PDF or DOCX format.
2. The system extracts relevant information and compares it with job postings.
3. Candidates receive feedback on their resume’s ATS score and suggestions for improvement.
4. Recruiters can view ranked candidates and detailed insights.

## Future Enhancements
- Integration with LinkedIn profiles for better job matching.
- Advanced NLP-based keyword optimization for resume improvement.
- Support for multiple resume formats and multilingual processing.

## Contributing
Feel free to fork the repository and submit pull requests. Suggestions and feature requests are welcome!

## License
This project is licensed under the MIT License.

