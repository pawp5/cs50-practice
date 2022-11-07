def errors(file, arg_num, ext=None):
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
        input, ext1 = file[1].split(".")
        output, ext2 = file[2].split(".")
        if ext1.lower() not in ext:
            return "Invalid input"
        if ext1 != ext2:
            return "Input and output have different extensions"