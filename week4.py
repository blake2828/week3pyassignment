def read_and_modify_file(input_filename, output_filename):
    """
    Reads content from input_filename,
    converts it to uppercase,
    and writes it into output_filename.
    """
    try:
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify content (example: uppercase transformation)
        modified_content = content.upper()

        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"✅ File processed successfully! Modified content saved in '{output_filename}'")

    except FileNotFoundError:
        print(f"❌ Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"❌ Error: Permission denied for file '{input_filename}'.")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


# --- Main Program ---
input_file = input("Enter the name of the file to read: ")
output_file = "modified_" + input_file  # Save new file with 'modified_' prefix

read_and_modify_file(input_file, output_file)
