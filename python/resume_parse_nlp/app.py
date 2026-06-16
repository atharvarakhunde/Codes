import json
from resume_parser import extract_resume_data

def read_resume(file_path):
    with open(file_path, "r") as file:
        return file.read()

if __name__ == "__main__":
    resume_text = read_resume("sample_resume.txt")
    extracted_data = extract_resume_data(resume_text)

    print("Extracted Resume Data:")
    print(json.dumps(extracted_data, indent=4))
