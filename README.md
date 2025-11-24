# Library-Management

- A Python command-line application to manage a books collection with CSV persistence and pandas-backed display.<br>

> - Provides workflows to add books, check them out to borrowers, check them back in, and view available or borrowed titles.

> - Data is stored in CSV files (library.csv and checked-out.csv) so it persists between runs.

> - Uses pandas for tabular display, making the output clear and beginner-friendly.

### Features:

> - CSV persistence: books are saved in library.csv and checked-out.csv, ensuring data is not lost when the program exits.

> - File generation: automatically creates CSV files with headers if they don’t exist.

> - Validation: ISBN existence checks, duplicate prevention across files, and careful character validation for titles/authors.

> - Display: prints a pandas DataFrame with a 1-based index and a pause so users can read before continuing.

> - CLI menu: text-driven interface with options to add, check out, check in, view, delete, and exit.

### Purpose:

> - Teach and demonstrate Python CLI design with persistent storage.

> - Show how to integrate pandas for data handling and display.

> - Reinforce best practices in input validation and defensive programming.

> - Working intensively with the operating system.
---

### Improvements over the old version:

> - Data persistence with CSV files (instead of in-memory dictionaries).

> - More defensive checks and validation.

> - Clearer comments and docstrings for beginners.

> - Tabular display with pandas for readability.

> - Building functions in an extensive and organized manner.

> - In-depth interaction with the operating system.















