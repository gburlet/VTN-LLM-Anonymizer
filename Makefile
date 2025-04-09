anonymize:
	python anonymize_pdf.py data_in/sample_noa.pdf data_out/noa_anon.md data_in/sensitive_strings.csv data_out/mappings.json

sensitize:
	python sensitize_markdown.py data_out/noa_anon.md data_reverse/sample_noa.md data_out/mappings.json