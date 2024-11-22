# -*- coding: utf-8 -*-
"""
Created on Tue Nov 19 07:01:33 2024

@author: camer
"""

import pandas as pd
from random import randint

names = ["Alex","Sam","Jessie","Cameron","Charlie","Pat"]

class Template:
    def __init__(self, original, marked):
        self.original = original
        self.marked = marked
        self.dists = []
    
    def add_dist(self, dist):
        self.dists.append(dist)      
        
    def generate_question(self):
        vals = []
        for dist in self.dists:
            vals.append(dist(vals))

        return self.marked.format(*vals)
        
    
templates = []
    
original = '''Question: Natalia sold clips to 48 of her friends in April, and then she sold half as many clips in May. How many clips did Natalia sell altogether in April and May?
Answer: Natalia sold 48/2 = <<48/2=24>>24 clips in May.
Natalia sold 48+24 = <<48+24=72>>72 clips altogether in April and May.
#### 72'''
marked = '''Question: {5:s} sold clips to {2:d} of her friends in April, and then she sold {0:s} as many clips in May. How many clips did {5:s} sell altogether in April and May?
Answer: {5:s} sold {2:d}/{1:d} = <<{2:d}/{1:d}={3:d}>>{3:d} clips in May. 
{5:s} sold {2:d}+{3:d} = <<{2:d}+{3:d}={4:d}>>{4:d} clips altogether in April and May. 
#### {4:d}'''
templates.append(Template(original, marked))
templates[0].add_dist(lambda x: ["half", "a third", "a quarter"][randint(0,2)])
templates[0].add_dist(lambda x: ["half", "a third", "a quarter"].index(x[0])+2)
templates[0].add_dist(lambda x: randint(1,100)*x[1])
templates[0].add_dist(lambda x: x[2]//x[1])
templates[0].add_dist(lambda x: x[2]+x[3])
templates[0].add_dist(lambda x: names[randint(0,len(names)-1)])

original = '''Weng earns $12 an hour for babysitting. Yesterday, she just did 50 minutes of babysitting. How much did she earn?
Weng earns 12/60 = $<<12/60=0.2>>0.2 per minute.
Working 50 minutes, she earned 0.2 x 50 = $<<0.2*50=10>>10.
#### 10'''
marked = '''Question: {4:s} earns ${0:d} an hour for babysitting. Yesterday, she just did {1:d} minutes of babysitting. How much did she earn? 
Answer: {4:s} earns {0:d}/60 = $<<{0:d}/60={2:.1f}>>{2:.1f} per minute. 
Working {1:d} minutes, she earned {2:.1f} x {1:d} = $<<{2:.1f}*{1:d}={3:d}>>{3:d}. 
#### {3:d}'''
templates.append(Template(original, marked))
templates[1].add_dist(lambda x: randint(1, 6)*6)
templates[1].add_dist(lambda x: randint(1,10)*10)
templates[1].add_dist(lambda x: x[1]/60)
templates[1].add_dist(lambda x: int(x[2]*x[1]))
templates[1].add_dist(lambda x: names[randint(0,len(names)-1)])


original = '''Question: Betty is saving money for a new wallet which costs $100. Betty has only half of the money she needs. Her parents decided to give her $15 for that purpose, and her grandparents twice as much as her parents. How much more money does Betty need to buy the wallet?
Answer: In the beginning, Betty has only 100 / 2 = $<<100/2=50>>50.
Betty's grandparents gave her 15 * 2 = $<<15*2=30>>30.
This means, Betty needs 100 - 50 - 30 - 15 = $<<100-50-30-15=5>>5 more.
#### 5'''
marked = '''Question: {9:s} is saving money for a new wallet which costs ${4:d}. {9:s} has only {0:s} of the money she needs. Her parents decided to give her ${5:d} for that purpose, and her grandparents {2:s} as much as her parents. How much more money does {9:s} need to buy the wallet?
Answer: In the beginning, {9:s} has only {4:d} / {1:d} = $<<{4:d}/{1:d}={6:d}>>{6:d}. 
{9:s}'s grandparents gave her {5:d} * {3:d} = $<<{5:d}*{3:d}={7:d}>>{7:d}. 
This means, {9:s} needs {4:d} - {6:d} - {7:d} - {5:d} = $<<{4:d}-{6:d}-{7:d}-{5:d}={8:d}>>{8:d} more. 
#### {8:d}'''
templates.append(Template(original, marked))
templates[2].add_dist(lambda x: ["half", "a third", "a quarter"][randint(0,2)])
templates[2].add_dist(lambda x:  ["half", "a third", "a quarter"].index(x[0])+2)
templates[2].add_dist(lambda x: ["twice", "three times", "four times"][randint(0,2)])
templates[2].add_dist(lambda x:  ["twice", "three times", "four times"].index(x[2])+2)
templates[2].add_dist(lambda x: randint(1,100)*x[1]*(1+x[3]))
templates[2].add_dist(lambda x: randint(0, (x[1]-1)*x[4]//(x[1]*(1+x[3]))))
templates[2].add_dist(lambda x: x[4]//x[1])
templates[2].add_dist(lambda x: x[5]*x[3])
templates[2].add_dist(lambda x: x[4]-x[6]-x[7]-x[5])
templates[2].add_dist(lambda x: names[randint(0,len(names)-1)])

original = '''Question: Julie is reading a 120-page book. Yesterday, she was able to read 12 pages and today, she read twice as many pages as yesterday. If she wants to read half of the remaining pages tomorrow, how many pages should she read?
Answer: Julie read 12 x 2 = <<12*2=24>>24 pages today.
So she was able to read a total of 12 + 24 = <<12+24=36>>36 pages since yesterday.
There are 120 - 36 = <<120-36=84>>84 pages left to be read.
Since she wants to read half of the remaining pages tomorrow, then she should read 84/2 = <<84/2=42>>42 pages.
#### 42'''
marked = '''Question: {10:s} is reading a {7:d}-page book. Yesterday, she was able to read {4:d} pages and today, she read {0:s} as many pages as yesterday. If she wants to read {2:s} of the remaining pages tomorrow, how many pages should she read?
Answer: {10:s} read {4:d} x {1:d} = <<{4:d}*{1:d}={5:d}>>{5:d} pages today. 
So she was able to read a total of {4:d} + {5:d} = <<{4:d}+{5:d}={6:d}>>{6:d} pages since yesterday. 
There are {7:d} - {6:d} = <<{7:d}-{6:d} ={8:d}>>{8:d} pages left to be read. 
Since she wants to read {2:s} of the remaining pages tomorrow, then she should read {8:d}/{3:d} = <<{8:d}/{3:d}={9:d}>>{9:d} pages. 
#### {9:d}'''
templates.append(Template(original, marked))
templates[3].add_dist(lambda x: ["twice", "three times", "four times"][randint(0,2)])
templates[3].add_dist(lambda x:  ["twice", "three times", "four times"].index(x[0])+2)
templates[3].add_dist(lambda x: ["half", "a third", "a quarter"][randint(0,2)])
templates[3].add_dist(lambda x:  ["half", "a third", "a quarter"].index(x[2])+2)
templates[3].add_dist(lambda x: randint(1, 20)*x[3])
templates[3].add_dist(lambda x: x[4]*x[1])
templates[3].add_dist(lambda x: x[4]+x[5])
templates[3].add_dist(lambda x: randint(x[6]//x[3],x[6]//x[3]+20)*x[1]*x[3])
templates[3].add_dist(lambda x: x[7]-x[6])
templates[3].add_dist(lambda x: x[8]//x[3])
templates[3].add_dist(lambda x: names[randint(0,len(names)-1)])

original = '''Question: James writes a 3-page letter to 2 different friends twice a week.  How many pages does he write a year?
Answer: He writes each friend 3*2=<<3*2=6>>6 pages a week
So he writes 6*2=<<6*2=12>>12 pages every week
That means he writes 12*52=<<12*52=624>>624 pages a year
#### 624'''
marked =  '''Question: {9:s} writes a {2:d}-page letter to {3:d} different friends {4:s} a {0:s}.  How many pages does he write a year?
Answer: He writes each friend {2:d}*{5:d}=<<{2:d}*{5:d}={6:d}>>{6:d} pages a {0:s} 
So he writes {6:d}*{3:d}=<<{6:d}*{3:d}={7:d}>>{7:d} pages every {0:s}
That means he writes {7:d}*{1:d}=<<{7:d}*{1:d}={8:d}>>{8:d} pages a year 
#### {8:d}'''
templates.append(Template(original, marked))
templates[4].add_dist(lambda x: ["day", "week"][randint(0,1)])
templates[4].add_dist(lambda x: [365, 52][["day", "week"].index(x[0])])
templates[4].add_dist(lambda x: randint(1, 6))
templates[4].add_dist(lambda x: randint(1, 6))
templates[4].add_dist(lambda x: ["twice", "three times", "four times"][randint(0,1)])
templates[4].add_dist(lambda x: ["twice", "three times", "four times"].index(x[4])+2)
templates[4].add_dist(lambda x: x[2]*x[5])
templates[4].add_dist(lambda x: x[6]*x[3])
templates[4].add_dist(lambda x: x[7]*x[1])
templates[4].add_dist(lambda x: names[randint(0,len(names)-1)])

original = '''Question: Mark has a garden with flowers. He planted plants of three different colors in it. Ten of them are yellow, and there are 80% more of those in purple. There are only 25% as many green flowers as there are yellow and purple flowers. How many flowers does Mark have in his garden?
Answer: There are 80/100 * 10 = <<80/100*10=8>>8 more purple flowers than yellow flowers.
So in Mark's garden, there are 10 + 8 = <<10+8=18>>18 purple flowers.
Purple and yellow flowers sum up to 10 + 18 = <<10+18=28>>28 flowers.
That means in Mark's garden there are 25/100 * 28 = <<25/100*28=7>>7 green flowers.
So in total Mark has 28 + 7 = <<28+7=35>>35 plants in his garden.
#### 35'''
marked = '''Question: {9:s} has a garden with flowers. He planted plants of three different colors in it. {0:s} of them are yellow, and there are {2:d}% more of those in purple. There are only {6:d}% as many green flowers as there are yellow and purple flowers. How many flowers does {9:s} have in his garden?
Answer: There are {2:d}/100 * {1:d} = <<{2:d}/100*{1:d}={3:d}>>{3:d} more purple flowers than yellow flowers. 
So in {9:s}'s garden, there are {1:d} + {3:d} = <<{1:d}+{3:d}={4:d}>>{4:d} purple flowers. 
Purple and yellow flowers sum up to {1:d} + {4:d} = <<{1:d}+{4:d}={5:d}>>{5:d} flowers. 
That means in {9:s}'s garden there are {6:d}/100 * {5:d} = <<{6:d}/100*{5:d}={7:d}>>{7:d} green flowers. 
So in total {9:s} has {5:d} + {7:d} = <<{5:d}+{7:d}={8:d}>>{8:d} plants in his garden. 
#### {8:d}'''
templates.append(Template(original, marked))
templates[5].add_dist(lambda x: ["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty"][randint(0,5)])
templates[5].add_dist(lambda x: (["Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty"].index(x[0])+1)*10)
templates[5].add_dist(lambda x: (4*randint(0,2) + 2*(x[1]//10)%2)*10)
templates[5].add_dist(lambda x: x[2]*x[1]//100)
templates[5].add_dist(lambda x: x[1]+x[3])
templates[5].add_dist(lambda x: x[1]+x[4])
templates[5].add_dist(lambda x: 25*randint(1,3))
templates[5].add_dist(lambda x: x[6]*x[5]//100)
templates[5].add_dist(lambda x: x[5]+x[7])
templates[5].add_dist(lambda x: names[randint(0,len(names)-1)])

original = '''Question: Albert is wondering how much pizza he can eat in one day. He buys 2 large pizzas and 2 small pizzas. A large pizza has 16 slices and a small pizza has 8 slices. If he eats it all, how many pieces does he eat that day?
Answer: He eats 32 from the largest pizzas because 2 x 16 = <<2*16=32>>32
He eats 16 from the small pizza because 2 x 8 = <<2*8=16>>16
He eats 48 pieces because 32 + 16 = <<32+16=48>>48
#### 48'''
marked = '''Question: {7:s} is wondering how much pizza he can eat in one day. He buys {0:d} large pizzas and {1:d} small pizzas. A large pizza has {2:d} slices and a small pizza has {3:d} slices. If he eats it all, how many pieces does he eat that day?
Answer: He eats {4:d} from the largest pizzas because {0:d} x {2:d} = <<{0:d}*{2:d}={4:d}>>{4:d} 
He eats {5:d} from the small pizza because {1:d} x {3:d} = <<{1:d}*{3:d}={5:d}>>{5:d} 
He eats {6:d} pieces because {4:d} + {5:d} = <<{4:d}+{5:d}={6:d}>>{6:d} 
#### {6:d}'''
templates.append(Template(original, marked))
templates[6].add_dist(lambda x: randint(1, 5))
templates[6].add_dist(lambda x: randint(1,10))
templates[6].add_dist(lambda x: randint(2,5)*4)
templates[6].add_dist(lambda x: randint(2,4)*2)
templates[6].add_dist(lambda x: x[0]*x[2])
templates[6].add_dist(lambda x: x[1]*x[3])
templates[6].add_dist(lambda x: x[4]+x[5])
templates[6].add_dist(lambda x: names[randint(0,len(names)-1)])

original = '''Question: Ken created a care package to send to his brother, who was away at boarding school.  Ken placed a box on a scale, and then he poured into the box enough jelly beans to bring the weight to 2 pounds.  Then, he added enough brownies to cause the weight to triple.  Next, he added another 2 pounds of jelly beans.  And finally, he added enough gummy worms to double the weight once again.  What was the final weight of the box of goodies, in pounds?
Answer: To the initial 2 pounds of jelly beans, he added enough brownies to cause the weight to triple, bringing the weight to 2*3=<<2*3=6>>6 pounds.
Next, he added another 2 pounds of jelly beans, bringing the weight to 6+2=<<6+2=8>>8 pounds.
And finally, he added enough gummy worms to double the weight once again, to a final weight of 8*2=<<8*2=16>>16 pounds.
#### 16'''
marked = '''Question: {1:s} created a care package to send to his {0:s}, who was away at boarding school.  {1:s} placed a box on a scale, and then he poured into the box enough jelly beans to bring the weight to {2:d} pounds.  Then, he added enough brownies to cause the weight to {3:s}.  Next, he added another {8:d} pounds of jelly beans.  And finally, he added enough gummy worms to {5:s} the weight once again.  What was the final weight of the box of goodies, in pounds?
Answer: To the initial {2:d} pounds of jelly beans, he added enough brownies to cause the weight to {3:s}, bringing the weight to {2:d}*{4:d}=<<{2:d}*{4:d}={7:d}>>{7:d} pounds. 
Next, he added another {8:d} pounds of jelly beans, bringing the weight to {7:d}+{8:d}=<<{7:d}+{8:d}={9:d}>>{9:d} pounds. 
And finally, he added enough gummy worms to {5:s} the weight once again, to a final weight of {9:d}*{6:d}=<<{9:d}*{6:d}={10:d}>>{10:d} pounds. 
#### {10:d}'''
templates.append(Template(original, marked))
templates[7].add_dist(lambda x: ["brother", "sister", "cousin", "friend"][randint(0,3)])
templates[7].add_dist(lambda x: names[randint(0,len(names)-1)])
templates[7].add_dist(lambda x: randint(2, 5))
templates[7].add_dist(lambda x: ["double", "triple", "quadruple"][randint(0,2)])
templates[7].add_dist(lambda x: ["double", "triple", "quadruple"].index(x[3])+2)
templates[7].add_dist(lambda x: ["double", "triple", "quadruple"][randint(0,2)])
templates[7].add_dist(lambda x: ["double", "triple", "quadruple"].index(x[5])+2)
templates[7].add_dist(lambda x: x[2]*x[4])
templates[7].add_dist(lambda x: randint(2, 5))
templates[7].add_dist(lambda x: x[7]+x[8])
templates[7].add_dist(lambda x: x[9]*x[6])

original = '''Question: Alexis is applying for a new job and bought a new set of business clothes to wear to the interview. She went to a department store with a budget of $200 and spent $30 on a button-up shirt, $46 on suit pants, $38 on a suit coat, $11 on socks, and $18 on a belt. She also purchased a pair of shoes, but lost the receipt for them. She has $16 left from her budget. How much did Alexis pay for the shoes?
Answer: Let S be the amount Alexis paid for the shoes.
She spent S + 30 + 46 + 38 + 11 + 18 = S + <<+30+46+38+11+18=143>>143.
She used all but $16 of her budget, so S + 143 = 200 - 16 = 184.
Thus, Alexis paid S = 184 - 143 = $<<184-143=41>>41 for the shoes.
#### 41'''
marked = '''Question: {0:s} is applying for a new job and bought a new set of business clothes to wear to the interview. She went to a department store with a budget of ${8:d} and spent ${2:d} on a button-up shirt, ${3:d} on suit pants, ${4:d} on a suit coat, ${5:d} on socks, and ${6:d} on a belt. She also purchased a pair of shoes, but lost the receipt for them. She has ${11:d} left from her budget. How much did {0:s} pay for the shoes?
Answer: Let {1:s} be the amount {0:s} paid for the shoes.
 She spent {1:s} + {2:d} + {3:d} + {4:d} + {5:d} + {6:d} = {1:s} + <<+{2:d}+{3:d}+{4:d}+{5:d}+{6:d}={7:d}>>{7:d}. 
 She used all but ${11:d} of her budget, so {1:s} + {7:d} = {8:d}  -  {11:d} = {10:d}. 
 Thus, {0:s} paid {1:s} = {10:d} - {7:d} = $<<{10:d}-{7:d}={9:d}>>{9:d} for the shoes. 
 #### {9:d}'''
templates.append(Template(original, marked))
templates[8].add_dist(lambda x: names[randint(0,len(names)-1)])
templates[8].add_dist(lambda x: ["A","a","B","b","C","c","S","s", "X", "x","y", "y","Z", "z"][randint(0,13)])
templates[8].add_dist(lambda x: randint(20,50))
templates[8].add_dist(lambda x: randint(30,80))
templates[8].add_dist(lambda x: randint(30,80))
templates[8].add_dist(lambda x: randint(5,20))
templates[8].add_dist(lambda x: randint(10, 30))
templates[8].add_dist(lambda x: x[2]+x[3]+x[4]+x[5]+x[6])
templates[8].add_dist(lambda x: randint(x[7]//10+ 4, x[7]//10 +10)*10)
templates[8].add_dist(lambda x: randint(1, x[8]-x[7]-1))
templates[8].add_dist(lambda x: x[7]+x[9])
templates[8].add_dist(lambda x: x[8]-x[10])

original = '''Question: Tina makes $18.00 an hour.  If she works more than 8 hours per shift, she is eligible for overtime, which is paid by your hourly wage + 1/2 your hourly wage.  If she works 10 hours every day for 5 days, how much money does she make?
Answer: She works 8 hours a day for $18 per hour so she makes 8*18 = $<<8*18=144.00>>144.00 per 8-hour shift
She works 10 hours a day and anything over 8 hours is eligible for overtime, so she gets 10-8 = <<10-8=2>>2 hours of overtime 
Overtime is calculated as time and a half so and she makes $18/hour so her overtime pay is 18*.5 = $<<18*.5=9.00>>9.00 
Her overtime pay is 18+9 = $<<18+9=27.00>>27.00 Her base pay is $144.00 per 8-hour shift and she works 5 days and makes 5 * $144 = $<<144*5=720.00>>720.00 
Her overtime pay is $27.00 per hour and she works 2 hours of overtime per day and makes 27*2 = $<<27*2=54.00>>54.00 in overtime pay 
2 hours of overtime pay for 5 days means she makes 54*5 = $270.00 
In 5 days her base pay is $720.00 and she makes $270.00 in overtime pay so she makes $720 + $270 = $<<720+270=990.00>>990.00 
#### 990'''
marked = '''Question: {12:s} makes ${0:d}.00 an hour.  If she works more than {1:d} hours per shift, she is eligible for overtime, which is paid by your hourly wage + 1/2 your hourly wage.  If she works {2:d} hours every day for {3:d} days, how much money does she make? 
Answer: She works {1:d} hours a day for ${0:d} per hour so she makes {1:d}*{0:d} = $<<{1:d}*{0:d}={5:d}.00>>{5:d}.00 per {1:d}-hour shift
She works {2:d} hours a day and anything over {1:d} hours is eligible for overtime, so she gets {2:d}-{1:d} = <<{2:d}-{1:d}={4:d}>>{4:d} hours of overtime 
Overtime is calculated as time and a half so and she makes ${0:d}/hour so her overtime pay is {0:d}*.5 = $<<{0:d}*.5={7:d}.00>>{7:d}.00 
Her overtime pay is {0:d}+{7:d} = $<<{0:d}+{7:d}={8:d}.00>>{8:d}.00 
Her base pay is ${5:d}.00 per {1:d}-hour shift and she works {3:d} days and makes {3:d} * ${5:d} = $<<{5:d}*{3:d}={6:d}>>{6:d}.00 
Her overtime pay is ${8:d}.00 per hour and she works {4:d} hours of overtime per day and makes {8:d}*{4:d} = $<<{8:d}*{4:d}={9:d}.00>>{9:d}.00 in overtime pay 
{4:d} hours of overtime pay for {3:d} days means she makes {9:d}*{3:d} = ${10:d}.00 
In {3:d} days her base pay is ${6:d}.00 and she makes ${10:d}.00 in overtime pay so she makes ${6:d} + ${10:d} = $<<{6:d}+{10:d}={11:d}.00>>{11:d}.00 
#### {11:d}'''
templates.append(Template(original,marked))
templates[9].add_dist(lambda x: randint(6, 12)*2)
templates[9].add_dist(lambda x: randint(6,10))
templates[9].add_dist(lambda x: randint(x[1]+1, x[1]+5))
templates[9].add_dist(lambda x: randint(2, 10))
templates[9].add_dist(lambda x: x[2]-x[1])
templates[9].add_dist(lambda x: x[0]*x[1])
templates[9].add_dist(lambda x: x[3]*x[5])
templates[9].add_dist(lambda x: x[0]//2)
templates[9].add_dist(lambda x: x[0]+x[7])
templates[9].add_dist(lambda x: x[8]*x[4])
templates[9].add_dist(lambda x: x[9]*x[3])
templates[9].add_dist(lambda x: x[6]+x[10])
templates[9].add_dist(lambda x: names[randint(0,len(names)-1)])


original = '''Question: A deep-sea monster rises from the waters once every hundred years to feast on a ship and sate its hunger. Over three hundred years, it has consumed 847 people. Ships have been built larger over time, so each new ship has twice as many people as the last ship. How many people were on the ship the monster ate in the first hundred years?
Answer: Let S be the number of people on the first hundred years’ ship.
The second hundred years’ ship had twice as many as the first, so it had 2S people.
The third hundred years’ ship had twice as many as the second, so it had 2 * 2S = <<2*2=4>>4S people.
All the ships had S + 2S + 4S = 7S = 847 people.
Thus, the ship that the monster ate in the first hundred years had S = 847 / 7 = <<847/7=121>>121 people on it.
#### 121'''
marked = '''Question: A deep-sea monster rises from the waters once every hundred years to feast on a ship and sate its hunger. Over three hundred years, it has consumed {4:d} people. Ships have been built larger over time, so each new ship has {0:s} as many people as the last ship. How many people were on the ship the monster ate in the first hundred years?
Answer: Let {6:s} be the number of people on the first hundred years’ ship.
The second hundred years’ ship had {0:s} as many as the first, so it had {1:d}S people.
The third hundred years’ ship had {0:s} as many as the second, so it had {1:d} * {1:d}{6:s} = <<{1:d}*{1:d}={2:d}>>{2:d}{6:s} people.
All the ships had {6:s} + {1:d}{6:s} + {2:d}{6:s} = {3:d}{6:s} =  {4:d} people.
Thus, the ship that the monster ate in the first hundred years had {6:s} = {4:d} / {3:d} = <<{4:d}/{3:d}={5:d}>>{5:d} people on it.
#### {5:d}'''
templates.append(Template(original,marked))
templates[10].add_dist(lambda x: ["twice", "three times", "four times"][randint(0,2)])
templates[10].add_dist(lambda x: ["twice", "three times", "four times"].index(x[0])+2)
templates[10].add_dist(lambda x: x[1]**2)
templates[10].add_dist(lambda x: 1 + x[1]+x[2])
templates[10].add_dist(lambda x: randint(10, 100)*x[3])
templates[10].add_dist(lambda x: x[4]//x[3])
templates[10].add_dist(lambda x: ["A","a","B","b","C","c","S","s", "X", "x","y", "y","Z", "z"][randint(0,13)])

original = '''Question: Tobias is buying a new pair of shoes that costs $95. He has been saving up his money each month for the past three months. He gets a $5 allowance a month. He also mows lawns and shovels driveways. He charges $15 to mow a lawn and $7 to shovel. After buying the shoes, he has $15 in change. If he mows 4 lawns, how many driveways did he shovel?
Answer: He saved up $110 total because 95 + 15 = <<95+15=110>>110
He saved $15 from his allowance because 3 x 5 = <<3*5=15>>15
He earned $60 mowing lawns because 4 x 15 = <<4*15=60>>60
He earned $35 shoveling driveways because 110 - 60 - 15 = <<110-60-15=35>>35
He shoveled 5 driveways because 35 / 7 = <<35/7=5>>5
#### 5'''
marked = '''Question: {13:s} is buying a new pair of shoes that costs ${12:d}. He has been saving up his money each month for the past {0:s} months. He gets a ${2:d} allowance a month. He also mows lawns and shovels driveways. He charges ${3:d} to mow a lawn and ${7:d} to shovel. After buying the shoes, he has ${11:d} in change. If he mows {4:d} lawns, how many driveways did he shovel?
Answer: He saved up ${10:d} total because {12:d} + {11:d} = <<{12:d}+{11:d}={10:d}>>{10:d}
He saved ${6:d} from his allowance because {1:d} x {2:d} = <<{1:d}*{2:d}={6:d}>>{6:d}
He earned ${5:d} mowing lawns because {4:d} x {3:d} = <<{4:d}*{3:d}={5:d}>>{5:d}
He earned ${9:d} shoveling driveways because {10:d} - {5:d} - {6:d} = <<{10:d}-{5:d}-{6:d}={9:d}>>{9:d}
He shoveled {8:d} driveways because {9:d} / {7:d} = <<{9:d}/{7:d}={8:d}>>{8:d}
#### {8:d}'''
templates.append(Template(original,marked))
templates[11].add_dist(lambda x: ["two","three", "four", "five", "six"][randint(0,4)])
templates[11].add_dist(lambda x: ["two","three", "four", "five", "six"].index(x[0])+2)
templates[11].add_dist(lambda x: randint(5, 15))
templates[11].add_dist(lambda x: randint(10,25))
templates[11].add_dist(lambda x: randint(2,6))
templates[11].add_dist(lambda x: x[3]*x[4])
templates[11].add_dist(lambda x: x[1]*x[2])
templates[11].add_dist(lambda x: randint(5,25))
templates[11].add_dist(lambda x: randint(2,6))
templates[11].add_dist(lambda x: x[7]*x[8])
templates[11].add_dist(lambda x: x[9]+x[5]+x[6])
templates[11].add_dist(lambda x: randint(1,20))
templates[11].add_dist(lambda x: x[10]-x[11])
templates[11].add_dist(lambda x: names[randint(0,len(names)-1)])

original = '''Question: Randy has 60 mango trees on his farm. He also has 5 less than half as many coconut trees as mango trees. How many trees does Randy have in all on his farm?
Answer: Half of the number of Randy's mango trees is 60/2 = <<60/2=30>>30 trees.
So Randy has 30 - 5 = <<30-5=25>>25 coconut trees.
Therefore, Randy has 60 + 25 = <<60+25=85>>85 treeson his farm.
#### 85'''
marked = '''Question: {0:s} has {3:d} mango trees on his farm. He also has {5:d} less than {1:s} as many coconut trees as mango trees. How many trees does {0:s} have in all on his farm?
Answer: {1:s} of the number of {0:s}'s mango trees is {3:d}/{2:d} = <<{3:d}/{2:d}={4:d}>>{4:d} trees.
So {0:s} has {4:d} - {5:d} = <<{4:d}-{5:d}={6:d}>>{6:d} coconut trees.
Therefore, {0:s} has {3:d} + {6:d} = <<{3:d}+{6:d}={7:d}>>{7:d} trees on his farm.
#### {7:d}'''
templates.append(Template(original,marked))
templates[12].add_dist(lambda x: names[randint(0,len(names)-1)])
templates[12].add_dist(lambda x: ["half", "a third", "a quarter"][randint(0,2)])
templates[12].add_dist(lambda x: ["half", "a third", "a quarter"].index(x[1])+2)
templates[12].add_dist(lambda x: randint(1,30)*x[2])
templates[12].add_dist(lambda x: x[3]//x[2])
templates[12].add_dist(lambda x: randint(1, x[4]-1))
templates[12].add_dist(lambda x: x[4]-x[5])
templates[12].add_dist(lambda x: x[3]+x[6])

original ='''Question: Jasper will serve charcuterie at his dinner party. He buys 2 pounds of cheddar cheese for $10, a pound of cream cheese that cost half the price of the cheddar cheese, and a pack of cold cuts that cost twice the price of the cheddar cheese. How much does he spend on the ingredients?
Answer: A pound of cream cheese cost $10 / 2 = $<<10/2=5>>5.
A pack of cold cuts cost $10 x 2 = $<<10*2=20>>20.
Jasper spent $10 + $5 + $20 = $<<10+5+20=35>>35 on the ingredients.
#### 35'''
marked = '''Question: {0:s} will serve charcuterie at his dinner party. He buys {5:d} pounds of cheddar cheese for ${4:d}, a pound of cream cheese that cost {1:s} the price of the cheddar cheese, and a pack of cold cuts that cost {6:s} the price of the cheddar cheese. How much does he spend on the ingredients?
Answer: A pound of cream cheese cost ${4:d} / {2:d} = $<<{4:d}/{2:d}={3:d}>>{3:d}.
A pack of cold cuts cost ${4:d} x {7:d} = $<<{4:d}*{7:d}={8:d}>>{8:d}.
{0:s} spent ${4:d} + ${3:d} + ${8:d} = $<<{4:d}+{3:d}+{8:d}={9:d}>>{9:d} on the ingredients.
#### {9:d}'''
templates.append(Template(original,marked))
templates[13].add_dist(lambda x: names[randint(0,len(names)-1)])
templates[13].add_dist(lambda x: ["half", "a third", "a quarter"][randint(0,2)])
templates[13].add_dist(lambda x: ["half", "a third", "a quarter"].index(x[1])+2)
templates[13].add_dist(lambda x: randint(1, 10))
templates[13].add_dist(lambda x: x[2]*x[3])
templates[13].add_dist(lambda x: randint(2,8))
templates[13].add_dist(lambda x: ["twice", "three times", "four times"][randint(0,2)])
templates[13].add_dist(lambda x: ["twice", "three times", "four times"].index(x[6])+2)
templates[13].add_dist(lambda x: x[4]*x[7])
templates[13].add_dist(lambda x: x[3]+x[4]+x[8])

original = '''Question: Joy can read 8 pages of a book in 20 minutes. How many hours will it take her to read 120 pages?
Answer: In one hour, there are 3 sets of 20 minutes.
So, Joy can read 8 x 3 = <<8*3=24>>24 pages in an hour.
It will take her 120/24 = <<120/24=5>>5 hours to read 120 pages.
#### 5'''
marked = '''Question: {6:s} can read {2:d} pages of a book in {0:d} minutes. How many hours will it take her to read {5:d} pages?
Answer: In one hour, there are {1:d} sets of {0:d} minutes.
So, {6:s} can read {2:d} x {1:d} = <<{2:d}*{1:d}={3:d}>>{3:d} pages in an hour.
It will take her {5:d}/{3:d} = <<{5:d}/{3:d}={4:d}>>{4:d} hours to read {5:d} pages.
#### {4:d}'''
templates.append(Template(original,marked))
templates[14].add_dist(lambda x: [5,6,10,12,15,20,30][randint(0,6)])
templates[14].add_dist(lambda x: 60//x[0])
templates[14].add_dist(lambda x: randint(2, 10))
templates[14].add_dist(lambda x: x[1]*x[2])
templates[14].add_dist(lambda x: randint(2, 8))
templates[14].add_dist(lambda x: x[3]*x[4])
templates[14].add_dist(lambda x: names[randint(0,len(names)-1)])

original = '''Question: James creates a media empire.  He creates a movie for $2000.  Each DVD cost $6 to make.  He sells it for 2.5 times that much.  He sells 500 movies a day for 5 days a week.  How much profit does he make in 20 weeks?
Answer: He sold each DVD for 6*2.5=$<<6*2.5=15>>15
So he makes a profit of 15-6=$<<15-6=9>>9
So each day he makes a profit of 9*500=$<<9*500=4500>>4500
So he makes 4500*5=$<<4500*5=22500>>22,500
He makes 22,500*20=$<<22500*20=450000>>450,000
Then after the cost of creating the movie he has a profit of 450,000-2000=$<<450000-2000=448000>>448,000
#### 448000'''
marked = '''Question: {0:s} creates a media empire.  He creates a movie for ${1:d}.  Each DVD cost ${2:d} to make.  He sells it for {3:.1f} times that much.  He sells {4:d} movies a day for {5:d} days a week.  How much profit does he make in {6:d} weeks?
Answer: He sold each DVD for {2:d}*{3:.1f}=$<<{2:d}*{3:.1f}={7:d}>>{7:d}
So he makes a profit of {7:d}-{2:d}=$<<{7:d}-{2:d}={8:d}>>{8:d}
So each day he makes a profit of {8:d}*{4:d}=$<<{8:d}*{4:d}={9:d}>>{9:d}
So he makes {9:d}*{5:d}=$<<{9:d}*{5:d}={10:d}>>{10:d}
He makes {10:d}*{6:d}=$<<{10:d}*{6:d}={11:d}>>{11:d}
Then after the cost of creating the movie he has a profit of {11:d}-{1:d}=$<<{11:d}-{1:d}={12:d}>>{12:d}
#### {12:d}'''
templates.append(Template(original,marked))
templates[15].add_dist(lambda x: names[randint(0,len(names)-1)])
templates[15].add_dist(lambda x: randint(1,10)*1000)
templates[15].add_dist(lambda x: randint(1,5)*2)
templates[15].add_dist(lambda x: randint(1,4)+0.5)
templates[15].add_dist(lambda x: randint(1,10)*100)
templates[15].add_dist(lambda x: randint(2,7))
templates[15].add_dist(lambda x: randint(5, 35))
templates[15].add_dist(lambda x: int(x[2]*x[3]))
templates[15].add_dist(lambda x: x[7]-x[2])
templates[15].add_dist(lambda x: x[8]*x[4])
templates[15].add_dist(lambda x: x[9]*x[5])
templates[15].add_dist(lambda x: x[10]*x[6])
templates[15].add_dist(lambda x: x[11]-x[1])

question = '''The profit from a business transaction is shared among 2 business partners, Mike and Johnson in the ratio 2:5 respectively. If Johnson got $2500, how much will Mike have after spending some of his share on a shirt that costs $200?
According to the ratio, for every 5 parts that Johnson gets, Mike gets 2 parts
Since Johnson got $2500, each part is therefore $2500/5 = $<<2500/5=500>>500
Mike will get 2*$500 = $<<2*500=1000>>1000
After buying the shirt he will have $1000-$200 = $<<1000-200=800>>800 left
#### 800'''
marked = '''The profit from a business transaction is shared among 2 business partners, {0:s} and {1:s} in the ratio {2:d}:{3:d} respectively. If {1:s} got ${6:d}, how much will {0:s} have after spending some of his share on a shirt that costs ${7:d}?
According to the ratio, for every {3:d} parts that {1:s} gets, {0:s} gets {2:d} parts
Since {1:s} got ${6:d}, each part is therefore ${6:d}/{3:d} = $<<{6:d}/{3:d}={4:d}>>{4:d}
{0:s} will get {2:d}*${4:d} = $<<{2:d}*{4:d}={5:d}>>{5:d}
After buying the shirt he will have ${5:d}-${7:d} = $<<{5:d}-{7:d}={8:d}>>{8:d} left
#### {8:d}'''
templates.append(Template(original,marked))
templates[16].add_dist(lambda x: names[randint(0,len(names)-1)])
templates[16].add_dist(lambda x: [name for name in names if name != x[0] ][randint(0,len(names)-2)])
templates[16].add_dist(lambda x: randint(2,6))
templates[16].add_dist(lambda x: randint(2,6))
templates[16].add_dist(lambda x: randint(100,1000))
templates[16].add_dist(lambda x: x[2]*x[4])
templates[16].add_dist(lambda x: x[3]*x[4])
templates[16].add_dist(lambda x: randint(1,x[5]//5))
templates[16].add_dist(lambda x: x[5]-x[7])

original = '''Question: In a truck, there are 26 pink hard hats, 15 green hard hats, and 24 yellow hard hats.  If Carl takes away 4 pink hard hats, and John takes away 6 pink hard hats and twice as many green hard hats as the number of pink hard hats that he removed, then calculate the total number of hard hats that remained in the truck.
Answer: If there were 26 pink hard hats and Carl took away 4 pink hard hats, the number of pink hard hats that remained is 26-4 = <<26-4=22>>22
John also took away 6 pink hard hats, leaving 22-6 = <<22-6=16>>16 pink hard hats in the truck.
If John also took twice as many green hard hats as pink hard hats, he took 2*6 = <<6*2=12>>12 green hard hats.
The total number of green hard hats that remained in the truck is 15-12 = <<15-12=3>>3
In the truck, after some are taken, there were 3 green hard hats + 16 pink hard hats = <<3+16=19>>19 hard hats in the truck.
Altogether, 19 green and pink hard hats + 24 yellow hards hats = <<19+24=43>>43 hard hats remained in the truck
#### 43'''
marked = '''Question: In a truck, there are {10:d} pink hard hats, {6:d} green hard hats, and {11:d} yellow hard hats.  If {13:s} takes away {9:d} pink hard hats, and {14:s} takes away {3:d} pink hard hats and {1:s} as many green hard hats as the number of pink hard hats that he removed, then calculate the total number of hard hats that remained in the truck.
Answer: If there were {10:d} pink hard hats and {13:s} took away {9:d} pink hard hats, the number of pink hard hats that remained is {10:d}-{9:d} = <<{10:d}-{9:d}={8:d}>>
{14:s} also took away {3:d} pink hard hats, leaving {8:d}-{3:d} = <<{8:d}-{3:d}={4:d}>>{4:d} pink hard hats in the truck.
If {14:s} also took {1:s} as many green hard hats as pink hard hats, he took {2:d}*{4:d} = <<{4:d}*{2:d}={5:d}>>{5:d} green hard hats.
The total number of green hard hats that remained in the truck is {6:d}-{5:d} = <<{6:d}-{5:d}={0:d}>>{0:d}
In the truck, after some are taken, there were {0:d} green hard hats + {4:d} pink hard hats = <<{0:d}+{4:d}={7:d}>>{7:d} hard hats in the truck.
Altogether, {7:d} green and pink hard hats + {11:d}  yellow hards hats = <<{7:d}+ {11:d} ={12:d} >>{12:d} hard hats remained in the truck
#### {12:d}'''
templates.append(Template(original,marked))
templates[17].add_dist(lambda x: randint(2,30))
templates[17].add_dist(lambda x: ["twice", "three times", "four times"][randint(0,2)])
templates[17].add_dist(lambda x: ["twice", "three times", "four times"].index(x[1])+2)
templates[17].add_dist(lambda x: randint(2,10))
templates[17].add_dist(lambda x: randint(2,30))
templates[17].add_dist(lambda x: x[2]*x[4])
templates[17].add_dist(lambda x: x[0]+x[5])
templates[17].add_dist(lambda x: x[0]+x[4])
templates[17].add_dist(lambda x: x[3]+x[4])
templates[17].add_dist(lambda x: randint(2,10))
templates[17].add_dist(lambda x: x[8]+x[9])
templates[17].add_dist(lambda x: randint(2, 30))
templates[17].add_dist(lambda x: x[7]+x[11])
templates[17].add_dist(lambda x: names[randint(0,len(names)-1)])
templates[17].add_dist(lambda x: [name for name in names if name != x[14] ][randint(0,len(names)-2)])

original = '''Question: It takes Roque two hours to walk to work and one hour to ride his bike to work. Roque walks to and from work three times a week and rides his bike to and from work twice a week. How many hours in total does he take to get to and from work a week with walking and biking?
Answer: Roque takes 2*3 = <<2*3=6>>6 hours a week to walk to work.
Roque takes 6*2 = <<6*2=12>>12 hours a week to walk to and from work.
Roque takes 1*2 = <<1*2=2>>2 hours a week to bike to work.
Roque takes 2*2 = <<2*2=4>>4 hours a week to bike to and from work.
In total, Roque takes 12+4 = <<12+4=16>>16 hour a week to go to and from work.
#### 16
'''
marked = '''Question: It takes {13:s} {0:s} to walk to work and {6:s} to ride his bike to work. {13:s} walks to and from work {2:s} a week and rides his bike to and from work {9:s} a week. How many hours in total does he take to get to and from work a week with walking and biking?
Answer: {13:s} takes {1:d}*{3:d} = <<{1:d}*{3:d}={4:d}>>{4:d} hours a week to walk to work.
{13:s} takes {4:d}*2 = <<{4:d}*2={5:d}>>{5:d} hours a week to walk to and from work.
{13:s} takes {7:d}*{8:d} = <<{7:d}*{8:d}={10:d}>>{10:d} hours a week to bike to work.
{13:s} takes {10:d}*2 = <<{10:d}*2={11:d}>>{11:d} hours a week to bike to and from work.
In total, {13:s} takes {5:d}+{11:d} = <<{5:d}+{11:d}={12:d}>>{12:d} hour a week to go to and from work.
#### {12:d}'''
templates.append(Template(original,marked))
templates[18].add_dist(lambda x: ["one hour","two hours","three hours","four hours"][randint(0,3)])
templates[18].add_dist(lambda x: ["one hour","two hours","three hours","four hours"].index(x[0])+1)
templates[18].add_dist(lambda x: ["once","twice","three times","four times"][randint(0,3)])
templates[18].add_dist(lambda x: ["once","twice","three times","four times"].index(x[2])+1)
templates[18].add_dist(lambda x: x[1]*x[3])
templates[18].add_dist(lambda x: x[4]*2)
templates[18].add_dist(lambda x: ["one hour","two hours","three hours","four hours"][randint(0,3)])
templates[18].add_dist(lambda x: ["one hour","two hours","three hours","four hours"].index(x[6])+1)
templates[18].add_dist(lambda x: 5 - x[3])
templates[18].add_dist(lambda x: ["once","twice","three hours","four hours"][x[8]-1])
templates[18].add_dist(lambda x: x[7]*x[8])
templates[18].add_dist(lambda x: x[10]*2)
templates[18].add_dist(lambda x: x[5]+x[11])
templates[18].add_dist(lambda x: names[randint(0,len(names)-1)])

original = '''Question: Tim rides his bike back and forth to work for each of his 5 workdays.  His work is 20 miles away.  He also goes for a weekend bike ride of 200 miles.    If he can bike at 25 mph how much time does he spend biking a week?
Answer: He bikes 20*2=<<20*2=40>>40 miles each day for work
So he bikes 40*5=<<40*5=200>>200 miles for work
That means he bikes a total of 200+200=<<200+200=400>>400 miles for work
So he bikes a total of 400/25=<<400/25=16>>16 hours
#### 16'''
marked = '''Question: {0:s} rides his bike back and forth to work for each of his 5 workdays.  His work is {4:d} miles away.  He also goes for a weekend bike ride of {7:d} miles.    If he can bike at {2:d} mph how much time does he spend biking a week?
Answer: He bikes {4:d}*2=<<{4:d}*2={5:d}>>{5:d} miles each day for work
So he bikes {5:d}*5=<<{5:d}*5={6:d}>>{6:d} miles for work
That means he bikes a total of {6:d}+{7:d}=<<{6:d}+{7:d}={3:d}>>{3:d} miles for work
So he bikes a total of {3:d}/{2:d}=<<{3:d}/{2:d}={1:d}>>{1:d} hours
#### {1:d}'''
templates.append(Template(original,marked))
templates[19].add_dist(lambda x: names[randint(0,len(names)-1)])
templates[19].add_dist(lambda x: randint(5,25))
templates[19].add_dist(lambda x: randint(5,30))
templates[19].add_dist(lambda x: x[1]*x[2])
templates[19].add_dist(lambda x: randint(1, x[3]//15))
templates[19].add_dist(lambda x: x[4]*2)
templates[19].add_dist(lambda x: x[5]*5)
templates[19].add_dist(lambda x: x[3]-x[6])

original = '''Question: Bella bought stamps at the post office. Some of the stamps had a snowflake design, some had a truck design, and some had a rose design. Bella bought 11 snowflake stamps. She bought 9 more truck stamps than snowflake stamps, and 13 fewer rose stamps than truck stamps. How many stamps did Bella buy in all?
Answer:The number of truck stamps is 11 + 9 = <<11+9=20>>20.
The number of rose stamps is 20 − 13 = <<20-13=7>>7.
Bella bought 11 + 20 + 7 = <<11+20+7=38>>38 stamps in all.
#### 38'''
marked = '''Question: {6:s} bought stamps at the post office. Some of the stamps had a snowflake design, some had a truck design, and some had a rose design. {6:s} bought {3:d} snowflake stamps. She bought {4:d} more truck stamps than snowflake stamps, and {1:d} fewer rose stamps than truck stamps. How many stamps did {6:s} buy in all?
Answer: The number of truck stamps is {3:d} + {4:d} = <<{3:d}+{4:d}={2:d}>>{2:d}.
The number of rose stamps is {2:d} − {1:d} = <<{2:d}-{1:d}={0:d}>>{0:d}.
{6:s} bought {3:d} + {2:d} + {0:d} = <<{3:d}+{2:d}+{0:d}={5:d}>>{5:d} stamps in all.
#### {5:d}'''
templates.append(Template(original,marked))
templates[20].add_dist(lambda x: randint(1, 20))
templates[20].add_dist(lambda x: randint(2,20))
templates[20].add_dist(lambda x: x[0]+x[1])
templates[20].add_dist(lambda x: randint(2, x[2]))
templates[20].add_dist(lambda x: x[2]-x[3])
templates[20].add_dist(lambda x: x[0]+x[2]+x[3])
templates[20].add_dist(lambda x: names[randint(0,len(names)-1)])

original = '''Question: Each bird eats 12 beetles per day, each snake eats 3 birds per day, and each jaguar eats 5 snakes per day. If there are 6 jaguars in a forest, how many beetles are eaten each day?
Answer: First find the total number of snakes eaten: 5 snakes/jaguar * 6 jaguars = <<5*6=30>>30 snakes
Then find the total number of birds eaten per day: 30 snakes * 3 birds/snake = <<30*3=90>>90 snakes
Then multiply the number of snakes by the number of beetles per snake to find the total number of beetles eaten per day: 90 snakes * 12 beetles/snake = <<90*12=1080>>1080 beetles
#### 1080'''
marked = '''Question: Each bird eats {0:d} beetles per day, each snake eats {1:d} birds per day, and each jaguar eats {2:d} snakes per day. If there are {3:d} jaguars in a forest, how many beetles are eaten each day?
Answer: First find the total number of snakes eaten: {2:d} snakes/jaguar * {3:d} jaguars = <<{2:d}*{3:d}={4:d}>>{4:d} snakes
Then find the total number of birds eaten per day: {4:d} snakes * {1:d} birds/snake = <<{4:d}*{1:d}={5:d}>>{5:d} snakes
Then multiply the number of snakes by the number of beetles per snake to find the total number of beetles eaten per day: {5:d} snakes * {0:d} beetles/snake = <<{5:d}*{0:d}={6:d}>>{6:d} beetles
#### {6:d}'''
templates.append(Template(original,marked))
templates[21].add_dist(lambda x: randint(2,50))
templates[21].add_dist(lambda x: randint(2,10))
templates[21].add_dist(lambda x: randint(2,10))
templates[21].add_dist(lambda x: randint(2,20))
templates[21].add_dist(lambda x: x[2]*x[3])
templates[21].add_dist(lambda x: x[1]*x[4])
templates[21].add_dist(lambda x: x[0]*x[5])

original = '''Question: Samantha’s last name has three fewer letters than Bobbie’s last name. If Bobbie took two letters off her last name, she would have a last name twice the length of Jamie’s. Jamie’s full name is Jamie Grey. How many letters are in Samantha’s last name?
Answer: There are 4 letters in Jamie’s last name, so Bobbie’s name is 4*2 +2 = <<4*2+2=10>>10 letters long.
Samantha’s last name is 3 letters shorter than Bobbie’s, so there are 10 - 3 = <<10-3=7>>7 letters in Samantha’s last name.
#### 7'''
marked = '''Question: {0:s}’s last name has {9:d} fewer letters than {0:s}’s last name. If {0:s} took {5:d} letters off her last name, she would have a last name {6:s} the length of {2:s}’s. {2:s}’s full name is {2:s} {3:s}. How many letters are in {0:s}’s last name?
Answer: There are {4:d} letters in {2:s}’s last name, so {0:s}’s name is {4:d}*{7:d} +{5:d} = <<{4:d}*{7:d}+{5:d}={8:d}>>{8:d} letters long.
{0:s}’s last name is {9:d} letters shorter than {0:s}’s, so there are {8:d} - {9:d} = <<{8:d}-{9:d}={10:d}>>{10:d} letters in {0:s}’s last name.
#### {10:d}'''
templates.append(Template(original,marked))
templates[22].add_dist(lambda x: names[randint(0,len(names)-1)])
templates[22].add_dist(lambda x: [name for name in names if name != x[0] ][randint(0,len(names)-2)])
templates[22].add_dist(lambda x: [name for name in names if ((name != x[0]) and (name != x[1]))][randint(0,len(names)-3)])
templates[22].add_dist(lambda x: ["Ngo","Adam", "Black", "Austin", "Zickert", "Smithson", "Christoph"][randint(0,6)])
templates[22].add_dist(lambda x:  ["Ngo","Adam", "Black", "Austin", "Zickert", "Smithson","Christoph"].index(x[3])+3)
templates[22].add_dist(lambda x: randint(2,10))
templates[22].add_dist(lambda x: ["twice", "three times", "four times"][randint(0,2)])
templates[22].add_dist(lambda x: ["twice", "three times", "four times"].index(x[6])+2)
templates[22].add_dist(lambda x: x[4]*x[7]+x[5])
templates[22].add_dist(lambda x: randint(2, x[8]-2))
templates[22].add_dist(lambda x: x[8]-x[9])

original = '''Question: Ann's favorite store was having a summer clearance. For $75 she bought 5 pairs of shorts for $7 each and 2 pairs of shoes for $10 each. She also bought 4 tops, all at the same price. How much did each top cost?
Answer: She bought 5 shorts at $7 each so 5*7=$<<5*7=35>>35
She bought 2 pair of shoes at $10 each so 2*10=$<<2*10=20>>20
The shorts and shoes cost her 35+20 = $<<35+20=55>>55
We know she spent 75 total and the shorts and shoes cost $55 which left a difference of 75-55 = $<<75-55=20>>20
She bought 4 tops for a total of $20 so 20/4 = $5
#### 5'''
marked = '''Question: {0:s}'s favorite store was having a summer clearance. For ${11:d} she bought {1:d} pairs of shorts for ${2:d} each and {4:d} pairs of shoes for ${5:d} each. She also bought {8:d} tops, all at the same price. How much did each top cost?
Answer: She bought {1:d} shorts at ${2:d} each so {1:d}*{2:d}=$<<{1:d}*{2:d}={3:d}>>{3:d}
She bought {4:d} pair of shoes at ${5:d} each so {4:d}*{5:d}=$<<{4:d}*{5:d}={6:d}>>{6:d}
The shorts and shoes cost her {3:d}+{6:d} = $<<{3:d}+{6:d}={7:d}>>{7:d}
We know she spent 75 total and the shorts and shoes cost ${7:d} which left a difference of {11:d}-{7:d} = $<<{11:d}-{7:d}={10:d}>>{10:d}
She bought {8:d} tops for a total of ${10:d} so {10:d}/{8:d} = ${9:d} 
#### {9:d}'''
templates.append(Template(original,marked))
templates[23].add_dist(lambda x: names[randint(0,len(names)-1)])
templates[23].add_dist(lambda x: randint(2, 10))
templates[23].add_dist(lambda x: randint(5, 20))
templates[23].add_dist(lambda x: x[1]*x[2])
templates[23].add_dist(lambda x: randint(2, 10))
templates[23].add_dist(lambda x: randint(5, 30))
templates[23].add_dist(lambda x: x[4]*x[5])
templates[23].add_dist(lambda x: x[3]+x[6])
templates[23].add_dist(lambda x: randint(2, 10))
templates[23].add_dist(lambda x: randint(5, 20))
templates[23].add_dist(lambda x: x[8]*x[9])
templates[23].add_dist(lambda x: x[7]+x[10])

original = '''Question: Mary does her grocery shopping on Saturday. She does her shopping only at a specific store where she is allowed a credit of $100, which must be paid in full before her next shopping trip. That week she spent the full credit limit and paid $15 of it on Tuesday and $23 of it on Thursday. How much credit will Mary need to pay before her next shopping trip?
Answer: So far, Mary has paid back $15 +$23=$<<15+23=38>>38 of the credit.
So she still needs to pay $100-$38=$<<100-38=62>>62
#### 62'''
marked = '''Question: {0:s} does her grocery shopping on Saturday. She does her shopping only at a specific store where she is allowed a credit of ${4:d}, which must be paid in full before her next shopping trip. That week she spent the full credit limit and paid ${1:d} of it on Tuesday and ${2:d} of it on Thursday. How much credit will {0:s} need to pay before her next shopping trip?
Answer: So far, {0:s} has paid back ${1:d}+${2:d}=$<<{1:d}+{2:d}={3:d}>>{3:d} of the credit.
So she still needs to pay ${4:d}-${3:d}=$<<{4:d}-{3:d}={5:d}>>{5:d}
#### {5:d}'''
templates.append(Template(original,marked))
templates[24].add_dist(lambda x: names[randint(0,len(names)-1)])
templates[24].add_dist(lambda x: randint(1,100))
templates[24].add_dist(lambda x: randint(1,100))
templates[24].add_dist(lambda x: x[1]+x[2])
templates[24].add_dist(lambda x: randint((x[3]//10+1),50)*10)
templates[24].add_dist(lambda x: x[4]-x[3])
print(templates[24].generate_question())