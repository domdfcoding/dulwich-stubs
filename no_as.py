# stdlib
import pathlib
import re

# 3rd party
import isort  # type: ignore
from isort import Config

isort_config = Config(settings_file=".isort.cfg")

for filename in pathlib.Path("dulwich-stubs").rglob("*.pyi"):
	# print(filename)
	file_contents = filename.read_text()
	for entry in re.findall(r"([A-Za-z0-9_.]+) as ([A-Za-z0-9_.]+)", file_contents):
		if entry[0] == entry[1]:
			file_contents = file_contents.replace(f"{entry[0]} as {entry[1]}", entry[0])

	file_contents = isort.code(file_contents, config=isort_config)
	filename.write_text(file_contents)
