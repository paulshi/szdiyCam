# Copyright (C) 2014 SZDIY Hackers' Community
#
# This file is part of szdiyCam.
#
# szdiyCam is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# szdiyCam is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with szdiyCam.  If not, see <http://www.gnu.org/licenses/>.

from config import TMPDIRECTORY, imagePath
from SZDIYPic import SZDIYPic
from uploadToLinode import uploadAFileToLinode
from uploadToQiNiu import uploadingAFileToQiNiu
import time

def setDefaultNetworkTimeOut(timeout):
	import socket
	socket.setdefaulttimeout(timeout)

snapshot = SZDIYPic() #initialize an instance
setDefaultNetworkTimeOut(30) #set network timeout

while True:

	#takeAShot(name,width,height):
	snapshot.takeAShot('image.jpg',800,600)
	#resizeImageAndApplyWaterMark (inputFileName, outputFileName, quality)
	snapshot.resizeImageAndApplyWaterMark ('image.jpg', 'new.jpg', 80)
	uploadAFileToLinode(TMPDIRECTORY+'/'+'new.jpg')
	time.sleep(1)
	
	snapshot.takeAShot('image.jpg',2592,1944)
	snapshot.storeImg('image.jpg', TMPDIRECTORY) #this now saves the original image
	snapshot.resizeImageAndApplyWaterMark('image.jpg','new.jpg',95)
	uploadingAFileToQiNiu('szdiy','new.jpg',TMPDIRECTORY)

	time.sleep(20)


