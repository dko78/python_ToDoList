filenames = ["1.doc", "1.report", "3.prezentation"]

filenames = [filename.replace('.', '-') + ".txt" for filename in filenames]

print(filenames)