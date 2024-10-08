import pdfplumber

def extract_jobs_from_pdf(pdf_path):
    jobs = []

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                lines = text.split('\n')
                for line in lines:
                    # Filter for job-related lines
                    if any(char.isdigit() for char in line) and any(char.isalpha() for char in line):
                        jobs.append(line)

    return jobs

pdf_path = 'ISCO-08.pdf'
jobs = extract_jobs_from_pdf(pdf_path)

# Print the extracted jobs
file_to_write = ""
with open('job_list_hierarchical', 'w') as file:
    for job in jobs:
        temp = job
        file.write(temp + "\n")