import os

def verify_file_operations():
    filename = "input.txt"  # Your working file
    
    try:
        # 1. Check if file exists
        if not os.path.exists(filename):
            raise FileNotFoundError(f"'{filename}' doesn't exist")
        
        # 2. Read and display content
        with open(filename, 'r') as f:
            content = f.read()
            print(f"✅ CURRENT CONTENT IN '{filename}':")
            print("-" * 40)
            print(content.strip())
            print("-" * 40)
            
        # 3. Get file stats
        file_size = os.path.getsize(filename)
        print(f"📊 File Size: {file_size} bytes")
        print(f"📅 Last Modified: {os.path.getmtime(filename)}")
        
    except Exception as e:
        print(f"❌ Verification Failed: {e}")

if __name__ == "__main__":
    verify_file_operations()