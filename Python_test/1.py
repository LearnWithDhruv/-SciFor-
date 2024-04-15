with open("sample_file.txt", "w") as file:
    file.write("Hello, My name is Dhruv Khatter!\n")
    file.write("this is a sample text!\n")
    file.write("and I am using this file for my python test!\n")
    file.write("Count on to see no of lines, words and letters it has!\n")

def check_file(file_name, start_letter):
    total_lines = 0
    total_words = 0
    total_letters = 0
    lines_with_start_letter = 0

    with open(file_name, "r") as file:
        for line in file:
            total_lines += 1
            total_words += len(line.split())
            total_letters += len(line.strip())
            if line.strip().lower().startswith(start_letter.lower()):
                lines_with_start_letter += 1

    return total_lines, total_words, total_letters, lines_with_start_letter

file_name = "sample_file.txt"
start_letter = "T"
total_lines, total_words, total_letters, lines_with_start_letter = check_file(file_name, start_letter)


print(f"Total number of lines: {total_lines}")
print(f"Total number of words: {total_lines}")
print(f"Total number of letters: {total_lines}")
print(f"Total number of lines starting with: '{start_letter}' : {lines_with_start_letter}")