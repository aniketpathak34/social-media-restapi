
# Social Media REST API

The Social Media REST API enables seamless social interaction and content sharing. Integrate social features into your applications, fostering user engagement and collaboration through posts, likes, comments, and more.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The Social Media REST API empowers developers to create social networking functionalities within their applications. From user profiles to posts, likes, comments, and follows, the API offers a comprehensive set of endpoints to build engaging social experiences.

## Features

- **User Authentication & Profiles**: Register and authenticate users, and retrieve user profiles.
- **Create, Read, Update, Delete Posts**: Manage user-generated content seamlessly.
- **Like & Comment Functionality**: Enable users to interact with posts through likes and comments.
- **Follow & Unfollow Users**: Foster connections between users by allowing them to follow each other.
- **User-Friendly Swagger Documentation**: Interactive API documentation for easy integration.

## Technologies Used

- **Backend Framework**: Django with Django REST framework
- **Database**: PostgreSQL (can be customized to use other databases)
- **Authentication**: JSON Web Tokens (JWT)
- **Documentation**: Swagger

## Installation

pip install -r requirements.txt

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver




## User Profile Details To access this endpoint
Username : "admin"
Password : "admin"
## API Endpoints

The Social Media REST API provides the following endpoints:

- **POST /api/authenticate/**: Dummy authentication to obtain JWT tokens.
- **POST /api/token/**: Obtain JWT tokens for user authentication.
- **POST /api/follow/{id}/:** Follow a specific user.
- **POST /api/unfollow/{id}/:** Unfollow a specific user.
- **GET /api/user/**: Retrieve the authenticated user's profile.
- **POST /api/posts/**: Create a new post.
- **DELETE /api/delete/{id}/:** Delete a post by ID.
- **POST /api/like/{id}/:** Like a post by ID.
- **POST /api/unlike/{id}/:** Unlike a post by ID.
- **POST /api/comment/{id}/:** Add a comment to a post by ID.
- **GET /api/posts/{id}/:** Retrieve details of a specific post by ID.
- **GET /api/all_posts/**: List all posts with likes and comments.

Please note that some endpoints may require authentication through JWT tokens. While you can explore the interactive API documentation for an overview of the endpoints, tools like Postman are recommended for thorough testing and authentication.

## Authentication

JWT (JSON Web Tokens) is used for authentication. The `/api/authenticate/` endpoint provides dummy authentication to obtain JWT tokens for testing purposes. For real-world usage, implement proper user registration and login mechanisms to obtain valid JWT tokens.

## Usage

1. Register a user account or log in with existing credentials.

2. Explore the API documentation at https://social-media-api-kog0.onrender.com/. Note that JWT authentication is primarily accessible through tools like Postman.

3. Use API endpoints to manage user profiles, posts, likes, comments, and follows.

## Contributing

Contributions are appreciated! Feel free to contribute enhancements or features via pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
Usage
Follow installation instructions to integrate the Social Media REST API. Enable social networking features in your application, enabling users to connect, share, and engage effectively.
