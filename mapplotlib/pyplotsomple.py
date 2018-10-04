
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# plt.plot([5,2,3,4],[1,4,9,20], 'ro')
# # plt.axis([],[])
# plt.ylabel('numbers')
# plt.show()

font_list = fm.findSystemFonts(fontpaths=None, fontext='ttf')

# ttf 폰트 전체 가져오기
print([(f.name, f.fname) for f in fm.fontManager.ttflist ])
