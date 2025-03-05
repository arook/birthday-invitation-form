# Birthday Invitation Form

A beautiful web application for managing birthday party registrations. Users can fill out a form to register for the party, and they'll receive a confirmation email upon successful registration. All registration data is stored in a PostgreSQL database.

## Features

- Responsive and modern user interface
- Form validation (both client-side and server-side)
- Beautiful confirmation emails
- PostgreSQL database integration
- Flash messaging for user feedback

## Tech Stack

- **Backend**: Python with Flask
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, JavaScript, Bootstrap 5
- **Email**: Flask-Mail

## Setup Instructions

### Prerequisites

- Python 3.7+
- PostgreSQL
- SMTP email server credentials

### Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/birthday-invitation-form.git
   cd birthday-invitation-form
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

4. Configure the environment variables:
   - Rename the `.env.example` file to `.env` 
   - Edit the `.env` file to update your database and email settings

5. Create the PostgreSQL database:
   ```
   createdb -U caffery birthday_invitation
   ```

6. Run the application:
   ```
   python run.py
   ```

7. Open your browser and navigate to: `http://127.0.0.1:5000`

## Database Configuration

The application is configured to use PostgreSQL with the following default settings:
- Username: caffery
- Password: caffery
- Database: birthday_invitation
- Host: localhost
- Port: 5432

You can change these settings in the `.env` file.

## Email Configuration

To enable email sending, update the following settings in the `.env` file:
- `MAIL_SERVER`: Your SMTP server
- `MAIL_PORT`: Your SMTP port
- `MAIL_USERNAME`: Your email username/address
- `MAIL_PASSWORD`: Your email password or app-specific password
- `MAIL_DEFAULT_SENDER`: The email address that will appear as the sender

## License

This project is licensed under the MIT License - see the LICENSE file for details. 