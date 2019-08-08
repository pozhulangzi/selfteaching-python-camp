######################从字符串中统计英文单词词频的函数：######################
def stats_text_en(text):
                        import re
                        text_stats=re.sub("[~!@#$%^&*-+\n]"," ",text)          #去除标点

                        text_stats=text_stats.replace("'s"," is").replace("'t"," it").replace("'re"," are").replace("n't"," not")      #转换缩写单词


                        text_stats=text_stats.split()                      #转字符串为列表  


                        text_dict={}
                        for i in text_stats:
                                   if i in text_dict.keys():
                                       text_dict[i] += 1
                                   else:
                                       text_dict[i] = 1                     #统计词频          

                        T=sorted(text_dict.items(),key=lambda x: x[1],reverse=True)
                        
                        return  T                                       #按照词频排序并输出结果



######################从字符串中统计中文汉字词频的函数：######################
def stats_text_cn(text):
                        import re
                        text_stats=re.sub(r"[\n，。、？！~@#￥%……&*（）——+-=：《》；“”‘’；/【】「」]"," ",text)          
                        
                        text_stats=text_stats.replace(" ","").replace("/n","")       #去除标点,空格和换行符.replace()
                                                                                 
                        text_stats_list=[] 
                        for i in text_stats:
                                    text_stats_list.append(i)                      #转字符串为列表

                        text_dict={}
                        for i in text_stats_list:
                                   if i in text_dict.keys():
                                       text_dict[i] += 1
                                   else:
                                       text_dict[i] = 1                     #统计词频          

                        T=sorted(text_dict.items(),key=lambda x: x[1],reverse=True)
                        
                        return  T                                       #按照词频排序并输出结果


############################################################################
#######################合并两个函数使之能分别为一个中英文本字符串导出统计结果：################
#############定义函数，判断中英字符开始的位置
###########4种情况分割字符串#############调用函数，合并结果############
def stats_text(text):                           
            for s in text:
                if s>=u'\u4e00' and s<=u'\u9fa5':
                           a=text.find(s)
                elif s>=u'\u0041' and s<=u'\u007a':
                           b=text.find(s)
            
            if   a<b:
                zw=text[:a+1]
                yw=text[a+1:b+1]
            elif b<a:
                yw=text[:b+1]
                zw=text[b+1:a+1]
                     
            print(stats_text_cn(zw),"wuhuakeshuo",tats_text_en(yw))
            return 
