files = input('File name: ')


if files.endswith('.gif')
print('image/gif')
elif files.endswith('.jpg') or files.endswith('.jpeg'):
print('image/jpeg')

elif files.endswith('.png'):
print('image/png')

elif files.endswith('.pdf'):
print('application/pdf')

elif files.endswith('.txt'):
print('file/txt')

elif files.endswith('.zip'):
print('file/zip')

else: print('application/octet-stream')
