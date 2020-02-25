

extensions = ["folder" ,"3ds", "ai", "asp", "avi", "bin", "css", "csv", "dbf", "dll", "doc", "dwg", "eps", "exe", "fle", "gif", "html", "ico", "ini", "iso", "js", "jar", "jpg", "mkv", "mov", "mp3", "mp4", "nfo", "obj", "otf", "pdf", "pkg", "png", "ppt", "psd", "rtf", "svg", "ttf", "txt", "vcf", "wav", "wmv", "xls", "xml", "zip"]

class File:
    def __init__(self, file):
        self.fileName = file[0]
        self.fileSize = file[1]
        self.filePath = file[2]
        self.fileExt = file[3]

class FilePackage:
    def __init__(self, deleteButton, downloadButton, icon, label, line, eventHandler, file = None):
        self.deleteButton = deleteButton
        self.downloadButton = downloadButton
        self.icon = icon
        self.label = label
        self.line = line
        self.file = file

        self.eventHandler = eventHandler

        self.event_connector()

    def event_connector(self):
        self.downloadButton.clicked.connect(self.download)
        self.deleteButton.clicked.connect(self.delete)
        self.label.mousePressEvent = self.label_clicked

    def label_clicked(self, event):
        """Determine if the clicked label is linked to a folder or a file, if its a folder change the displayed folder folder
        
        Arguments:
            event {event} -- The event object of the label
        """
        if self.file.fileExt == "folder":
            self.eventHandler.path += self.file.fileName + "/"
            self.eventHandler.request_files(self.eventHandler.path)
        else:
            self.eventHandler.download_file(self.file)  

    def download(self):     
        self.eventHandler.download_file(self.file)

    def delete(self):
        if self.file.fileExt == "folder":
            self.eventHandler.delete_folder(self.file.filePath)

        else:
            self.eventHandler.delete_file(self.file.filePath)


    def update_label(self, name):
        self.label.setText(name)

    def visibility(self, state):
        self.deleteButton.setVisible(state)
        self.icon.setVisible(state)
        self.label.setVisible(state)
        self.line.setVisible(state)
        self.downloadButton.setVisible(state)

    def ui_activation(self, state):
        self.deleteButton.setEnabled(state)
        self.label.setEnabled(state)
        self.downloadButton.setEnabled(state)
        self.eventHandler.ui.backButton.setEnabled(state)
        self.eventHandler.ui.upButton.setEnabled(state)
        self.eventHandler.ui.downButton.setEnabled(state)
        self.eventHandler.ui.btnCreateFolder.setEnabled(state)
        self.eventHandler.ui.confirmName.setEnabled(state)
        self.eventHandler.ui.addFile.setEnabled(state)

    def set_file(self, file):
        global extensions
        iconChanged = False

        for x in extensions:
            if x == file.fileExt:
                self.icon.setStyleSheet("image: url(:/Images/" + x + ".png)")
                iconChanged = True
                break

        if iconChanged == False:
            self.icon.setStyleSheet("image: url(:/Images/none.png)")

        self.label.setText(file.fileName)
        self.file = file

    def remove_file(self):
        self.label.setText("Text")
        self.file = None
    
    