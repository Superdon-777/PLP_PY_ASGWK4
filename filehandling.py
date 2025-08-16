# filehandling.py

def read_and_write():
    try:
        with open('input.txt', 'r') as sourcefile:
            content = sourcefile.read()
    # Modification: convert source content to upper case
        modified = content.upper()
        with open('destination.txt', 'w') as destinationfile:
            destinationfile.write(modified)
        print("Capitalized content written to destination.txt")
    except FileNotFoundError:
        print("input.txt does not exist.")
    except Exception as e:
        print("An error occurred:", e)

def ask_filename_and_read():
    filename = input("Enter a filename to read: ")
    try:
        with open(filename, 'r') as f:
            print(f.read())
    except FileNotFoundError:
        print(f"File '{filename}' not found!")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    read_and_write()
    ask_filename_and_read()
