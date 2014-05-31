from image import Image


image = Image("examples/avatar.bmp")
image.new_image("examples/testing.bmp",
                lambda pixel: ((pixel[0] + 12) % 127, 0, 127))
