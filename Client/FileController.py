extensions = ["folder" ,"3ds", "ai", "asp", "avi", "bin", "css", "csv", "dbf", "dll", "doc", "dwg", "eps", "exe", "fle", "gif", "html", "ico", "ini", "iso", "js", "jar", "jpg", "mkv", "mov", "mp3", "mp4", "nfo", "obj", "otf", "pdf", "pkg", "png", "ppt", "psd", "rtf", "svg", "ttf", "txt", "vcf", "wav", "wmv", "xls", "xml", "zip"]

class File:
    def __init__(self, file):
        self.fileName = file[0]
        self.fileSize = file[1]
        self.filePath = file[2]
        self.fileExt = file[3]

class FilePackage:
    def __init__(self, renameButton, deleteButton, downloadButton, icon, label, line, eventHandler, file = None):
        self.renameButton = renameButton
        self.deleteButton = deleteButton
        self.downloadButton = downloadButton
        self.icon = icon
        self.label = label
        self.line = line
        self.eventHandler = eventHandler
        self.file = file

    def update_label(self, name):
        self.label.setText(name)

    def visibility(self, state):
        self.renameButton.setVisible(state)
        self.deleteButton.setVisible(state)
        self.icon.setVisible(state)
        self.label.setVisible(state)
        self.line.setVisible(state)
        self.downloadButton.setVisible(state)

    def set_file(self, file):
        global extensions
        iconChanged = False

        for x in extensions:
            if x == file.fileExt:
                self.icon.setStyleSheet("image: url(:/Images/" + x + ".png)")
                iconChanged = True
                break

        if not iconChanged:
            self.icon.setStyleSheet("image: url(:/Images/none.png)")

        self.label.setText(file.fileName)
        self.file = file

    def remove_file(self):
        self.label.setText("Text")
        self.file = None
    
    