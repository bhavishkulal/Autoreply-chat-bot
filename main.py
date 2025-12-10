import pyautogui
import time
import pyperclip
from client import get_reply_from_gemini


from reply import send_whatsapp_message

try:
    pyautogui.FAILSAFE = True  # Safety feature

    # === Step 1: Click on the icon at (1266, 1048) ===
    time.sleep(2)  # Time to switch to the screen
    pyautogui.click(1266, 1048)

    # === Step 2: Wait for page to load ===
    time.sleep(3)

    # === Step 3: Select text from (880, 290) to (1882, 907) ===
    start_x, start_y = 880, 290
    end_x, end_y = 1882, 907

    pyautogui.moveTo(start_x, start_y, duration=0.5)
    pyautogui.mouseDown()
    time.sleep(0.1)
    pyautogui.dragTo(end_x, end_y, duration=1.2, button="left")
    pyautogui.mouseUp()

    time.sleep(0.5)

    # === Step 4: Copy (Ctrl + C) ===
    pyautogui.hotkey("ctrl", "c")
    pyautogui.click(918, 327)
    time.sleep(0.5)

    # === Step 5: Read clipboard ===
    copied_text = pyperclip.paste()

    print("\n=== COPIED TEXT ===\n")
    print(copied_text)
    print("\n===================\n")

    reply =  get_reply_from_gemini(copied_text)



    print("\n=== GEMINI REPLY ===\n")
    print(reply)
    print("\n=====================\n")

    # === Send to WhatsApp ===
    message = reply
    send_whatsapp_message(message)

except Exception as e:
    print("\n❌ ERROR OCCURRED IN SCRIPT ❌\n")
    print(str(e))
    print("\n-----------------------------------\n")
