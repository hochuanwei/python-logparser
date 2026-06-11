from log_analyzer.parser import _line_breakdown as line_breakdown
from datetime import datetime

def test_valid_error_line(): # Feeds a valid error line to the function. Expects a list output with a date, ERROR, and the error message 
    line = "03/31/2025 13:45:54 ERROR - This is an error"
    results = line_breakdown(line)
    assert results[2] == "This is an error"
    assert results[1] == "ERROR"
    assert results[0] == datetime(2025,3,31,13,45,54)

def test_not_valid_line(): # Feeds a non-valid error line into the function. Expects a None output.
    line = "This is not a valid line."
    results = line_breakdown(line)
    assert results is None

def test_all_space_line(): # Feeds an all space line into the function. Expects a None output.
    line = "               "
    results = line_breakdown(line)
    assert results is None

def test_multiple_hyphens(): # Feeds a valid error line with multiple hyphen into the function. Expect the second hyphen to not affect the valid output.
    line = "03/31/2025 13:45:54 ERROR - This is an error - This is an error"
    results = line_breakdown(line)
    assert results[2] == "This is an error - This is an error"
    assert results[1] == "ERROR"
    assert results[0] == datetime(2025,3,31,13,45,54)

def test_partial_valid_line(): # Feeds a partially valid error line. Expects a None output.
    line = "03/31/2025 13:45:54 - This is an error"
    results = line_breakdown(line)
    assert results is None

def test_valid_warning_line(): # Feed a valid warning line. Expects a list output with date, WARNING, and the warning message.
    line = "03/31/2025 13:45:54 WARNING - Disk space not enough."
    results = line_breakdown(line)
    assert results[1] == "WARNING"
    assert results[2] == "Disk space not enough."

def test_whitespace_removal_message(): # Feeds a valid error/warning line with extra whitespaces in the message. Expects the whitespace to be removed properly from the output data. 
    line = "03/31/2025 13:45:54 WARNING -        Extra spaces around message.              "
    results = line_breakdown(line)
    assert results[2] == "Extra spaces around message."
