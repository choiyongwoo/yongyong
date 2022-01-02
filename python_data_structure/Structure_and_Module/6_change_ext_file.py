#터미널에서 파일 및 확장자를 지정하면 새 확장자의 이름으로 복사본을 만듦
import os
import sys
import shutil

def change_file_ext():
    if len(sys.argv)< 2:
        print('Usage: python {0} filename.old_ext "new_ext"'.format(sys.argv[0]))
        sys.exit()
    
    #os.path.splitext() 파일명을 이름과 확장자로 분리해서 반환하는 함수
    name= os.path.splitext(sys.argv[1])[0]+'.'+sys.argv[2]
    print(name)
    
    try:
        shutil.copyfile(sys.argv[1], name)
    except OSError as err:
        print(err)

if __name__=='__main__':
    change_file_ext()