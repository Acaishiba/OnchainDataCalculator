import math
import sys

print("请选择要输入的参数类型：")
print("1. 以左边LP-reserve0计算")
print("2. 以右边LP-reserve1计算")


choice = input("请输入选项编号：")

reserve0 = input("LP-reserve0的代币名称是")
reserve1 = input("LP-reserve1的代币名称是")

if choice == "1":
    a = float(input("The amount of reserve0 you want to deposit is："))
    print("The deposited reserve0=：", a,reserve0)
    p = float(input("初始价格 is："))
    f = float(input("格子上限 is："))
    g = float(input("格子下限 is："))

    tempVx = a / (1 - math.sqrt(p / f))
    tempVy = p * tempVx

    b = tempVx * (p - math.sqrt(p * g))

    print("虚拟reserve0为",tempVx,reserve0)
    print("虚拟reserve1为",tempVy,reserve1)
    print("需要投入的LP-reserve1为",b,reserve1) 
elif choice == "2":
    b = float(input("The amount of reserve1 you want to deposit is："))
    print("The deposited reserve1=：", b,reserve1)
    p = float(input("初始价格 is："))
    f = float(input("格子上限 is："))
    g = float(input("格子下限 is："))

    tempVx = b / (p - math.sqrt( p * g ))
    tempVy = p * tempVx

    a = tempVx * (1 - math.sqrt( p / f ))

    print("虚拟reserve0为",tempVx,reserve0)
    print("虚拟reserve1为",tempVy,reserve1)
    print("需要投入的LP-reserve0为",a,reserve0) 
else:
    print("无效选项！请重新运行程序并输入正确的选项编号。")
    sys.exit()



k = p * tempVx * tempVx 

print("是否进行无常损失计算：")
print("1. 是")
print("2. 否")

choice = input("请输入选项编号：")

if choice == "1":
    pm = float(input("预计算的价格为："))
    am = a + math.sqrt(k / pm ) - tempVx
    bm = b + math.sqrt(pm * k ) - p * tempVx
    loss = am * pm + bm - a * pm - b
    print("无常损失为", loss,reserve1)
elif choice == "2":
    print("exit")

