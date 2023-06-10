import argparse

from builder import Builder, Template


def cli_parser():
    parser = argparse.ArgumentParser(
        prog="archbuilder",
        description="Use '%(prog)s' to quickly build project structures from JSON templates"
    )
    parser.add_argument("project", type=str)
    parser.add_argument("template", type=str)

    return parser.parse_args()


def main():
    args = cli_parser()

    template = Template(args.template)
    project = Builder(args.project, template)

    project.build()


if __name__ == "__main__":
    main()
