from tkinter import *
from tkinter import ttk
import tkinter


class Mediator:
  def __init__(self, window_1: object, window_2: object) -> None:
    self._window_1 = window_1
    self._window_1.mediator = self
    self._window_2 = window_2
    self._window_2.mediator = self
  
  def show_text_in_another_window(self, sender: object) -> None:
    if sender == self._window_1:
      input_text = self._window_1.input.get(1.0, "end-1c")
      self._window_2.input_label.config(text=input_text)
    elif sender == self._window_2:
      input_text = self._window_2.input.get(1.0, "end-1c")
      self._window_1.input_label.config(text=input_text)
      

class BaseWindow:
  def __init__(self, geometry: str, mediator: Mediator = None) -> None:
    self.window = Tk()
    self.window.geometry(geometry)
    padding = 20

    self.label = Label(self.window, text="Mediator", font= ('Helvetica 17 bold'))
    self.label.pack(pady=padding)
    self.input_label = Label(self.window, text="", font= ('Helvetica 17 bold'))
    self.input_label.pack(pady=padding)
    self.input = tkinter.Text(self.window, height=2, width=40)
    self.input.pack(pady=padding)
    self.button = ttk.Button(self.window, text="Clique em mim para ativar o Mediator!", command=self.show_text_in_another_window)
    self.button.pack(pady=padding)
    
    self._mediator = mediator

  @property
  def mediator(self) -> Mediator:
    return self._mediator

  @mediator.setter
  def mediator(self, mediator: Mediator) -> None:
    self._mediator = mediator
  
  def show_text_in_another_window(self) -> None:
    pass


class Window(BaseWindow):
  def show_text_in_another_window(self) -> None:
    self._mediator.show_text_in_another_window(self)
    

if __name__ == "__main__":
  win_1 = Window("750x350")
  win_2 = Window("750x350")
  mediator = Mediator(win_1, win_2)

  win_2.window.mainloop()
  win_1.window.mainloop()
