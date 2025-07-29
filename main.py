# Password Strength Analyzer with Custom Wordlist Generator
# Author: [Your Name]
# Date: [Today's Date]

from zxcvbn import zxcvbn
import re

# -------------------------------
# Password Strength Analyzer
# -------------------------------
def analyze_password():
    print("\n🔒 Password Strength Analyzer")
    password = input("Enter your password to analyze: ")

    # Analyze password strength
    result = zxcvbn(password)
    score = result['score']
    crack_time = result['crack_times_display']['offline_fast_hashing_1e10_per_second']
    suggestions = result['feedback']['suggestions']

    print("\n--- Password Strength Report ---")
    print(f"Strength Score (0-4): {score}")
    print(f"Estimated Crack Time: {crack_time}")

    if suggestions:
        print("\nSuggestions to improve your password:")
        for s in suggestions:
            print(f"- {s}")
    else:
        print("\n✅ Your password is strong!")

# -------------------------------
# Custom Wordlist Generator
# -------------------------------
def generate_wordlist():
    print("\n📝 Custom Wordlist Generator")
    name = input("Enter your name: ")
    dob = input("Enter your year of birth (YYYY): ")
    pet = input("Enter your pet's name: ")

    # Generate wordlist patterns
    patterns = set()  # Use set to avoid duplicates
    base_words = [name, pet, dob]
    for word in base_words:
        word = word.strip()
        if not word:
            continue
        patterns.add(word)
        patterns.add(word[::-1])  # Reverse
        patterns.add(word + "123")
        patterns.add(word + dob)
        patterns.add(re.sub(r"[aA]", "@", word))  # Simple leetspeak
        patterns.add(re.sub(r"[sS]", "$", word))  # Simple leetspeak
        patterns.add(word.capitalize())
        patterns.add(word.lower())

    # Save to wordlist.txt
    filename = "wordlist.txt"
    with open(filename, "w") as file:
        for entry in sorted(patterns):
            file.write(entry + "\n")

    print(f"\n Wordlist generated successfully as '{filename}'.")

# -------------------------------
# Main Menu
# -------------------------------
def main():
    while True:
        print("\n==============================")
        print("🔐 Password Tool")
        print("==============================")
        print("1. Analyze Password Strength")
        print("2. Generate Custom Wordlist")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            analyze_password()
        elif choice == "2":
            generate_wordlist()
        elif choice == "3":
            print("\n👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")

# -------------------------------
# Run the program
# -------------------------------
if __name__ == "__main__":
    main()
