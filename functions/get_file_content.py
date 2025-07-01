import os


def get_file_content(working_directory, file_path):
    wd = os.path.abspath(working_directory)
    filepath = os.path.abspath(os.path.join(wd, file_path))
    if not filepath.startswith(wd):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(filepath):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        MAX_CHARS = 10000

        with open(filepath, "r") as f:
            file_content_string = f.read(MAX_CHARS + 1)
            if len(file_content_string) > MAX_CHARS:
                file_content_string = file_content_string[:MAX_CHARS] + f'\n[...File "{file_path}" truncated at 10000 characters]'
            return file_content_string
    except Exception as e:
        return f"Error reading file: {e}"
