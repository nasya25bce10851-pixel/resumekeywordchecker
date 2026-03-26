def extract_keywords(text):
    # Convert to lowercase and split words
    words = text.lower().split()
    return set(words)


def check_resume():
    print(" Resume Keyword Checker \n")
    
    # Input
    resume_text = input("Paste your resume text:\n")
    job_description = input("\nPaste job description:\n")
    
    # Extract keywords
    resume_keywords = extract_keywords(resume_text)
    job_keywords = extract_keywords(job_description)
    
    # Find matching keywords
    matched = resume_keywords.intersection(job_keywords)
    missing = job_keywords.difference(resume_keywords)
    
    # Score calculation
    score = (len(matched) / len(job_keywords)) * 100 if job_keywords else 0
    
    print("\nRESULT ")
    print(f"Match Score: {round(score,2)}%")
    print("\nMatched Keywords:")
    print(matched)
    
    print("\nMissing Keywords:")
    print(missing)


check_resume()
