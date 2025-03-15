#include "colors.inc"
#include "norbert-cylinder.inc"
#include "norbert-lights-camera.inc"

intersection {
  union {
    Make_Cylinder(<0, 0, 0>, Yellow)
  }

  box {
    <-2, -2, -2>
    <2, 0.75, 2>
    texture {
      pigment {color SkyBlue}
    }
  }
}
