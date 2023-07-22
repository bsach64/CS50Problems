file_name = input("File: ").strip().lower()

if '.' in file_name:
    file_name = file_name.split('.')
    if file_name[-1] == 'jpg' or file_name[-1] == 'jpeg':
        print('image/jpeg')
    elif file_name[-1] == 'png':
        print('image/png')
    elif file_name[-1] == 'gif':
        print('image/gif')
    elif file_name[-1] == 'pdf':
        print('application/pdf')
    elif file_name[-1] == 'txt':
        print('text/plain')
    elif file_name[-1] == 'zip':
        print('application/zip')
    else:
        print('application/octet-stream')
else:
    print('application/octet-stream')