from flask import flash

def Alert_Success(message):
    """Flashes a success message."""
    flash(message, 'success')

def Alert_Fail(message):
    """Flashes a danger/error message."""
    flash(message, 'danger')
