import os  # Add at top

def main():
    print("=== FILE HANDLER ===")
    
    # Get filename (unchanged)
    filename = input("Enter filename (e.g., test.txt): ").strip()
    
    try:
        # === NEW: STEP 2 VALIDATION (MINIMAL VERSION) ===
        if not os.path.exists(filename):
            raise FileNotFoundError(f"'{filename}' doesn't exist")
        if not os.access(filename, os.R_OK):
            raise PermissionError(f"Can't read '{filename}'")
        # === END OF STEP 2 ADDITIONS ===
        
        # YOUR EXISTING CODE (keep all read/write/append logic)
        with open(filename, 'r') as f:
            print("\n📄 CONTENTS:")
            print(f.read())
            
        # ... [rest of your operations] ...
        
    except FileNotFoundError as e:
        print(f"\n❌ File Error: {e}")
    except PermissionError as e:
        print(f"\n❌ Access Error: {e}")
    except Exception as e:
        print(f"\n❌ Unexpected Error: {e}")
    finally:
        print("\nDone.")

if __name__ == "__main__":
    main()