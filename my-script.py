def prompt_for_input(expected_message):
    # Prompt the user for input
    user_input = input("Enter the input message to continue: ")
    
    # Check if the user input matches the expected message
    if user_input == "cyberknights":
        print("Input matched. Continuing the pipeline...")
        return True
    else:
        print("Input did not match. Stopping the pipeline.")
        return False

# Main pipeline execution
def main():
    expected_message = "continue"  # Define the expected message to match
    if prompt_for_input(expected_message):
        # Continue with the rest of the pipeline
        print("Executing the next step of the pipeline...")
        # Add your pipeline code here
    else:
        # Handle the case where the input doesn't match
        print("Pipeline halted.")

if __name__ == "__main__":
    main()

