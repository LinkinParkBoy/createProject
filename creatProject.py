import os
import logging
import sys

logging.basicConfig(level = logging.INFO,format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

dirArray = ['contributed', 'data', 'modle', 'src', 'doc']
childArray = ['test', 'tmp', 'util', 'modle']
fileArray = ['__init__.py', 'LICENSE.md', 'README.md', 'requirements.txt', 'setup.py',]
#info
def info():
    print('To create project template: createProject yourprojectname')
    print('It consist file:')
    print('dir: contributed,data,modle,src,test,tmp,util')
    print('files:__init__.py,LICENSE.md,README.md,requirements.txt,setup.py')


#create function
def createFun(projectname):
    res = os.mkdir(projectname)
    logger.info('create project dir' + str(res))

    os.chdir(projectname)
    print(os.getcwd())

    for i in dirArray:
        res = os.mkdir(i)
        logger.info('create subdir '+ str(res))

    for j in fileArray:
        res = open(j,'a')
        res.close()
        logger.info('create files'+ str(res))

    # create childarray of src
    os.chdir('src')
    print(os.getcwd())
    for j in childArray:
        result = os.mkdir(j)
        logging.info('create subdir' + str(result))


if __name__ == '__main__':
    info()
    print('--------------------------')
    createFun(sys.argv[1])
