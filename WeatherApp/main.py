from ParseData import parse_data
import tkinter as tk


county_data = parse_data()

import kivy
kivy.require('2.1.0') # replace with your current kivy version !

from kivy.app import App

from kivy.uix.scrollview import ScrollView
from kivy.app import runTouchApp

from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window





class MyApp(App):
    def build(self):
      layout = GridLayout(cols = 2)
      layout.size_hint_y= None
      layout.padding = 40
      layout.spacing = 30
      layout.bind(minimum_height=layout.setter('height'))#checks when window maximized
      for county in county_data:
        #print(f"county: {county['name']}\t\trestriction: {county['restriction']}")
        layout.add_widget(Label(text = county["name"]))

        if(county["restriction"] == True):
          layout.add_widget(Label(text = "fire restriction active"))
        else:
          layout.add_widget(Label(text = "no fire restriction"))
      root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
      root.add_widget(layout)
      root.pos_hint = {'center_x':0.5,'top': 1}
      return root


if __name__ == '__main__':
    MyApp().run()

