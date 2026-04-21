import os
import re
from collections import Counter

# ඉංග්‍රීසි තාක්ෂණික වචන
ENGLISH_KEYWORDS = [
    "Indrakheela", "Hardware", "Signal", "Processing", "Logic", "CPU", 
    "Kernel", "Latency", "Buffer", "Metadata", "Debug", "Sovereign", 
    "Infrastructure", "De-coupling", "Memory", "Stress", "Protocol"
]

# සිංහල පාරිභාෂික වචන
SINHALA_KEYWORDS = [
    "පංචස්කන්ධ", "උපාදාන", "රූප", "වේදනා", "සංඥා", "සංස්කාර", "විඤ්ඤාණ",
    "අනිච්ච", "දුක්ඛ", "අනත්ත", "ආයතන", "ප්‍රතිසංස්කරණය", "අන්තලික්ඛ",
    "අමනුෂ්‍ය", "ස්වෛරී", "පද්ධති", "ඉන්ද්‍රකීල"
]

BUILD_ORDER = [
    "toc.md", "01-system-intro.md", "02-indrakheela.md", "03-rupa-skandha.md",
    "04-vedana-skandha.md", "05-sanna-skandha.md", "06-sankhara-skandha.md",
    "07-vinnana-skandha.md", "08-stress-analysis.md", "09-system-recovery.md",
    "10-conclusion-roadmap.md", "11-future-research.md", "99-appendices.md"
]

def extract_terms(text, keywords):
    found_terms = []
    for term in keywords:
        # සිංහල යුනිකෝඩ් වචන සහ ඉංග්‍රීසි වචන දෙකම හඳුනා ගැනීමට Regex
        matches = re.findall(rf'{term}', text, re.IGNORECASE)
        found_terms.extend(matches)
    return found_terms

def build_manuscript():
    if not os.path.exists("build"):
        os.makedirs("build")
    
    merged_content = ""
    all_eng_terms = []
    all_sin_terms = []

    print("🚀 'ජහිතා භවන්ති' ද්විභාෂා පාරිභාෂික විශ්ලේෂණය ආරම්භ වේ...\n")

    for file_name in BUILD_ORDER:
        file_path = os.path.join("src", file_name)
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                all_eng_terms.extend(extract_terms(content, ENGLISH_KEYWORDS))
                all_sin_terms.extend(extract_terms(content, SINHALA_KEYWORDS))
                merged_content += content + "\n\n"

    # වාර ගණන ගණනය කිරීම
    eng_counts = Counter(all_eng_terms)
    sin_counts = Counter(all_sin_terms)

    # 1. ඒකාබද්ධ කළ ග්‍රන්ථය සුරැකීම
    with open("build/Full_Manuscript.md", "w", encoding="utf-8") as f:
        f.write(merged_content)

    # 2. ද්විභාෂා දර්ශකය (Bilingual Index) සුරැකීම
    with open("build/Complete_Index.txt", "w", encoding="utf-8") as f:
        f.write("ජහිතා භවන්ති - Bilingual Terminology Index\n")
        f.write("="*50 + "\n\n")
        
        f.write("[ සිංහල පාරිභාෂික වචන (Sinhala Terms) ]\n")
        f.write("-" * 40 + "\n")
        for term, count in sin_counts.most_common():
            f.write(f"{term:<25} : {count} වරක්\n")
            
        f.write("\n[ තාක්ෂණික පාරිභාෂික වචන (English Terms) ]\n")
        f.write("-" * 40 + "\n")
        for term, count in eng_counts.most_common():
            f.write(f"{term:<25} : {count} වරක්\n")

    print(f"✅ ගොනු ඒකාබද්ධ කිරීම සාර්ථකයි.")
    print(f"📊 සිංහල පාරිභාෂික වචන {len(sin_counts)} ක් සහ ඉංග්‍රීසි වචන {len(eng_counts)} ක් විශ්ලේෂණය කරන ලදී.")
    print(f"📂 සම්පූර්ණ දර්ශකය 'build/Complete_Index.txt' හි පවතී.\n")

if __name__ == "__main__":
    build_manuscript()
    
