#  Resume Analyzer CLI

A Python-based command-line tool that analyzes `.pdf` resumes by extracting text, counting key skill mentions, and suggesting improvements based on keyword gaps. Perfect for developers, recruiters, and job seekers who want quick resume insights.

---

##  Features

-  Extracts text from PDF resumes
-  Identifies and counts keywords (e.g., Python, SQL, ML)
-  Suggests missing skills based on a predefined list
-  Lightweight CLI-based tool

---

##  Built With

- Python
- [PyMuPDF](https://pymupdf.readthedocs.io/) (`fitz` module)
- Standard Python libraries

---

##  Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/theaadishjain/resume-analyzer-cli.git
   cd resume-analyzer-cli
2.Install dependencies
```bash
pip install PyMuPDF
```

Sample Output

 Keywords Found:
- Python (2)
- SQL (1)
- Machine Learning (0)

 Suggested Skills to Add:
- Machine Learning
- Data Structures
