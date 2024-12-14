import pyttsx3  # Import the pyttsx3 library for text-to-speech functionality
from kivy.app import App  # Import the App class from Kivy to create the main application
from kivy.uix.screenmanager import ScreenManager, Screen  # Import ScreenManager and Screen to manage different screens
from kivy.uix.boxlayout import BoxLayout  # Import BoxLayout for arranging widgets vertically/horizontally
from kivy.uix.button import Button  # Import Button to create clickable UI elements
from kivy.uix.label import Label  # Import Label to display text
from kivy.uix.switch import Switch  # Import Switch to create toggle switches for user input
from kivy.core.window import Window  # Import Window to customize the window size and background

# Set the window size and background color (for an Android-like resolution)
Window.size = (360, 600)  # Define window dimensions (Width x Height)
Window.clearcolor = (0.1, 0.1, 0.9, 1)  # Set the app's background color to blue (RGBA format)

# Initialize the TTS engine for text-to-speech functionality
tts_engine = pyttsx3.init()

# Function to make the app speak a given message
def speak(message):
    tts_engine.say(message)  # Queue the message to be spoken
    tts_engine.runAndWait()  # Process and output the speech

# Welcome Screen Class
class WelcomeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Initialize the parent class (Screen)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)  # Create a vertical layout
        label = Label(text="Hello there!\nReady to hear me?", color=(1, 1, 1, 1), font_size=24)  # Add a label with text
        next_button = Button(text="Next", size_hint=(1, 0.2), background_color=(0.2, 0.5, 1, 1))  # Create a "Next" button
        next_button.bind(on_press=self.next_screen)  # Bind the button press to navigate to the next screen
        layout.add_widget(label)  # Add the label to the layout
        layout.add_widget(next_button)  # Add the next button to the layout
        self.add_widget(layout)  # Add the layout to the screen

    # Method to navigate to the menu screen
    def next_screen(self, instance):
        speak("Next")  # Speak "Next" when the button is pressed
        self.manager.current = "menu"  # Switch to the "menu" screen

# Menu Screen Class
class MenuScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Initialize the parent class (Screen)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)  # Create a vertical layout
        options = ["Settings", "Share", "About", "Coffee"]  # List of menu options
        for option in options:  # Loop through the menu options
            button = Button(text=option, size_hint=(1, 0.2), background_color=(0.2, 0.5, 1, 1))  # Create a button for each option
            button.bind(on_press=lambda instance, text=option: self.open_screen(text))  # Bind the button to open the respective screen
            layout.add_widget(button)  # Add the button to the layout
        self.add_widget(layout)  # Add the layout to the screen

    # Method to navigate to the appropriate screen based on the button pressed
    def open_screen(self, screen_name):
        speak(f"You pressed {screen_name}")  # Speak the name of the button pressed
        self.manager.current = screen_name.lower()  # Switch to the screen by name

# Settings Screen with Submenus Class
class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Initialize the parent class (Screen)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)  # Create a vertical layout
        settings = ["Display", "Volume", "Sound Type", "Fonts"]  # List of settings options
        for setting in settings:  # Loop through the settings options
            button = Button(text=setting, size_hint=(1, 0.2), background_color=(0.2, 0.5, 1, 1))  # Create a button for each setting
            button.bind(on_press=lambda instance, text=setting: self.open_screen(text))  # Bind each button to open the corresponding submenu
            layout.add_widget(button)  # Add the button to the layout
        back_button = Button(text="Back", size_hint=(1, 0.2), background_color=(1, 0.3, 0.3, 1))  # Create a "Back" button
        back_button.bind(on_press=lambda x: (speak("Back"), setattr(self.manager, 'current', 'menu')))  # Go back to the main menu
        layout.add_widget(back_button)  # Add the back button to the layout
        self.add_widget(layout)  # Add the layout to the screen

    # Method to navigate to the specific submenu based on the button pressed
    def open_screen(self, screen_name):
        speak(f"You opened {screen_name}")  # Speak the name of the submenu
        if screen_name.lower() == "display":
            self.manager.current = "display"  # Navigate to the Display Screen
        elif screen_name.lower() == "volume":
            self.manager.current = "volume"  # Navigate to the Volume Screen
        elif screen_name.lower() == "sound type":
            self.manager.current = "soundtype"  # Navigate to the Sound Type Screen
        elif screen_name.lower() == "fonts":
            self.manager.current = "fonts"  # Navigate to the Fonts Screen

# Display Submenu Screen with Light/Dark Theme Toggles
class DisplayScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Initialize the parent class (Screen)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)  # Create a vertical layout
        label = Label(text="Display Settings", color=(1, 1, 1, 1), font_size=24)  # Add a label for Display Settings
        layout.add_widget(label)  # Add the label to the layout

        # Light Theme toggle
        light_theme_label = Label(text="Light Theme", color=(1, 1, 1, 1), font_size=18)  # Label for Light Theme
        light_theme_switch = Switch()  # Create a switch for toggling Light Theme
        light_theme_switch.bind(active=lambda instance, value: self.toggle_theme("Light Theme", value))  # Bind toggle action
        layout.add_widget(light_theme_label)  # Add the Light Theme label to the layout
        layout.add_widget(light_theme_switch)  # Add the Light Theme toggle to the layout

        # Dark Theme toggle
        dark_theme_label = Label(text="Dark Theme", color=(1, 1, 1, 1), font_size=18)  # Label for Dark Theme
        dark_theme_switch = Switch()  # Create a switch for toggling Dark Theme
        dark_theme_switch.bind(active=lambda instance, value: self.toggle_theme("Dark Theme", value))  # Bind toggle action
        layout.add_widget(dark_theme_label)  # Add the Dark Theme label to the layout
        layout.add_widget(dark_theme_switch)  # Add the Dark Theme toggle to the layout

        # Back button to return to the Settings screen
        back_button = Button(text="Back", size_hint=(1, 0.2), background_color=(1, 0.3, 0.3, 1))  # Create a "Back" button
        back_button.bind(on_press=lambda x: (speak("Back"), setattr(self.manager, 'current', 'settings')))  # Return to Settings
        layout.add_widget(back_button)  # Add the back button to the layout
        self.add_widget(layout)  # Add the layout to the screen

    # Method to handle theme toggles
    def toggle_theme(self, theme_name, is_active):
        if is_active:  # If the toggle is active, speak that the theme is activated
            speak(f"{theme_name} activated")
        else:  # If the toggle is not active, speak that the theme is deactivated
            speak(f"{theme_name} deactivated")

# Placeholder Volume Screen Class
class VolumeScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Initialize the parent class (Screen)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)  # Create a vertical layout
        label = Label(text="Volume Settings", color=(1, 1, 1, 1), font_size=24)  # Add a label for Volume Settings
        layout.add_widget(label)  # Add the label to the layout
        back_button = Button(text="Back", size_hint=(1, 0.2), background_color=(1, 0.3, 0.3, 1))  # Create a "Back" button
        back_button.bind(on_press=lambda x: (speak("Back"), setattr(self.manager, 'current', 'settings')))  # Return to Settings
        layout.add_widget(back_button)  # Add the back button to the layout
        self.add_widget(layout)  # Add the layout to the screen

# Main App Class
class MyApp(App):
    def build(self):
        sm = ScreenManager()  # Create a ScreenManager to handle multiple screens
        sm.add_widget(WelcomeScreen(name="welcome"))  # Add the Welcome screen
        sm.add_widget(MenuScreen(name="menu"))  # Add the Menu screen
        sm.add_widget(SettingsScreen(name="settings"))  # Add the Settings screen
        sm.add_widget(DisplayScreen(name="display"))  # Add the Display screen
        sm.add_widget(VolumeScreen(name="volume"))  # Add the Volume screen
        return sm  # Return the ScreenManager as the root widget

# Run the application
if __name__ == "__main__":
    MyApp().run()  # Start the Kivy application
