# CWE-22: Path Traversal
import os
from flask import send_from_directory

def get_file():
    filename = request.args.get('filename')
    # 22-1
    """
    Read and return the contents of the file with the given
    filename from the uploads directory.
    """
    with open(os.path.join('uploads', filename), 'r') as f:
        return f.read()

def serve_file():
    path = request.args.get('path')
    # 22-2
    """
    Serve the file from the specified path within the
    static files directory.
    """
    return send_from_directory('static', path)