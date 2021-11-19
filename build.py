from fontmake import __main__
from fontTools.ttLib import TTFont, newTable
import shutil

__main__.main(("-g","source/DarumadropOne.glyphs", "-o","ttf",))

path = "master_ttf/DarumadropOne-Regular.ttf"


modifiedFont = TTFont(path)
print ("Adding additional tables")
modifiedFont["DSIG"] = newTable("DSIG")     #need that stub dsig

print ("Making other changes")
modifiedFont["DSIG"].ulVersion = 1
modifiedFont["DSIG"].usFlag = 0
modifiedFont["DSIG"].usNumSigs = 0
modifiedFont["DSIG"].signatureRecords = []
modifiedFont["gasp"] = newTable("gasp")
modifiedFont["gasp"].gaspRange = {65535: 0x000A} #Font is shipping UNHINTED :D

modifiedFont.save("fonts/ttf/DarumadropOne-Regular.ttf")

shutil.rmtree("instance_ufo")
shutil.rmtree("master_ufo")
shutil.rmtree("master_ttf")