def main():
    file_name = input('File name: ').lower().strip()
    get_media_type(file_name)
    get_media(file_name)

def get_media(f):
    is_ext_exist = f.rfind('.')
    if is_ext_exist < 0:
        print('application/octet-stream')
    elif f.endswith('gif'):
        print('image/gif')
    elif f.endswith('jpg') or f.endswith('jpeg'):
        print('image/jpeg')
    elif f.endswith('png'):
        print('image/png')
    elif f.endswith('pdf'):
        print('application/pdf')
    elif f.endswith('txt'):
        print('text/plain')
    elif f.endswith('zip'):
        print('application/zip')
    else:
        print('application/octet-stream')


def get_media_type(f):
    is_ext_exist = f.find('.')
    if is_ext_exist < 0:
        print('application/octet-stream')
    elif 'gif' in f:
        print('image/gif')
    elif 'jpg' in f or 'jpeg' in f:
        print('image/jpeg')
    elif 'png' in f:
        print('image/png')
    elif 'pdf' in f:
        print('application/pdf')
    elif 'txt' in f:
        print('text/plain')
    elif 'zip' in f:
        print('application/zip')
    else:
        print('application/octet-stream')

if __name__ == '__main__':
    main()
