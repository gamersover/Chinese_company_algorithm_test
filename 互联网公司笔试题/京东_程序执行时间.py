#coding=UTF-8
'''
问题描述：产品经理(PM)有很多好的idea，而这些idea需要程序员实现。现在有N个PM，在某个时间会想出一个idea，每个
idea有提出时间、所需时间和优先等级。对于一个PM来说，最想要实现的idea首先考虑优先等级高的，相同的情况下优先所需
时间最小的，还相同的情况下选择最早想出的，没有PM会在同一时刻提出两个idea。
同时有M个程序员，每个程序员空闲的时候就会查看每个PM尚未执行并且最想完成的idea，然后从中挑选出所需时间最小的一个
idea实现，如果所需时间相同则选择PM序号最小的，直到完成了idea才重复上述操作。如果有多个同时处于空闲状态的程序员，
那么他们会依此进行查看idea的操作。
求每个idea实现的时间。
输入第一行三个数N,M,P分别表示有N个PM，M个程序员，P个idea。随后有P行，每行有4个数字，分别是PM序号、提出时间、
优先等级和所需时间。输出P行，分别表示每个idea实现的时间点。
例：输入：
2 2 5
1 1 1 2
1 2 1 1
1 3 2 2
2 1 1 2
2 3 5 5
输出：
3
4
5
3
9
'''
# class idea:
#     def __init__(self, pm, pro_time, prio, exe_time):
#         self.pm = pm
#         self.pro_time = pro_time
#         self.prio = prio
#         self.exe_time = exe_time
#         self.values = [self.prio,self.exe_time,self.pro_time,self.pm]
#         self.real_val = [self.pm,self.pro_time,self.prio,self.exe_time]
# 
# class code:
#     def __init__(self,time):
#         self.time = time
#     
#     def search_idea(self):
#         self.can_idea = []
#         for i in range(len(Idea)):
#             if Idea[i].pro_time <= self.time:
#                 self.can_idea.append(Idea[i])
#         return self.can_idea
#     def update_time(self,sel_idea):
#         self.time += sel_idea.exe_time
#         Idea.remove(sel_idea)
#             
# def sel_from_can(can_idea):
#     dic = {}
#     for i in can_idea:
#         dic[i.pm] = []
#     for i in can_idea:
#         dic[i.pm].append(i)
#     sel_dic = {}
#     for i in dic:
#         idea_li = [j.values for j in dic[i]]
#         sel_dic[i] = idea_li.index(min(idea_li))
#     last = []
#     for i in sel_dic:
#         last.append([dic[i][sel_dic[i]].values[1],dic[i][sel_dic[i]].values[3]])
#     index = last.index(min(last))
#     p = list(sel_dic.keys())[index]
#     i = sel_dic[list(sel_dic.keys())[index]]
#     return dic[p][i]
#        
# inp = [int(i) for i in input().split(' ')]
# P = inp[0]
# C = inp[1]
# I = inp[2]
# Idea = []
# for i in range(I):
#     ina = [int(i) for i in input().split(' ')]
#     Idea.append(idea(ina[0],ina[1],ina[2],ina[3]))   
# Idea_copy = Idea.copy()
# 
# i_pro_time = [Idea[i].pro_time for i in range(I)]
# min_pro_time = min(i_pro_time)
# Code = []
# for i in range(C):
#     Code.append(code(min_pro_time))
# 
# i = 0
# re = []
# while Idea:
#     if Code[i].time < min([Idea[i].pro_time for i in range(len(Idea))]):
#         Code[i].time = min([Idea[i].pro_time for i in range(len(Idea))])
#     can_idea = Code[i].search_idea()
#     sel_idea = sel_from_can(can_idea)
#     Code[i].update_time(sel_idea)
#     re.append([Code[i].time, sel_idea])
#     can_Code_time = []
#     for i in range(C):
#         can_Code_time.append(Code[i].time)
#     i = can_Code_time.index(min(can_Code_time))   
# re_dic = {}
# for i in range(len(re)):
#     re_dic[Idea_copy.index(re[i][1])] =  re[i][0]    
# for i in re_dic:
#     print(re_dic[i])

#-------上面为以前写的-------
#-------下面为最新写的-------

class Idea(object):
    def __init__(self, pm_no, prop_time, prio_level, exe_time):
        self.pm_no = pm_no
        self.prop_time = prop_time
        self.prio_level = prio_level
        self.exe_time = exe_time
        self.is_exe = False

    def update_state(self, imple_time):
        self.is_exe = True
        self.imple_time = imple_time


class Coder(object):
    def __init__(self, time):
        self.time = time

    def select_idea(self, ideas):
        # 选出空闲时间的未执行的idea
        prob_ideas = [idea for idea in ideas if idea.prop_time <=
                      self.time and idea.is_exe == False]
        # 选出pm最想执行的idea
        can_ideas = pm_select_idea(prob_ideas)
        # coder选择最终执行的idea
        temp_ideas = [[idea.exe_time, idea.pm_no] for idea in can_ideas]
        idea = can_ideas[temp_ideas.index(min(temp_ideas))]
        return idea

    def update_time(self, exe_time):
        self.time += exe_time

# 从合适ideas中对每个pm选取最想执行的一个idea
def pm_select_idea(ideas):
    idea_dict = {}
    for idea in ideas:
        if idea.pm_no not in idea_dict:
            idea_dict[idea.pm_no] = []
        idea_dict[idea.pm_no].append(idea)
    cand_ideas = []
    for k in idea_dict:
        temp_ideas = [[i.prio_level, i.exe_time, i.prop_time] for i in idea_dict[k]]
        cand_ideas.append(idea_dict[k][temp_ideas.index(min(temp_ideas))])
    return cand_ideas

# 获取未执行idea中的最小提出时间
def get_min_time(ideas):
    return min(idea.prop_time for idea in ideas if idea.is_exe==False)

# 获得下一个程序员的index
def get_next_coder(coders):
    coder_time = [coder.time for coder in coders]
    return coder_time.index(min(coder_time))

# 检查所有idea是否都已经实现
def all_done(ideas):
    return all(idea.is_exe for idea in ideas)

if __name__ == "__main__":
    ideas = [Idea(1,1,1,2), Idea(1,2,1,1), Idea(1,3,2,2), Idea(2,1,1,2), Idea(2,3,5,5)]
    coder_number = 2
    idea_number = 5
    coders = [Coder(0) for i in range(coder_number)]

    i = 0
    while not all_done(ideas):
        # 初始化程序员的时间，取执行完的时间与当前ideas中的最小提出时间的最大值
        coders[i].time = max(get_min_time(ideas), coders[i].time)
        # 从所有idea中选取最终执行的idea
        idea = coders[i].select_idea(ideas)
        # 执行idea, 更新程序员的时间，与idea的执行状态
        coders[i].update_time(idea.exe_time)
        idea.update_state(coders[i].time)
        # 获取下一个程序员的index
        i = get_next_coder(coders)

    for idea in ideas:
        print(idea.imple_time)

