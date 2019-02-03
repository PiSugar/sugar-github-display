![Demo](https://raw.githubusercontent.com/PiSugar/sugar-github-display/master/demo.jpg)

## sugar-github-display

跟踪显示github项目数据的小Demo。每10秒钟会刷新一次数据。

硬件: Raspberry Pi 0W + Waveshare 1.3inch_LCD_HAT + PiSugar 900mah。

在运行demo前，请先安装屏幕相关软件，请参考： https://gist.github.com/JdaieLin/9c38e0cc4c57247db505d8577d1bda79

运行Demo：

```
git clone https://github.com/PiSugar/sugar-github-display.git
cd sugar-github-display

# 按照项目url开启跟踪显示
sudo python3 main.py https://github.com/PiSugar/sugar-github-display

```
