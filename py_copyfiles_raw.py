import sys
import os

import shutil

#from PyQt4.QtGui import *
#from PyQt4.QtCore import *
#from PyQt5.QtGui import *
#from PyQt5.QtCore import *
#from PyQt5.QtWidgets import *

fld1 = 'v0424_ysw_v3update'
fld2 = 'v0452_ysw_FramePatchFrom-v0424-to-v0442'

#src = r'C:/Temp/FramePatch/RCT_089_1160/images/render 3d/Light-Env/v0424_ysw_v3update/normal_1224x852x1_linear/roger_normal_1224x852x1_linear.0003.exr'
#dst = r'C:/Temp/FramePatch/RCT_089_1160/images/render 3d/Light-Env/v0452_ysw_FramePatchFrom-v0424-to-v0442/normal_1224x852x1_linear/roger_normal_1224x852x1_linear.0003.exr'

src = 'C:/Temp/FramePatch/RCT_089_1160/images/render 3d/Light-Env/v0424_ysw_v3update/normal_1224x852x1_linear/roger_normal_1224x852x1_linear.0003.exr'
dst = 'C:/Temp/FramePatch/RCT_089_1160/images/render 3d/Light-Env/v0452_ysw_FramePatchFrom-v0424-to-v0442/normal_1224x852x1_linear/roger_normal_1224x852x1_linear.0003.exr'


raw_src = r"{}".format(src)
raw_dst = r"{}".format(dst)

print("raw_src : ", raw_src)
print("raw_src type : ", type(raw_src))

shutil.copyfile(raw_src,raw_dst)
#shutil.copyfile(src,dst)
