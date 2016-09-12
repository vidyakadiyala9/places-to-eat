import sys
import fnmatch
import os
import itertools


def recursive_find_files(base_dir, pattern):
    for dirpath, _, filenames in os.walk(base_dir):
        for filename in filenames:
            if fnmatch.fnmatch(filename, pattern):
                yield os.path.join(dirpath, filename)


IGNORE_FILENAMES = {
    'README.md',
}


def lint_location_document(file_path):
    if os.path.basename(file_path) in IGNORE_FILENAMES:
        return

    with open(file_path) as file_to_lint:
        lines = file_to_lint.readlines()
        if not lines[0].startswith('# '):
            yield (
                "First line of the file must be a top level heading in the "
                "format '# This is the Title'"
            )
        if not any(line.startswith('* Address: ') for line in lines):
            yield (
                "Location not found in document.  There should a line in "
                "the format '* Address: 1234 Main St, Boulder, CO 80302'"
            )
        if not any(line.startswith('* Hours: ') for line in lines):
            yield (
                "Hours of operation not found in document.  There should a line in "
                "the format '* Hours: M-F 9-5'"
            )
        if not any(line.startswith('* Phone: ') for line in lines):
            yield (
                "Phone number not found in document.  There should a line in "
                "the format '* Phone: 555-555-5555'"
            )


def prefix_errors(file_path, errors):
    for error in errors:
        yield "{path}: {error}".format(path=file_path, error=error)


if __name__ == '__main__':
    file_paths = sys.argv[1:]

    if not file_paths:
        raise ValueError(
            "Must provide file paths as arguments to the "
            "`lint_markdown_files.py` script.  Directories will be recursively "
            "traversed for markdown files.  Files will be directly linted"
        )

    errors = []

    for path_to_lint in sys.argv[1:]:
        if not os.path.exists(path_to_lint):
            errors.append(
                "{path}: File Not Found".format(path=path_to_lint)
            )
        elif os.path.isfile(path_to_lint):
            errors.extend(tuple(prefix_errors(path_to_lint, lint_location_document(path_to_lint))))
        elif os.path.isdir(path_to_lint):
            errors.extend(tuple(itertools.chain.from_iterable(
                prefix_errors(_path, lint_location_document(_path))
                for _path
                in recursive_find_files(path_to_lint, "*.md")
            )))

    if errors:
        sys.stderr.write('\n'.join(errors))
        sys.stderr.write('\n\n')
        sys.exit(1)

    print("No errors found.\n")
    sys.exit(0)
