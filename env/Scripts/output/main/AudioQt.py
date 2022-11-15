from PyQt5.QtMultimedia import QAudioOutput, QMediaContent, QMediaPlayer
from PyQt5.QtCore import QUrl


    
def definicion(name,url):
    name=QMediaPlayer()
    urlR = QUrl.fromLocalFile(url)
    content = QMediaContent(urlR)
    name.setMedia(content)
    
    return name
        