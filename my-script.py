import sys

# Define your predefined values
PREDEFINED_VALUES = ['value1']

def main():

    if message not in PREDEFINED_VALUES:
        print(f"Error: '{message}' is not a valid value. Expected one of {PREDEFINED_VALUES}.")
        sys.exit(1)  # Exit with code 1 to indicate failure
    else:
        print(f"Received valid message: {message}")
        sys.exit(0)  # Exit with code 0 to indicate success

if __name__ == "__main__":
    main()
