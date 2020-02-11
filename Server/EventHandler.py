class EventHandler:
    def __init__(self, server):
        self.server = server
        self.ui = server.ui
        self.app = server.app

    def register_events_handlers(self):
        self.ui.startButton.clicked.connect(self.server.server_execute)
        self.app.aboutToQuit.connect(self.about_to_quit)
        

    def register_start_button_as_stop(self):
        self.ui.startButton.clicked.disconnect()
        self.ui.startButton.clicked.connect(self.server.server_stop)

    def register_stop_button_as_start(self):
        self.ui.startButton.clicked.disconnect()
        self.ui.startButton.clicked.connect(self.server.server_execute)

    def about_to_quit(self):
        self.server.write_log("Closing server application")