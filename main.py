import sys

def main():
    """
    Prints command-line arguments to the screen.
    """
    args = sys.argv[1:]  # Get arguments excluding the script name
    if args:
        with open("output.txt", "a") as file:
            file.write("Command-line arguments:")
            for arg in args:
                file.write(f"  {arg}")
            file.write("\n")
            file.close()
    else:
        print("No command-line arguments provided.")

if __name__ == "__main__":
    main()
    
# pyinstaller --onefile .\main.py