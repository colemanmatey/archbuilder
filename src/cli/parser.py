import argparse

def arguments():
    parser = argparse.ArgumentParser(
        prog="archbuilder",
        description="Use '%(prog)s' to quickly build project structures from JSON templates"
    )
    parser.add_argument("project", type=str)
    parser.add_argument("template", type=str)

    return parser.parse_args()