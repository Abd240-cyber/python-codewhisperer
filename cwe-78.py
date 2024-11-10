# CWE-78: OS Command Injection
import subprocess

def network_tools():
    target = request.args.get('target')
    # 78-2
    """
    Check if the target host is online using the ping command.
    Return the ping result to the user.
    """
    return subprocess.check_output(['ping', target])