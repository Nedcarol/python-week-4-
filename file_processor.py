# Always create or overwrite 'input.txt' with sample content
with open("input.txt", "w") as f:
    f.write("Hello world!\n")
    f.write("Python is amazing.\n")
    f.write("This is a file processing task.\n")
    f.write("We are counting words.\n")
    f.write("All text will be uppercase.\n")

# Step 1: Read the contents of the file
with open("input.txt", "r") as file:
    content = file.read()

# Step 2: Count the number of words
word_count = len(content.split())

# Step 3: Convert text to uppercase
upper_text = content.upper()

# Step 4: Write processed text and word count to output.txt
with open("output.txt", "w") as output:
    output.write("PROCESSED TEXT:\n")
    output.write(upper_text + "\n")
    output.write(f"\nWORD COUNT: {word_count}\n")

# Step 5: Print success message
print("✅ Output file 'output.txt' created successfully!")
