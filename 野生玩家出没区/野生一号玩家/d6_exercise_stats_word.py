######################从字符串中统计英文单词词频的函数：######################
def stats_text_en(text):
                        import re
                        text_stats=re.sub("[~!@#$%^&*-+]"," ",text)          #去除标点

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
                        text_stats=re.sub("[\n，。、？！~@#￥%……&*（）——+-=：《》；“”‘’；/]"," ",text)          
                        
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

