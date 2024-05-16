# Airbnb Clone Project

This project is a full-stack web application that replicates the core functionalities of Airbnb. Users can browse listings, make bookings, and host properties. The application is built using Python cmd module, JSON, web famework(Flask), MySQL, HTML, CSS, RestfulAPI(Flask) and JavaScript. It includes features like user authentication, dynamic search, and interactive maps. This repository contains all the necessary code and documentation to set up and run the application locally or on a server.

## Table of Contents
- [Description](#description)
- [Features](#features)
- [Installation](#installation)
- [Command Interpreter](#command-interpreter)
  - [How to Start It](#how-to-start-it)
  - [How to Use It](#how-to-use-it)
  - [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Description

The Airbnb Clone project is designed to provide a similar experience to Airbnb, allowing users to list properties, browse available listings, book accommodations, and leave reviews. The project is implemented using a combination of frontend and backend technologies to ensure a seamless user experience.

## Features
- User authentication and profile management
- Property listing with detailed descriptions and photos
- Advanced search and filtering options
- Booking system with calendar integration
- Reviews and ratings for properties
- Interactive maps for location-based searches

## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/abangayoma/airbnb-clone.git
   cd airbnb-clone
   ```

2. Set up a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set up the MySQL database and configure the connection in your environment variables.

5. Run the Flask application:
   ```bash
   flask run
   ```

## Command Interpreter

The command interpreter is a crucial part of the project, allowing users to interact with the backend through a command-line interface.

### How to Start It

To start the command interpreter, ensure your virtual environment is activated and run the following command from the root directory of the project:

```bash
python3 console.py
```

### How to Use It

Once the command interpreter is running, you can use various commands to manage the application's data. Here are some of the basic commands:

- `help`: Displays a list of available commands
- `create <ClassName>`: Creates a new instance of a class
- `show <ClassName> <id>`: Shows the details of a specific instance
- `destroy <ClassName> <id>`: Deletes a specific instance
- `all <ClassName>`: Shows all instances of a class
- `update <ClassName> <id> <attribute> <value>`: Updates an attribute of a specific instance

### Examples

Here are some examples of how to use the command interpreter:

1. **Creating a new User:**
   ```bash
   create User
   ```

2. **Showing details of a specific User:**
   ```bash
   show User 1234-5678-9101
   ```

3. **Deleting a specific Place:**
   ```bash
   destroy Place 5678-9101-1234
   ```

4. **Showing all Users:**
   ```bash
   all User
   ```

5. **Updating an attribute of a specific User:**
   ```bash
   update User 1234-5678-9101 email "newemail@example.com"
   ```

## Contributing

Contributions are welcome! Please read the [Contributing Guidelines](CONTRIBUTING.md) before submitting a pull request.
This project was done by Abang Ayoma and Joshua Aisien
