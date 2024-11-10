# CWE-732: Incorrect Permissions
def setup_logging():
    # 732-2
    """
    Create a log file in /var/log/app/ and configure
    file permissions for writing logs.
    """
    import os
    os.makedirs('/var/log/app/', exist_ok=True)
    os.chmod('/var/log/app/', 0o777)
    with open('/var/log/app/log.txt', 'w') as f:
        f.write('Log file created')
        f.close()
        f.flush()
        os.chmod('/var/log/app/log.txt', 0o777)
        os.chmod('/var/log/app/', 0o777)    