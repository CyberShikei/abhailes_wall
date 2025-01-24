def get_image_data(data):
    image_title = data['title']
    image_name = image_title.replace(" ", "_") + '.jpg'
    image_path = 'images/' + image_name
    image_url = data['hdurl']
    image_date = data['date']
    image_desc = data['explanation']

    return (image_path, image_url, image_date, image_desc, image_title)
