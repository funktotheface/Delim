# [delim](https://delim-d091d4e3b1c2.herokuapp.com/)

## Overview
Delim is a sleek and user-friendly application designed to help users keep track of what’s in their kitchen and when it’s set to expire.

The app addresses a common problem: not knowing what’s in your cupboards or fridge, leading to accidental food waste as items pass their expiration dates. By providing users with a simple, customizable database to manage their kitchen inventory, Delim empowers users to take control of their food storage, minimize waste, and save money.

With Delim, users can easily:

* Add items to their inventory with custom details like quantity and expiration dates.
* view, edit, or delete items to keep their inventory up to date.
* get insights on what needs to be used soon, ensuring that nothing goes to waste.

## Table of Contents
[Overview](#Overview)
UX Design Process
Link to User Stories
Wireframes
Accessibility
Design Rationale
Reasoning for Final Changes
Key Features
Implemented
Deployment
Deployment Overview
Pre-Deployment Checklist
Deploying to Platform
Forking and Cloning the Repository
Fork the Project
Clone the Project
Local Development Setup
Environment Variables
Database and Migrations
Services Used
Tech Stack
AI Implementation and Orchestration
Use Cases and Reflections
Testing Summary
Manual Testing
Automated Testing
Upcoming Features


## UX Design Process
### User Stories
I based my design around some core User Stories, the goal was to provide immediate access to the core functionality of the application in a smooth and user firnedly manner, while being aesthetically pleasing and unitrusive.

[Github User Stories Project Board](https://github.com/users/funktotheface/projects/7/views/1)

### Wireframes:
While my end project deviated considerably from my initial wireframes, I feel the core concepts are present and the scope for future features such as recipe suggestions was accounted for in the original design layout.


<img src="readme images/delim readme resources/wireframes/Home Screen.png" alt="Home Screen Wireframe" width="500"/>
<img src="readme images/delim readme resources/wireframes/Inventory Screen.png" alt="Inventory Screen Wireframe" width="500"/>
<img src="readme images/delim readme resources/wireframes/Add_Edit Item.png" alt="Add / Edit Item Screen Wireframe" width="500"/>
<img src="readme images/delim readme resources/wireframes/Recipes.png" alt="Recipes Screen Wireframe" width="500"/>



# Accessibility

Accessibility was a key focus during the development of Delim, ensuring the app is easy to use for everyone, including those with disabilities. The design choices and technical implementation reflect a commitment to inclusivity and usability:

## 1. Simplified UI and Layout
* The user interface and layout were intentionally designed to be simple and self-explanatory, minimizing cognitive load and making navigation intuitive for all users.

## 2.Serene Aesthetic
* A calm, muted blue color scheme was chosen to create a serene and undistracting experience, aligning with the app’s goal of providing a stress-free tool for kitchen organization.

## 3. Screen Reader Compatibility
* HTML accessibility features, such as ARIA labels, were implemented to ensure the app is fully functional with screen readers, improving usability for visually impaired users.

## 4. Lighthouse Accessibility Score
* The app achieved an impressive Lighthouse accessibility score of 96, as well as a matching score for best practices.
* While Lighthouse flagged insufficient contrast between the background and foreground colors, user testing did not reveal any issues with readability or usability. Based on this feedback, the original muted blue color scheme was retained to preserve the app’s aesthetic and maintain a positive user experience.

By prioritizing accessibility in both design and development, Delim offers an inclusive and welcoming experience for all users.

# Design Rationale  

The design of **Delim** is centered on creating a minimalist, user-friendly experience that prioritizes clarity, functionality, and user autonomy. Below are the key design decisions that guided the development process:  

## Key Design Decisions  
- **Minimalist Aesthetic**:  
   - The app features an uncluttered user interface, allowing users to focus on the app’s functionality without distractions.  
   - Emphasis was placed on user autonomy, ensuring that the app is a flexible tool that can adapt to each user's specific needs.  

## Layout  
- A spacious, open layout ensures the app feels accessible and easy to navigate.  
- Controls are positioned in convenient, intuitive locations and are self-explanatory, reducing the learning curve for new users.  
- Important data, such as expiration dates and inventory status, is presented clearly and prominently, ensuring users can quickly access the information they need.  

## Color Scheme  
- A muted blue color palette was chosen to evoke a calm and serene atmosphere.  
- The color scheme balances an unoffending level of contrast while ensuring that key features remain distinguishable, contributing to a pleasant and stress-free user experience.  

<img src="readme images/palette (2).png" alt="delim color scheme" width="500">

## Typography  
- **Primary Font**: The majority of the content is presented in **Nunito**, a sans-serif font from Google Fonts. Its clean and modern design ensures exceptional readability, making navigation and interaction simple and intuitive.  
- **Logo Font**: The logo is styled in **Belgiano Serif**, selected for its friendly and approachable aesthetic. Its subtle elegance allows it to stand out as a distinctive element of the app while maintaining harmony with the rest of the design.  
- **Lowercase Logo**: The logo is presented in all lowercase to convey a subtle, unassuming vibe that reflects the app’s focus on simplicity and user empowerment. 
<img src="readme images/text2.png" alt="delim logo"> 

## Overall Impact  
These design choices work together to create an unintimidating and enjoyable user experience, keeping the focus on the app's functionality and how it serves the user. By blending simplicity, clarity, and adaptability, **Delim** ensures that users can seamlessly manage their kitchen inventory without distractions or complexity.  
 


# Key Features  

- **Customizable Inventory Management:**  
   - Users can easily add, edit, and remove items from their kitchen inventory.  
   - Each item includes details such as name, category, quantity, and expiration date.  

- **Expiration Tracking:**  
   - Automatically sorts items by expiration date to help users prioritize what to use first.  
   - Alerts users when items are nearing or past their expiration date to reduce waste.  

- **Search and Filter Options:**  
   - Users can search their inventory by item name.  
   - Filters allow users to sort their inventory by category or expiration date.  

- **Random Humorous Quotes:**  
   - Each time the user visits the home screen, a random humorous or motivational quote is displayed to add a touch of fun to their experience.  This is achieved by fetching a random item from a json file each time the page is loaded.

- **Animated Logo Intro Overlay:**  
   - A sleek, animated site logo is presented on an introductory overlay, setting a polished and professional tone. This is created by embedding an svg into the html and animating it via CSS, JavaScript is also used to ensure that the animation is presented as an overlay to the page content, and that it only plays out on the first time a user vists the page per browsing session, this is to make sure users arent forced to watch a reptative animation while navigating the site. 

- **Morphing Gradient Background:**  
   - The app features a dynamic, morphing gradient background that enhances visual appeal without detracting from usability.  This was achieved by using a system of html elements and CSS manipulation. The feature does not function as a traditonal background and as such presented its own obstacles such as sizing and layering. Z index had to be taken into account for this feature. While it is not perfectly implemented I am excited to continbue devloping this feature and refining its execution. 

- **Mobile-Friendly Design:**  
   - Fully responsive UI optimized for both desktop and mobile devices.  
   - Simple, self-explanatory controls make it easy to navigate on any screen size.  

- **Accessibility:**  
   - ARIA labels and semantic HTML for screen reader compatibility.  
   - Muted blue color palette provides a calming aesthetic without overwhelming users.  

- **User Authentication:**  
   - Secure user registration and login system with password hashing.  
   - Allows users to maintain their own personalized inventory.  

- **Dashboard Overview:**  
   - A clean, concise dashboard displays the user’s current inventory and highlights items nearing expiration.  

- **Focus on User Autonomy:**  
   - Minimalist design and functionality allow users to tailor the app to their specific needs.  


# Deployment  

## Deployment Overview  
The application was developed using **Visual Studio Code** as the integrated development environment (IDE). **GitHub** served as the version control system, and the project was deployed to **Heroku** using a connected repository.  

---

## Pre-Deployment Checklist  
Before deploying the application, ensure the following steps have been completed:  

1. **Requirements File**  
   - Keep `requirements.txt` updated with all project dependencies:  
     ```bash  
     pip3 freeze --local > requirements.txt  
     ```  

2. **Procfile**  
   - Include a `Procfile` to instruct Heroku to use Gunicorn:  
     ```bash  
     web: gunicorn [your_project_name].wsgi  
     ```  

3. **Allowed Hosts**  
   - Update the `ALLOWED_HOSTS` variable in `settings.py` to include Heroku’s domain:  
     ```python  
     ALLOWED_HOSTS = ['herokuapp.com', 'localhost']  
     ```  

4. **Environment Variables**  
   - Store sensitive data like `DATABASE_URL` and `SECRET_KEY` in an `.env` file and add `.env` to `.gitignore`.  
   - Add these variables to Heroku’s **Config Vars** via the app’s settings.  

---

## Deploying to Heroku  
Follow these steps to deploy the app:  

1. **Create a Heroku App**  
   - Log in to Heroku and click **Create New App**.  
   - Enter a unique name for the app and select the appropriate region.  

2. **Connect to GitHub**  
   - In the **Deploy** tab of your Heroku app, link it to your GitHub repository.  

3. **Set Config Vars**  
   - Add the required environment variables under **Settings → Config Vars**:  
     ```plaintext  
     DATABASE_URL: your_postgres_url  
     SECRET_KEY: your_secret_key  
     DISABLE_COLLECTSTATIC: 1  # Remove this after final deployment  
     ```  

4. **Deploy the Branch**  
   - Under the **Deploy** tab, select the branch you want to deploy (typically `main`).  
   - Click **Deploy Branch** and wait for the process to complete.  
   - Once deployed, click **View** to access the live site.  

---

## Live Link  
[delim Live Link](https://delim-d091d4e3b1c2.herokuapp.com/)  


## Forking and Cloning the Repository  

### Fork the Project  
1. Navigate to the GitHub repository.  
2. Click **Fork** (top-right) to create a copy in your GitHub account.  

### Clone the Project  
1. On the repository page, click **Code** and copy the HTTPS/SSH URL.  
2. In your terminal, run:  
   ```bash  
   git clone https://github.com/your-username/yoga-studio.git
   ```
3. Install dependencies:
   pip3 install -r requirements.txt


## Local Development Setup
### Environment Variables
1. Create an env.py file in the root directory:
   ```
    import os  
    os.environ["DATABASE_URL"] = "your_postgres_url"    
    os.environ["SECRET_KEY"] = "your_secret_key"  
    os.environ["DEBUG"] = "True"  # For local development only
   ```

3. Add env.py to .gitignore.
   
### Database and Migrations
1. Apply migrations
    ```
    python3 manage.py migrate
    ```
2. Create a superuser:
   ```
   python3 manage.py createsuperuser
   ```
### Services Used
1. PostgreSQL Database


### Key Notes
1. Debug Mode - this should always be disabled in production:
   ```bash  
   DEBUG = False
   ```
3. Static Files:
   
   Remove DISABLE_COLLECTSTATIC from Heroku Config Vars after final deployment
5. Use gitignore to protect sensitive data like the secret key.
   
   For more details, refer to the [Django Deployment Checklist](https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/).

# Tech Stack
The technologies used to create delim are:
## Backend
* Django 4.2
* PostgreSQL

## Frontend
* HTML5
* CSS3
* Bootstrap / Bootswatch
* JavaScript

## Tools
* Crispy forms
* Whitenoise

# AI Assistance in Building Delim

AI was a valuable partner throughout the development of **Delim**, assisting in various areas from code creation to debugging and testing. Here’s a more detailed look at the contributions AI made:

## 1. **Code Creation:**
   - **Initial Functionality:**
     One of the first areas where AI was instrumental was in the creation of the user authentication system. When we started with Django, I wasn’t sure how to integrate secure user logins, so I turned to AI for guidance. It provided a clear, step-by-step explanation on setting up Django-Allauth for user authentication, including the necessary code snippets. This saved me time by providing a solid foundation for user registration and login systems.
   
   - **Inventory Management Feature:**
     For the core functionality of the app, which is tracking kitchen inventory, AI helped in structuring the database models. I wasn’t sure about the best way to design the database schema, especially for handling expiry dates and quantities. AI recommended the most efficient approach, helping me create a **Product** model that was simple, effective, and easy to scale in the future. It also suggested ways to manage database queries to pull relevant items based on expiration dates, which was crucial for the app’s core features.
   
   - **UI Layout and Design Elements:**
     I wanted the UI to be clean, simple, and intuitive. AI provided suggestions on HTML structure and it helped me come up with a simple, elegant layout that was responsive and easy to navigate. Later, it assisted with fine-tuning the CSS for the morphing gradient background and animated logo intro that were part of the design.

## 2. **Debugging:**
   - **Identifying Errors in Backend Logic:**
     At one point, I ran into an issue where the app wasn’t correctly calculating the remaining shelf life of certain items in the inventory. I spent a while trying to figure it out, but when I shared the code with AI, it quickly identified a logical error in the way expiration dates were being compared. AI suggested a more robust way to handle date comparisons, which led to the correct results and smoother functionality.
   
   - **Front-End Bugs:**
     Another memorable debugging moment occurred when I had a bug that caused the background gradient to flicker in some browsers. I wasn’t sure what was causing this issue, but when I shared the problem with AI, it recommended using a fallback gradient method to ensure better browser compatibility. That suggestion fixed the flickering problem, and the gradient effect was consistent across different devices and browsers.

   - **Optimizing Queries and Performance:**
     As the app started growing, I noticed some queries taking too long to execute. I consulted AI on how to optimize database queries, particularly with filtering expired items. AI recommended using **select_related** for database joins and **values_list** for retrieving specific columns, which significantly improved query performance and reduced loading times.

## 3. **Unit Test Creation:**
   - **Creating Test Cases:**
     Early on, I wasn’t sure where to begin with unit testing, so I asked AI to guide me through creating tests for the core functionalities. For example, I needed to test the expiration date logic, but wasn’t confident in how to set up the tests. AI helped by suggesting test cases that covered scenarios like adding items with future expiration dates, updating expiration dates, and checking which items should be flagged as expired. It even provided a sample test suite for the model, which I used as a template to write additional tests.
   
   - **Test Automation Suggestions:**
     Another time, I ran into an issue with automating the tests. I didn’t know how to integrate the **Django TestCase** framework with the custom user model I had set up for authentication. AI quickly pointed me to Django’s documentation and gave me a sample test that covered user login and item creation. With its help, I could easily ensure that critical workflows, like logging in and managing inventory, were being properly tested.
   
   - **Edge Case Testing:**
     One specific instance where AI was particularly helpful was when I was unsure about edge cases, like handling inventory items with invalid expiration dates or quantities. AI provided detailed examples of how to test such edge cases and write more comprehensive tests. I learned how to test for null values, invalid data, and boundary conditions, which significantly improved the robustness of my testing process.

## Overall Impact:
   - **Efficiency and Speed:**
     AI helped streamline development by automating repetitive tasks, such as creating boilerplate code, handling common debugging issues, and generating unit tests. For example, when I was trying to create the "inventory update" feature, AI saved me hours of work by suggesting common patterns for form handling and database updates in Django.
   
   - **Improved Code Quality:**
     With AI’s suggestions, my code became more efficient and maintainable. For example, I used AI’s advice to refactor redundant code and optimize functions, which not only made the app perform better but also made it easier for future updates.
   
   - **Confidence in Best Practices:**
     AI ensured that I followed best practices in areas like security (ensuring that sensitive data was properly handled), accessibility (helping me implement screen reader-friendly elements), and user experience (offering UI suggestions that focused on clarity and simplicity).

AI has played a central role in helping me develop **Delim** by providing quick solutions, enhancing the overall quality of the app, and speeding up the development process. The collaboration has allowed me to focus on the creative and strategic aspects of the project, while leaving the repetitive or complex tasks to be handled efficiently by AI.






# Manual Testing
delim has been subjected to extensive manual testing across multiple devices by helpful friends and family memebers. delim has also been subjected to rigorous validation tests inclduing; HTML, CSS, JavaScript and Google Lighthouse.

An example of manual testing leading to the betterment of the application was the discovery of a 403 error caused by the user pressing the sign in button after a browser had already run an autosubmit on the users credentials, this was circumvented by applying a custom script to disable the sign in button for a brief period after being pressed. 

<img src="readme images/delim readme resources/validation/cssvalid.png" alt="css validation" width=500>
<img src="readme images/delim readme resources/validation/dashhtmlvalid.png" alt="html validation" width=500>
<img src="readme images/delim readme resources/validation/lighthouse.png" alt="lighthouse validation" width=500>



# Automated Testing
A comprehensive suite of automated unit tests were created for delim. Ai was instrumental in creating these tests. This was achieved by carefully exposing AI to the various mechanics and relationships between different pices of code in the application in order to create bespoke and robust unit tests to be run on the application. a detailed breakdown of the automated testing is presented below:

## views testing

### 1. Item Details View Test
**Purpose:** Verifies that the application correctly returns detailed information about a specific inventory item via the item-details API endpoint. This test checks the functionality of displaying inventory item data, such as name, quantity, category, expiry date, and associated user.  
**Importance:** Ensures that users can access accurate and detailed information about inventory items, which is vital for tracking the status and expiry of ingredients.

### 2. Index View Test
**Purpose:** Confirms that the application’s home page (index) correctly includes a random quote for the user, ensuring dynamic content is presented as expected.  
**Importance:** This test helps verify that the home page renders correctly with the expected content, which contributes to the overall user experience and engagement.

### 3. Dashboard View Test
**Purpose:** Ensures that the dashboard view loads properly with all relevant context, including inventory items and those nearing expiration. It also verifies that logged-in users see the correct data related to their inventory.  
**Importance:** The dashboard serves as a critical overview of a user’s pantry, so ensuring it is populated with the correct information is vital to maintaining the app’s functionality and usefulness.

### 4. Sign-Up View Test
**Purpose:** Tests the sign-up process for new users, both for rendering the sign-up form and handling form submissions. It verifies that a new user can successfully register and that invalid form submissions are appropriately handled.  
**Importance:** User registration is fundamental to personalizing the app experience. This test ensures the app correctly handles new user creation and authentication processes.

### 5. Add Item View Test
**Purpose:** Verifies the functionality of the form used to add new items to the inventory, including both the display of the form and the successful addition of new items upon form submission.  
**Importance:** This test ensures that users can correctly add items to their inventory, a core feature of the app. By verifying the form submission process, it helps ensure that the inventory management system works as expected.

### 6. Edit Item View Test
**Purpose:** Checks that users can edit existing inventory items by modifying details such as quantity and expiration date. It ensures that changes are properly saved and reflected in the database.  
**Importance:** Inventory management involves updating records regularly, so this test is crucial for ensuring that users can efficiently modify their items as needed.

### 7. Delete Item View Test
**Purpose:** Tests the ability of the app to delete inventory items and confirms that the item is actually removed from the database after deletion.  
**Importance:** Deleting items from the inventory is a key function to keep the system up-to-date. This test ensures that the app performs this action correctly and prevents users from seeing outdated or irrelevant data.

## Models Testing
### 1. InventoryItem Model Tests

### Test: test_string_representation
**Purpose:** Verifies that the string representation of an InventoryItem correctly returns the item's name.  
**Importance:** This test ensures that when we call `str()` on an InventoryItem instance, it returns a readable and meaningful value (in this case, the name of the item). This is important for displaying the inventory items in the user interface and debugging.

### Test: test_default_unit
**Purpose:** Confirms that the default unit for an item is set to 'u' (unit), which is the default if the user doesn't specify a unit.  
**Importance:** Ensures that the system provides a default value for the unit field, preventing errors or empty values when this field is not provided by the user. This helps maintain consistency in the data.

### Test: test_quantity_validation
**Purpose:** Verifies that the quantity field is properly validated and that values outside the acceptable range (less than 0 or greater than 1000) raise a `ValidationError`.  
**Importance:** Ensures that the app prevents the creation of inventory items with invalid quantities. This maintains data integrity and avoids issues such as negative or excessively large quantities, which would be unrealistic for an inventory management system.

### Test: test_category_relationship
**Purpose:** Confirms that an InventoryItem correctly links to its Category, verifying the integrity of the foreign key relationship.  
**Importance:** This test ensures that the InventoryItem model correctly references the Category model, which is important for organizing inventory items by category. It verifies the integrity of database relationships, ensuring items are associated with valid categories.

### Test: test_expiry_date_can_be_null
**Purpose:** Verifies that the expiry_date field in the InventoryItem model can be null, allowing items that do not have an expiry date (such as long-lasting or non-perishable goods).  
**Importance:** This test ensures flexibility in managing items with varying expiration requirements. Items that don't expire should be handled appropriately without throwing errors or requiring an unnecessary date.

### 2. Category Model Tests

### Test: test_string_representation
**Purpose:** Verifies that the string representation of the Category model correctly returns the category's name.  
**Importance:** This test ensures that when we call `str()` on a Category instance, it returns a meaningful value (in this case, the name of the category). This is important for displaying category names throughout the application.

### Test: test_unique_name
**Purpose:** Ensures that the names of categories are unique, meaning there cannot be multiple categories with the same name.  
**Importance:** This test maintains data integrity by preventing duplicate categories. It ensures that users can create categories without confusion and maintain a clean and organized list of categories.

### Test: test_plural_verbose_name
**Purpose:** Verifies that the plural name for the Category model is correctly set to "Categories".  
**Importance:** This test ensures that the `verbose_name_plural` attribute is correctly configured in the model's metadata, ensuring proper pluralization is displayed in the Django admin and other views when dealing with multiple categories.

## Forms Testing

### 1. UserRegisterForm Tests

### Test: test_valid_form
**Purpose:** Verifies that the UserRegisterForm is valid when proper input is provided (e.g., a valid username, email, and matching passwords).  
**Importance:** Ensures that users can successfully register with valid data, thus facilitating smooth user onboarding. This test ensures that the registration process works correctly and that the form enforces necessary constraints, such as requiring matching passwords.

### Test: test_password_mismatch
**Purpose:** Verifies that the UserRegisterForm becomes invalid if the passwords provided in the password1 and password2 fields do not match.  
**Importance:** This test prevents users from entering inconsistent password values, which is a critical feature for security and proper user account creation. By ensuring the password fields match, it reduces the likelihood of user confusion and potential account access issues.

### 2. InventoryItemForm Tests

### Test: test_valid_form
**Purpose:** Verifies that the InventoryItemForm is valid when all required fields are correctly filled out (e.g., name, quantity, unit, category, and expiry date).  
**Importance:** This test ensures that users can successfully add new inventory items when the form is properly filled. It checks that the form’s required fields are being properly validated and that the system behaves as expected when valid input is provided.

### Test: test_invalid_form_quantity_out_of_bounds
**Purpose:** Verifies that the InventoryItemForm is invalid if the quantity is outside the acceptable range (less than 0 or greater than 1000).  
**Importance:** This test ensures that the quantity field respects the business logic constraints (e.g., no negative quantities or overly large values). It is crucial for preventing errors and maintaining data integrity in the application, especially since inventory systems require realistic and accurate quantities.

### Test: test_invalid_form_both_category_and_new_category
**Purpose:** Verifies that the InventoryItemForm is invalid if both the category and new_category fields are provided simultaneously.  
**Importance:** This test ensures that the form enforces proper logic when dealing with categories. If a new category is specified, the category field should not be filled out. This prevents conflicting data and ensures that inventory items are either assigned to an existing category or a new category is created as needed, but not both.


# Upcoming Features
## delim has the scope for a wealth of features that are planned to be implemented in the near future, these features include:

* integrated recpie API to suggest recipe ideas based on expiring goods, allowing users to get suggestions on easy ways to use expiring goods and reduce their waste.

* A data display dashboard showing items the user has allowed to expire, giving real feedback on how the user can improve their waste management. 

* The ability to add items to inventory by use of barcode scanning to streamline the process of populating the users inventory

* multi user support, I would like to allow multiple users to have access to the same inventory, opening up the application to household use.





