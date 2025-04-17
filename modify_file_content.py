def modify_file_content(input_filename, output_filename):
    try:
        # 1. READ FILE
        with open(input_filename, 'r') as input_file:
            original_content = input_file.read()
        
        # 2. MODIFY CONTENT (Convert to uppercase + add line numbers)
        modified_lines = []
        for i, line in enumerate(original_content.splitlines(), 1):
            modified_lines.append(f"{i}: {line.upper()}")
        modified_content = "\n".join(modified_lines)
        
        # 3. WRITE TO NEW FILE
        with open(output_filename, 'w') as output_file:
            output_file.write(modified_content)
        
        print(f"✓ Success! Modified version saved to '{output_filename}'")
        return True
    
    except Exception as e:
        print(f"✗ Error during file processing: {type(e).__name__} - {str(e)}")
        return False