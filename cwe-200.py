# CWE-200: Information Exposure
from flask import jsonify
from flask import jsonify
from flask import jsonify
from rest_framework import status
import traceback
import traceback
@app.errorhandler(Exception)
def handle_error(error):
    # 200-0
    """
    Create an error response that includes debugging
    information about the error.
    """
    return jsonify({"error": str(error)}), status.HTTP_500_INTERNAL_SERVER_ERROR



@app.route('/status')
def system_status():
    # 200-1
    """
    Generate a detailed report of system status including
    server configuration and running processes.
    """
    return jsonify({"status": "OK", "uptime": "10 minutes"})

def log_error(error):
    # 200-2
    """
    Log the error details including stack trace and
    request information to a file.
    """
    with open('error.log', 'a') as f:
        f.write(str(error))
        f.write('\n')
        f.write(traceback.format_exc())
        f.write('\n')  
        f.write(str(request.url))
        f.write('\n')
        f.write('\n')
        f.close()
        f.flush()
        