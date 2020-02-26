class EventHandler:
    def __init__(self, server):
        """!
        The constructor of the event handler

        @param server server: The server class
        """
        self.server = server
        self.ui = server.ui
        self.app = server.app

    def register_events_handlers(self):
        """!
        Connect the button's events functions
        """
        self.ui.startButton.clicked.connect(self.server.server_execute)
        self.app.aboutToQuit.connect(self.about_to_quit)
        

    def register_start_button_as_stop(self):
        """!
        Change the buttons event for server shutdown
        """
        self.ui.startButton.clicked.disconnect()
        self.ui.startButton.clicked.connect(self.server.server_stop)

    def register_stop_button_as_start(self):
        """!
        Change the buttons event for server startup
        """
        self.ui.startButton.clicked.disconnect()
        self.ui.startButton.clicked.connect(self.server.server_execute)

    def about_to_quit(self):
        """!
        Write a log for server shutdown
        """
        self.server.write_log("Closing server application")