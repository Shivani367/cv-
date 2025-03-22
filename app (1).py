import streamlit as st
import fitz  # PyMuPDF
import requests
import json

def ai_output(input_text, pdf_text, prompt):
    combined_input = f"{input_text}\n\n{pdf_text}\n\n{prompt}"
    response = requests.post(
        url="https://api.aimlapi.com/chat/completions",
        headers={
            "Authorization": "Bearer 6cb41c23403144868c5befe28e649fc4",
            "Content-Type": "application/json",
        },
        data=json.dumps(
            {
                "model": "gpt-4o",
                "messages": [{"role": "user", "content": combined_input}],
                "max_tokens": 512,
                "stream": False,
            }
        ),
    )
    response.raise_for_status()
    return response.json().get("choices", [{}])[0].get("message", {}).get("content", "Error: No response")

def ai_ans(input_text, prompt):
    combined_input = f"{input_text}\n\n{prompt}"
    response = requests.post(
        url="https://api.aimlapi.com/chat/completions",
        headers={
            "Authorization": "Bearer 6cb41c23403144868c5befe28e649fc4",
            "Content-Type": "application/json",
        },
        data=json.dumps(
            {
                "model": "gpt-4o",
                "messages": [{"role": "user", "content": combined_input}],
                "max_tokens": 512,
                "stream": False,
            }
        ),
    )
    response.raise_for_status()
    return response.json().get("choices", [{}])[0].get("message", {}).get("content", "Error: No response")

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        pdf_document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        text = "".join(page.get_text() for page in pdf_document)
        pdf_document.close()
        return text
    else:
        raise FileNotFoundError("No file uploaded")

st.set_page_config(page_title="ATS Resume Expert")
st.header("HARIMAY ATS Tracking System")

input_text = st.text_area("Job Description:", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])
job_role = st.text_input("Enter Job Role", key="job")

if uploaded_file is not None:
    pdf_text = input_pdf_setup(uploaded_file)
    st.write("PDF file uploaded and processed successfully.")
else:
    pdf_text = ""
    st.write("Please upload the resume.")

submit1 = st.button("Tell me about the Resume")
submit2 = st.button("Percentage Match")
submit3 = st.button("Job Skills")
submit4 = st.button("Missing Keywords")

input_prompt1 = """
You are an experienced Technical Human Resource Manager. Your task is to review the provided resume against the job description.
Please share your professional evaluation on whether the candidate's profile aligns with the role.
Highlight the strengths and weaknesses of the applicant in relation to the specified job requirements.
"""

input_prompt2 = """
You are a skilled ATS (Applicant Tracking System) scanner with a deep understanding of ATS functionality.
Your task is to evaluate the resume against the provided job description. Provide the percentage match if the resume aligns
with the job description. First, present the output as a percentage, then list missing keywords, and finally, offer your thoughts.
"""

input_prompt3 = """
You are an advanced career advisor and job market expert with deep insights into various industries. When given a job role, your task is to identify and list the key skills and qualifications that are most commonly required for success in that position. Please provide a structured output that includes:

1. A detailed list of technical and hard skills.
2. A summary of soft skills crucial for the role.
3. Recommended educational qualifications and certifications associated with the job.
"""

input_prompt4 = """
You are an expert in resume optimization and keyword integration for job applications. I am providing my resume content along with a job description. Your task is to analyze the resume and identify any important keywords or skills from the job description that are missing in my resume. For each missing keyword or skill, provide the following:

1. A clear explanation of all the missing keywords or skills and why they are important for the role.
2. A detailed suggestion for a sentence or bullet point that can be added to the resume to include the missing keyword.
3. Guidance on where in the resume (e.g., Professional Experience, Skills, Education, Projects) the new content should be inserted for the best impact.

Ensure that the suggestions are tailored to the context of my existing resume, maintaining a natural flow and relevance to my career background.
Also, tell me why I would not be selected for an interview for this position according to my resume.
"""

if submit1:
    if pdf_text:
        response = ai_output(input_text, pdf_text, input_prompt1)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.write("Please upload the resume.")
elif submit2:
    if pdf_text:
        response = ai_output(input_text, pdf_text, input_prompt2)
        st.subheader("The Response is:")
        st.write(response)
    else:
        st.write("Please upload the resume.")
elif submit3:
    response = ai_ans(job_role, input_prompt3)
    st.subheader("The Response is:")
    st.write(response)
elif submit4:
    if pdf_text:
        response = ai_output(input_text, pdf_text, input_prompt4)
        st.subheader("Missing things which need to be present in your resume:")
        st.write(response)
