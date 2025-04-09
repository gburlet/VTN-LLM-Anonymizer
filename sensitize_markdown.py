import argparse
import json
import re


def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Reverse the markdown UUID replacement."
    )
    parser.add_argument(
        "md_input", type=str, help="Path to the input markdown file with UUIDs."
    )
    parser.add_argument(
        "md_output",
        type=str,
        help="Path to the output markdown file with sensitive strings.",
    )
    parser.add_argument(
        "json_input",
        type=str,
        help="Path to the JSON file of UUID -> sensitive string map.",
    )
    return parser.parse_args()


def load_json(json_file):
    with open(json_file, "r", encoding="utf-8") as file:
        return json.load(file)


def replace_uuids_in_markdown(md_file, replacements):
    with open(md_file, "r", encoding="utf-8") as file:
        content = file.read()

    # Replace each UUID with the corresponding sensitive string
    for uuid_str, sensitive_str in replacements.items():
        content = content.replace(uuid_str, sensitive_str)

    return content


def save_markdown(md_output, md_content):
    with open(md_output, "w", encoding="utf-8") as file:
        file.write(md_content)


def main():
    args = parse_arguments()

    # Load UUID -> sensitive string mapping
    replacements = load_json(args.json_input)

    # Replace UUIDs in markdown with sensitive strings
    md_content = replace_uuids_in_markdown(args.md_input, replacements)

    # Save the reversed markdown content
    save_markdown(args.md_output, md_content)


if __name__ == "__main__":
    main()
