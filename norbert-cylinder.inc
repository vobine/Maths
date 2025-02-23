#macro Make_Cylinder(rot, col)
  cylinder {
    <-2, 0, 0>
    <2, 0, 0>
    1.0
    rotate rot
    texture {
      pigment {col}
    }
  }
#end
