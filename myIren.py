
from vtk import vtkInteractorStyleTrackballCamera
from PySide2.QtWidgets import QCheckBox
import vtk

Rotating = 0
Panning = 0
Zooming = 0
class myIren(vtkInteractorStyleTrackballCamera ):
    def __init__(self, ren , iren):
        self.renWin = ren.GetRenderWindow()
        self.iren = iren
        self.ren =ren
        self.Rotating = 0
        self.Panning = 0
        self.Zooming = 0
        self.AddObserver( "LeftButtonPressEvent", self._buttonEvent )
        self.AddObserver( "LeftButtonReleaseEvent", self._buttonEvent )
        self.AddObserver( "MiddleButtonPressEvent", self._buttonEvent )
        self.AddObserver( "MiddleButtonReleaseEvent", self._buttonEvent )
        self.AddObserver( "RightButtonPressEvent", self._buttonEvent )
        self.AddObserver( "RightButtonReleaseEvent", self._buttonEvent )
        # self.AddObserver("MiddleButtonPressEvent",self.ButtonEvent)
        # self.AddObserver("MiddleButtonReleaseEvent",self.ButtonEvent)
        self.AddObserver( "MouseMoveEvent", self._mouseMove )

    def _middleButtonPressEvent(self,obj,event):
        print("Middle Button pressed")
        self.OnMiddleButtonDown()
        return

    def _middleButtonReleaseEvent(self,obj,event):
        print("Middle Button released")
        self.OnMiddleButtonUp()
        return
    def _buttonEvent(self, obj, event) :
        # global Rotating, Panning, Zooming
        if event == "LeftButtonPressEvent":
            self.Rotating = 1
            #print(self)
        elif event == "LeftButtonReleaseEvent":
            self.Rotating = 0

        elif event == "MiddleButtonPressEvent":
            self.Panning = 1
        elif event == "MiddleButtonReleaseEvent":
            self.Panning = 0

        elif event == "RightButtonPressEvent":
            self.Zooming = 1
        elif event == "RightButtonReleaseEvent":
            self.Zooming = 0

    def _mouseMove(self, obj,  event) :
        # global Rotating, Panning, Zooming
        # global self.iren, self.renWin, self.ren
        lastXYpos = self.iren.GetLastEventPosition()
        lastX = lastXYpos[0]
        lastY = lastXYpos[1]

        xypos = self.iren.GetEventPosition()
        x = xypos[0]
        y = xypos[1]

        center = self.renWin.GetSize()
        centerX = center[0] / 2.0
        centerY = center[1] / 2.0

        if self.Rotating :
            self._rotate( self.ren, self.ren.GetActiveCamera(), x, y, lastX, lastY,
                         centerX, centerY )
        elif self.Panning :
            self._pan( self.ren, self.ren.GetActiveCamera(), x, y, lastX, lastY, centerX,
                      centerY )
        elif self.Zooming :
            self._dolly( self.ren, self.ren.GetActiveCamera(), x, y, lastX, lastY,
                        centerX, centerY )

    def _rotate(self, renn, camera, x, y, lastX, lastY, centerX, centerY) :
        # self.ren.ResetCamera()
        camera.Azimuth( (lastX - x) * 0.4)
        # camera.Elevation(lastY-y)
        camera.OrthogonalizeViewUp()
        self.renWin.Render()
    def _pan(self, ren, camera, x, y, lastX, lastY, centerX, centerY) :
        camera.Elevation( (lastY - y) * 0.1)
        self.renWin.Render()

    def _dolly(self, ren, camera, x, y, lastX, lastY, centerX, centerY) :
        dollyFactor = pow( 1.02, (0.1 * (y - lastY)) )
        if camera.GetParallelProjection():
            parallelScale = camera.GetParallelScale() * dollyFactor
            camera.SetParallelScale( parallelScale )
        else :
            camera.Dolly( dollyFactor)
            self.ResetCameraClippingRange()
        self.renWin.Render()

