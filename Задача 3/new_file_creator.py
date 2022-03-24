import os

new_file_name = 'new_file.txt'
base_path = os.getcwd()
print(base_path)
new_file_path = os.path.join(base_path, new_file_name)
print(new_file_path)

print(os.listdir())
txt_files = []
for file in os.listdir():
    if file.endswith('.txt'):
        txt_files.append(file)
print(txt_files)
all_files_list = []
for txt_file in txt_files:
    with open(txt_file, 'r', encoding='utf-8') as file:
        raws = file.readlines()
        lenght = len(raws)
        all_files_list.append([txt_file, lenght, raws])
print(all_files_list)
all_files_list.sort(key= lambda x: x[1])
print(all_files_list)
for item in all_files_list:
    with open(new_file_path, 'a', encoding='utf-8') as doc:
        doc.write(f'\n{item[0]}')
        doc.write(f'\n{str(item[1])}')
        for line in item[2]:
            doc.write(f'\n{line.strip()}')