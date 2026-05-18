from datetime import datetime

def line_breakdown(line): # Parses the error/warning line and break it down into a list

    try:
        processed_line = line.split("-", 1)
        processed_line[1] = processed_line[1].lstrip()
        processed_line[1] = processed_line[1].rstrip()
        date_time_status_line = processed_line[0].split()

        date_and_time_str = date_time_status_line[0] + " " + date_time_status_line[1]
        date_and_time = datetime.strptime(date_and_time_str, "%m/%d/%Y %H:%M:%S")
        status = date_time_status_line[2]
        message = str(processed_line[1]).strip('\n')

        line_list = [date_and_time, status, message]

        return line_list
    
    except (IndexError, ValueError):
        return None