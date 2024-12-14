# Number Randomizer Application

---

### Group 4: Llesis | Galario | Edio | Paculob | Tee | Sambaan | Ajido

---
## **Overview**

<p align="justify">
OOP_RANDOMIZER is a Python-based application designed to randomize and manage integers, offering a flexible yet simple solution to generate randomized outputs. It utilizes core principles of Object-Oriented Programming (OOP), such as encapsulation and inheritance, to organize and manage the application's logic. By restricting access to internal methods and attributes, encapsulation ensures data security and allows modifications without affecting other components of the system. Inheritance is applied to streamline the creation of related components, enabling the reuse and extension of functionality across classes.
</p>

---

The application specializes in randomizing:

- A range of integers (e.g., 1 to 100).
- A list of specific integers (e.g., [3, 7, 15, 42]).

## **The Core Features**

- **Randomization Engine:** Generates unique and customizable outputs based on user-defined inputs.

- **Temporary History Display:** Recent randomization results are displayed in the output section of the GUI, next to the "By List" and "By Range" pages. If you switch modes (e.g., from "By List" to "By Range"), the previous results will be cleared to accommodate the current mode. Results are not saved permanently but can be copied manually.

- **Copy Functionality:** Allows users to copy results for use outside the application.

- **User-Friendly Interface:** Ensures an efficient and smooth user experience.

## **Python Package Structure**

```
OOP_Randomizer/
├── randomizer/
│   ├── __init__.py
│   ├── backend.py
│   ├── history.py
│   ├── gui.py
├── app.py
└── README.md
```

### **Folders**

- **`OOP_RANDOMIZER/`**: This is the root folder that contains the main `app.py` entry file. It's where the overall application is initiated from.

- **`randomizer/`**: The `randomizer` folder is responsible for managing the core components of the application. Each Python file in this folder serves a specific role in handling different parts of the application's logic:

### **Files (.py)**

- **`app.py`**: Main application entry point.
- **`randomizer/__init__.py`**: Empty file that marks the `randomizer` directory as a Python package.
- **`randomizer/backend.py`**: Core logic for data randomization.
- **`randomizer/gui.py`**: GUI implementation.
- **`randomizer/history.py`**: Manages temporary history during the application's runtime.
- **`README.md`**: Contains the documentation.

## **Installation Guide**

### **Prerequisites**
Ensure you have the following installed:
- Python 3.8 or higher.
- pip (Python package manager).

### **Installation Steps**
1. **Clone the repository:**
   ```
   git clone https://github.com/OOP-Group4/NumberRandomizer.git
   cd OOP_Randomizer
    ```
2. **Install the required dependencies:**
   ```
   pip install -r requirements.txt
    ```
3. **Run the application:**
   ```
   python app.py
    ```
## **How to Use?**

### **Launching the Application**
1. Launch the application by executing `app.py` from your terminal or IDE.
2. The graphical user interface (GUI) will appear, allowing you to perform randomization tasks.

### **Randomization**
- **By Range**: Input a minimum and maximum integer to randomize within that range.
- **By List**: Provide a custom list of integers to randomize from.

### **Viewing Temporary History**
- The results from recent randomizations will appear in the output section of the GUI.
- History resets when switching between "By List" and "By Range" modes or when restarting the application.

### **Copying Results**
1. After performing a randomization task, click the **Copy** button in the GUI.
2. The randomization results will be copied to your clipboard, ready for use in other applications.

## **Example of Functionalities**

### *Example 1: Generating Random Numbers (By Range)*

- **Use Case:**
  - A user wants to randomly select several numbers within a specified range. This feature is helpful for many real-life applications like games, education, or decision-making.

- **Steps:**
  1. Open the application and select the **By Range** tab.
  2. In the Minimum field, input the starting value of your range (e.g., 1).
  3. In the Maximum field, input the upper limit of your range (e.g., 100).
  4. Click the **Generate** button repeatedly until you get the number of random numbers you need.

---

### *Example 2: Deciding the Order of Groups Using Shuffle*

- **Use Case:**
  - A teacher can use the shuffle functionality to randomly decide the order in which student groups will present in class. Instead of choosing a fixed order or randomly picking groups one by one, the teacher can shuffle the list of groups to ensure a fair and random selection.

- **Steps:**
  1. Open the application and select the **By List** tab.
  2. Input the names of the student groups or teams in the classroom. For example:  
     `[1, 2, 3, 4, 5]`
  3. Click the **Shuffle** button to randomize the order of the groups.

- **Expected Result:**
  - The application randomly shuffles the list of groups and presents a new order each time the button is pressed. Example result after shuffling:  
    `[4, 2, 1, 5, 3]`
  - The teacher can then use the shuffled list to assign the presentation order: Group 4 presents first, Group 2 second, and so on.

