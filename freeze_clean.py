import re

def clean_requirements(file_in, file_out):
    with open(file_in, "r") as f:
        lines = f.readlines()
    
    clean_lines = []
    for line in lines:
        # Remove local paths and use version specifiers
        if "@ file://" in line:
            package = re.match(r"([\w\-]+)", line).group(1)
            clean_lines.append(f"{package}\n")
        else:
            clean_lines.append(line)

    with open(file_out, "w") as f:
        f.writelines(clean_lines)

clean_requirements("requirements.txt", "requirements_clean.txt")
