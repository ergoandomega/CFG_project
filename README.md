# Fitagotchi
A web application that helps a user achieve their health and fitness goals.

## Summary
This web application allows a user to find out their BMI based on their height and weight and have a goal based on the BMI. There are two elements that assist the user on their health journey: a randomised low-fat recipe generator, which works by taking a user's inputted ingredient and returning two recipes based on that input, and a workout guide, which consists of 3 randomised exercises that a user can perform in order to complete a workout.

## Installation Guide
Use the terminal to install Python tools `flask`, `mysql-connector` and `requests`:
```bash
pip install flask
```
```bash
pip install mysql-connector-python
```
```bash
pip install requests
```

Create a new Python file called `config.py` by using the `config.template.py` file, and insert your app key and app ID for the edamam API - this information is unique to each user account and is therefore encrypted in the program's code.

<img width="441" alt="Screenshot 2022-08-15 at 16 19 58" src="https://user-images.githubusercontent.com/107500701/184668029-49f12780-f2ed-4480-9b8c-daf95d4b26bb.png">

## Documentation
* Edamam API documentation can be found here https://developer.edamam.com/edamam-docs-recipe-api
* Wger API documentation can be found here https://wger.de/en/software/api
* ZenQuotes documentation can be found here https://premium.zenquotes.io/zenquotes-documentation/

## Navigating the App
The web application initially asks the user to sign up or sign in. The user must be signed in before they will be able to view the other parts of the website.

<img width="328" alt="Screenshot 2022-08-15 at 16 24 36" src="https://user-images.githubusercontent.com/107500701/184664933-d76ce334-7c43-4797-a210-ddf1fc0f27e9.png">

The navigation bar for the site is located at the bottom of the page, allowing the user to browse through the different pages on the site.

<img width="750" alt="Screenshot 2022-08-15 at 16 24 14" src="https://user-images.githubusercontent.com/107500701/184664770-2ca97259-0e7b-4464-a9a8-b35e6f5857e9.png">

A signout button is located in the top right corner of the webpage.

<img width="62" alt="Screenshot 2022-08-15 at 16 24 15" src="https://user-images.githubusercontent.com/107500701/184664761-2e0c2c08-346a-47aa-9c67-7398db974baf.png">
