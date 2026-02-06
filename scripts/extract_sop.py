import fitz  # PyMuPDF

pdf_path = "data/SFO_Expenses_SOP_v1.1.pdf"
txt_path = "data/sop.txt"

doc = fitz.open(pdf_path)
all_text = ""

for page in doc:
    all_text += page.get_text() + "\n"

with open(txt_path, "w", encoding="utf-8") as f:
    f.write(all_text)

print(f"Extracted text saved to {txt_path}")
