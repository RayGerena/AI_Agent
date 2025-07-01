import os


def write_file(working_directory, file_path, content):
    wd = os.path.abspath(working_directory)
    filepath = os.path.abspath(os.path.join(wd, file_path))
    if not filepath.startswith(wd):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    try:
        with open(filepath, "w") as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error writing to file: {e}"
