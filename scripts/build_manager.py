
import os
import re
from collections import Counter

# අප විසින් හඳුනාගත යුතු ප්‍රධාන තාක්ෂණික පාරිභාෂික වචන ලැයිස්තුව
TECHNICAL_KEYWORDS = [
    "Indrakheela", "Hardware", "Signal", "Input", "Processing", "Logic", "CPU", 
    "Kernel", "Latency", "Buffer", "Metadata", "Debug", "Open-Source", 
    "Sovereign", "Infrastructure", "De-coupling", "Memory", "Stress", "Protocol",
    "Automation", "Interface", "Architecture", "Root", "Cache", "Synchronize"
]

BUILD_ORDER = [
    "toc.md", "01-system-intro.md", "02-indrakheela.md", "03-rupa-skandha.md",
    "04-vedana-skandha.md", "05-sanna-skandha.md", "06-sankhara-skandha.md",
    "07-vinnana-skandha.md", "08-stress-analysis.md", "09-system-recovery.md",
    "10-conclusion-roadmap.md", "11-future-research.md", "99-appendices.md"
]

def extract_technical_terms(text):
    # පෙළ තුළ ඇති ඉංග්‍රීසි තාක්ෂණික වචන සොයා ගැනීම (Case-insensitive)
    found_terms = []
    for term in TECHNICAL_KEYWORDS:
        # වචනය සම්පූර්ණයෙන් ගැලපේදැයි බැලීමට Regex භාවිතා කරයි
        matches = re.findall(rf'\b{term}\b', text, re.IGNORECASE)
        found_terms.extend([m.capitalize() for m in matches])
    return found_terms

def build_manuscript():
    if not os.path.exists("build"):
        os.makedirs("build")
    
    merged_content = ""
    all_found_terms = []

    print("🚀 'ජහිතා භවන්ති' තාක්ෂණික විශ්ලේෂණය ආරම්භ වේ...\n")

    for file_name in BUILD_ORDER:
        file_path = os.path.join("src", file_name)
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                # තාක්ෂණික වචන සොයා ගැනීම
                all_found_terms.extend(extract_technical_terms(content))
                merged_content += content + "\n\n"

    # වචන වාර ගණන ගණනය කිරීම
    term_counts = Counter(all_found_terms)

    # 1. සම්පූර්ණ ගොනුව සුරැකීම
    with open("build/Full_Manuscript.md", "w", encoding="utf-8") as f:
        f.write(merged_content)

    # 2. තාක්ෂණික පාරිභාෂික ලැයිස්තුව (Technical Index) වෙනම සුරැකීම
    with open("build/Technical_Index.txt", "w", encoding="utf-8") as f:
        f.write("Jahitha Bhavanthi - Technical Terms Frequency Index\n")
        f.write("="*50 + "\n")
        for term, count in term_counts.most_common():
            f.write(f"{term:<25} : {count} වරක්\n")

    print(f"✅ ගොනු ඒකාබද්ධ කිරීම අවසන්.")
    print(f"📊 තාක්ෂණික වචන {len(term_counts)} ක් හඳුනාගන්නා ලදී.")
    print(f"📂 දර්ශකය 'build/Technical_Index.txt' හි සුරැකෙන ලදී.\n")

if __name__ == "__main__":
    build_manuscript()
  
