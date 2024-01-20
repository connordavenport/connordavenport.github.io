i = '/Users/connordavenport/Downloads/Iskra Orange_files/face.svg'

newPage()

import math

#image(i,(0,0))
fs = 98
def draw_clock_face(center_x, center_y, radius):
    for i in range(12):
        angle = -math.radians((i-2)* (360 / 12))  # Calculate angle in radians
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        ff = FormattedString()
        ff.openTypeFeatures(ss02=True,ss07=True)
        ff.append(str(i + 1), fontSize=fs, font="ABCMaxiPlusVariableUnlicensedTrial-Regular", fontVariations=dict(wght=322))
        
        bb = BezierPath()
        bb.text(ff)
        with savedState():
            translate(x-(bb.bounds()[2] - bb.bounds()[0])/2,y)
            fill(58/255, 181/255, 91/255)
            drawPath(bb)
        bb.removeOverlap()
        #text(ff, (x, y), align="center")
# Call the function to draw the clock face
fontSize(fs)
draw_clock_face(495,(500-textSize("12")[0]/4),428)

saveImage(i.replace("face", "typeface"))