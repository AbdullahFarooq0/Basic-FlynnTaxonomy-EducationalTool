# Entry point for the project
from sisd import visualize_sisd
from simd import visualize_simd
from misd import visualize_misd
from mimd import visualize_mimd
from ui import launch_gui

def main():
    print("Flynn's Taxonomy Visualization")
    print("1. SISD")
    print("2. SIMD")
    print("3. MISD")
    print("4. MIMD")
    choice = input("Select an option (1-4): ")

    if choice == '1':
        visualize_sisd(3, 5)
    elif choice == '2':
        visualize_simd([1, 2, 3, 4])
    elif choice == '3':
        visualize_misd(5)
    elif choice == '4':
        visualize_mimd([5, 2, 9], [1, 2, 3])
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
