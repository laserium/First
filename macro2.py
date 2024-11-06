import pyautogui
import mouse
import time

time.sleep(2)

def perform_action():
    # F2 키 누르기
    pyautogui.press('F2')

    # 잠시 대기
    time.sleep(1)

    # 마우스 왼쪽 버튼 클릭
    mouse.click('left')


# F2 키와 마우스 클릭을 수행하는 함수 호출
perform_action()
