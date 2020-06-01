import images2chips
import sys
import os

URLS = {
    'dataset-sample' : 'https://dl.dropboxusercontent.com/s/h8a8kev0rktf4kq/dataset-sample.tar.gz?dl=0',
    'dataset-medium' : 'https://dl.dropboxusercontent.com/s/r0dj9mhyv4bgbme/dataset-medium.tar.gz?dl=0',
}

def download_dataset(root, dataset):
    """ Download a dataset, extract it and create the tiles """

    # if dataset is not in URLS, then exit
    if dataset not in URLS:
        print("Dataset name is wrong, please check it.")
        sys.exit(0)

    filename = f'{dataset}.tar.gz'
    url = URLS[dataset]    # extract download link

    # if file not exits, then download it, otherwise print a message
    if not os.path.exists(os.path.join(root, filename)):
        print(f'downloading dataset "{dataset}"')
        os.system('curl ' + url + ' -o ' + os.path.join(root, filename))    # curl [url] -o [filename], filename is a file name or a relative path
    else:
        print('zipfile ' + filename + ' already exists, remove it if you want to re-download.')

    # extract file if the file isn't extracted.
    if not os.path.exists(os.path.join(root, dataset)):
        print('extracting ' + filename)
        os.system('tar -xvf ' + os.path.join(root, filename))
    else:
        print('folder ' + dataset + 'already exists, remove it if you want to re-create.')


    image_chips = os.path.join(dataset, 'image_chips')
    label_chips = os.path.join(dataset, 'label_chips')

    # creating chips is chips haven't created
    if not os.path.exists(os.path.join(root, image_chips)) and not os.path.exists(os.path.join(root, label_chips)):
        print("creating chips")
        images2chips.run(os.path.join(root, dataset))
    else:
        print(f'chip folders "{image_chips}" and "{label_chips}" already exist, remove them to recreate chips.')


if __name__ == '__main__':
    # dataset = 'dataset-sample'  # 0.5 GB download
    dataset = 'dataset-medium' # 9.0 GB download

    download_dataset(root='/home/chsy1996/Downloads/datasets', dataset=dataset)