import pyautogui
import time


class PyAutoGUIController:
    def __init__(self):
        self.screen_width, self.screen_height = pyautogui.size()
        self.mouse_position = (0, 0)
        self.language = "EN"

    def click(self, x, y):
        pyautogui.click(x, y)

    def double_click(self, x, y):
        pyautogui.doubleClick(x, y)

    def right_click(self, x, y):
        pyautogui.rightClick(x, y)

    def type_text(self, text):
        pyautogui.typewrite(text)

    def press_key(self, key):
        pyautogui.press(key)

    def hold_key(self, key):
        pyautogui.keyDown(key)

    def release_key(self, key):
        pyautogui.keyUp(key)

    def press_combo(self, key1, key2):
        pyautogui.keyDown(key1)
        pyautogui.press(key2)
        pyautogui.keyUp(key1)
        time.sleep(1)

    def open_programm(self, programm_name):
        pyautogui.press('win')
        time.sleep(0.5)
        pyautogui.typewrite('outlook')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(5)

    def write_email(self, recipient, subject, body):

        # Open email program
        self.open_programm("outlook")
        time.sleep(2)

        # Click New Email button
        self.press_combo("ctrl", "n")
        time.sleep(1)

        # Type recipient                
        self.type_text(recipient)
        time.sleep(0.5)
        self.press_key('tab')
        self.press_key('tab')
        self.press_key('tab')

        # Type subject
        self.type_text(subject)
        self.press_key('tab')

        # Type body
        if self.language == "EN":
            self.type_text("Kind regards\n Jan-Niklas Dohrke")
        elif self.language == "DE":
            self.type_text("Hallo")
            self.press_key("enter")
            self.press_key("enter")
            self.type_text(body)
            self.press_key("enter")
            self.press_key("enter")
            self.type_text("Mit freundlichen Gruessen")
            self.press_key("enter")
            self.type_text("Jan-Niklas Dohrke")

    def order_primer(self, order_file="", recipient="Sylvia", subject="Primerbestellung", ):
        body = "Anbei eine neue Primerbestellung."
        self.language = "DE"
        self.write_email(recipient, subject, body)
        # self.add_attachment(orderfile)
        self.language = "EN"


if __name__ == "__main__":
    controller = PyAutoGUIController()
    controller.order_primer()
