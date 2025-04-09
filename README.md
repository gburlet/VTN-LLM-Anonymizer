# VTN-LLM-Anonymizer
An example Python application for anonymizing sensitive data in PDFs prior to LLM prompting

Instructions:
pip install -f requirements.txt
make anonymize
make sensitize

The above will run the demo through the anonymization pipeline: this will ingest the PDF with sensitive information into text (markdown) and replace the sensitive fields with uuids. The reverse action (sensitize) will replace any references of these uuids with the original sensitive client data.
