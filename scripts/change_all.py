import os
import sys


def process_files(directory: str, extension: str, as_is: str, to_be: str):
    for filename in os.listdir(directory):
        if filename.endswith(extension):
            file_path = os.path.join(directory, filename)
            with open(file_path) as file:
                content = file.read()

            updated_content = content.replace(as_is, to_be)

            with open(file_path, "w") as file:
                file.write(updated_content)


def help_message():
    print("Usage:")
    print("  To use this script, follow the syntax below:", end="\n\n")
    print(
        "    python change_all.py <directory_path> <file_extension> <as_is text> <to_be text>",  # noqa
        end="\n\n",
    )
    print("Example:", end="\n\n")
    print("  python change_all.py . .md status.fleeting_note status/fleeting_note")


def error_message():
    RED = "\033[91m"
    BOLD = "\033[1m"
    RESET = "\033[0m"

    print(BOLD + RED + "Too less arguments." + RESET, end="\n\n")


if __name__ == "__main__":
    if len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        help_message()
        sys.exit(0)

    if len(sys.argv) < 5:
        error_message()
        help_message()
        sys.exit(1)

    directory_path = sys.argv[1]
    extension = sys.argv[2]
    as_is = sys.argv[3]
    to_be = sys.argv[4]

    process_files(*sys.argv[1:])
