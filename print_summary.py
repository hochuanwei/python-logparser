def print_summary(linenum, totalerrornum, totalwarningnum): # Prints a summary of total errors and warnings detected
    print(f"\n------------\nSummary\n------------\n")
    print(f"Total line parsed: {linenum}")
    print(f"Total errors: {totalerrornum}")
    print(f"Total warnings: {totalwarningnum}")

def print_errors(errorline, errorlinenum): # Prints out the errors detected
    print("\n------------\nErrors\n------------\n")
    for line, num in zip(errorline, errorlinenum):
        print(f"Error message: {line}\nLine number: {num}\n")

def print_warnings(warningline, warninglinenum): # Prints out the warnings detected
    print("\n------------\nWarnings\n------------\n")
    for line, num in zip(warningline, warninglinenum):
        print(f"Warning message: {line}\nLine number: {num}\n")