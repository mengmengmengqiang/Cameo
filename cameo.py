import cv2
from managers import WindowManager, CaptureManager


class Cameo(object):
    def __init__(self, windowName='Cameo'):
        self._windowManager = WindowManager(windowName, self.onKeypress)
        self._captureManager = CaptureManager(cv2.VideoCapture(0),
                                              self._windowManager,
                                              True)
        self._pictureNumber: int = 0
        self._videoNumber: int = 0

    def run(self):
        """Run the main loop.
        :rtype: object
        """

        # print the key-operation
        print("Press space  to take a screenshot\n" +
              "      escape to quit\n" +
              "      tab    to start/stop recording a screencast\n")
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame

            # TODO: Filter the frame (Chapter3).

            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keycode):
        """ Handle a keypress

        space       ->    Take a screenshot.
        tab         ->    Start/stop recording a screencast.
        escape      ->    Quit.

        """
        if keycode == 32:  # space
            self._pictureNumber += 1
            print("Take a screenshot named screenshot" + str(self._pictureNumber) + ".png\n")

            self._captureManager.writeImage('screenshot' + str(self._pictureNumber) + ".png")
        elif keycode == 9:  # tab
            if not self._captureManager.isWritingVideo:
                self._videoNumber += 1
                print("Start recording a screencast...\n")

                self._captureManager.startWritingVideo('screencast' + str(self._videoNumber) + ".avi")
            else:
                self._captureManager.stopWritingVideo()
                print("Stop recording a screencast... \n" +
                      "screencast" + str(self._videoNumber) + ".avi saved.\n")
        elif keycode == 27:  # escape
            print("Quit.\n")
            self._windowManager.destroyWindow()
