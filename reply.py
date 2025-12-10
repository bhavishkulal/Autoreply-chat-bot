import pyautogui
import time
import pyperclip

def send_whatsapp_message(message):
    time.sleep(1)

  
  
    # === 2. Click inside message typing bar ===
    # Replace this with your typing bar coordinates
    typing_x, typing_y = 1030, 949   
    pyautogui.moveTo(typing_x, typing_y, duration=0.4)
    pyautogui.click()

    # === 3. Paste the message ===
    pyperclip.copy(message)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.3)

    # === 4. Click Send Button ===
    # Replace this with your send button coordinates
    send_x, send_y = 1852, 936     
    pyautogui.moveTo(send_x, send_y, duration=0.4)
    pyautogui.click()

    print("\n[✓] Message sent on WhatsApp")

