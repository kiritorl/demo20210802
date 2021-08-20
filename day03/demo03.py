import os


def listFile(path):
    files = os.listdir(path)
    for file in files:
        newPath = os.path.join(path, file)
        if os.path.isdir(newPath):
            print(newPath)
            listFile(newPath)
            pass
        else:
            print(os.path.join(path, file))
        pass
    pass


# listFile("D:/pycode/py20210802")




