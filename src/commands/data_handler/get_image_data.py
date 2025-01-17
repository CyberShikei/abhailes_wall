def get_image_data(data):
    image_name = data.iloc[0]['title']
    image_name = image_name.replace(" ", "_") + '.jpg'
    image_path = 'images/' + image_name
    image_url = data.iloc[0]['hdurl']
    image_date = data.iloc[0]['date']
    image_desc = data.iloc[0]['explanation']

    return (image_path, image_url, image_date, image_desc)
