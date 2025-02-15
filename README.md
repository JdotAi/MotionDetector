# MotionDetector 🕵🏼‍♂️
A simple motion detector that shows movement through color differences. To do this we have to think about the essence of what a motion detector is: it understands what happened in the past and compares it to what it knows now. The program copies the last frame and overlays it with an inverted version - when you mix two inverted colors you get gray. So when the frames match it will be grey, and when there's movement or the colors don't line up, you'll see the original color.

## Quick Start
```bash
pip install opencv-python numpy
python motion_detector.py
```

Press 'q' to quit.
