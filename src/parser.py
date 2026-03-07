def parse_input(lines):
    # Get rid of all whitespace and ignore empty lines (PA1 code)
    stripped_lines = []
    for line in lines:
        line = line.strip()
        if line != "":
            stripped_lines.append(line)

    # Make k and m into variables
    first_line = stripped_lines[0]
    k_val, m_val = first_line.split()

    # Make cache requests into int variables
    if len(stripped_lines) < 2:
        requests = None
    else:
        requests = stripped_lines[1].split()        
        for i in range(len(requests)):
            requests[i] = int(requests[i])

    return int(k_val), int(m_val), requests
    