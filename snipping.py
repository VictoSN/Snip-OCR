import platform
import subprocess
from pathlib import Path
from datetime import datetime

class Snipping:
    def __init__(self):
        
        self.screenshots_folder = Path("screenshots")
    
    def screenshot(self):
        self.screenshots_folder.mkdir(exist_ok=True)
        name = "Image_" + datetime.now().strftime('%y%m%d_%H%M%S')
        output = str(self.screenshots_folder / f"{name}.png")
        
        # mss does not work in wayland
        if platform.system() == "Windows":
            import mss, mss.tools
            with mss.mss() as sct:
                monitor = sct.monitors[1]
                img = sct.grab(monitor)
                mss.tools.to_png(img.rgb, img.size, output=output)
        else:
            import subprocess
            subprocess.run(["grim", output])