import datetime
import os
import pathlib
import re
import sys

from jinja2 import Environment, PackageLoader


def is_valid_project_name(project_name):
    if not project_name:
        print("You didn't provide the name of the project.\n")
        return False

    if len(project_name) > 40:
        print("The project name has to be less than or equal to 40 characters long.\n")
        return False

    is_valid = re.match(r"^(?:(?:[a-z]|[A-Z]|[0-9]|_*))+$", project_name)

    if not is_valid:
        print("The project name can only contain letters, numbers, and underscores.\n")
        return False

    return True


def is_valid_project_author(project_author):
    if not project_author:
        print("You didn't specify the author of the project.\n")
        return False

    return True


def create_directory(output_path, name):
    target_path = pathlib.Path(output_path, name)
    absolute_path = str(target_path.resolve())

    try:
        os.mkdir(target_path)
        print(f"Created {absolute_path} succesfully.")
    except OSError:
        sys.exit(f"Creation of directory {absolute_path} failed. Exiting.\n")

    return absolute_path


def write_file_from_template(template, output_path, template_variables):
    try:
        with open(output_path, "w") as file:
            file.write(template.render(template_variables))
        print(f"Created {output_path} successfully.")
    except:
        sys.exit(f"Creation of {output_path} failed. Exiting.\n")


def main():
    for _ in range(3):
        project_name = input("What is the name of your project?\n")

        if is_valid_project_name(project_name):
            break
    else:
        sys.exit("I give up... Exiting.")

    print()

    for _ in range(3):
        project_author = input("Who is the author of the project?\n")

        if is_valid_project_author(project_author):
            break
    else:
        print()
        sys.exit("I give up... Exiting.\n")

    print()

    print("## PROJECT DETAILS ##")
    print(f"Project name: {project_name}")
    print(f"Author:       {project_author}")

    print()

    root_directory = create_directory("..", project_name)
    source_directory = create_directory(root_directory, project_name)

    print()

    env = Environment(loader=PackageLoader("auto_project_builder", "templates"))

    templates = [
        env.get_template("README.md.template"),
        env.get_template("LICENSE.template"),
        env.get_template(".gitignore.template"),
        env.get_template("main.py.template"),
    ]

    output_paths = [
        pathlib.Path(root_directory, "README.md"),
        pathlib.Path(root_directory, "LICENSE"),
        pathlib.Path(root_directory, ".gitignore"),
        pathlib.Path(source_directory, "main.py"),
    ]

    templates_variables = [
        {"project_name": project_name},
        {"year": datetime.datetime.now().year, project_author: project_author},
        {},
        {},
    ]

    for template, output_path, template_variables in zip(
        templates, output_paths, templates_variables
    ):
        write_file_from_template(template, output_path, template_variables)


main()
