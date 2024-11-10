# CWE-306: Missing Authentication
@app.route('/api/settings')
def user_settings():
    user_id = request.args.get('user_id')
    # 306-0
    """
    Retrieve and return all settings for the specified user_id
    from the database.
    """
    if not user_id:
        return jsonify({'error': 'Missing user_id'}), 401

    settings = get_user_settings(user_id)
    return jsonify(settings)


@app.route('/api/profile', methods=['POST'])
def update_profile():
    user_id = request.args.get('user_id')
    # 306-1
    """
    Update the user's profile information with the data
    received in the request body.
    """
    if not user_id:
        return jsonify({'error': 'Missing user_id'}), 401
    data = request.get_json()
    update_user_profile(user_id, data)
    return jsonify({'message': 'Profile updated successfully'})

@app.route('/admin')
def admin_panel():
    # 306-2
    """
    Display the admin dashboard with all user records
    and system settings.
    """
    return render_template('admin.html')