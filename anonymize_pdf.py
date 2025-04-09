import argparse
import fitz  # PyMuPDF
import uuid
import csv
import json
import re


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Convert PDF to Markdown with UUID replacements."
    )
    parser.add_argument("pdf_input", type=str, help="Path to the input PDF file.")
    parser.add_argument("md_output", type=str, help="Path to the output markdown file.")
    parser.add_argument(
        "csv_input", type=str, help="Path to the CSV file of sensitive strings."
    )
    parser.add_argument("json_output", type=str, help="Path to the output JSON file.")
    return parser.parse_args()


def load_sensitive_strings(csv_file):
    replacements = {}
    with open(csv_file, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            sensitive_str = row[0]
            uuid_str = str(uuid.uuid4())
            replacements[uuid_str] = sensitive_str
    return replacements


def convert_pdf_to_markdown(pdf_file, replacements):
    doc = fitz.open(pdf_file)
    md_output = ""
    for page_num in range(doc.page_count):
        page = doc.load_page(page_num)
        text = page.get_text("text")

        for uuid_str, sensitive_str in replacements.items():
            text = re.sub(re.escape(sensitive_str), uuid_str, text)

        md_output += f"\n\n### Page {page_num + 1}\n\n{text}"

    return md_output


def save_markdown(md_output, md_file):
    with open(md_file, "w", encoding="utf-8") as file:
        file.write(md_output)


def save_json(json_file, replacements):
    with open(json_file, "w", encoding="utf-8") as file:
        json.dump(replacements, file, ensure_ascii=False, indent=4)


def main():
    args = parse_arguments()

    # Load sensitive strings and generate replacements
    replacements = load_sensitive_strings(args.csv_input)

    # Convert PDF to Markdown with replaced sensitive strings
    md_output = convert_pdf_to_markdown(args.pdf_input, replacements)

    # Save output markdown and json files
    save_markdown(md_output, args.md_output)
    save_json(args.json_output, replacements)


if __name__ == "__main__":
    main()
