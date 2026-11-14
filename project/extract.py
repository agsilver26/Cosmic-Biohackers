import PdfReader

# Load your NASA medical PDF
reader = PdfReader("final_summary.pdf")
all_text = ""

# Loop through pages and extract text
for page in reader.pages:
    text = page.extract_text()
    if text:
        all_text += text + "\n"

# Save it as a clean text file
with open("medical_knowledge.txt", "w", encoding="utf-8") as f:
    f.write(all_text)

print("PDF successfully converted to an offline text database!")