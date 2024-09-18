import requests
from PIL import Image
from http import HTTPStatus

response = requests.get(url="https://api.thecatapi.com/v1/images/search")
if response.status_code == HTTPStatus.OK:
    response = response.json()
    img_url = response[0]['url']
    print(f'Ссылка на изображение: {img_url}')
    data = requests.get(img_url).content
    with open('img.jpg', 'wb') as file:
        file.write(data)
    image = Image.open('img.jpg')
    width, height = image.size
    wb_image = image.convert('L')
    wb_image = wb_image.resize((width + 50, height + 50))
    wb_image.show()
    wb_image.save('wb_img.jpg')
else:
    print("Попробуйте еще раз")
