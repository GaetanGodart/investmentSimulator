from screeninfo import get_monitors
import ttkbootstrap as tkb
from ttkbootstrap.constants import *

root = tkb.Window(themename="darkly")
root.title("Investment simulator")

for m in get_monitors():
    if(m.is_primary):
        root.geometry(f"{m.width*0.8:.0f}x{m.height*0.8:.0f}+{m.width*0.1:.0f}+{m.height*0.1:.0f}")
        break

root.mainloop()