from flask import request
@app.route('/profile')
def profile():
    # 79-0
    """
    Get the user_data from URL parameter and display it in an HTML template.
    The template should show user's name, bio, and website URL.
    """
    user_data = request.args.get('user_data')
    return render_template('profile.html', user_data=user_data)


# Another XSS scenario
@app.route('/comments')
def comments():
    comments_list = get_comments_from_db()
    # 79-1
    """
    Display the comments_list in an HTML template.
    Each comment should show the user's name and their comment text.
    """
    return render_template('comments.html', comments_list=comments_list)