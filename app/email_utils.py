from flask import render_template
from flask_mail import Message
from app import mail

def send_confirmation_email(registration):
    """Send a beautiful confirmation email to the registrant."""
    subject = "🎉 Thank You for Your Birthday Party Registration!"
    
    # Create a beautiful HTML email
    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <style>
            body {{ font-family: 'Arial', sans-serif; color: #333; max-width: 600px; margin: 0 auto; padding: 20px; }}
            .container {{ background-color: #f9f9f9; border-radius: 8px; padding: 20px; border: 1px solid #ddd; }}
            .header {{ text-align: center; margin-bottom: 20px; }}
            .header h1 {{ color: #ff6b6b; margin-bottom: 5px; }}
            .content {{ line-height: 1.6; }}
            .footer {{ margin-top: 30px; font-size: 0.9em; color: #777; text-align: center; }}
            .highlight {{ background-color: #fff3cd; padding: 15px; border-radius: 5px; margin: 15px 0; border-left: 4px solid #ffc107; }}
            .button {{ display: inline-block; background-color: #4CAF50; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin-top: 15px; }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>🎉 Birthday Celebration 🎉</h1>
                <p>Your registration has been confirmed!</p>
            </div>
            
            <div class="content">
                <p>Dear <strong>{registration.full_name}</strong>,</p>
                
                <p>Thank you for registering for our birthday celebration! We're thrilled that you'll be joining us for this special occasion.</p>
                
                <div class="highlight">
                    <p><strong>Event Details:</strong></p>
                    <p>🗓️ Date: Saturday, July 15th, 2023</p>
                    <p>🕔 Time: 7:00 PM - 11:00 PM</p>
                    <p>📍 Location: Crystal Garden Venue, 123 Party Lane</p>
                </div>
                
                <p>We've noted your preferences and any special requests you've mentioned. If you need to make any changes to your registration, please don't hesitate to contact us.</p>
                
                <p>We look forward to celebrating with you!</p>
                
                <p>Warm regards,<br>The Celebration Team</p>
            </div>
            
            <div class="footer">
                <p>This is an automated message. Please do not reply to this email.</p>
                <p>© 2023 Birthday Celebration Team. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>
    """
    
    # Create a plain text alternative for email clients that don't support HTML
    text_body = f"""
    🎉 Birthday Celebration 🎉
    
    Dear {registration.full_name},
    
    Thank you for registering for our birthday celebration! We're thrilled that you'll be joining us for this special occasion.
    
    Event Details:
    - Date: Saturday, July 15th, 2023
    - Time: 7:00 PM - 11:00 PM
    - Location: Crystal Garden Venue, 123 Party Lane
    
    We've noted your preferences and any special requests you've mentioned. If you need to make any changes to your registration, please don't hesitate to contact us.
    
    We look forward to celebrating with you!
    
    Warm regards,
    The Celebration Team
    """
    
    msg = Message(
        subject=subject,
        recipients=[registration.email],
        body=text_body,
        html=html_body
    )
    
    mail.send(msg)
    return True 