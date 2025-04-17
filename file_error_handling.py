import os

def main():
    print("=== FILE HANDLING WITH ERROR HANDLING ===")
    
    # Ask user for filename
    filename = input("Enter filename (e.g., test.txt): ").strip()
    
    try:
        # CREATE/WRITE TO FILE
        with open(filename, 'w') as f:
            f.write("Line 1: Hello World\n")
            f.write("Line 2: 12345\n")
        print(f"\n✅ Successfully created '{filename}'")
        
        # READ FILE
        with open(filename, 'r') as f:
            print("\n📄 FILE CONTENTS:")
            print(f.read())
        
        # APPEND TO FILE
        with open(filename, 'a') as f:
            f.write("Line 3: Appended text\n")
        print(f"\n✅ Successfully appended to '{filename}'")
        
        # READ AGAIN
        with open(filename, 'r') as f:
            print("\n📄 UPDATED CONTENTS:")
            print(f.read())
            
    except FileNotFoundError:
        print(f"\n❌ Error: Folder does not exist")
    except PermissionError:
        print(f"\n❌ Error: Permission denied for '{filename}'")
    except Exception as e:
        print(f"\n❌ Unexpected error: {type(e).__name__} - {e}")
    finally:
        print("\nProgram finished.")

if __name__ == "__main__":
    main()