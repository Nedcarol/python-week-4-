# file_read_write.py

# Step 1: Open input.txt and read content
with open("input.txt", "r") as infile:
    content = infile.read()

# Step 2: Convert content to uppercase
modified = content.upper()

# Step 3: Save to output.txt
with open("output.txt", "w") as outfile:
    outfile.write(modified)

# Step 4: Confirm success
print("✅ File processed and saved as 'output.txt'.")
