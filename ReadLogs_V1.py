import tkinter as tk
import re

def read_log_file(log_file_path):
  """Reads a log file and returns a list of lines."""
  with open(log_file_path, "r") as f:
    log_lines = f.readlines()
  return log_lines

def read_all_instances_of_word_from_log_file(log_file_path, word):
  """Reads all instances of a word from a log file and returns a list of lines that contain the word."""
  log_lines = read_log_file(log_file_path)
  all_instances_of_word_lines = []
  for line in log_lines:
    if re.search(word, line):
      all_instances_of_word_lines.append(line)
  return all_instances_of_word_lines

def show_all_instances_in_pop_up_window(all_instances_of_word_lines):
  """Shows all instances of a word in a new pop-up window."""
  root = tk.Tk()
  root.title("Log File Instances")
  text_box = tk.Text(root, width=250, height=300)
  for line in all_instances_of_word_lines:
    text_box.insert(tk.END, line + "\n")
  text_box.pack()
  root.mainloop()

# Example usage:

log_file_path = "C:/Users/nl020568/Documents/GitHub/gitHubTest/Assets/log.txt"
word = "ERROR"

# Read all instances of the word from the log file
all_instances_of_word_lines = read_all_instances_of_word_from_log_file(log_file_path, word)

# Show all instances of the word in a new pop-up window
show_all_instances_in_pop_up_window(all_instances_of_word_lines)