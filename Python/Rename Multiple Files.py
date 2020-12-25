import os

def main():
    path = r"C:\Users\Shivam\Desktop\svg"
    for filename in enumerate(os.listdir(path)):
        dst = filename[1].replace('-','_')
        src = os.path.join(path,filename[1])
        dst = os.path.join(path,dst)
        os.rename(src,dst)


if __name__ == '__main__':
    main()