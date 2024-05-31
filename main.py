#! /usr/bin/env python3

import sys

from PIL import Image


def main(name) -> None:
	try:
		with Image.open(f'img_exif/{name}') as img:
			img.load()
	except FileNotFoundError:
		print(f'File {name} does not exist')
	except KeyboardInterrupt:
		print('Exit')
		sys.exit()

	try:
		img.save(f'img_no_exif/{name}')
	except NameError as er:
		print(er)
	

if __name__ == '__main__':
	name = input('Image name: ')
	main(name)
	
