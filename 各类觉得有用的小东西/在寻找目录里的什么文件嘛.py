from pathlib import Path

path = Path()
#找出当前目录py后缀的文件
for file in path.glob('*.py'):
    print(file)
#所有文件
for file in path.glob('*'):
    print(file)
#前缀
for file in path.glob('速度偷师源代码.*'):
    print(file)
