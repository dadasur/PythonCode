import sys
import os
from pathlib import Path
import re
import smtplib

EXPECTED_ARG_COUNT = 4

def DirectoryValidation(directorypath):
    errors = []

    if not directorypath or not directorypath.strip():
        errors.append("Directory path is not provided.")
        return errors

    path = Path(directorypath)

    if not path.is_absolute():
        errors.append("Path is not absolute.")

    if not path.exists():
        errors.append("Directory does not exist.")
    else:
        if not path.is_dir():
            errors.append("Path is not a directory.")

        if not os.access(path, os.R_OK):
            errors.append("Directory is not readable.")

    return errors

def validateinterval(interval):
    
    if interval is None or str(interval).strip() == "":
        return False, "Time interval is not provided."
    try:
        interval_value = float(interval)
    except (ValueError, TypeError):
        return False, f"Invalid time interval: '{interval}'. Must be a numeric value."

    if interval_value <= 0:
        return False, "Time interval must be greater than zero."

    return True, "Time interval validation successful."

def emailvalidate(email):
    
    # 1. Check whether the email address is provided
    if not email or not email.strip():
        return False, "Email address is not provided."

    # 2. Validate the basic format of the email address
    email_pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

    if not re.match(email_pattern, email):
        return False, "Invalid email address format."

    return True, "Email validation successful."

import smtplib


def smtpconnectionvalidate(smtp_server,smtp_port,username,password):
    try:
        with smtplib.SMTP(smtp_server, smtp_port, timeout=10) as server:
            server.starttls()
            server.login(username, password)

        return True, "SMTP authentication successful."

    except smtplib.SMTPAuthenticationError:
        return False, "SMTP authentication failed. Check username/password."

    except smtplib.SMTPConnectError:
        return False, "Unable to connect to SMTP server."

    except smtplib.SMTPServerDisconnected:
        return False, "SMTP server disconnected unexpectedly."

    except TimeoutError:
        return False, "Connection timed out."

    except Exception as ex:
        return False, f"SMTP validation failed: {str(ex)}"

def validatecommandline():
    if len(sys.argv) != EXPECTED_ARG_COUNT:
        return (
            False,
            f"Invalid number of arguments. Expected "
            f"{EXPECTED_ARG_COUNT - 1}, received {len(sys.argv) - 1}."
        )

    return True, "Argument count validation successful."

def filevalidate(filepath):
    errors = []

    try:
        path = Path(filepath)
        if not path.exists():
            errors.append("File does not exist.")
            return errors
        if not path.is_file():
            errors.append("Path does not represent a regular file.")

        if not os.access(path, os.R_OK):
            errors.append("File is not readable.")

        if not os.access(path.parent, os.W_OK):
            errors.append(
                "Insufficient permission to delete the file."
            )

        try:
            with open(path, "a"):
                pass
        except PermissionError:
            errors.append(
                "File is locked or currently in use."
            )

    except PermissionError:
        errors.append(
            "Permission denied while accessing the file."
        )

    except OSError as ex:
        errors.append(
            f"Operating system error: {ex}"
        )

    return errors
