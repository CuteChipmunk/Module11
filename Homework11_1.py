from PIL import Image, ImageFilter

"""Модуль pillow помогает работать с изображениями, можно менять размер, накладывать разные фильтры, 
например, можно сделать картинку более четкой, сохранять изображение в другом формате и т.д."""

new_size = (128, 128)
original_picture = Image.open('1.jpg')
print(original_picture.format, original_picture.size, original_picture.mode)

original_picture.thumbnail(new_size) #меняем размер изображения
print(original_picture.format, original_picture.size, original_picture.mode)
original_picture.save('2.jpg') #сохраяем в новом размере
#original_picture.show() #смотрим

image_filters = original_picture.filter(ImageFilter.CONTOUR)
image_filters.save('3.png')
print(image_filters.format, image_filters.mode)
#image_filters.show()


