from diagnostic_tool import DiagnosticTool


def main():
    diagnostic_tool = DiagnosticTool()
    while True:
        try:
            print("\nVehicle Diagnostic Tool")
            print("1. Run Diagnostics")
            print("2. Exit")
            choice = input("Enter your choice (1/2): ")

            if choice == '1':
                diagnostic_tool.run()
            elif choice == '2':
                print("Exiting the program. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting...")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            print("Please try again.")


if __name__ == "__main__":
    main()
