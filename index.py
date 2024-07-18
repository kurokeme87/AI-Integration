import os
import time
from dotenv import load_dotenv
import json
from openai import OpenAI
from tenacity import retry, stop_after_attempt, wait_exponential

# Load environment variables
load_dotenv()

# Set up AIML API token
API_TOKEN = os.getenv("AIML_API_TOKEN")
BASE_URL = "https://api.aimlapi.com"

client = OpenAI(
    api_key=API_TOKEN,
    base_url=BASE_URL,
)


@retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))
def generate_ai_content(prompt, system_content):
    try:
        chat_completion = client.chat.completions.create(
            model="mistralai/Mistral-7B-Instruct-v0.2",
            messages=[
                {"role": "system", "content": system_content},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            max_tokens=256,
        )
        return chat_completion.choices[0].message.content.strip()
    except Exception as e:
        print(f"Error generating content: {e}")
        raise


def generate_resume_summary(job_title):
    system_content = "You are a professional resume writer. Create a concise yet comprehensive resume summary that highlights key skills, experiences, and achievements relevant to the job title."
    prompt = f"Write a professional resume summary for a {job_title}. Include relevant skills, experiences, and achievements:"
    return generate_ai_content(prompt, system_content)


def extract_keywords(job_title):
    system_content = "You are a job market expert. Provide relevant keywords suitable for ATS (Applicant Tracking System) scanning."
    prompt = f"List 10-15 relevant keywords for a {job_title}, separated by commas. These should be optimized for ATS scanning:"
    keywords = generate_ai_content(prompt, system_content)
    return [keyword.strip() for keyword in keywords.split(",")] if keywords else []


def generate_role_objectives(job_title):
    system_content = "You are a career counselor. Provide clear, actionable, and numbered role objectives that align with the job title and industry standards."
    prompt = f"List 5-7 numbered role objectives for a {job_title}. Ensure they are clear, actionable, and align with industry standards:"
    objectives = generate_ai_content(prompt, system_content)
    return (
        [
            obj.strip()
            for obj in objectives.split("\n")
            if obj.strip() and obj[0].isdigit()
        ]
        if objectives
        else []
    )


def generate_resume_content(job_title):
    content = {
        "resume_summary": generate_resume_summary(job_title),
        "optimized_keywords": extract_keywords(job_title),
        "role_objectives": generate_role_objectives(job_title),
    }
    return json.dumps(content, indent=2)


# Example usage
if __name__ == "__main__":
    job_title = input("Enter the job title: ")
    try:
        resume_content = generate_resume_content(job_title)
        print(resume_content)
    except Exception as e:
        print(f"Failed to generate resume content: {e}")
