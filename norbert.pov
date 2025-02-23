#include "colors.inc"
#include "textures.inc"

camera {
  location <4, 4, 4>
  look_at <0, 0, 0>
}

light_source {
  <2, 4, -3>
  color White
}

light_source {
  <2, 4, 3>
  color White
}

intersection {
  union {
    cylinder {
      <-2, 0, 0>
      <2, 0, 0>
      1.0
      texture {
        pigment {color Yellow}
      }
    }

    cylinder {
      <0, 0, -2>
      <0, 0, 2>
      1.0
      texture {
        pigment {color Green}
      }
    }
  }

  box {
    <-2, -2, -2>
    <2, 0.75, 2>
    texture {
      pigment {color Gray50}
    }
  }
}