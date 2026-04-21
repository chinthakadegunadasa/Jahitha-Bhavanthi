#!/bin/bash

# Build settings
BOOK_NAME="Jahitha_Bhavanthi_v1.0"
OUTPUT_DIR="build"
SOURCE_DIR="src"
FONT="Iskoola Pota" # හෝ "Nirmala UI"

# Create build directory if not exists
mkdir -p $OUTPUT_DIR

echo "🚀 Starting Production Build for $BOOK_NAME..."

# List files in specific order for the book
FILES=(
    "$SOURCE_DIR/toc.md"
    "$SOURCE_DIR/01-system-intro.md"
    "$SOURCE_DIR/02-indrakheela.md"
    "$SOURCE_DIR/03-rupa-skandha.md"
    "$SOURCE_DIR/04-vedana-skandha.md"
    "$SOURCE_DIR/05-sanna-skandha.md"
    "$SOURCE_DIR/06-sankhara-skandha.md"
    "$SOURCE_DIR/07-vinnana-skandha.md"
    "$SOURCE_DIR/08-stress-analysis.md"
    "$SOURCE_DIR/09-system-recovery.md"
    "$SOURCE_DIR/10-conclusion-roadmap.md"
    "$SOURCE_DIR/11-future-research.md"
    "$SOURCE_DIR/99-appendices.md"
)

echo "📝 Merging chapters and generating PDF..."

# Generate PDF with Unicode support (XeLaTeX)
pandoc "${FILES[@]}" \
    -o "$OUTPUT_DIR/$BOOK_NAME.pdf" \
    --pdf-engine=xelatex \
    -V mainfont="$FONT" \
    --toc \
    --number-sections \
    -V geometry:margin=1in

echo "📂 Generating DOCX for editing..."

# Generate Word Document
pandoc "${FILES[@]}" \
    -o "$OUTPUT_DIR/$BOOK_NAME.docx" \
    --toc

echo "✅ Build Completed! Check the /$OUTPUT_DIR folder."
