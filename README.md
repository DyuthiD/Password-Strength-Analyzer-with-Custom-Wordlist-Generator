
## 🔐 Password Strength Analyzer with Custom Wordlist Generator

### 📌 Overview

This project is a **Python-based tool** that analyzes the strength of user-provided passwords and generates **custom wordlists** based on user-specific inputs.
It helps users understand how predictable passwords can be guessed by attackers and encourages the use of stronger passwords.

---

### ✨ Features

* **Password Strength Analyzer** using `zxcvbn`

  * Provides strength score (0–4)
  * Displays estimated crack time
  * Suggests improvements for weak passwords
* **Custom Wordlist Generator**

  * Generates wordlists using personal inputs (name, date of birth, pet name, etc.)
  * Uses patterns like reversing words, adding numbers, and basic leetspeak
  * Saves the list as `wordlist.txt`
---

### 🛠 Tools & Technologies

* **Python 3.x**
* **Libraries:**

  * `zxcvbn` – Password strength evaluation
  * `NLTK` – For text processing (future expansion)
* **VS Code** – For coding and debugging

---

### 🚀 How to Run

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/password-analyzer.git
   cd password-analyzer
   ```

2. **Install required libraries**

   ```bash
   pip install zxcvbn
   ```

3. **Run the program**

   ```bash
   python main.py
   ```
---

### 🖼 Sample Output

```
==============================
🔐 Password Tool
==============================
1. Analyze Password Strength
2. Generate Custom Wordlist
3. Exit
Enter your choice (1/2/3): 1
```

---

### 📌 Future Improvements

* Add **GUI (Tkinter)**
* Generate **larger wordlists** with advanced patterns
* Integrate with penetration testing tools

---

### 👤 Author

**Dyuthi D**
Internship at **Elevate Labs**

---
