
import os
import subprocess
import sys

# ව්‍යාපෘති මානයන් සහ සැකසුම් (B5 Standard)
PAPER_SIZE = 'paperwidth=176mm, paperheight=250mm, margin=20mm'
FONT = 'LKLUG'
SOURCE_DIR = 'src'
BUILD_DIR = 'build'
OUTPUT_PDF = os.path.join(BUILD_DIR, 'Jahitha_Bhavanthi_B5_Master.pdf')
OUTPUT_DOCX = os.path.join(BUILD_DIR, 'Jahitha_Bhavanthi_Draft.docx')

def run_build():
    # 1. Build ෆෝල්ඩරය පරීක්ෂා කිරීම
    if not os.path.exists(BUILD_DIR):
        os.makedirs(BUILD_DIR)
        print(f"[*] Created {BUILD_DIR} directory.")

    # 2. ගොනු ලැයිස්තුගත කිරීම සහ පරීක්ෂා කිරීම
    # 'src' ෆෝල්ඩරයේ ඇති අංකිත .md ගොනු පමණක් ලබා ගැනීම (00, 01, 02...)
    md_files = sorted([os.path.join(SOURCE_DIR, f) for f in os.listdir(SOURCE_DIR) 
                       if f.endswith('.md') and f[0].isdigit()])

    if not md_files:
        print("[!] Error: No markdown files found in 'src/' folder with numeric prefix.")
        sys.exit(1)

    print(f"[*] Found {len(md_files)} chapters. Starting Pandoc build...")

    # 3. Pandoc විධානය සකස් කිරීම (PDF සඳහා)
    # toc.md තිබේ නම් එය ලැයිස්තුවේ මුලට එක් කෙරේ
    pandoc_cmd_pdf = [
        'pandoc',
        *md_files,
        '--pdf-engine=xelatex',
        '-V', f'mainfont={FONT}',
        '-V', f'geometry:{PAPER_SIZE}',
        '--toc',
        '--toc-depth=3',
        '--number-sections',
        '-o', OUTPUT_PDF
    ]

    # 4. Pandoc විධානය (DOCX සඳහා)
    pandoc_cmd_docx = [
        'pandoc',
        *md_files,
        '-o', OUTPUT_DOCX
    ]

    try:
        # PDF Build එක ක්‍රියාත්මක කිරීම
        print("[*] Generating Master PDF (B5)...")
        subprocess.run(pandoc_cmd_pdf, check=True)
        print(f"[+] Success! PDF generated at: {OUTPUT_PDF}")

        # DOCX Build එක ක්‍රියාත්මක කිරීම
        print("[*] Generating Draft DOCX...")
        subprocess.run(pandoc_cmd_docx, check=True)
        print(f"[+] Success! DOCX generated at: {OUTPUT_DOCX}")

    except subprocess.CalledProcessError as e:
        print(f"[!] Build failed with error code: {e.returncode}")
        sys.exit(1)
    except FileNotFoundError:
        print("[!] Error: Pandoc is not installed or not in PATH.")
        sys.exit(1)

if __name__ == "__main__":
    print("=== Jahitha Bhavanthi Build System v2.0 ===")
    run_build()
    
