def errors(file, arg_num, ext=""):
    limit = arg_num + 1
    # command-line error checker
    if len(file) > limit:
        return "Too many command-line arguments"
    elif len(file) < limit:
        return "Too few command-line arguments"

    try:
        # read file by line
        file_name = open(file[1])
    except FileNotFoundError:
        return f"Could not read {file[1]}"
    else:
        text = file[1].split(".")
        if text[-1] != ext.lower():
            return f"Not a {ext.upper()} file"