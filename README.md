#  **DogHTTP Explorer**  

**DogHTTP Explorer** is a Django web application that allows users to explore HTTP response codes using fun dog images. Users can filter response codes, save custom lists with associated images, and manage these lists (view, edit, delete).



##   **Features**
-   **User Authentication**:
      - Secure **Signup**, **Login**, and **Logout**.
      - Protect application views from unauthenticated access.
-   **Search Functionality**:
      - Filter response codes like `2xx`, `3xx`, or patterns like `20x`.
      - Display matching dog images and save lists for future reference.
-   **List Management**:
      - View, edit, and delete saved lists with response codes and dog images.
-   **Interactive UI**:
      - Responsive design with navigation and dynamic features.

---

##  **Installation and Setup**

###  **1. Prerequisites**
Ensure you have the following installed:
- Python 3.10+
- Django 5.1+
- pip (Python package manager)

###  **2. Installation Steps**
1. Clone the repository:
   ```bash
   git clone <your-repository-link>
   cd DogHTTP-Explorer

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate (for macOS/Linux)
   venv\scripts\activate ( for windows)

3. Install dependencies
   ```bash
   pip install -r requirements.txt

4. Set up the database
   ```base
   python manage.py makemigrations
   python manage.py migrate

5. Create an admin user for django admin panel
   ```bash
   python manage.py create superuser

6. Run the development server
   ```bash
   python manage.py runserver

7. Visit the app at: http://127.0.0.1:8000/

---

## Runtime Complexities
- Authentication:
    - User login/signup operations → O(1) for database lookups.
- Search Functionality:
    - Filter response codes → O(n) where n is the number of response codes in the database.
- List Management:
    - Viewing lists → O(n) for user-specific list retrieval.
    - Editing/Deleting lists → O(1) for updates or deletions by primary key.
 
 ## How to Use
  - User Authentication
      - Navigate to the Signup page from the navigation bar to create a new account.
      - Once registered, log in using the Login page.
      - After logging in, you can access all the features.
  - Search for HTTP Response Codes
      - Go to the Search page.
      - Use filters like:
        - 2xx to display all success-related codes.
        - 20x to display all codes starting with 20.
        - A specific code like 404 to view a single response code.
        - The matching dog images will appear for your filter.
  - Save Filtered Lists
      - After searching, click Save List to store the results.
      - Provide a name for your list.
      - Your list will include the response codes, dog images, and a timestamp.
  - Manage Saved Lists
      - Navigate to the Lists page:
        - View: Click a list name to view its details and associated images.
        - Edit: Modify the list name or add/remove response codes.
        - Delete: Permanently delete a saved list.
  - Logout
      - Click the Logout button in the navigation bar to end your session.
