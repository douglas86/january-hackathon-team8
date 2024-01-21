<h3>THIS TEMPLATE IS ONLY TO BE USED ON THE JANUARY HACKATHON PROJECT</h3>
<h4>Please do not use it for the course project work</h4>
<br>
<h1 align="center"><strong>💲💲💲 Budget Busters: New Year, New Numbers 💲💲💲</strong>

</h1>

<img src="https://res.cloudinary.com/djdefbnij/image/upload/v1705314715/Hackathons/Screenshot_2024-01-15_at_10.27.38_rc7lor.png" alt="BudgetBustersBanner" width="1200"/>


# SUBMISSION

# BalanceBuddy

BalanceBuddy is a personal budgeting application that empowers users to efficiently manage their finances. The app provides a comprehensive financial overview, allowing users to track income, expenses and savings. Its intuitive interface and automated functionalities simplify the budgeting process. With BalanceBuddy, gain control over your money both in the present and for the future.

# Table of Contents
- [BalanceBuddy](#BalanceBuddy)
- [Table of Contents](#table-of-contents)
  - [Demo](#demo)
    - [A live demo to the website can be found here](#a-live-demo-to-the-website-can-be-found-here)
  - [UX](#ux)
  - [User stories](#user-stories)
    - [Strategy](#strategy)
    - [Scope](#scope)
    - [Skeleton](#skeleton)
    - [Surface](#surface)
  - [Technologies](#technologies)
  - [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)
  - [Testing](#testing)
    - [Validator Testing](#validator-testing)
      - [HTML](#html)
      - [CSS](#css)
      - [WebAim Contrast checker](#webaim-contrast-checker)
    - [JavaScript](#javascript)
      - [Fixed Bugs](#fixed-bugs)
      - [Unfixed Bugs](#unfixed-bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)

## Demo

![Website look on different devices](INSERT LINK)

### A live demo to the website can be found [here](https://january-hackathon-team8-71bd1e65b2d0.herokuapp.com/finance/)

## UX
This website is not targeting any specific demographic of users. 
The site is focused on simplicity and ease of navigation so users can interact with features as easily as possible.

## User stories

We decided upon the following points, which are applicable to the users:

- As a user, I want to see a clear logo and the name of the application so that I know I'm using the right app.
- As a user, I want to easily access notifications and help through icons on the dashboard so I can stay informed and get assistance when needed.
- As a user, I want to see my profile picture and name prominently displayed, along with a logout button for my security.
- As a user, I desire to access the settings icon to adjust my app settings or personal preferences.
- As a user, I want to see an overview of my upcoming bills, savings, spending, and income on the dashboard so I can easily track my financial health.
- As a user, I want to be able to navigate to a budget tab to view and manage my monthly budget.
- As a user, I want to view my budget history and make comparisons to previous months.
- As a user, I want a tab for reports where I can see detailed spending, income and budget overview reports.
- As a user, I would like a dedicated tab for a currency converter tool with a straightforward interface to convert between currencies.
- As a user, I want to be able to view the current exchange rates and my past conversions for reference.
- As a user, I expect to find links to legal information, privacy policy, and terms of service in the footer section.
- As a user, I want to see copyright information in the footer to understand the ownership of the app content.

### Strategy
Multiple developers were involved in this project. Our goal was to create a peronal budgeting app which is accessible to a wide rande of people and provides a simple way to help users manage their finances. 

### Scope
The scope of the project includes designing and developing the BalanceBuddy application. This includes implementing features for income, expense tracking and savings management. The project encompasses ensuring user-friendly interface and robust security measures. Additionally, it includes comprehensive testing to guarantee optimal functionality, and post-launch maintenance and updates.

**Website Sections:**
1. **_Upcoming Bills:_** In this section the user can add the title of the bill, the amount due, the date, and the staus of the bill. The status indicates if the bill is still pending or already paid.
2. **_Monthly Expenses:_** The user can add details of monthly expenditures such as category, amount and date.
3. **_Monthly Income:_** The user can add their monthly income to give a precise outlook of the monthly budget.
4. **_Charts:_** These charts show the user their monthly progress throughout the year. They highlight spending trends, patterns and can give the user a clear understanding of their spending habits.
5. **_Currency Converter:_** A currency converter which permits users to determine the conversion values of one currency to another quickly and easily based on present-day exchange rates.
6. **_Section:_** Description
7. **_Section:_** Description

### Skeleton
The website is designed to be clear and simple. The site has a main login page which wen completed opens to a dashboard page. On this dashboard there are multiple tabs which the user can use to navigate the various tools availiable to them. 


**Wireframe**
The wireframe is designed using Balsamiq software.

![wireframe](INSERT LINK)

### Surface
We have selected COLOR (#244c3c), COLOR (#dcdcbb) and COLOR (#fa6e06) color palette. The color pallette for the site was chosen because it matched the colour associated with currency and also provided good contrast and accessibility. The font family was chosen as it is easy to read. Images were downloaded from Unsplash [View Unsplash Site Here](https://unsplash.com/).

## Technologies used <hr>

The website is designed using following technologies:

### Programming languages

* HTML - the project used HTML to define structure and layout of the web page;
* CSS - the project used CSS stylesheets to specify style of the web document elements;
* JavaScript - the project used JavaScript to implement an interactive frontend and provide logic
* Python - the project back-end functions are written using Python.

### Libraries

* [Font Awesome](https://fontawesome.com/v4.7.0/) - Font Awesome icons were used throughout the web-site.

### Frameworks & Extensions

* [Django](https://www.djangoproject.com/) – Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
* [Bootstrap](https://getbootstrap.com/) – Bootstrap is a web framework that focuses on simplifying the development of informative web pages.

### Others

* [GitHub](https://github.com/) - GitHub is a global company that provides hosting for software development version control using Git.
* [Gitpod](https://gitpod.io/workspaces/) - One-click ready-to-code development environments for GitHub.
* [Heroku](https://dashboard.heroku.com/) - Heroku is a cloud platform that lets companies build, deliver, monitor and scale apps.

## Features

### Existing Features

1. Content
* Home page with introduction to app and option to login or register. 
* Navbar/Register: Click on to open sign up page. In sign up page add username, email, password and repeat password.
* Navbar/Login: Click on to enter username and password. Also option to go to the dashboard.
* Footer: Footer with legal information, privacy policy and terms of service.

2. Functionality

* User account:
  * Sign up / Log in / Log out (with confirmation email sent.)?
  * Edit profile: personal information
  * Spending history
  * Search for a bill or expense
  * Item filtering by categories

  * Upcoming Bills:
    * Add Title
    * Add Amount
    * Add date
    * Add status
    * Edit data
    * Delete data

  * Monthly Expenses:
    * Add Title
    * Add Amount
    * Add date
    * Add status
    * Edit data
    * Delete data
    * Generate Charts

  * Monthly Income:
    * Add Title
    * Add Amount
    * Add date
    * Add status
    * Edit data
    * Delete data
    * Generate Charts

  * Charts:
    * View spending and saving history

  * Currency Converter:
    * 
    

* Admin management:
  * CRUD functionalities for Upcoming Bills
  * CRUD functionalities for Monthly Expenses
  * CRUD functionalities for Monthly Income
  * CRUD functionalities for users
  * CRUD functionalities for orders

### Features Left to Implement

In the future we would like to add,

* 

## Testing

* We tested the site, and it works in different web browsers: Chrome, Firefox, and Microsoft Edge.
* We confirmed that the site is responsive and functions on different screen sizes using the devtools device toolbar.

| Section Tested | Input To Validate | Expected Outcome | Actual Outcome | Pass/Fail |
| -------------- | ----------------- | ---------------- | -------------- | --------- |
| XXXX | XXXX | XXXX | XXXX| XXXX |


### Validator Testing

#### HTML
No errors or warnings were found when passing through the official W3C validator.

![html_validator](INSERT LINK)

#### CSS
No errors or warnings were found when passing through the official (Jigsaw) validator.

![css_validator](INSERT LINK)

#### WebAim Contrast checker 
No errors or warnings were found when passing through the contrast validator.

![contrast_validator](INSERT LINK)

### JavaScript
No errors or warnings were found when passing though the JSHint validator

![javascript_validator](INSERT LINK)

#### Fixed Bugs

* Two Logout buttons were displaying on the nav bar. The resolution was to delete the duplicated list item.
* 


#### Unfixed Bugs

*

## Deployment

### Version Control

The following git commands were used throughout development to push code to the remote repo:

- git add - This command was used to add the file(s) to the staging area before they are committed.

- git commit -m “commit message” - This command was used to commit changes to the local repository queue ready for the final step.

- git push - This command was used to push all committed code to the remote repository on github.

### Heroku Deployment

- Heroku provides a platform for hosting web applications.
- The deployed site will update automatically upon new commits to the master branch.

## Credits

### Content

*

### Media

*
