# User Directory App

A simple one-page JavaScript application that fetches user data from a public JSON API and displays it dynamically on the webpage.

## Features

- Fetches user data using the **Fetch API**
- Uses **async/await** for asynchronous operations
- Displays a **loading message** while fetching data
- Handles API and network errors gracefully
- Dynamically creates HTML elements using the **DOM**
- Displays the first three users from the API response

## Technologies Used

- HTML5
- CSS3
- JavaScript (ES6+)
- Fetch API

## Project Structure

```text
.
├── index.html
├── style.css
├── script.js
└── README.md
```

## API Used

This project uses the free public API provided by JSONPlaceholder.

**API Endpoint**

```text
https://jsonplaceholder.typicode.com/users
```

## How It Works

1. The page loads.
2. A **"Loading users..."** message is displayed.
3. JavaScript sends a GET request using the Fetch API.
4. The response is converted into a JavaScript object using `response.json()`.
5. The first three users are selected.
6. User cards are created dynamically and displayed on the page.
7. If an error occurs, an appropriate error message is shown.

## Concepts Demonstrated

- DOM Manipulation
- Fetch API
- Async/Await
- Promises
- Error Handling (`try...catch`)
- HTTP Response Validation (`response.ok`)
- Template Literals
- Array Methods (`slice()`, `forEach()`)

## How to Run

1. Clone or download this repository.
2. Open the project folder.
3. Open `index.html` in your web browser.

No additional setup or installation is required.

## Future Improvements

- Add a search feature
- Display all users with pagination
- Add a loading spinner instead of text
- Improve UI with modern CSS
- Add responsive design for mobile devices
- Display additional user details such as company and address

## Learning Outcomes

This project helped practice:

- Working with REST APIs
- Fetching and displaying remote data
- Creating and manipulating DOM elements
- Handling asynchronous JavaScript
- Implementing proper error handling
- Building a simple interactive web application

## Author

**Brij Patel**
