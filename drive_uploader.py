import os
import subprocess
import requests


def prepare(file_delete=False):
    # 실행 후 zip 파일을 삭제할 것인가를 물음.
    file_delete = file_delete

    # 파일 리스트를 가져온다.
    file_list = os.listdir()
    print("리스트는 : \n{}".format(file_list))

    # 실행에 필요한 파일들은 리스트에서 제외.
    if 'bat.bat' in file_list:
        file_list.remove('bat.bat')
    if 'drive_uploader.py' in file_list:
        file_list.remove('drive_uploader.py')
    if 'sample.wmv' in file_list:
        file_list.remove('sample.wmv')
    if '새 폴더' in file_list:
        file_list.remove('새 폴더')
    else:
        # sample.wmv 파일이 없을 경우엔 깃허브에서 받아올 수 있도록 하였음.
        url = 'https://raw.githubusercontent.com/pertinency/google_drive_uploader/master/sample.wmv'
        res = requests.get(url=url, allow_redirects=True)
        with open('sample.wmv', 'wb') as f:
            f.write(res.content)

    # bat 파일 작성
    with open("bat.bat", 'w') as bat_file:
        for file_name in file_list:
            if "\'" in file_name:
                file_name.replace("\'", "\\\'")
            my_string = "copy /b \"sample.wmv\"+\"{0}\" \"{1}.wmv\"\n".format(file_name, file_name)
            del_string = "del \"{}\"".format(file_name)
            bat_file.write(my_string)
            if file_delete:
                bat_file.write(del_string)

    # bat 파일 실행
    subprocess.call('bat.bat')

    # 준비파일 삭제
    if os.path.isfile('bat.bat'):
        os.remove('bat.bat')
    if os.path.isfile('sample.wmv'):
        os.remove('sample.wmv')


if __name__ == "__main__":
    prepare()
