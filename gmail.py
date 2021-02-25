from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from googleapiclient import errors
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from email.mime.text import MIMEText
import base64


def create_message(sender, to, subject, message_text):
    """Create a message for an email.

    Args:
      sender: Email address of the sender.
      to: Email address of the receiver.
      subject: The subject of the email message.
      message_text: The text of the email message.

    Returns:
      An object containing a base64url encoded email object.
    """
    message = MIMEText(message_text)
    message["to"] = to
    message["from"] = sender
    message["subject"] = subject
    encoded_message = base64.urlsafe_b64encode(message.as_bytes())
    return {"raw": encoded_message.decode()}


def send_message(service, user_id, message):
    """Send an email message.

    Args:
      service: Authorized Gmail API service instance.
      user_id: User's email address. The special value "me"
      can be used to indicate the authenticated user.
      message: Message to be sent.

    Returns:
      Sent Message.
    """
    try:
        message = (
            service.users().messages().send(userId=user_id, body=message).execute()
        )
        print("Message Id: %s" % message["id"])
        return message
    except errors.HttpError:
        print("An error occurred: %s" % error)


# Do not modify these
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.send",
]


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # token.pickle is used to store the access and refresh tokens after the
    # authorization flow is first completed
    if os.path.exists("token.pickle"):  # check the file exists
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)  # load stored credentials if they exist

    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if (
            creds and creds.expired and creds.refresh_token
        ):  # token may be invalid as it has now expired
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # Save the credentials for the next run
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    # object to communicate with the API
    service = build("gmail", "v1", credentials=creds)

    """ 
    TASK
        # create a valid message using create_message()
        # Make the subject/body say whatever you want!
        # send the message to your uni address using send_message()
    END TASK 
    """
    create_message('YOUR_EMAIL@gmail.com', 'YOUR_EMAIL@warwick.ac.uk', 'Automated Email', 'Hello, World!')
    send_message(service, 'me', msg)


if __name__ == "__main__":
    main()
