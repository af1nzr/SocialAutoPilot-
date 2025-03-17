from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QMessageBox, QCheckBox, QDialog
from automation.instagram import InstagramBot
from automation.facebook import FacebookBot
import logging

# Configure logging
logging.basicConfig(filename="logs/bot.log", level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Social Media Bot")
        self.setGeometry(200, 200, 400, 300)
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.instagram_button = QPushButton("Instagram Bot")
        self.instagram_button.clicked.connect(self.show_instagram_options)
        layout.addWidget(self.instagram_button)

        self.facebook_button = QPushButton("Facebook Bot")
        self.facebook_button.clicked.connect(self.show_facebook_options)
        layout.addWidget(self.facebook_button)

        self.setLayout(layout)

    def show_instagram_options(self):
        options = BotOptionsDialog("Instagram")
        if options.exec():
            self.run_bot("Instagram", options.get_selected_options())

    def show_facebook_options(self):
        options = BotOptionsDialog("Facebook")
        if options.exec():
            self.run_bot("Facebook", options.get_selected_options())

    def run_bot(self, platform, actions):
        if platform == "Instagram":
            bot = InstagramBot()
        elif platform == "Facebook":
            bot = FacebookBot()
        else:
            QMessageBox.critical(self, "Error", "Unknown platform selected")
            return
        
        bot.start(actions)
        QMessageBox.information(self, "Success", f"{platform} bot started with selected actions!")

class BotOptionsDialog(QDialog):
    def __init__(self, platform):
        super().__init__()
        self.setWindowTitle(f"{platform} Bot Options")
        self.setGeometry(300, 300, 250, 200)
        self.selected_actions = []

        layout = QVBoxLayout()

        self.like_posts = QCheckBox("Auto-like posts")
        self.comment_posts = QCheckBox("Auto-comment on posts")
        self.follow_people = QCheckBox("Auto-follow people")
        self.send_messages = QCheckBox("Auto-send messages")

        layout.addWidget(self.like_posts)
        layout.addWidget(self.comment_posts)
        layout.addWidget(self.follow_people)
        layout.addWidget(self.send_messages)

        submit_button = QPushButton("Start Bot")
        submit_button.clicked.connect(self.accept)
        layout.addWidget(submit_button)

        self.setLayout(layout)

    def get_selected_options(self):
        actions = []
        if self.like_posts.isChecked():
            actions.append("like")
        if self.comment_posts.isChecked():
            actions.append("comment")
        if self.follow_people.isChecked():
            actions.append("follow")
        if self.send_messages.isChecked():
            actions.append("message")
        return actions
