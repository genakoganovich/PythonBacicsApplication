from filecmp import cmp
import zipfile
import os, os.path


def convert_win_to_linux_eol(file_path):
    # replacement strings
    WINDOWS_LINE_ENDING = b'\r\n'
    UNIX_LINE_ENDING = b'\n'

    with open(file_path, 'rb') as open_file:
        content = open_file.read()

    # Windows ➡ Unix
    content = content.replace(WINDOWS_LINE_ENDING, UNIX_LINE_ENDING)

    # Unix ➡ Windows
    # content = content.replace(UNIX_LINE_ENDING, WINDOWS_LINE_ENDING)

    with open(file_path, 'wb') as open_file:
        open_file.write(content)


def create_answer(name, output_name):
    try:
        with zipfile.ZipFile(name) as archive, open(output_name, "w") as f_out:
            answer = sorted({os.path.dirname(i.filename) + '\n'
                             for i in archive.filelist if i.filename.endswith('.py')})
            f_out.writelines(answer)

    except zipfile.BadZipFile as error:
        print(error)

    convert_win_to_linux_eol(output_name)


def test():
    name = 'main.zip'
    create_answer(name, str(name).replace('.zip', '_ans_test.txt'))
    # assert cmp('sample_ans.txt', 'sample_ans_test.txt')

test()
