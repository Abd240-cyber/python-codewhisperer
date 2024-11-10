# CWE-434: Unrestricted File Upload
from werkzeug.utils import secure_filename
@app.route('/upload', methods=['POST'])
def upload_file():
    file = request.files['file']
    # 434-0
    """
    Save the uploaded profile picture to the uploads directory.
    Accept only image files.
    """
    return save_profile_picture(file)

def save_document():
    doc = request.files['document']
    # 434-1
    """
    Save the uploaded document to the documents directory.
    Generate a secure filename and return the save path.
    """
    filename = secure_filename(doc.filename)
    return doc.save(os.path.join('documents', filename))

def process_image():
    image = request.files['image']
    # 434-2
    """
    Process the uploaded image file: resize it to 100x100
    and save it as a thumbnail.
    """
    from PIL import Image
    im = Image.open(image)
    im.thumbnail((100, 100))
    return im.save('thumbnails/' + image.filename)