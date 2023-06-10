
from builder import Builder, Template
from cli import arguments

def main():
    args = arguments()

    template = Template(args.template)
    project = Builder(args.project, template)

    project.build()


if __name__ == "__main__":
    main()
