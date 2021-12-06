from tkinter import Tk
from gui.introView import IntroView
from gui.mainView import MainView

class UI:
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start_gui(self):
        self._show_intro_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None

    def _handle_intro(self):
        self._show_intro_view()

    def _handle_main(self):
        self._show_main_view()

    def _show_intro_view(self):
        self._hide_current_view()

        self._current_view = IntroView(
            self._root,
            self._handle_main
        )

        self._current_view.pack()

    def _show_main_view(self):
        self._hide_current_view()

        self._current_view = MainView(
            self._root,
            self._handle_intro
        )

        self._current_view.pack()
