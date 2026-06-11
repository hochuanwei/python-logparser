LOG ANALYZER

PROBLEM STATEMENT: 
- Engineers often spend a significant amount of time manually review large log files to identify failures. This project automates log analysis by detecting error and warning patterns, generating summary reports, accelerating the debugging process.

FEATURES:
- Parse and analyze log files for error and warning patterns.
- Display summary reports of detected errors and warnings.
- Include unit tests covering core parsing and analysis logic.

INSTALLATION:
```bash
git clone https://github.com/hochuanwei/python-logparser.git
cd python-logparser
pip install -r requirements.txt
```

USAGE:
``` bash
py main.py -f sample.log
```

sample.log:
05/01/2026 00:00:01 EVENT - Running file test_contents.add
05/01/2026 00:13:23 WARNING - File template_output.txt already exists. Overwriting file with new output.
05/01/2026 00:30:45 ERROR - Input data not sufficient to create output. Terminating test.
05/01/2026 00:30:51 ERROR - Return value is 1. Test terminated. Awaiting review.

Expected output:
Running log parser.

------------
Summary
------------

Total line parsed: 4
Total errors: 2
Total warnings: 1

------------
Errors
------------
Error message: Input data not sufficient to create output. Terminating test.
Line number: 3

Error message: Return value is 1. Test terminated. Awaiting review.
Line number: 4

------------
Warnings
------------

Warning message: File template_output.txt already exists. Overwritting file with new output.
Line number: 2

TESTS:
To run, use the commands:
pip install pytest
py -m pytest tests/

TEST COVERAGE:
Unit tests validate the core parsing and analysis functionality of the application:
- Error detection
- Warning detection
- False positive detection
- Partial log line formatting detection
- Whitespace removal in log lines
- Consecutive errors detection
- Multiple consecutive errors detection

ROADMAP:
- Insert detected errors and warnings into a relational MySQL database
- Export analysis results into CSV format
- Web dashboard
