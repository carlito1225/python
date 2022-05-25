'''
雞兔同籠
雞加兔子共有83隻,雞的腳加兔子的腳共有240隻,求雞與兔子各有幾隻?

83*2=166
240-166=74/(4-2)=37 兔子
83-37=46 雞
'''

total=83
feet=240
rabbit=(feet-total*2)/(4-2)
chicken = total-rabbit
print("雞:%d 兔:%d" % (chicken, rabbit))
