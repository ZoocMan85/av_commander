from django.shortcuts import render
from api.av_edge import GameRoomPowerOn, GameRoomPowerOff, GameRoomVolumeUp, GameRoomVolumeDown

def power_on(request):
     GameRoomPowerOn(request)
     print("Command Executed")
     return render(request, 'api/power_on.html')

def power_off(request):
     GameRoomPowerOff(request)
     print("Command Executed")
     return render(request, 'api/power_off.html')     

def volume_up(request):
     GameRoomVolumeUp(request)
     print("Command Executed")
     return render(request, 'api/volume_up.html')        

def volume_down(request):
     GameRoomVolumeDown(request)
     print("Command Executed")
     return render(request, 'api/volume_down.html')        
