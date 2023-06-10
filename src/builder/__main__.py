import sys

from builder import Builder, Template


def main():
    template = Template(sys.argv[2])
    project = Builder(sys.argv[1], template)
    project.build()


if __name__ == "__main__":
    main()
