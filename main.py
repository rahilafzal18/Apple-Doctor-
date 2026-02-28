import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
import google.generativeai as genai

# --- API CONFIGURATION ---
API_KEY = "AIzaSyBpu2OteQAg3wPd9lrCM1GDLDpx3gLMMqw"
genai.configure(api_key=API_KEY)

class AppleDoctor(App):
    def build(self):
        # Developer ka naam app title mein
        self.title = "Developer Rahil Afzal - Apple Doctor"
        
        layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # App Header
        layout.add_widget(Label(text="APPLE DOCTOR", font_size='30sp', bold=True))
        layout.add_widget(Label(text="Developer: Rahil Afzal", font_size='15sp', color=(0, 1, 0, 1)))
        
        # Display Area
        self.result_label = Label(
            text="Kashmir Apple Variety & Pesticide Guide\nPress button to Scan",
            halign="center"
        )
        layout.add_widget(self.result_label)
        
        # Button
        btn_scan = Button(text="[ START SCAN ]", size_hint=(1, 0.2), background_color=(0.1, 0.8, 0.1, 1))
        btn_scan.bind(on_press=self.run_analysis)
        layout.add_widget(btn_scan)
        
        return layout

    def run_analysis(self, instance):
        self.result_label.text = "AI is Analyzing Apple Variety...\nChecking Pesticide Dose..."
        # Sample AI result for testing
        self.result_label.text = "Variety: Ambri (Kashmir)\nDisease: Apple Scab\nPesticide: Mancozeb\nDose: 2g per 1 Litre"

if __name__ == "__main__":
    AppleDoctor().run()
