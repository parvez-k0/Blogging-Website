# ShareItAll

ShareItAll is an engaging platform that allows users to share their thoughts, connect with others, and create meaningful conversations. Whether you're sipping chai or taking a break, ShareItAll brings people closer through words.

## Features

- **User Authentication**: Secure registration and login functionality.
- **Post Your Thoughts**: Share your ideas, thoughts, and stories in the form of tweets.
- **Image Support**: Upload and display images alongside your posts.
- **Edit & Delete**: Edit or delete your own posts seamlessly.
- **Responsive Design**: Optimized for all screen sizes with Bootstrap.

## Tech Stack

- **Frontend**: HTML, CSS, Bootstrap
- **Backend**: Django (Python)
- **Database**: SQLite (Development)


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/shareitall.git
   ```

2. Navigate to the project directory:
   ```bash
   cd shareitall
   ```

3. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

4. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Apply migrations:
   ```bash
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and visit:
   ```
   http://127.0.0.1:8000
   ```

## Usage

- Register or log in to your account.
- Create, view, and share your tweets.
- Edit or delete your posts as needed.
- Log out securely when you're done.

## Project Structure

```
shareitall/
├── templates/      # HTML files for the UI
├── static/         # CSS, JS, and images
├── app/            # Django app containing models, views, and urls
├── db.sqlite3      # Development database
├── manage.py       # Django management script
└── requirements.txt # List of dependencies
```

## Contributing

Contributions are welcome! Here's how you can get started:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to your branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

## License
**MOHD PARVEZ KHAN**
This project is licensed under the [MIT License](LICENSE).

---

Feel free to reach out with any questions or feedback! Together, let's make ShareItAll the best place to share thoughts and connect.
