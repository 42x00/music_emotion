import jacinle.io
import html
import re
import pandas as pd

tmp = jacinle.io.load('/Users/ykli/Downloads/tmp.txt')
tmp = ' '.join(tmp)
tmp = html.unescape(tmp)

pattern = re.compile(
    r'<div id.*?color: (.*?); top: (.*?)px; left: (.*?)px.*?playx\("(.*?)", "(.*?)", "(.*?)",(.*?), this.*?open\("(.*?)"')
tmp = pattern.findall(tmp)

pd.DataFrame(tmp[:1841]).to_csv('tmp.csv', index=False)
