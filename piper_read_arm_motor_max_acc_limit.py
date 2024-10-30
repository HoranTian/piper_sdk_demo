#!/usr/bin/env python3
# -*-coding:utf8-*-
# 注意demo无法直接运行，需要pip安装sdk后才能运行
# 读取机械臂的所有电机的最大加速度限制

from typing import (
    Optional,
)
import time
from piper_sdk import *

# 测试代码
if __name__ == "__main__":
    piper = C_PiperInterface()
    piper.ConnectPort()
    while True:
        # piper.SearchMotorMaxAngleSpdAccLimit(1,0x02)
        # piper.SearchAllMotorMaxAngleSpd()
        # piper.SearchAllMotorMaxAccLimit()
        
        # print(piper.GetCurrentMotorMaxAccLimit())
        # print(piper.GetCurrentMotorAngleLimitMaxVel())
        # print(piper.GetAllMotorAngleLimitMaxSpd())
        print(piper.GetAllMotorMaxAccLimit())
        time.sleep(0.01)