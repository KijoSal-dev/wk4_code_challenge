def process_text_file(input_filename="input.txt", output_filename="output.txt"):
    """
    Reads a text file, counts words, converts text to uppercase,
    and writes the processed text and word count to a new file.

    Args:
        input_filename (str): The name of the input text file.
        output_filename (str): The name of the output text file.
    """

    try:
        # Read the contents of the input file
        with open(input_filename, "r") as infile:
            text = infile.read()

        # Count the number of words
        words = text.split()
        word_count = len(words)

        # Convert text to uppercase
        uppercase_text = text.upper()

        # Write the processed text and word count to the output file
        with open(output_filename, "w") as outfile:
            outfile.write(uppercase_text + "\n")
            outfile.write(f"Word Count: {word_count}\n")

        print(f"Successfully created {output_filename} with processed text and word count.")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    # Create input.txt if it doesn't exist and write some lines to it
    try:
        with open("input.txt", "w") as f:
            f.write("This is a text file.\n")
            f.write("It contains facts bout python.\n")
            f.write("Python is fun and exciting!\n")
            f.write("Python is an interpreted, high-level programming language used in rapid application development.\n")
            f.write("Python is a popular and one of the most used programming languages.\n")
    except Exception as e:
        print(f"Error creating input.txt: {e}")
    else:
        process_text_file()  # Process the file