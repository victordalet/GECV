import pyautogui


class GoogleEarth:

    @staticmethod
    def launch():
        pyautogui.hotkey('win', 's')
        pyautogui.write('google earth')
        pyautogui.sleep(1)
        pyautogui.press('enter')
        pyautogui.sleep(10)

    @staticmethod
    def zoom_in(index: int):
        for i in range(index):
            pyautogui.press('=')

    @staticmethod
    def zoom_out(index: int):
        for i in range(index):
            pyautogui.press('-')

    @staticmethod
    def move_up(index: int):
        for i in range(index):
            pyautogui.press('up')

    @staticmethod
    def move_down(index: int):
        for i in range(index):
            pyautogui.press('down')

    @staticmethod
    def move_left(index: int):
        for i in range(index):
            pyautogui.press('left')

    @staticmethod
    def move_right(index: int):
        for i in range(index):
            pyautogui.press('right')

    @staticmethod
    def full_screen():
        pyautogui.hotkey('fn', 'f11')
        pyautogui.sleep(1)

    @staticmethod
    def screenshot(path: str):
        screenshot = pyautogui.screenshot()
        screenshot.save(path)
