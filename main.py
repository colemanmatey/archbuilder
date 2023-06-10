from builder.template import Template
from builder.builder import Builder


template = Template('sass.json')
project = Builder('sass', template)
project.build()


