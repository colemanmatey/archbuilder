import argparse

from builder import Builder, Template


def cli_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("project_name", type=str)
    parser.add_argument("template_name", type=str)

    return parser.parse_args()


def main():
    args = cli_parser()

    template = Template(args.template)
    project = Builder(args.project, template)

    project.build()


if __name__ == "__main__":
    main()
