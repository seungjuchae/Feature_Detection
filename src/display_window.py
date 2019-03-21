import sdl2
import sdl2.ext

class Display(object):
  def __init__(self, width, height):
    sdl2.ext.init()
    
    # Config for the window
    self.width, self.height = width, height
    self.window = sdl2.ext.Window("Feature_detection", size=(width,height), position=(0,0))

    # Showing Window 
    self.window.show()

  def paint(self, img):
    # Gets every SDL events that are on event queue.
    events = sdl2.ext.get_events()
    for event in events:
      if event.type == sdl2.SDL_QUIT:
        exit(0)

    # Based on numpy.ndarray, it draw a 3D pixel array from the passed source
    surf = sdl2.ext.pixels3d(self.window.get_surface())
    surf[:, :, 0:3] = img.swapaxes(0,1)

    # blit
    self.window.refresh()