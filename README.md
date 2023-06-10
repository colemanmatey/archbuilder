
# Archbuilder

Archbuilder is a tool that aims to speed up the setting up of projects by creating the project directories and files from user-defined templates.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Archbuilder.
```bash
  pip install archbuilder
```
    
## Usage

1. Python script
```python
# Import the following classes
from builder.template import Template
from builder.builder import Builder

# Create a template from a json file
template = Template('sass.json')

# Create the project tree from the template
project = Builder('sass', template)
project.build()
```

2. Command-line
Invoke archbuilder to create your project. Pass the name of the project as the first argument and the path to the json file as the second argument
```bash
archbuilder sass sass.json
```
## Contributing

Contributions are always welcome!

For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.
## License

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
