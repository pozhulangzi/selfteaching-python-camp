text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

#1、将字符串text里的better全部换成worse
text1=text.replace("better","worse")


#2、随后，将字符串text1里单词中包含ea的单词剔除
text2_list=text1.split()

for i in text2_list:
        while i.find("ea")==-1:
               break
        else:
              text2_list.remove(i)

text3=" ".join(text2_list)


#将字符串字母大小写翻转
text4=text3.swapcase()


#将所有单词按a...z升序排列，并输出结果
# 思路:
# *先将字符串里的特殊字符去除，（其实是我多虑了，并不需要这一步，花了一上午去了解去除字符串也是醉了）(算了一下，还是有必要去除几个特殊字符)
# 然后再拆分转换为列表，（.splist）
# *再用sorted函数来头字母升序处理，
# 最后合并为字符串，(.join)
# 输出结果。
import re
text4=re.sub('[*,-]','',text4)
text5_list=text4.split()
text5_list=sorted(text5_list)
text5=" ".join(text5_list)
print(text5)