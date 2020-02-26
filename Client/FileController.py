

extensions = ["folder" ,"3ds", "ai", "asp", "avi", "bin", "css", "csv", "dbf", "dll", "doc", "dwg", "eps", "exe", "fle", "gif", "html", "ico", "ini", "iso", "js", "jar", "jpg", "mkv", "mov", "mp3", "mp4", "nfo", "obj", "otf", "pdf", "pkg", "png", "ppt", "psd", "rtf", "svg", "ttf", "txt", "vcf", "wav", "wmv", "xls", "xml", "zip"]

class File:
    def __init__(self, file):
        """!
        The constructor of a file class
        """
        self.fileName = file[0]
        self.fileSize = file[1]
        self.filePath = file[2]
        self.fileExt = file[3]

class FilePackage:
    def __init__(self, deleteButton, downloadButton, icon, label, line, eventHandler, file = None):
        """!
        The constructor of a package of elements that linked to a specific file

        @param deleteButton QButton: The delete button of the file
        @param downloadButton QButton: The download button of the file
        @param icon QLabel: The icon of the file
        @param label QLabel: The name label of the file
        @param line QLine: The graphical seperator
        @param eventHandler: The event handler class
        @param file file: The linked file
        """
        self.deleteButton = deleteButton
        self.downloadButton = downloadButton
        self.icon = icon
        self.label = label
        self.line = line
        self.file = file

        self.eventHandler = eventHandler

        self.event_connector()

    def event_connector(self):
        """!
        Connect the buttons and label functions
        """
        self.downloadButton.clicked.connect(self.download)
        self.deleteButton.clicked.connect(self.delete)
        self.label.mousePressEvent = self.label_clicked

    def label_clicked(self, event):
        """!
        The event of clicking a file label, If it is a folder load that folder, If its a file download that file

        @param event QEvent: Additional event info (No use)
        """
        if self.file.fileExt == "folder":
            self.eventHandler.path += self.file.fileName + "/"
            self.eventHandler.request_files(self.eventHandler.path)
        else:
            self.eventHandler.download_file(self.file)  

    def download(self):    
        """!
        The download button event function
        """ 
        self.eventHandler.download_file(self.file)

    def delete(self):
        """!
        The delet ebutton event function, seperates the different between a folder and a file
        """
        if self.file.fileExt == "folder":
            self.eventHandler.delete_folder(self.file.filePath)

        else:
            self.eventHandler.delete_file(self.file.filePath)


    def update_label(self, name):
        """!
        Update the label text as the given name

        @param name str: The label text
        """
        self.label.setText(name)

    def visibility(self, state):
        """!
        Set the visibility of all the ui elements in this package

        @param state bool: The given state of visibility
        """
        self.deleteButton.setVisible(state)
        self.icon.setVisible(state)
        self.label.setVisible(state)
        self.line.setVisible(state)
        self.downloadButton.setVisible(state)

    def ui_activation(self, state):
        """!
        Set all the ui interactive elements state

        @param state bool: The given state
        """
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
        """!
        Link the given file with the package, change the icon accordingly

        @param file file: The file to link
        """
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
        """!
        Remove the current linked file
        """
        self.label.setText("Text")
        self.file = None
    
    