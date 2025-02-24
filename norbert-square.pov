#include "colors.inc"
#include "norbert-cylinder.inc"
#include "norbert-lights-camera.inc"

intersection {
  Make_Cylinder(<0, 0, 0>, Yellow)
  Make_Cylinder(<0, 90, 0>, Green)

  box {
    <-2, -2, -2>
    <2, 0.75, 2>
    texture {
      pigment {color SkyBlue}
    }
  }
}
