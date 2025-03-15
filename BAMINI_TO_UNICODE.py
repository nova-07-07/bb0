from PyPDF2 import PdfReader
from reportlab.pdfgen import canvas
import os

# Bamini to Unicode mapping
BAMINI_TO_UNICODE = {
"m":"அ", "M":"ஆ", ",":"இ", "<":"ஈ", "c":"உ", "C":"ஊ", "v":"எ", "V":"ஏ", "I":"ஐ", "x":"ஒ", "X":"ஓ", "xs":"ஔ",
">":",",
"f":"க", "q":"ங", "r":"ச", "Q":"ஞ", "l":"ட", "z":"ண", "j":"த", "e":"ந", "g":"ப", "k":"ம",
"a":"ய", "u":"ர", "y":"ல", "t":"வ", "o":"ழ", "s":"ள", "w":"ற", "d":"ன",

"[":"ஜ", "\\":"ஷ", "]":"ஸ", "`":"ஹ", "~":"க்ஷ",

"fh":"கா", "fp":"கி", "fP":"கீ", "F":"கு", "$":"கூ", "nf":"கெ","Nf":"கே", "if":"கை", "nfh":"கொ", "Nfh":"கோ", "nfs":"கௌ",
"qh":"ஙா", "qp":"ஙி", "qP":"ஙீ", "q§":"ஙு", "q_":"ஙூ", "nq":"ஙெ", "Nq":"ஙே", "iq":"ஙை", "nqh":"ஙொ", "Nqh":"ஙோ", "nqs":"ஙௌ",
"rh":"சா", "rp":"சி", "rP":"சீ", "R":"சு", "#":"சூ", "nr":"செ", "Nr":"சே", "ir":"சை", "nrh":"சொ", "Nrh":"சோ", "nrs":"சௌ",
"Qh":"ஞா", "Qp":"ஞி", "QP":"ஞீ", "Q§":"ஞு", "Q_":"ஞூ", "nQ":"ஞெ", "NQ":"ஞே", "iQ":"ஞை", "nQh":"ஞொ", "NQh":"ஞோ", "nQs":"ஞௌ",
"lh":"டா", "lp":"டி","b":"டி", "lP":"டீ", "L":"டு", "^":"டூ", "nl":"டெ", "Nl":"டே", "il":"டை", "nlh":"டொ", "Nlh":"டோ", "nls":"டௌ",
"zh":"ணா", "zp":"ணி", "zP":"ணீ", "Z":"ணு", "Z}":"ணூ", "nz":"ணெ", "Nz":"ணே", "iz":"ணை", "nzh":"ணொ", "Nzh":"ணோ", "nzs":"ணௌ",
"jh":"தா", "jp":"தி", "jP":"தீ", "J":"து", "J}":"தூ", "nj":"தெ", "Nj":"தே", "ij":"தை", "njh":"தொ", "Njh":"தோ", "njs":"தௌ",
"eh":"நா", "ep":"நி", "eP":"நீ", "E":"நு", "E}":"நூ", "ne":"நெ", "Ne":"நே", "ie":"நை", "neh":"நொ", "Neh":"நோ", "nes":"நௌ",
"gh":"பா", "gp":"பி", "gP":"பீ", "G":"பு", "G+":"பூ", "G+kp":"பூமி", "ng":"பெ", "Ng":"பே", "ig":"பை", "ngh":"பொ", "Ngh":"போ", "ngs":"பௌ",
"kh":"மா", "kp":"மி", "kP":"மீ", "K":"மு", "%":"மூ", "nk":"மெ", "Nk":"மே", "ik":"மை", "nkh":"மொ", "Nkh":"மோ", "nks":"மௌ",
"ah":"யா", "ap":"யி", "aP":"யீ", "A":"யு", "A+":"யூ", "na":"யெ", "Na":"யே", "ia":"யை", "nah":"யொ", "Nah":"யோ", "nas":"யௌ",
"uh":"ரா", "up":"ரி", "uP":"ரீ", "U":"ரு", "&":"ரூ", "nu":"ரெ", "Nu":"ரே", "iu":"ரை", "nuh":"ரொ", "Nuh":"ரோ", "nus":"ரௌ",
"yh":"லா", "yp":"லி", "yP":"லீ", "Y":"லு", "Y}":"லூ", "ny":"லெ", "Ny":"லே", "iy":"லை", "nyh":"லொ", "Nyh":"லோ", "nys":"லௌ",
"th":"வா", "tp":"வி", "tP":"வீ", "T":"வு", "T+":"வூ", "nt":"வெ", "Nt":"வே", "it":"வை", "nth":"வொ", "Nth":"வோ", "nts":"வௌ",
"oh":"ழா", "op":"ழி", "oP":"ழீ", "O":"ழு", "*":"ழூ", "no":"ழெ", "No":"ழே", "io":"ழை", "noh":"ழொ", "Noh":"ழோ", "nos":"ழௌ",
"sh":"ளா", "sp":"ளி", "sP":"ளீ", "S":"ளு", "ns":"ளெ", "Ns":"ளே", "is":"ளை", "nsh":"ளொ", "Nsh":"ளோ", "nss":"ளௌ",
"wh":"றா", "wp":"றி", "wP":"றீ", "W":"று", "W}":"றூ", "nw":"றெ", "Nw":"றே", "iw":"றை", "nwh":"றொ", "Nwh":"றோ", "nws":"றௌ",
"dh":"னா", "dp":"னி", "dP":"னீ", "D":"னு", "D}":"னூ", "nd":"னெ", "Nd":"னே", "id":"னை", "ndh":"னொ", "Ndh":"னோ", "nds":"னௌ",

"f;":"க்", "q;":"ங்", "r;":"ச்", "Q;":"ஞ்", "l;":"ட்", "z;":"ண்", "j;":"த்", "e;":"ந்", "g;":"ப்", "k;":"ம்",
"a;":"ய்", "u;":"ர்", "y;":"ல்", "t;":"வ்", "o;":"ழ்", "s;":"ள்", "w;":"ற்", "d;":"ன்",

"h":"ா", "p":"ி", "P":"ீ", "§":"ு", "_":"ூ", "n":"ெ", "N":"ே", "i":"ை","@":";", "o":"ொ", "O":"ோ", "s":"ௌ", ";":"்", "/":"ஂ", "௃":"ஃ"

}

# Function to convert Bamini text to Unicode
def convert_bamini_text(text):
    for bamini, unicode_char in sorted(BAMINI_TO_UNICODE.items(), key=lambda x: -len(x[0])):
        text = text.replace(bamini, unicode_char)
        text = text.replace("ப+","பூ")
        text = text.replace("அங்ே க","அங்கே")
        text = text.replace("ஆண்டுகொள்ௌ","ஆண்டுகொள்ள")
        text = text.replace("அவா்கௌது","அவர்களது")
        text = text.replace("  ஷ்"," ஷ்")
        text = text.replace(" ஷ்","ஷ்")
        text = text.replace(" க்","க்")
        text = text.replace("என் ற","என்ற")
        text = text.replace(" ன்","ன்")
        text = text.replace("முோவது","முழுவது")
        text = text.replace("திட்டம ்","திட்டம ்")
        text = text.replace("அழைக்கப்பட் டது ்","அழைக்கப்பட்டது ்")
    return text

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""  # Extract text safely
    return text.strip()

# Function to create a Unicode text file
def save_unicode_text(text, output_txt):
    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(text)

# Input and output paths
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()  # Hide the main window

input_pdf = filedialog.askopenfilename(title="Select a PDF File", filetypes=[("PDF Files", "*.pdf")])

if input_pdf:  # Proceed only if a file is selected
    extracted_text = extract_text_from_pdf(input_pdf)
    converted_text = convert_bamini_text(extracted_text)
    save_unicode_text(converted_text, "converted_unicode1.txt")
else:
    print("No file selected.")

def get_unique_filename(base_name):
    if not os.path.exists(base_name):  
        return base_name  # Use the base name if it doesn’t exist
    i = 1
    while True:
        new_name = f"{base_name.split('.')[0]}{i}.txt"
        if not os.path.exists(new_name):
            return new_name
        i += 1

# Set output file name dynamically
output_txt = get_unique_filename("converted_unicode.txt")

# Process PDF
extracted_text = extract_text_from_pdf(input_pdf)
converted_text = convert_bamini_text(extracted_text)
save_unicode_text(converted_text, output_txt)

print("Conversion complete. Output saved to:", output_txt)
