contents = ["All carrots are to be sliced ",
            "longitudinally.",
            "The carrots were reportedly sliced."
           ]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(rf"ToDoList/Files/{filename}", 'w')
    file.write(content)
