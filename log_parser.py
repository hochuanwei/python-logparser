def log_parser(filename):
    import line_breakdown

    num = 0 # Line number counter as we continue to read the file
    errorline = [] # List of stored errors detected
    errorlinenum = [] # List of line number where errors are located
    errorlinedatetime = [] # List of the date and time the error are reported at
    warningline = [] # List of stored warnings
    warninglinenum = [] # List of line numbers where warnings are located

    try:
        with open(filename, "r") as f:
            for line in f:
                num += 1
                data_line = line_breakdown.line_breakdown(line)

                if data_line == None:
                    continue # Skip lines that doesn't follow the log format

                if str(data_line[1]).lower() == "error": # Stores the error date and time, message, and line number
                    errorlinedatetime.append(data_line[0])
                    errorline.append(data_line[2])
                    errorlinenum.append(num)
                elif str(data_line[1]).lower() == "warning": # Stores the warning message, and line number
                    warningline.append(data_line[2])
                    warninglinenum.append(num)
                else:
                    continue

    except FileNotFoundError:
        print(f"File {filename} not found. Please check the file destination.")
        return

    return {
        "total_lines": num,
        "error_lines": errorline,
        "error_linenums": errorlinenum,
        "error_datetime": errorlinedatetime,
        "warning_lines": warningline,
        "warning_linenums": warninglinenum
    }


if __name__ == "__main__":
    import argparse
    print("Runing log parser.")

    parser = argparse.ArgumentParser(
        description="Provide the file name to be parsed"
    )

    parser.add_argument(
        "-f", "--file", metavar="filename",
        required=True, help="the logfile to parse"
    )

    args = parser.parse_args()
    log_parser(args.file)