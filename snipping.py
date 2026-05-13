import mss, mss.tools
from pathlib import Path
from datetime import datetime

class Snipping:
    def __init__(self):
        self.screenshots_folder = Path("screenshots")
    
    def screenshot(self, x=0, y=0, w=0, h=0):
        self.screenshots_folder.mkdir(exist_ok=True)
        name = "Image_" + datetime.now().strftime('%y%m%d_%H%M%S.%f')[:-5]
        output = str(self.screenshots_folder / f"{name}.png")
        region = {
            "left": x,
            "top": y,
            "width": w,
            "height": h
        }

        with mss.mss() as sct:
            if region:
                img = sct.grab(region)
            else:
                monitor = sct.monitors[1]
                img = sct.grab(monitor)
            mss.tools.to_png(img.rgb, img.size, output=output)