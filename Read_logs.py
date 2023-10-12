import re

def read_log_file(log_file_path):
  """Reads a log file and returns a list of lines."""
  with open(log_file_path, "r") as f:
    log_lines = f.readlines()
  return log_lines

def read_specific_text_from_log_file(log_file_path, specific_text):
  """Reads specific text from a log file and returns a list of lines that contain the specific text."""
  log_lines = read_log_file(log_file_path)
  specific_text_lines = []
  for line in log_lines:
    if specific_text in line:
      specific_text_lines.append(line)
  return specific_text_lines

def extract_whole_line_from_log_file(log_file_path, specific_text):
  """Extracts the whole line from a log file that contains the specific text."""
  specific_text_lines = read_specific_text_from_log_file(log_file_path, specific_text)
  if specific_text_lines:
    return specific_text_lines[0]
  else:
    return None

def summarize_log_file(log_file_path, specific_text):
  """Summarizes a log file based on the specific text."""
  whole_line = extract_whole_line_from_log_file(log_file_path, specific_text)
  if whole_line:
    summary = f"The specific text '{specific_text}' was found in the log file '{log_file_path}' on the following line:\n{whole_line}"
  else:
    summary = f"The specific text '{specific_text}' was not found in the log file '{log_file_path}'."
  return summary


# Example usage:

log_file_path = "C:/Users/nl020568/Documents/GitHub/gitHubTest/Assets/log.txt"
specific_text = "ERROR"

# Read the log file
log_lines = read_log_file(log_file_path)

# Read the specific text from the log file
specific_text_lines = read_specific_text_from_log_file(log_file_path, specific_text)

# Extract the whole line from the log file that contains the specific text
whole_line = extract_whole_line_from_log_file(log_file_path, specific_text)

# Summarize the log file based on the specific text
summary = summarize_log_file(log_file_path, specific_text)

# Print the summary
print(summary)
