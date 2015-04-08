# This is file starts and controls MRL InMoov 
# service and attaches it to the Blender virtual InMoov
# Blender (2.72b) must be running a Blender.py TCP/IP server file

vPortLeft = "vPortLeft"
vPortRight = "vPortRight"

###########################################################################
### special virtual blender handling - not in "regular" scripts - begin ###

# start blender service
blender = Runtime.start("blender", "Blender")

# connect blender service to running Blender (2.72b) instance
if (not blender.connect()):
	print("could not connect")

# get Blender.py version 
# FIXME - compare expected version !
blender.getVersion()

# pre-create Arduinos 
i01_left = Runtime.start("i01.left", "Arduino")
i01_right = Runtime.start("i01.right", "Arduino")

# blender "attach" will connect Arduinos with serial ports running
# over tcp/ip sockets to Blender.py
blender.attach(i01_left)
blender.attach(i01_right)

### special virtual blender handling - not in "regular" scripts - end  ###
##########################################################################

# resume "regular" script
# connect head
i01 = Runtime.start("i01", "InMoov")
i01.startHead(vPortLeft)
i01.startLeftArm(vPortLeft)

# virtual InMoov config begin ##############
jaw = Runtime.getService("i01.head.jaw")
jaw.setMinMax(0,180)
neck = Runtime.getService("i01.head.neck")
neck.setMinMax(0,720)
neck.map(0,180,340,170)
neck.moveTo(74)
# virtual InMoov config end ##############

mc = i01.startMouthControl("vPortLeft")
speech = i01.startMouth()
speech.speak("ow my neck hurts")