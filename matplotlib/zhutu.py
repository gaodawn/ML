 # 导入绘图模块
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
  # 构建数据
GDP = [12406.8,13908.57,9386.87,9143.64]
  # 中文乱码的处理
font=FontProperties(fname="/System/Library/Fonts/STHeiti Light.ttc",size=14)
#plt.rc('font',family=['‘STHeiti Light']) 
plt.rcParams['axes.unicode_minus'] = False
  # 绘图
plt.bar(range(4), GDP, align = 'center',color='steelblue', alpha = 0.8)
  # 添加轴标签
plt.ylabel('GDP')
  # 添加标题
plt.title('四个直辖市GDP大比拼',FontProperties=font)
  # 添加刻度标签
plt.xticks(range(4),['北京市','上海市','天津市','重庆市'],FontProperties=font)
  # 设置Y轴的刻度范围
plt.ylim([5000,15000])
  # 为每个条形图添加数值标签
for x,y in enumerate(GDP):
    plt.text(x,y+100,'%s' %round(y,1),ha='center')

  # 显示图形
plt.show()
