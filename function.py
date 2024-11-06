# import time
# import pyautogui
# import cv2
# from PIL import Image

# icon_path = 'D:\\test_dir\\find.png'
# save_path = 'D:\\test_dir\\find1.png'
# # 获取屏幕尺寸
# screen_size = pyautogui.size()
# width, height = screen_size.width, screen_size.height
# print(f"屏幕宽度: {width}, 屏幕高度: {height}")

# time.sleep(5)

# #获取当前鼠标的位置并点击
# x,y = pyautogui.position()   
# posStr = "Position:" + str(x).rjust(4)+','+str(y).rjust(4)
# print(x, y)

# pyautogui.click(x, y)


# 图标查找缩放比例问题

# # # 在屏幕上查找图标
# icon_location = pyautogui.locateOnScreen(save_path)

# if icon_location:
#     print(f"图标位置: {icon_location}")  # 输出图标的坐标和大小 (left, top, width, height)
    
#     # 获取图标的中心坐标
#     center_x, center_y = pyautogui.center(icon_location)
#     print(f"图标中心坐标: ({center_x}, {center_y})")
# else:
#     print("未找到图标！")







# -*- coding: utf-8 -*-
import time
import pyautogui
import pyscreeze
import logging as log
import cv2
import os

# 屏幕缩放系数，mac系统通常为2，Windows一般为1
screen_scale = 1

# 保存的软件图标路径和输出截屏文件路径
button_path = 'D:\\test_dir\\find.png'
output_path = 'D:\\test_dir\\output.png'
log_ouput_path = 'D:\\test_dir\\info.log'

# 配置 logging
log.basicConfig(
    filename=log_ouput_path,  # 指定日志文件名
    level=log.INFO,       # 设置日志级别
    filemode='w',
    format='-- %(asctime)s - %(levelname)s - %(message)s'  # 日志格式
)

def capture_and_compare_software_images():
    """截取屏幕并与目标图标进行匹配，若匹配则执行点击操作。"""
    # 检查图标文件是否存在
    if not os.path.exists(button_path):
        log.error(f"图标文件不存在: {button_path}")
        return

    # 读取目标图标
    target = cv2.imread(button_path, cv2.IMREAD_GRAYSCALE)
    if target is None:
        log.error("无法读取目标图标，可能文件损坏或格式不支持。")
        return

    # 截取屏幕并读取截屏图像
    pyscreeze.screenshot(output_path)
    temp = cv2.imread(output_path, cv2.IMREAD_GRAYSCALE)
    if temp is None:
        log.error("无法读取截屏图像，可能截屏失败。")
        return

    # 获取目标图标和截屏图像的尺寸
    theight, twidth = target.shape[:2]
    tempheight, tempwidth = temp.shape[:2]
    log.info(f"目标图标宽高: {twidth}x{theight}")
    log.info(f"截屏图像宽高: {tempwidth}x{tempheight}")

    # 缩放截屏图像
    scale_temp = cv2.resize(temp, (int(tempwidth / screen_scale), int(tempheight / screen_scale)))
    stempheight, stempwidth = scale_temp.shape[:2]
    log.info(f"缩放后截屏图像宽高: {stempwidth}x{stempheight}")

    # 匹配图标
    res = cv2.matchTemplate(scale_temp, target, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)

    # 如果匹配度足够高，则执行点击
    if max_val >= 0.60:
        # 计算点击位置
        top_left = max_loc
        tag_center_x = top_left[0] + twidth // 2
        tag_center_y = top_left[1] + theight // 2
        log.info(f"找到图标，点击位置: ({tag_center_x}, {tag_center_y})")
        pyautogui.click(tag_center_x, tag_center_y, button='left')
        log.info(f"x = {tag_center_x}, y = {tag_center_y}")
    else:
        log.error("未找到目标图标。".encode("utf-8"))

if __name__ == "__main__":
    capture_and_compare_software_images()
