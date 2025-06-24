import argparse
import fitz  # PyMuPDF

# List of common tech skills to analyze (you can expand this)
SKILLS = [
    "python", "java", "sql", "machine learning", "deep learning",
    "data science", "django", "flask", "c++", "git", "nlp", "react",
    "aws", "docker", "tensorflow", "pytorch", "linux"
]

def extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = ""
        for page in doc:
            text += page.get_text()
        return text.lower()
    except Exception as e:
        print(f"❌ Error reading PDF: {e}")
        return ""

def analyze_skills(text):
    skill_count = {}
    for skill in SKILLS:
        count = text.count(skill.lower())
        skill_count[skill] = count
    return skill_count

def suggest_improvements(skill_count):
    suggestions = []
    for skill, count in skill_count.items():
        if count == 0:
            suggestions.append(f"- Consider mentioning {skill.title()} if relevant to your experience.")
    return suggestions

def main():
    parser = argparse.ArgumentParser(description="🔍 Resume Analyzer CLI Tool")
    parser.add_argument("pdf", help="Path to the resume PDF file")
    args = parser.parse_args()

    print("\n📄 Extracting text from resume...")
    resume_text = extract_text_from_pdf(args.pdf)

    if not resume_text:
        print("❌ No text found or error reading the file.")
        return

    print("\n✅ Analyzing for key skills...")
    skill_count = analyze_skills(resume_text)

    print("\n📊 Skill Mentions:")
    for skill, count in skill_count.items():
        status = "✅" if count > 0 else "❌"
        print(f"{status} {skill.title()}: {count} mention(s)")

    suggestions = suggest_improvements(skill_count)
    if suggestions:
        print("\n💡 Suggestions:")
        for s in suggestions:
            print(s)
    else:
        print("\n🎉 Great! Your resume covers all key skills.")

if __name__ == "__main__":
    main()
