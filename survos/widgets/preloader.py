

from ..qt_compat import QtGui, QtCore, QtWidgets

from .base import HWidgets, HeaderLabel

class RefContainer(QtWidgets.QWidget):

    def __init__(self, title, link_url, description, parent=None):
        super(RefContainer, self).__init__(parent)
        self.setFixedWidth(250)
        self.setFixedHeight(150)
        vbox = QtWidgets.QVBoxLayout()
        self.setLayout(vbox)
        title = QtWidgets.QLabel('<a href="{}">{}</a>'.format(link_url, title))
        title.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        title.setStyleSheet('font-size: 18pt; color: #6194BC;')
        title.setOpenExternalLinks(True)
        vbox.addWidget(title)
        desc = QtWidgets.QLabel(description)
        desc.setWordWrap(True)
        desc.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        desc.setStyleSheet('font-size: 14pt;')
        vbox.addWidget(desc, 1)

class PreButton(QtWidgets.QPushButton):

    def __init__(self, title, description, parent=None):
        super(PreButton, self).__init__(parent)
        self.setStyleSheet('QPushButton {'
                           '  background-color: #6194BC; color: #fefefe;'
                           '}'
                           'QPushButton:hover {'
                           '  background-color: #009999;'
                           '}')
        self.setFixedWidth(250)
        vbox = QtWidgets.QVBoxLayout()
        self.setLayout(vbox)
        title = QtWidgets.QLabel('{}'.format(title))
        title.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        title.setStyleSheet('font-size: 18pt; border-radius: 2px;')
        vbox.addWidget(title)

        desc = QtWidgets.QLabel(description)
        desc.setWordWrap(True)
        desc.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignHCenter)
        desc.setStyleSheet('background-color: transparent; font-size: 14pt; color: #fefefe;')
        vbox.addWidget(desc, 1)
        title.mousePressEvent = self.mousePressEvent
        desc.mousePressEvent = self.mousePressEvent

class PreWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(PreWidget, self).__init__(parent)
        main_layout = QtWidgets.QVBoxLayout()
        main_layout.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.setLayout(main_layout)

        container = QtWidgets.QWidget(self)
        vbox = QtWidgets.QVBoxLayout(container)
        container.setMaximumWidth(950)
        container.setMaximumHeight(530)
        container.setLayout(vbox)
        container.setStyleSheet('QWidget {'
                                '  background-color: #fefefe; '
                                '  border-radius: 10px;'
                                '}')
        main_layout.addWidget(container)

        title = HeaderLabel('<b>SuRVoS</b>: <u>Su</u>per-<u>R</u>egion '
                            '<u>Vo</u>lume <u>S</u>egmentation workbench',
                            fontsize=28, padding=30, margin=5)
        vbox.addWidget(title)

        ref1 = RefContainer('Source Repository',
                            'https://github.com/DiamondLightSource/SuRVoS',
                            'Find the latest version of the software, contribute or suggest improvements.')
        ref2 = RefContainer('Documentation',
                            'https://github.com/DiamondLightSource/SuRVoS/wiki',
                            'Discover how does <b>SuRVoS</b> work and how to get the'
                            ' most out of it.')
        ref3 = RefContainer('Issues and Help',
                            'https://github.com/DiamondLightSource/SuRVoS/issues',
                            'Did you have any trouble or did you find any bug? '
                            'We will try to help.')
        vbox.addWidget(HWidgets(None, ref1, None, ref2, None, ref3, None,
                                stretch=[1,0,1,0,1,0,1]))

        self.open = PreButton('Open Dataset',
                              'Load an existing dataset of supported file formats:'
                              '\n\nMRC (.mrc, .rec), HDF5 (.h5, .hdf5)'
                              ', Tiff Stacks (.tif, .tiff)', parent=self)
        self.open.setFixedWidth(300)
        self.open.setFixedHeight(250)
        self.load = PreButton('Load workspace',
                              'Load a workspace previously created with SuRVoS.'
                              '\n\nAll the feature channels, super-regions and annotations'
                              ' will be recovered.', parent=self)
        self.load.setFixedWidth(300)
        self.load.setFixedHeight(250)

        actions_container = QtWidgets.QWidget()
        hbox = QtWidgets.QHBoxLayout()
        actions_container.setLayout(hbox)

        hbox.addWidget(QtWidgets.QWidget(), 1)
        hbox.addWidget(self.open)
        hbox.addWidget(QtWidgets.QWidget(), 1)
        hbox.addWidget(self.load)
        hbox.addWidget(QtWidgets.QWidget(), 1)

        vbox.addWidget(actions_container)
        vbox.addWidget(QtWidgets.QWidget(), 1)
