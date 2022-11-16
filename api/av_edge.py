import telnetlib
import time

# POWERS GAMING WALL ON
def GameRoomPowerOn(request):
    HOST = "10.128.0.20"
    tn = telnetlib.Telnet(HOST, 24)
    grtv1 = "config set device cec poweron GAMERM_TV1" 
    grtv2 = "config set device cec poweron GAMERM_TV2" 
    grtv3 = "config set device cec poweron GAMERM_TV3" 
    grtv4 = "config set device cec poweron GAMERM_TV4" 
    print("Successfully connected to %s" % HOST)
    tn.write(grtv1.encode('ascii') + b"\r\n")
    time.sleep(10)
    tn.write(grtv2.encode('ascii') + b"\r\n")
    time.sleep(10)
    tn.write(grtv3.encode('ascii') + b"\r\n")
    time.sleep(10)
    tn.write(grtv4.encode('ascii') + b"\r\n")
    time.sleep(10)
    print("Power on Command Sent to Gaming Wall")
    print("Closing telnet session")
    tn.close()


# POWERS GAMING WALL OFF
def GameRoomPowerOff(request):
    HOST = "10.128.0.20"
    tn = telnetlib.Telnet(HOST, 24)
    grtv1 = "config set device cec poweroff GAMERM_TV1" 
    grtv2 = "config set device cec poweroff GAMERM_TV2" 
    grtv3 = "config set device cec poweroff GAMERM_TV3" 
    grtv4 = "config set device cec poweroff GAMERM_TV4" 
    print("Successfully connected to %s" % HOST)
    tn.write(grtv1.encode('ascii') + b"\r\n")
    time.sleep(10)
    tn.write(grtv2.encode('ascii') + b"\r\n")
    time.sleep(10)
    tn.write(grtv3.encode('ascii') + b"\r\n")
    time.sleep(10)
    tn.write(grtv4.encode('ascii') + b"\r\n")
    time.sleep(10)
    print("Power off Command Sent to Gaming Wall")
    print("Closing telnet session")
    tn.close()    

# VOLUME UP GAMING WALL
def GameRoomVolumeUp(request):
    HOST = "10.128.0.20"
    tn = telnetlib.Telnet(HOST, 24)
    grtv1 = "config set device rs232 1 kf 00 09 \r GAMERM_TV1" 
    grtv2 = "config set device rs232 1 kf 00 09 \r GAMERM_TV2" 
    grtv3 = "config set device rs232 1 kf 00 09 \r GAMERM_TV3" 
    grtv4 = "config set device rs232 1 kf 00 09 \r GAMERM_TV4" 
    print("Successfully connected to %s" % HOST)
    tn.write(grtv1.encode('ascii') + b"\r\n")
    time.sleep(10)
    tn.write(grtv2.encode('ascii') + b"\r\n")
    time.sleep(10)
    tn.write(grtv3.encode('ascii') + b"\r\n")
    time.sleep(10)
    tn.write(grtv4.encode('ascii') + b"\r\n")
    time.sleep(10)
    print("Volume Command Sent to Gaming Wall")
    print("Closing telnet session")
    tn.close()    


# VOLUME DOWN GAMING WALL
def GameRoomVolumeDown(request):
    HOST = "10.128.0.20"
    tn = telnetlib.Telnet(HOST, 24)
    grtv1 = "config set device rs232 1 kf 00 00 \r GAMERM_TV1" 
    grtv2 = "config set device rs232 1 kf 00 00 \r GAMERM_TV2" 
    grtv3 = "config set device rs232 1 kf 00 00 \r GAMERM_TV3" 
    grtv4 = "config set device rs232 1 kf 00 00 \r GAMERM_TV4" 
    print("Successfully connected to %s" % HOST)
    tn.write(grtv1.encode('ascii') + b"\r\n")
    time.sleep(10)
    tn.write(grtv2.encode('ascii') + b"\r\n")
    time.sleep(10)
    tn.write(grtv3.encode('ascii') + b"\r\n")
    time.sleep(10)
    tn.write(grtv4.encode('ascii') + b"\r\n")
    time.sleep(10)
    print("Volume Command Sent to Gaming Wall")
    print("Closing telnet session")
    tn.close()       