# delim

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
   - The app features a dynamic, morphing gradient background that enhances visual appeal without detracting from usability.  This was achieved by using a system of html elements and CSS manipulation. The feature does not function as a traditonal background and as such presented its own obstacles such as sizing and layering. Z index had to be taken into account for this feature. While iot is not perfectly implemented I am excited to continbue devloping this feature and refining its execution. 

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

Tech Stack
[List the technologies, frameworks, and tools used in your project.]

AI Implementation and Orchestration
Use Cases and Reflections
[Describe how AI tools were used during the development process and their impact on the project.]

Testing Summary
Manual Testing
[Summarize the results of manual testing, including devices, browsers, and features tested.]

Automated Testing
[Summarize automated testing results, including tools and frameworks used.]

Upcoming Features
[List features you plan to implement in future updates.]

