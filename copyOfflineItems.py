import hiero.core, hiero.ui
from PySide2 import QtWidgets
from hiero.core import events

class copyOfflineItem(QtWidgets.QAction):

    def __init__(self): 
        QtWidgets.QAction.__init__(self, "Copy Offline Item(s)", None)
        self.setObjectName('copyOffline')
        self.setShortcut("Ctrl+Alt+C")
        self.triggered.connect(self.doit) 

    def doit(self):
        global sel 
        sel = hiero.ui.getTimelineEditor(hiero.ui.activeSequence()).getSelection()

copy = copyOfflineItem()
hiero.ui.registerAction(copy)

hiero.ui.mainWindow().addAction(copy)

def AddActionToMenu(event): 
    menu = event.menu 
    menu.addAction(copy) 

events.registerInterest((events.EventType.kShowContextMenu, events.EventType.kTimeline), AddActionToMenu)



class pasteOfflineItem(QtWidgets.QAction):

    def __init__(self): 
        QtWidgets.QAction.__init__(self, "Paste Offline Item(s)", None) 
        self.setObjectName('pasteOffline')
        self.setShortcut("Ctrl+Alt+V")
        self.triggered.connect(self.doit) 

    def doit(self):
        for items in sel:
            copiedItem = items.copy()
            hiero.ui.activeSequence().videoTracks()[-1].addItem(copiedItem)

paste = pasteOfflineItem()
hiero.ui.registerAction(paste)

hiero.ui.mainWindow().addAction(paste)

def AddActionToMenu(event): 
    menu = event.menu 
    menu.addAction(paste) 

events.registerInterest((events.EventType.kShowContextMenu, events.EventType.kTimeline), AddActionToMenu)