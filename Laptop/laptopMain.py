import time
import pygame
# from Control import *
# import Control.ShowScreen

# class ErrorDefinitionExample(Exception):    # Exception을 상속받아서 새로운 예외를 만듦
#     def __init__(self):
#         super().__init__('3의 배수가 아닙니다.')
def ConvertYesNo(str):
    if str == 'y' or str == 'yes' or str == 'Y' or str == 'Yes' or str == 'YES':
        return 1
    elif str == 'n' or str == 'no' or str == 'N' or str == 'No' or str == 'NO':
        return 0
    else:
        return 2

def LaptopMain():
    while True:
        tmpStr = ConvertYesNo(input("Start Drone Controlling (y/n)? "))
        if tmpStr == 1:
            print("Wait.. Start Searching Drone Connection") # connection to companion computer
            
            while True:
                connectingStatus = 0
                timeStart = time.time()
                
                while True:
                    time.sleep(1.0)
                    # Here You need to make codes for connecting protocal
                    # Here You need to make codes for connecting protocal
                    # Here You need to make codes for connecting protocal
                    # Here You need to make codes for connecting protocal
                    # Here You need to make codes for connecting protocal
                    # Here You need to make codes for connecting protocal
                    # Here You need to make codes for connecting protocal
                    # Here You need to make codes for connecting protocal
                    # Here You need to make codes for connecting protocal
                    connectingStatus = int(input("connectingStatus: ")) # Drone connecting module
                    
                    if connectingStatus != 0:
                        print("Drone Connected!")
                        print(f"Drone Connection Mode : {connectingStatus}")
                        # Here You need to make codes for connection Info
                        # Here You need to make codes for connection Info
                        # Here You need to make codes for connection Info
                        # Here You need to make codes for connection Info
                        # Here You need to make codes for connection Info
                        break
                    
                    if(time.time() > timeStart + 25.0): # If 10 seconds exceed then return to First State 
                        print("Connection Failed")
                        connectingStatus = 0
                        break
                    
                while connectingStatus != 0:  # on Connecting Status under codes will be operated
                    tmpStr = ConvertYesNo(input("start program(Y)? Or Quit Program(N)?"))
                    if tmpStr == 1:
                        pygame.init()
                        screenWidth = 1920
                        screenHeight = 1080
                        screen = pygame.display.set_mode((screenWidth, screenHeight))
                        # background
                        background = pygame.image.load(r".\Laptop\Resource\background.jpg")
                        rect1 = pygame.image.load(r".\Laptop\Resource\rect.png")
                        rect1Size = rect1.get_rect().size
                        rect1Width = rect1Size[0]
                        rect1Height = rect1Size[1]
                        rect1xPos = (screenWidth - rect1Width)/2
                        rect1yPos = screenHeight - rect1Height
                        
                        pygame.display.set_caption("Drone Flight Controller")
                        running = True
                        while running:
                            for event in pygame.event.get():
                                if event.type == pygame.QUIT:
                                    running = False
                                    print()
                            screen.blit(background, (0, 0)) # background Drawing
                            screen.blit(rect1, (rect1xPos, rect1yPos))
                            pygame.display.update()
                        pygame.quit()
                    elif tmpStr == 0:
                        break
                    else: print("You Entered Wrong command")
                    # Here You need to make codes for control signal, monitoring, receiving
                    # Here You need to make codes for control signal, monitoring, receiving
                    # Here You need to make codes for control signal, monitoring, receiving
                    # Here You need to make codes for control signal, monitoring, receiving
                    # Here You need to make codes for control signal, monitoring, receiving
                    # Here You need to make codes for control signal, monitoring, receiving
                    # Here You need to make codes for control signal, monitoring, receiving
                    # Here You need to make codes for control signal, monitoring, receiving
                    # Here You need to make codes for control signal, monitoring, receiving
                while True:
                    tmpStr = ConvertYesNo(input("ReFind Connection (y/n)?"))
                    if tmpStr == 1:
                        print("Searching Drone Connection")
                        break;
                    elif tmpStr == 0: break
                    else: print("You Entered Wrong command")
                if tmpStr != 1: break
        elif tmpStr == 0:
            print("Program Exit")
            break
        else: print("You Entered Wrong command")
LaptopMain()