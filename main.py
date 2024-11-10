import json
from PySide6.QtGui import QIcon, Qt
from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QPlainTextEdit, QRadioButton, QPushButton, QListWidget,\
    QHBoxLayout, QVBoxLayout
from GeniusRequest.genius import get_lyrics, get_artist_song_name_list, get_artist_id


class LyricsFinder(QWidget):
    def __init__(self):
        super(LyricsFinder, self).__init__()
        self.main_lay = QVBoxLayout()
        self.search_bar = QLineEdit()
        self.search_context = QRadioButton("Songs")
        self.search_btn = QPushButton()
        self.search_result = QListWidget()
        self.lyrics = QPlainTextEdit()
        self.setup_ui()

    def setup_ui(self):
        # set stylesheet
        with open("Stylesheet/ss.css", "r") as f:
            self.setStyleSheet(f.read())
        self.setWindowTitle("Lyric's Finder")
        self.setWindowIcon(QIcon("Ico/music-outline.svg"))
        # btn search
        self.search_btn.setIcon(QIcon("Ico/search.svg"))
        # radio btn
        self.search_context.clicked.connect(self.s_set_text)
        self.search_context.setStyleSheet("""   color: black;
                                                font: 50 8pt "MS Shell Dlg 2";
                                                font-weight:bold;
                                            """
                                          )
        # search bar layout
        s_lay = QHBoxLayout()
        s_lay.addWidget(self.search_bar)
        s_lay.addWidget(self.search_context)
        s_lay.addWidget(self.search_btn)
        # result layout
        result_lay = QHBoxLayout()
        result_lay.addWidget(self.search_result)
        result_lay.addWidget(self.lyrics)
        self.lyrics.setStyleSheet("""   color: black;
                                        font: 60 14pt "MS Shell Dlg 2";
                                        """)
        # main
        self.main_lay.addLayout(s_lay)
        self.main_lay.addLayout(result_lay)
        # layout
        self.setLayout(self.main_lay)
        self.lyrics.setTextInteractionFlags(Qt.TextSelectableByMouse or Qt.TextSelectableByKeyboard)
        # connect btn
        self.search_btn.clicked.connect(self.search_songs)
        self.search_result.itemDoubleClicked.connect(self.show_lyrics)

    def s_set_text(self):
        if self.search_context.isChecked():
            self.search_context.setText("Artists")
        else:
            self.search_context.setText("Songs")

    def search_songs(self):
        if self.search_context.text() == "Artists":
            artist_id = get_artist_id(self.search_bar.text())
            with open("temp.json", "w") as f:
                artist_songs = get_artist_song_name_list(artist_id)
                json.dump(artist_songs, f)
            self.search_result.clear()
            for title in artist_songs.keys():
                self.search_result.addItem(title)
        else:
            song_direkt = get_artist_id(self.search_bar.text(), False)
            with open("temp.json", "w") as f:
                artist_songs = song_direkt
                json.dump(artist_songs, f)
            self.search_result.clear()
            for title in artist_songs.keys():
                self.search_result.addItem(title)

    def show_lyrics(self):
        songs = self.search_result.currentItem().text()

        with open("temp.json", "r") as f:
            url_dict = json.load(f)
        url = url_dict[songs]
        self.lyrics.setPlainText(get_lyrics(url))

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Return and self.search_result.currentItem():
            self.show_lyrics()
        if event.key() == Qt.Key_Return:
            self.search_btn.click()


app = QApplication([])

main = LyricsFinder()
main.show()

app.exec()
