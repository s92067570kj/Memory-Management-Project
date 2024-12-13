# main.py

from memory_manager import FirstFitMemoryManager

def main():
    memory_sizes = [100, 500, 200, 300, 600]
    manager = FirstFitMemoryManager(memory_sizes)

    while True:
        print("\nMemory Management Menu:")
        print("1. Allocate Memory")
        print("2. Deallocate Memory")
        print("3. Display Memory Status")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            try:
                process_id = int(input("Enter Process ID: "))
                process_size = int(input("Enter Memory Size to Allocate: "))
                
                if process_size > 0:
                    manager.allocate(process_id, process_size)
                else:
                    print("Memory size must be a positive integer.")
                    
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == "2":
            try:
                process_id = int(input("Enter Process ID to Deallocate: "))
                manager.deallocate(process_id)
                
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

        elif choice == "3":
            manager.display()

        elif choice == "4":
            print("Exiting the Memory Management Program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
