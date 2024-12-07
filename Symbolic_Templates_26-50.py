
from datasets import load_dataset
from names_dataset import NameDataset 
import random

gsm8k = load_dataset("gsm8k", "main")

names = [
    "Alex", "Jordan", "Taylor", "Morgan", "Casey", "Avery", "Riley", "Jamie", 
    "Quinn", "Parker", "Rowan", "Skylar", "Reese", "Drew", "Emerson", "Hayden", 
    "Charlie", "Blair", "Sawyer", "Dakota", "Finley", "Arden", "Jules", "Micah", 
    "Sage", "River", "Sam", "Shay", "Elliot", "Phoenix", "Leslie", "Terry", 
    "Robin", "Cameron", "Kai", "Harper", "Payton", "Devon", "Hollis", "Blake", 
    "Remy", "Toby", "Kennedy", "Adrian", "August", "Ari", "Lennon", "Marley", 
    "Brett", "Francis", "Kendall", "Eden", "Rowe", "Monroe", "Shiloh", "Ash", 
    "Marlowe", "Ellis", "Case", "Aspen", "London", "Justice", "Jesse", "Alden", 
    "Linden", "Robin", "Tatum", "Wren", "Mackenzie", "Addison", "Luca", "Keegan", 
    "Oakley", "Sky", "Spencer", "Chandler", "Sloan", "Darcy", "Reagan", "Frankie", 
    "Rory", "Leighton", "Perry", "Gray", "Lane", "Arlo", "Ellery", "Corey", 
    "Kieran", "Bailey", "Presley", "Hunter", "Shane", "Cypress", "Quincy", 
    "Haven", "Sasha", "Scout"
]

male_family = ["nephew", "cousin", "brother"]
female_family = ["niece", "cousin", "sister"]


def template_1 (names, male_family, female_family): 

    question_1_templates = {}

    for i in range(1,51):

        name = random.choice(names)

        b = random.randint(5, 100)
        c = random.randint(5, 100)
        d = random.randint(5, 100)

        dividend = b + c * d
        divisors = [i for i in range(1, dividend + 1) if dividend % i == 0]
        a = random.choice(divisors)

        question = f'''{name} had {a} boxes of pencils with the same number of pencils in each box.
        He kept {b} pencils and shared the remaining pencils equally with his {c} friends.
        If his friends got {d} pencils each, how many pencils are in each box?'''

        # Applying gsm_symbolic template change
        ###########
        # Doing the same thing for the answer

        answer = f'''{name} shared {c} x {d} = <<{c}*{d}={c*d}>>{c*d} pencils with his friends.
        So, he had {b} + {c*d} = <<{b}+{c*d}={b+c*d}>>{b+c*d} pencils in all. Therefore,
        each box had {b+c*d}/{a} = <<{b+c*d}/{a}={(b+c*d)//a}>>{(b+c*d)//a} pencils inside.\n#### {(b+c*d)//a}'''

        question_1_templates[f'question_{i}'] = question
        question_1_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

    return question_1_templates

def template_2(names, male_family, female_family):

    question_2_templates = {} 

    for i in range(1,51):

        name = random.choice(names)

        a = random.randint(5, 100)
        b = random.randint(5, a)
        c = random.randint(5, 100)
        d = random.randint(5, c)
        e = random.randint(5, 100)
        f = random.randint(5, 100)

        # Applying Template

        # Caleb bought 10a cartons of ice cream and 4b cartons of frozen yoghurt. 
        # Each carton of ice cream cost $4c and each carton of frozen yoghurt cost $1d. 
        # How much more did Caleb spend on ice cream than on frozen yoghurt?

        question = f'''{name} bought {a} cartons of ice cream and {b} cartons of frozen yoghurt. 
        Each carton of ice cream cost ${c} and each carton of frozen yoghurt cost ${d}. 
        How much more did {name} spend on ice cream than on frozen yoghurt?'''

        # The cost of the ice cream is 10 × $4 = $<<10*4=40>>40.
        # The cost of the frozen yoghurt is 4 × $1 = $<<4*1=4>>4.
        # Caleb spent $40 − $4 = $36 more on ice cream than on frozen yogurt.
        # #### 36

        answer = f"""The cost of the ice cream is {a} x ${c} = $<<{a}*{c}={a*c}>>{a*c}.
        The cost of the frozen yoghurt is {b} x ${d} = $<<{b}*{d}={b*d}>>{b*d}.
        {name} spent ${a*c} - ${b*d} = ${(a*c)-(b*d)} more on ice cream than on frozen yogurt.
        #### {(a*c)-(b*d)}"""

        question_2_templates[f'question_{i}'] = question
        question_2_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

    return question_2_templates

def template_3(names, male_family, female_family):

    question_3_templates = {} 

    for i in range(1,51):

        name = random.choice(names)

        a = random.randint(20, 100)

        divisors1 = [i for i in range(2, a + 1) if a % i == 0]
        b = random.choice(divisors1)

        dividend = int(a-(a/b))
        divisors2 = [j for j in range(2, dividend + 1) if dividend % j == 0]
        c = random.choice(divisors2)
        
        bound1 = int((a-(a/b))-((a-(a/b))/c))
        d = random.randint(5, bound1)
        

        # Applying Template

        # Leah earned $28a working odd jobs around the neighborhood. 
        # She spent a seventhb of it on a milkshake and put half of the rest in her savings account.
        # She left the remaining money in her wallet. 
        # Her dog got ahold of her wallet and shredded all the money inside but $1c.
        # How many dollars did Leah lose?


        question = f'''{name} earned ${a} working odd jobs around the neighborhood. 
        She spent a {b}th of it on a milkshake and put a {c}th of the rest in her savings account.
        She left the remaining money in her wallet. 
        Her dog got ahold of her wallet and shredded all the money inside but ${d}.
        How many dollars did {name} lose?'''

        #   Leah spent 28 / 7 = $<<28/7=4>>4 on a milkshake.
        # She had 28 - 4 = $<<28-4=24>>24 left.
        # She put half in her savings account and half in her wallet, so she had 24 / 2 = $<<24/2=12>>12 in her wallet.
        # He    r dog shredded all the money in her wallet but $1, so Leah lost 12 - 1 = $<<12-1=11>>11.
        # #### 11

        answer = f'''{name} spent {a} / {b} = $<<{a}/{b}={a//b}>>{a//b} on a milkshake.
        She had {a} - {a//b} = $<<{a}-{a//b}={a-(a//b)}>>{a-(a//b)} left.
        She put {c}th in her savings account and the rest in her wallet, so she had {a-(a//b)} - ({a-(a//b)} / {c}) = $<<{a-(a//b)} - ({a-(a//b)} / {c})>>{a-(a//b)-((a-(a//b))//c)} in her wallet.
        Her dog shredded all the money in her wallet but ${d}, so {name} lost {a-(a//b)-((a-(a//b))//c)} - {d} = $<<{a-(a//b)-((a-(a//b))//c)}-{d}={(a-(a//b)-((a-(a//b))//c))-d}>>{(a-(a//b)-((a-(a//b))//c))-d}.
        #### {(a-(a//b)-((a-(a//b))//c))-d}'''

        question_3_templates[f'question_{i}'] = question
        question_3_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)
    
    return question_3_templates

def template_4(names, male_family, female_family):

    question_4_templates = {} 

    for i in range(1,51):

        name = random.choice(names) 
        a = random.randint(5, 100)
        b = random.randint(5, 100)
        c = random.randint(5, 100)

        dividend = b+c
        divisors1 = [i for i in range(1, dividend + 1) if ((dividend / (i+b+c))*100) % 1 == 0]
        a = random.choice(divisors1)
        
        d = random.randint(5, 100)
        e = random.randint(5, 100)
        f = random.randint(5, 100)

        # Applying Template

        # """There are 25 roses in a garden. 
        # There are 40 tulips. 
        # There are 35 daisies. 
        # What percentage of flowers are not roses?"""


        question = f"""There are {a} roses in a garden. 
        There are {b} tulips. 
        There are {c} daisies. 
        What percentage of flowers are not roses?"""

        # There are 25+40+35=<<25+40+35=100>>100 flowers total.
        # There are 40+35=<<40+35=75>>75 flowers that are not roses.
        # Therefore, (75/100)*100=<<(75/100)*100=75>>75% of the flowers are not roses.
        # #### 75

        answer = f"""There are {a}+{b}+{c}=<<{a}+{b}+{c}={a+b+c}>>{a+b+c} flowers total.
        There are {b}+{c}=<<{b}+{c}={b+c}>>{b+c} flowers that are not roses.
        Therefore, ({b+c}/{a+b+c})*100=<<({b+c}/{a+b+c})*100={int(((b+c)/(a+b+c))*100)}>>{int(((b+c)/(a+b+c))*100)}% of the flowers are not roses.
        #### {int(((b+c)/(a+b+c))*100)}"""

        question_4_templates[f'question_{i}'] = question
        question_4_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

    return question_4_templates

def template_5(names, male_family, female_family):

    question_5_templates = {} 

    for i in range(1,51):

        name = random.choice(names)

        
        b = random.randint(2, 10)
        a = random.randint(5, b*20)

        

        # Applying Template

        # Leo's assignment was divided into three parts. 
        # He finished the first part of his assignment in 25 minutes. 
        # It took him twice as long to finish the second part. 
        # If he was able to finish his assignment in 2 hours, how many minutes did Leo finish the third part of the assignment?



        question = f'''{name}'s assignment was divided into three parts. 
        He finished the first part of his assignment in {a} minutes. 
        It took him twice as long to finish the second part. 
        If he was able to finish his assignment in {b} hours, how many minutes did Leo finish the third part of the assignment?'''

        # It took Leo 25 x 2 = <<25*2=50>>50 minutes to finish the second part of the assignment.
        # Leo finished the first and second parts of the assignment in 25 + 50 = <<25+50=75>>75 minutes.
        # He finished the entire assignment in 60 x 2 = <<60*2=120>>120 minutes.
        # Therefore, it took Leo 120 - 75 = <<120-75=45>>45 minutes to finish the third part of the assignment.
        # #### 45

        answer = f'''It took {name} {a} x 2 = <<{a}*2={a*2}>>{a*2} minutes to finish the second part of the assignment.
        {name} finished the first and second parts of the assignment in {a} + {a*2} = <<{a}+{a*2}={a+a*2}>>{a+a*2} minutes.
        He finished the entire assignment in 60 x {b} = <<60*{b}={60*b}>>{60*b} minutes.
        Therefore, it took {name} {60*b} - {a+a*2} = <<{60*b}-{a+a*2}={(60*b)-(a+a*2)}>>{(60*b)-(a+a*2)} minutes to finish the third part of the assignment.
        #### {(60*b)-(a+a*2)}'''

        question_5_templates[f'question_{i}'] = question
        question_5_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

    return question_5_templates

def template_6(names, male_family, female_family):

    question_6_templates = {} 

    for i in range(1,51):

        name = random.choice(names)

        a = random.randint(10, 100)
        divisors1 = [i for i in range(3, a + 1) if a % i == 0]
        b  = random.choice(divisors1)
        
        divisors2 = [i for i in range(3, a + 1) if a % i == 0]
        c = random.choice(divisors2)

        dividend = int(a-((a/b)+(a/c)))
        divisors3 = [i for i in range(2, dividend + 1) if dividend % i == 0]
        d =  random.choice(divisors3)
        

        # Applying Template

        # Liza bought 10 kilograms of butter to make cookies. 
        # She used one-half of it for chocolate chip cookies, one-fifth of it for peanut butter cookies, and one-third of the remaining butter for sugar cookies. 
        # How many kilograms of butter are left after making those three kinds of cookies?



        question = f'''{name} bought {a} kilograms of butter to make cookies. 
        She used 1/{b}th of it for chocolate chip cookies, 1/{c}th of it for peanut butter cookies, and 1/{d}th of the remaining butter for sugar cookies. 
        How many kilograms of butter are left after making those three kinds of cookies?'''

        # Liza used 10/2 = <<10/2=5>>5 kilograms of butter for the chocolate chip cookies.
        # Then, she used 10/5 = <<10/5=2>>2 kilograms of butter for the peanut butter cookies.
        # She used 5 + 2 = <<5+2=7>>7 kilograms of butter for the chocolate and peanut butter cookies.
        # So, only 10 -7 = <<10-7=3>>3 kilograms of butter was left.
        # Then, Liza used 3/3 = <<3/3=1>>1 kilograms of butter for the sugar cookies.
        # Therefore, only 3-1 = <<3-1=2>>2 kilograms of butter were left.
        # #### 2

        answer = f'''{name} used {a}/{b} = <<{a}/{b}={a//b}>>{a//b} kilograms of butter for the chocolate chip cookies.
        Then, she used {a}/{c} = <<{a}/{c}={a//c}>>{a//c} kilograms of butter for the peanut butter cookies.
        She used {a//b} + {a//c} = <<{a//b}+{a//c}={(a//b)+(a//c)}>>{(a//b)+(a//c)} kilograms of butter for the chocolate and peanut butter cookies.
        So, only {a} - {(a//b)+(a//c)} = <<{a}-{(a//b)+(a//c)}={a-((a//b)+(a//c))}>>{a-((a//b)+(a//c))} kilograms of butter was left.
        Then, {name} used {a-((a//b)+(a//c))}/{d} = <<{a-((a//b)+(a//c))}/{d}={(a-((a//b)+(a//c)))/d}>>{(a-((a//b)+(a//c)))//d} kilograms of butter for the sugar cookies.
        Therefore, only {a-((a//b)+(a//c))}-{(a-((a//b)+(a//c)))//d} = <<{a-((a//b)+(a//c))}-{(a-((a//b)+(a//c)))//d}={(a-((a//b)+(a//c)))-((a-((a//b)+(a//c)))//d)}>>{(a-((a//b)+(a//c)))-((a-((a//b)+(a//c)))//d)} kilograms of butter were left.
        #### {(a-((a//b)+(a//c)))-((a-((a//b)+(a//c)))//d)}'''

        question_6_templates[f'question_{i}'] = question
        question_6_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

    return question_6_templates

def template_7(names, male_family, female_family):

    question_7_templates = {} 

    for i in range(1,51):

        subject = random.choice(['Mathematics', 'English','Business'])

        a = random.randint(1, 5)
        c = random.randint(5, 20)
        d = random.randint(5, 20)

        e = random.randint(5, 100)

        dividend = a*e
        divisors3 = [i for i in range(a+1, dividend+1) if dividend % i == 0]
        b =  random.choice(divisors3)
        
        

        # Applying Template

        # A Statistics student wants to find out the average daily allowance of the middle school students. 
        # According to his survey, 2/3 of the students receive an average of $6 allowance per day while the rest gets an average of $4 a day. 
        # If he surveyed 60 students, what is the total amount of money those 60 students get in a day?

        question = f'''A {subject} student wants to find out the average daily allowance of the middle school students. 
        According to his survey, {a}/{b} of the students receive an average of ${c} allowance per day while the rest gets an average of ${d} a day. 
        If he surveyed {e} students, what is the total amount of money those 60 students get in a day?'''

        # 'There are 60 students x 2/3 = <<60*2/3=40>>40 students who have a $6 daily allowance.
        # While there are 60 students - 40 students = <<60-40=20>>20 students who have a $4 daily allowance.
        # The sum of the allowances of the 40 students who received $6 daily is 40 students x $6/day = $<<40*6=240>>240.
        # The sum of the allowances of the 20 students who received $4 daily is 20 students x $4/day = $<<20*4=80>>80.
        # The total daily amount of money of those 60 students is $240 + $80 = $<<240+80=320>>320.
        # #### 320'''

        answer = f'''There are {e} students x {a}/{b} = <<{e}*{a}/{b}={int(e*(a/b))}>>{int(e*(a/b))} students who have a ${c} daily allowance.
        While there are {e} students - {int(e*(a/b))} students = <<{e}-{int(e*(a/b))}={int(e-(e*(a/b)))}>>{int(e-(e*(a/b)))} students who have a ${d} daily allowance.
        The sum of the allowances of the {int(e*(a/b))} students who received ${c} daily is {int(e*(a/b))} students x ${c}/day = $<<{int(e*(a/b))}*{c}={int((e*(a/b))*c)}>>{int((e*(a/b))*c)}.
        The sum of the allowances of the {int(e-(e*(a/b)))} students who received ${d} daily is {int(e-(e*(a/b)))} students x ${d}/day = $<<{int(e-(e*(a/b)))}*{d}={(int(e-(e*(a/b)))*d)}>>{int((e-(e*(a/b)))*d)}.
        The total daily amount of money of those {e} students is ${int((e*(a/b))*c)} + ${int((e-(e*(a/b)))*d)} = $<<{int((e*(a/b))*c)}+{int((e-(e*(a/b)))*d)}={int(((e*(a/b))*c)+((e-(e*(a/b)))*d))}>>{int(((e*(a/b))*c)+((e-(e*(a/b)))*d))}.
        #### {int(((e*(a/b))*c)+((e-(e*(a/b)))*d))}'''

        question_7_templates[f'question_{i}'] = question
        question_7_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)
    
    return question_7_templates

def template_8(names, male_family, female_family):

    question_8_templates = {} 

    for i in range(1,51):

        name = random.choice(names)
        subject = random.choice(['Mathematics', 'English','Business'])

        a = random.randint(5, 100)
        b = random.randint(5, 100)
        c = random.randint(5, 100)
        d = random.randint(5, a+b+c)
        e = random.randint(5, 100)
        f = random.randint(5, 100)

        # Applying Template

        # Every hour Joanne has to collect the coins out of the fountain inside the mall. 
        # During the first hour, she collected 15 coins. 
        # For the next two hours, she collected 35 coins from the fountain. 
        # In the fourth hour, she collected 50 coins from the fountain but she gave 15 of them to her coworker so she could buy a soda. 
        # How many coins did she have after the fourth hour?


        question = f'''Every hour {name} has to collect the coins out of the fountain inside the mall. 
        During the first hour, she collected {a} coins. 
        For the next two hours, she collected {b} coins from the fountain. 
        In the fourth hour, she collected {c} coins from the fountain but she gave {d} of them to her coworker so she could buy a soda. 
        How many coins did she have after the fourth hour?'''

        # # 15a coins collected in hour one
        # 35b coins collected in hour two
        # 35b coins collected in hour three
        # 50c coins collected in hour four
        # Before giving her coworker some coins there were 15+35+35+50=<<15+35+35+50=135>>135 coins
        # The number of coins after given 15 to her coworker is 135-15=<<135-15=120>>120
        # #### 120        

        answer = f'''{a} coins collected in hour one
        {b} coins collected in hour two
        {b} coins collected in hour three
        {c} coins collected in hour four
        Before giving her coworker some coins there were {a}+{b}+{b}+{c}=<<{a}+{b}+{b}+{c}={a+b+b+c}>>{a+b+b+c} coins
        The number of coins after given {d} to her coworker is {a+b+b+c}-{d}=<<{a+b+b+c}-{d}={a+b+b+c-d}>>{a+b+b+c-d}
        #### {a+b+b+c-d}''' 

        question_8_templates[f'question_{i}'] = question
        question_8_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

    return question_8_templates

def template_9(names, male_family, female_family):

    question_9_templates = {} 

    for i in range(1,51):

        name = random.choice(names)

        subject = random.choice(['Mathematics', 'English','Business'])

        a = random.randint(5, 20)
        b = random.randint(1, 10)
        c = random.randint(1, 10)
        d = random.randint(5, 20)
        e = random.randint(5, 100)
        f = random.randint(5, 100)

        # Applying Template

        # Jerry’s two daughters play softball on different teams. 
        # They each have 8 games this season. Each team practices 4 hours for every game they play. 
        # If each game lasts for 2 hours, how many hours will Jerry spend at the field watching his daughters play and practice altogether?


        question = f'''{name}'s two daughters play softball on different teams. 
        They each have {a} games this season. Each team practices {b} hours for every game they play. 
        If each game lasts for {c} hours, how many hours will {name} spend at the field watching his daughters play and practice altogether?'''

        # Jerry will spend 8a games x 2c hours per game = <<8*2=16>>16 hours watching one daughter play her games.
        # He will spend 16 x 2 = <<16*2=32>>32 hours watching both daughters play their games.
        # He will spend 8 games x 4 hours of practice = <<8*4=32>>32 hours watching one daughter practice.
        # He will spend 32 x 2 = <<32*2=64>>64 hours watching both daughters practice.
        # He will spend a total of 32 hours watching games + 64 hours watching practice = <<32+64=96>>96 hours.
        # #### 96 

        answer = f'''{name} will spend {a} games x {c} hours per game = <<{a}*{c}={a*c}>>{a*c} hours watching one daughter play her games.
        He will spend {a*c} x 2 = <<{a*c}*2={(a*c)*2}>>{(a*c)*2} hours watching both daughters play their games.
        He will spend {a} games x {b} hours of practice = <<{a}*{b}={a*b}>>{a*b} hours watching one daughter practice.
        He will spend {a*b} x 2 = <<{a*b}*2={(a*b)*2}>>{(a*b)*2} hours watching both daughters practice.
        He will spend a total of {(a*c)*2} hours watching games + {(a*b)*2} hours watching practice = <<{(a*c)*2}+{(a*b)*2}={(a*c)*2+(a*b)*2}>>{(a*c)*2+(a*b)*2} hours.
        #### {(a*c)*2+(a*b)*2}'''

        question_9_templates[f'question_{i}'] = question
        question_9_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

    return question_9_templates

def template_10 (names, male_family, female_family):

    question_10_templates = {} 

    for i in range(1,51):

        name = random.choice(names)
        subject = random.choice(['Mathematics', 'English','Business'])

        a = random.randint(5, 10)
        b = random.randint(5, 10)

        divisors = [i for i in range(100,1000) if ((1/b)*i)%1==0 and ((i-((1/b)*i)-(2*((1/b)*i)))/a)%1 == 0]
        c = random.choice(divisors)
        d = random.randint(5, 20)
        e = random.randint(5, 100)
        f = random.randint(5, 100)

        # Applying Template

        # A bear is preparing to hibernate for the winter and needs to gain 1000c pounds. 
        # At the end of summer, the bear feasts on berries and small woodland animals. 
        # During autumn, it devours acorns and salmon. 
        # It gained a fiftha of the weight it needed from berries during summer, and during autumn, it gained twice that amount from acorns.
        # Salmon made up half of the remaining weight it had needed to gain. How many pounds did it gain eating small animals?

        question = f'''A bear is preparing to hibernate for the winter and needs to gain {c} pounds. 
        At the end of summer, the bear feasts on berries and small woodland animals. 
        During autumn, it devours acorns and salmon. 
        It gained a {b}th of the weight it needed from berries during summer, and during autumn, it gained twice that amount from acorns.
        Salmon made up {a}th of the remaining weight it had needed to gain. How many pounds did it gain eating small animals?'''

        # The bear gained 1 / 5 * 1000 = <<1/5*1000=200>>200 pounds from berries.
        # It gained 2 * 200 = <<2*200=400>>400 pounds from acorns.
        # It still needed 1000 - 200 - 400 = <<1000-200-400=400>>400 pounds.
        # Thus, it gained 400 / 2 = <<400/2=200>>200 pounds from salmon.
        # Therefore, the bear gained 400 - 200 = <<400-200=200>>200 pounds from small animals.
        # #### 200

        answer = f'''The bear gained 1 / {b} * {c} = <<1/{b}*{c}={int((1/b)*c)}>>{int((1/b)*c)} pounds from berries.
    It gained 2 * {int((1/b)*c)} = <<2*{int((1/b)*c)}={int(2*((1/b)*c))}>>{int(2*((1/b)*c))} pounds from acorns.
    It still needed {c} - {int((1/b)*c)} - {int(2*((1/b)*c))} = <<{c}-{int((1/b)*c)}-{int(2*((1/b)*c))}={int(c-((1/b)*c)-(2*((1/b)*c)))}>>{int(c-((1/b)*c)-(2*((1/b)*c)))} pounds.
    Thus, it gained {int(c-((1/b)*c)-(2*((1/b)*c)))} / {a} = <<{int(c-((1/b)*c)-(2*((1/b)*c)))}/{a}={int((c-((1/b)*c)-(2*((1/b)*c)))/a)}>>{int((c-((1/b)*c)-(2*((1/b)*c)))/a)} pounds from salmon.
    Therefore, the bear gained {int(c-((1/b)*c)-(2*((1/b)*c)))} - {int((c-((1/b)*c)-(2*((1/b)*c)))/a)} = <<{int(c-((1/b)*c)-(2*((1/b)*c)))}-{int((c-((1/b)*c)-(2*((1/b)*c)))/a)}={int((c-((1/b)*c)-(2*((1/b)*c)))-((c-((1/b)*c)-(2*((1/b)*c)))/a))}>>{int((c-((1/b)*c)-(2*((1/b)*c)))-((c-((1/b)*c)-(2*((1/b)*c)))/a))} pounds from small animals.
    #### {int((c-((1/b)*c)-(2*((1/b)*c)))-((c-((1/b)*c)-(2*((1/b)*c)))/a))}'''

        question_10_templates[f'question_{i}'] = question
        question_10_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

    return question_10_templates

def template_11 (names, male_family, female_family):

    question_11_templates = {} 

    i=1
    while i < 51:

        name = random.choice(names)
        subject = random.choice(['Mathematics', 'English','Business'])

        a = random.randint(10, 50)
        d = random.randint(5, 10)
        c = random.randint(a*d, 1000)
        
        divisor = [i for i in range(51,100) if ((c-(a*d))/(i-a))%1 == 0]

        if divisor: 
            b = random.choice(divisor)
        else: 
            continue
        # Applying Template

        # There are 290 liters of oil in 24 cans. 
        # If 10 of the cans are holding 8 liters each, how much oil is each of the remaining cans holding?


        question = f"""There are {c} liters of oil in {b} cans. 
        If {a} of the cans are holding {d} liters each, how much oil is each of the remaining cans holding?"""

        # 10 cans are holding 8 liters each for a total of 10 * 8 = <<10*8=80>>80 liters
        # There are 290 - 80 = <<290-80=210>>210 litres left
        # There are 24 - 10 =<<24-10=14>>14 cans left
        # Each of the remaining cans is holding 210 / 14 = <<210/14=15>>15 liters each
        # #### 15

        s1 = a*d
        s2 = c-s1
        s3 = b-a
        s4 = int(s2/s3)

        answer = f'''{a} cans are holding {d} liters each for a total of {a} * {d} = <<{a}*{d}={s1}>>{s1} liters
        There are {c} - {s1} = <<{c}-{s1}={s2}>>{s2} litres left
        There are {b} - {a} =<<{b}-{a}={s3}>>{s3} cans left
        Each of the remaining cans is holding {s2} / {s3} = <<{s2}/{s3}={s4}>>{s4} liters each
        #### {s4}'''

        question_11_templates[f'question_{i}'] = question
        question_11_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

        i += 1

    return question_11_templates

def template_12 (names, male_family, female_family):

    question_12_templates = {} 

    for i in range(1,51):

        name = random.choice(names)
        subject = random.choice(['Mathematics', 'English','Business'])

        a = random.randint(50, 100)
        b = random.randint(5, 25)
        c = random.randint(5, 25)
        d = random.randint(5, 100)
        e = random.randint(5, 100)
        f = random.randint(5, 100)

        # Applying Template

        # Shawna's workout goal is 30 situps. 
        # On Monday, Shawna was only able to do 12 situps, so she decided that she would make up for the rest on Tuesday. 
        # However, she was only able to do 19 situps on Tuesday. 
        # How many situps would Shawna have to do on Wednesday to meet her minimum goal and make up for the ones she didn't do?



        question = f'''{name}'s workout goal is {a} situps. 
        On Monday, {name} was only able to do {b} situps, so she decided that she would make up for the rest on Tuesday. 
        However, she was only able to do {c} situps on Tuesday. 
        How many situps would {name} have to do on Wednesday to meet her minimum goal and make up for the ones she didn't do?'''

        # On Monday, Shawna was short of 30 - 12 = <<30-12=18>>18 situps
        # On Tuesday, Shawna was short of 30 - 19 = <<30-19=11>>11 situps
        # On Wednesday, Shawna would have to do 30 + 18 + 11 = <<30+18+11=59>>59 situps
        # #### 59

        s1 = a-b
        s2 = a-c
        s3 = b-a
        s4 = a+s1+s2

        answer = f'''On Monday, {name} was short of {a} - {b} = <<{a}-{b}={s1}>>{s1} situps
        On Tuesday, {name} was short of {a} - {c} = <<{a}-{c}={s2}>>{s2} situps
        On Wednesday, {name} would have to do {a} + {s1} + {s2} = <<{a}+{s1}+{s2}={s4}>>{s4} situps
        #### {s4}'''

        question_12_templates[f'question_{i}'] = question
        question_12_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

    return question_12_templates

def template_13 (names, male_family, female_family):

    question_13_templates = {} 

    for i in range(1,51):

        name = random.choice(names)
        subject = random.choice(['Mathematics', 'English','Business'])

        a = random.randint(5, 25)
        b = random.randint(5, 50)
        c = random.randint(5, 60)

        divisor = [i for i in range(5,60) if i%2==0]
        c = random.choice(divisor)
        

        # Applying Template

        # James earns $20 an hour while working at his main job.  
        # He earns 20% less while working his second job.  
        # He works 30 hours at his main job and half that much at his second job.  
        # How much does he earn per week?

        question = f'''{name} earns ${a} an hour while working at his main job.  
        He earns {b}% less while working his second job.  
        He works {c} hours at his main job and half that much at his second job.  
        How much does he earn per week?'''

        # James earns 20*.2=$<<20*.2=4>>4 less while working his second job
        # So he earns 20-4=$<<20-4=16>>16 an hour
        # At his first job he earns 20*30=$<<20*30=600>>600
        # He works 30/2=<<30/2=15>>15 hours at his second job
        # So he earns 15*16=$<<15*16=240>>240
        # So he earns 600+240=$<<600+240=840>>840 a week
        # #### 840    

        s1 = round(b * 1e-2,2)
        s2 = round(a*s1,2)
        s3 = round(a-s2,2)
        s4 = a*c
        s5 = int(c/2)
        s6 = round(s5 *s3,2)
        s7 = round(s4+s6,2)

        answer = f'''{name} earns {a}*{s1}=$<<{a}*{s1}={s2}>>{s2} less while working his second job
        So he earns {a}-{s2}=$<<{a}-{s2}={s3}>>{s3} an hour
        At his first job he earns {a}*{c}=$<<{a}*{c}={s4}>>{s4}
        He works {c}/2=<<{c}/2={s5}>>{s5} hours at his second job
        So he earns {s5}*{s3}=$<<{s5}*{s3}={s6}>>{s6}
        So he earns {s4}+{s6}=$<<{s4}+{s6}={s7}>>{s7} a week
        #### {s7}'''

        question_13_templates[f'question_{i}'] = question
        question_13_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

    return question_13_templates

def template_14 (names, male_family, female_family):

    question_14_templates = {} 

    for i in range(1,51):

        name = random.choice(names)
        subject = random.choice(['Mathematics', 'English','Business'])

        a = random.randint(5, 50)
        b = random.randint(5, 25)
        c = random.randint(5, 25)
        d = random.randint(5, 10)
        e = random.randint(5, 100)
        f = random.randint(5, 100)

        # Applying Template

        # Lee mows one lawn and charges $33. 
        # Last week he mowed 16 lawns and three customers each gave him a $10 tip. 
        # How many dollars did Lee earn mowing lawns last week?


        question = f'''{name} mows one lawn and charges ${a}. 
        Last week he mowed {b} lawns and {d} customers each gave him a ${c} tip. 
        How many dollars did {name} earn mowing lawns last week?'''

        # 33 * 16 = $<<33*16=528>>528
        # 3 * 10 = $<<3*10=30>>30
        # 528 + 30 = $<<528+30=558>>558
        # Lee earned $558 mowing lawns last week.
        # #### 558    

        s1 = a*b
        s2 = d*c
        s3 = s1+s2
        

        answer = f'''{a} * {b} = $<<{a}*{b}={s1}>>{s1}
        {d} * {c} = $<<{d}*{c}={s2}>>{s2}
        {s1} + {s2} = $<<{s1}+{s2}={s3}>>{s3}
        {name} earned ${s3} mowing lawns last week.
        #### {s3}'''

        question_14_templates[f'question_{i}'] = question
        question_14_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

    return question_14_templates

def template_15(names, male_family, female_family):


    question_15_templates = {} 

    i = 1
    while i < 51:

        name = random.choice(names)
        subject = random.choice(['Mathematics', 'English','Business'])

        # a = random.randint(500, 2000)
        b = random.randint(50, 100)
        c = random.randint(10, 50)
        d = random.randint(5, 50)
        e = random.randint(5, 12)
        
        divisor = [i for i in range(500,2000) if (i*(c/100))%1 == 0 and ((i-((i*(c/100))+d))/12)%1 == 0]

        if divisor:
            a = random.choice(divisor)
        else:
            continue

        # Applying Template

        # Tara has been planning to buy a laptop which costs $1000. 
        # A computer shop accepts payment in installments of $65 per month provided that a 20% down payment is made.
        # If Tara wants to pay an additional $20 for the down payment, how much will her balance be after paying for 4 months?



        question = f'''{name} has been planning to buy a laptop which costs ${a}. 
        A computer shop accepts payment in installments of ${b} per month provided that a {c}% down payment is made.
        If {name} wants to pay an additional ${d} for the down payment, how much will her balance be after paying for {e} months?'''

        # Tara has to make a $1000 x 20/100 = $<<1000*20/100=200>>200 down payment.
        # Since Tara wants to pay $20 more for the down payment, her total down payment will be $200 + $20 = $<<200+20=220>>220.
        # So her remaining balance payable over a year is $1000 - $220 = $<<1000-220=780>>780.
        # Tara has to make a monthly payment of $780/year / 12 months/year = $<<780/12=65>>65/month.
        # The total cost of her payments for 4 months is $65/month x 4 months = $<<65*4=260>>260.
        # Therefore, Tara's balance after 4 months is $780 - $260 = $<<780-260=520>>520.
        # #### 520

        s1 = int(a*(c/100))
        s2 = s1+d
        s3 = a-s2
        s4 = int(s3/12)
        s5 = s4*e
        s6 = s3-s5
        s7 = s4+s6

        answer = f'''{name} has to make a ${a} x {c}/100 = $<<{a}*{c}/100={s1}>>{s1} down payment.
        Since {name} wants to pay ${d} more for the down payment, her total down payment will be ${s1} + ${d} = $<<{s1}+{d}={s2}>>{s2}.
        So her remaining balance payable over a year is ${a} - ${s2} = $<<{a}-{s2}={s3}>>{s3}.
        {name} has to make a monthly payment of ${s3}/year / 12 months/year = $<<{s3}/12={s4}>>{s4}/month.
        The total cost of her payments for {e} months is ${s4}/month x {e} months = $<<{s4}*{e}={s5}>>{s5}.
        Therefore, {name}'s balance after {e} months is ${s3} - ${s5} = $<<{s3}-{s5}={s6}>>{s6}.
        #### {s6}'''

        question_15_templates[f'question_{i}'] = question
        question_15_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

        i += 1

    return question_15_templates

def template_16(names, male_family, female_family):

    question_16_templates = {} 

    i =1
    while i < 51:

        name = random.choice(names)
        subject = random.choice(['Mathematics', 'English','Business'])

        a = random.randint(2, 10)
        b = random.randint(5, 10)
        d = random.randint(2, 10)

        low = max(3*a,4*d)

        divisor = [i for i in range(low,500) if ((i-b-(3*a))/3)%1 ==0 and ((i-b-(3*a))/3)+(((i-(4*d))/3)/2)%1 ==0]

        if divisor:
            c = random.choice(divisor)
        else: 
            continue

        # Applying Template

        # Jesse and Mia are competing in a week long race. 
        # They have one week to run 30 miles. On the first three days Jesse averages (2/3) of a mile.
        #  On day four she runs 10 miles. Mia averages 3 miles a day over the first 4 days. 
        # What is the average of their average that they have to run over the final three days?

        question = f'''{name} and Mia are competing in a week long race. 
        They have one week to run {c} miles. On the first three days {name} averages {a} miles a day.
        On day four she runs {b} miles. Mia averages {d} miles a day over the first 4 days. 
        What is the average of their average that they have to run over the final three days?'''

        # Jesse runs 2 miles in the first three days because 3 x (2/3) = <<3*(2/3)=2>>2
        # Jesse has 18 miles left to run because 30 - 10 - 2 = <<30-10-2=18>>18
        # Jesse has to run an average of 6 miles a day because 18 / 3 = <<18/3=6>>6
        # Mia runs 12 miles over the first four days because 4 x 3 = <<4*3=12>>12
        # She has 18 miles left to run because 30 - 12 = <<30-12=18>>18
        # She has to run six miles a day because 18 / 3 = <<18/3=6>>6
        # The total they both have to run is <<12=12>>12 miles a day
        # The average they have to run per day on average is 6 miles because 12 / 2 = <<12/2=6>>6
        # #### 6

        s1 = 3*a      # (c-b(3*a)/3) and ((c-b(3*a))/3)+(((c-(4*d))/3)/2)
        s2 = c-b-s1
        s3 = int(s2/3)
        s4 = 4*d
        s5 = c-s4
        s6 = int(s5/3)
        s7 = s3+s6
        s8 = int(s7/2)

        answer = f'''{name} runs {s1} miles in the first three days because 3 x {a} = <<3*{a}={s1}>>{s1}
        {name} has {s2} miles left to run because {c} - {b} - {s1} = <<{c}-{b}-{s1}={s2}>>{s2}
        {name} has to run an average of {s3} miles a day because {s2} / 3 = <<{s2}/3={s3}>>{s3}
        Mia runs {s4} miles over the first four days because 4 x {d} = <<4*{d}={s4}>>{s4}
        She has {s5} miles left to run because {c} - {s4} = <<{c}-{s4}={s5}>>{s5}
        She has to run {s6} miles a day because {s5} / 3 = <<{s5}/3={s6}>>{s6}
        The total they both have to run is <<{s3}+{s6}>>{s7} miles a day
        The average they have to run per day on average is {s8} miles because {s7} / 2 = <<{s7}/2={s8}>>{s8}
        #### {s8}'''

        question_16_templates[f'question_{i}'] = question
        question_16_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

        i += 1

    return question_16_templates

def template_17(names, male_family, female_family):


    question_17_templates = {} 

    i = 1
    while i <51: 

        name = random.choice(names)
        subject = random.choice(['Mathematics', 'English','Business'])

        a = random.randint(5, 30)
        b = random.randint(5, 50)
        c= random.randint(100,300)
        
        divisor = [i for i in range(2,50) if (3/4)*((i/(a+i))*c)%1 == 0]

        if divisor: 
            b = random.choice(divisor)
        else: 
            continue


        # Applying Template

        # Jesse and Mia are competing in a week long race. 
        # They have one week to run 30 miles. On the first three days Jesse averages (2/3) of a mile.
        #  On day four she runs 10 miles. Mia averages 3 miles a day over the first 4 days. 
        # What is the average of their average that they have to run over the final three days?

        question = f'''The ratio of coins that Elsa has to that which {name} has is {a}:{b}. 
        If the total number of coins they have is {c}, and {name} spends 3/4 of what she has on toys, how many will she remain with?'''

        # The total ratio of the coins they both have is 10+45 = <<10+45=55>>55
        # The fraction of the ratio representing the number of coins that Amalie has is 45/55, and since the total number of coins they both have is 440, Amalie has 45/55*440 = <<45/55*440=360>>360 coins.
        # When Amalie spends 3/4 of what she has, she parts with 3/4*360 = <<3/4*360=270>>270 coins.
        # She still has 360 coins - 270 coins = <<360-270=90>>90 coins
        # #### 90

        s1 = a+b            # (3/4)*((b)/((a+b)*c))
        s2 = int((b/s1)*c)
        s3 = int((3/4)*s2)
        s4 = s2-s3


        answer = f'''The total ratio of the coins they both have is {a}+{b} = <<{a}+{b}={s1}>>{s1}
        The fraction of the ratio representing the number of coins that {name} has is {b}/{s1}, and since the total number of coins they both have is {c}, {name} has {b}/{s1}*{c} = <<{b}/{s1}*{c}={s2}>>{s2} coins.
        When {name} spends 3/4 of what she has, she parts with 3/4*{s2} = <<3/4*{s2}={s3}>>{s3} coins.
        She still has {s2} coins - {s3} coins = <<{s2}-{s3}={s4}>>{s4} coins
        #### {s4}'''

        question_17_templates[f'question_{i}'] = question
        question_17_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

        i+=1

    return question_17_templates

def template_18(names, male_family, female_family):

    question_18_templates = {} 

    for i in range(1,51):

        name = random.choice(names)
        subject = random.choice(['Mathematics', 'English','Business'])

        a = random.randint(5, 100)
        b = random.randint(5, 50)
        c = random.randint(100, 300)
        d = random.randint(5, 10)
        e = random.randint(5, 12)
        f = random.randint(5, 100)

        # Applying Template

        # Carly collected 7 starfish with 5 arms each and one seastar with 14 arms. 
        # How many arms do the animals she collected have in total?


        question = f'''{name} collected {a} starfish with 5 arms each and {b} seastar with 14 arms. 
        How many arms do the animals she collected have in total?'''

        # First find the total number of starfish arms: 7 starfish * 5 arms/starfish = <<7*5=35>>35 arms
        # Then add the number of seastar arms to find the total number of arms: 35 arms + 14 arms = <<35+14=49>>49 arms
        # #### 49

        s1 = a*5
        s2 = s1+(b*14)
        s3 = (3/d)*s2
        s4 = s2-s3
        s5 = c-s4
        s6 = s5/3
        s7 = s3+s6
        s8 = s7/2

        answer = f'''First find the total number of starfish arms: {a} starfish * 5 arms/starfish = <<{a}*5={s1}>>{s1} arms
        Then add the number of seastar arms to find the total number of arms: {s1} arms + {b} * 14 arms = <<{s1}+({b}*14)={s2}>>{s2} arms
        #### {s2}'''

        question_18_templates[f'question_{i}'] = question
        question_18_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

    return question_18_templates

def template_19(names, male_family, female_family):

    question_19_templates = {} 

    i = 1
    while i < 51:


        name = random.choice(names)
        subject = random.choice(['Mathematics', 'English','Business'])

        a = random.randint(5, 50)
        b = random.randint(50, 200)
        c = random.randint(5, 10)
        
        divisor = [i for i in range(2,20) if ((b-a)/i)%1==0]

        if divisor:
            c = random.choice(divisor)
        else: 
            continue

        # Applying Template

        # Jesse and Mia are competing in a week long race. 
        # They have one week to run 30 miles. On the first three days Jesse averages (2/3) of a mile.
        #  On day four she runs 10 miles. Mia averages 3 miles a day over the first 4 days. 
        # What is the average of their average that they have to run over the final three days?

        question = f'''{name} has {a} less apples than Martha, and Harry has 1/{c}th as many apples as {name}. 
        If Martha has {b} apples, how many apples does Harry have?'''


        # Tim has 68-30 = <<68-30=38>>38 apples.
        # Harry has 38/2 = <<38/2=19>>19 apples.
        # #### 19

        s1 = b-a
        s2 = int(s1/c)
    

        answer = f'''{name} has {b}-{a} = <<{b}-{a}={s1}>>{s1} apples.
        Harry has {s1}/{c} = <<{s1}/{c}={s2}>>{s2} apples.
        #### {s2}'''

        question_19_templates[f'question_{i}'] = question
        question_19_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

        i+=1

    return question_19_templates

def template_20(names, male_family, female_family):

    question_20_templates = {} 

    for i in range(1,51):

        name = random.choice(names)
        subject = random.choice(['Mathematics', 'English','Business'])

        a = random.randint(5, 20)
        b = random.randint(5, 50)
        c = random.randint(5, 50)
        d = random.randint(5, (a*b)+c)
        e = random.randint(5, 12)
        f = random.randint(5, 100)

        # Applying Template

        # At a flea market, Hillary sells handmade crafts for 12 dollars per craft. 
        # Today, Hillary sells 3 crafts and is given an extra 7 dollars from an appreciative customer. 
        # Later on, Hillary deposits 18 dollars from today's profits into her bank account. 
        # How many dollars is Hillary left with after making the deposit?


        question = f'''At a flea market, {name} sells handmade crafts for {b} dollars per craft. 
        Today, {name} sells {a} crafts and is given an extra {c} dollars from an appreciative customer. 
        Later on, {name} deposits {d} dollars from today's profits into her bank account. 
        How many dollars is {name} left with after making the deposit?'''

        # Hillary sells 3 crafts for 12 dollars each, for a total of 3 crafts * $12/craft = $<<3*12=36>>36
        # She receives an extra 7 dollars from a customer, increasing the total to $36 + $7 = $<<36+7=43>>43
        # She then deposits 18 dollars in the bank, leaving her with $43 - $18 = $25
        # #### 25

        s1 = a*b
        s2 = s1 +c
        s3 = s2-d

        answer = f'''{name} sells {a} crafts for {b} dollars each, for a total of {a} crafts * ${b}/craft = $<<{a}*{b}={s1}>>{s1}
        She receives an extra {c} dollars from a customer, increasing the total to ${s1} + ${c} = $<<{s1}+{c}={s2}>>{s2}
        She then deposits {d} dollars in the bank, leaving her with ${s2} - ${d} = ${s3}
        #### {s3}'''

        question_20_templates[f'question_{i}'] = question
        question_20_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

    return question_20_templates

def template_21(names, male_family, female_family):

    question_21_templates = {} 

    for i in range(1,51):

        name = random.choice(names)
        subject = random.choice(['Mathematics', 'English','Business'])

        a = random.randint(5, 20)
        b = random.randint(5, 50)
        c = random.randint(5, 50)
        
        divisor = [i for i in range(5,100) if ((a*b*i)*(3/4))%1 ==0]
        c = random.choice(divisor)


        # Applying Template

        # Nancy is filling an aquarium for her fish. 
        # She fills it halfway and goes to answer the door. 
        # While she's gone, her cat knocks the aquarium over and spills half the water in it. 
        # Then Nancy comes back and triples the amount of water in the aquarium. 
        # If the aquarium is 4 feet long, 6 feet wide, and 3 feet high, how many cubic feet of water are in the aquarium?



        question = f'''{name} is filling an aquarium for her fish. 
        She fills it halfway and goes to answer the door. 
        While she's gone, her cat knocks the aquarium over and spills half the water in it. 
        Then {name} comes back and triples the amount of water in the aquarium. 
        If the aquarium is {a} feet long, {b} feet wide, and {c} feet high, how many cubic feet of water are in the aquarium?'''

        # First calculate the volume of the aquarium by multiplying its length, width and height: 4 ft * 6 ft * 3 ft = <<4*6*3=72>>72 cubic ft
        # Then figure out what proportion of the aquarium is full after the cat knocks it over: 1/2 * 1/2 = 1/4
        # Then figure out what proportion of the aquarium is full after Nancy refills it: 3 * 1/4 = 3/4
        # Now multiply the proportion of the aquarium that's full by the aquarium's volume to find out how much water is in it: 72 cubic ft * 3/4 = <<72*3/4=54>>54 cubic ft
        # #### 54

        s1 = a*b*c
        s2 = int(s1*(3/4))
        

        answer = f'''First calculate the volume of the aquarium by multiplying its length, width and height: {a} ft * {b} ft * {c} ft = <<{a}*{b}*{c}={s1}>>{s1} cubic ft
        Then figure out what proportion of the aquarium is full after the cat knocks it over: 1/2 * 1/2 = 1/4
        Then figure out what proportion of the aquarium is full after {name} refills it: 3 * 1/4 = 3/4
        Now multiply the proportion of the aquarium that's full by the aquarium's volume to find out how much water is in it: {s1} cubic ft * 3/4 = <<{s1}*3/4={s2}>>{s2} cubic ft
        #### {s2}'''

        question_21_templates[f'question_{i}'] = question
        question_21_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

    return question_21_templates

def template_22(names, male_family, female_family):


    question_22_templates = {} 

    for i in range(1,51):

        name = random.choice(names)
        subject = random.choice(['Mathematics', 'English','Business'])

        a = random.randint(5, 20)
        c = random.randint(5, 50)
        d = random.randint(5, 20)
        

        divisors = [i for i in range(5,200) if ((i+c+d)/a)%1 ==0]
        b =random.choice(divisors)

        # Applying Template

        # At a flea market, Hillary sells handmade crafts for 12 dollars per craft. 
        # Today, Hillary sells 3 crafts and is given an extra 7 dollars from an appreciative customer. 
        # Later on, Hillary deposits 18 dollars from today's profits into her bank account. 
        # How many dollars is Hillary left with after making the deposit?


        question = f'''It is {name}'s turn to provide a snack for the baseball team after the game and he has decided to bring trail mix. 
        The trail mix comes in packs of {a} individual pouches. {name} has {b} members on his baseball team, plus {c} coaches and {d} helpers. 
        How many packs of trail mix does he need to buy?'''


        # Roger will need 13 + 3 + 2 = <<13+3+2=18>>18 pouches of trail mix.
        # If you divide the amount of trail mix pouches by the amount in each pack, 18 / 6 = <<18/6=3>>3 packs of trail mix.
        # #### 3

        s1 = b+c+d
        s2 = int(s1/a)
        

        answer = f'''{name} will need {b} + {c} + {d} = <<{b}+{c}+{d}={s1}>>{s1} pouches of trail mix.
        If you divide the amount of trail mix pouches by the amount in each pack, {s1} / {a} = <<{s1}/{a}={s2}>>{s2} packs of trail mix.
        #### {s2}'''

        question_22_templates[f'question_{i}'] = question
        question_22_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

    return question_22_templates

def template_23 (names, male_family, female_family):


    question_23_templates = {} 

    for i in range(1,51):

        name = random.choice(names)
        subject = random.choice(['Mathematics', 'English','Business'])

        a = random.randint(100, 300)
        b = random.randint(25,50)
        c = random.randint(5, 25)
        d = random.randint(5, 20)
        e = random.randint(5, 12)
        f = random.randint(5, 100)

        divisor = [i for i in range(100,300) if (((i-b)-(b-c))/2)%1==0]
        a = random.choice(divisor)

        # Applying Template

        # Second person = 27 - 7 = <<27-7=20>>20 kg
        # 103 - 27 - 20 = <<103-27-20=56>>56 kg
        # 56/2 = <<56/2=28>>28 kg
        # The last two people each lost 28 kilograms of weight.
        # #### 28


        question = f'''Four people lost a total of {a} kilograms of weight. 
        The first person lost {b} kilograms. 
        The second person lost {c} kilograms less than the first person. 
        The two remaining people lost the same amount. 
        How many kilograms did each of the last two people lose?'''



        # Roger will need 13 + 3 + 2 = <<13+3+2=18>>18 pouches of trail mix.
        # If you divide the amount of trail mix pouches by the amount in each pack, 18 / 6 = <<18/6=3>>3 packs of trail mix.
        # #### 3

        s1 = b-c
        s2 = a-b-s1
        s3 = int(s2/2)
        

        answer = f'''Second person = {b} - {c} = <<{b}-{c}={s1}>>{s1} kg
        {a} - {b} - {s1} = <<{a}-{b}-{s1}={s2}>>{s2} kg
        {s2}/2 = <<{s2}/2={s3}>>{s3} kg
        The last two people each lost {s3} kilograms of weight.
        #### {s3}'''

        question_23_templates[f'question_{i}'] = question
        question_23_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

    return question_23_templates

def template_24 (names, male_family, female_family):

    question_24_templates = {} 

    for i in range(1,51):

        name = random.choice(names)
        subject = random.choice(['Mathematics', 'English','Business'])

        a = random.randint(5, 20)
        b = random.randint(5, 20)
        c = random.randint(2, 10)
        d = random.randint(2, 10)
        e = random.randint(2, 10)
        f = random.randint(2, 10)

        # Applying Template

        # At a flea market, Hillary sells handmade crafts for 12 dollars per craft. 
        # Today, Hillary sells 3 crafts and is given an extra 7 dollars from an appreciative customer. 
        # Later on, Hillary deposits 18 dollars from today's profits into her bank account. 
        # How many dollars is Hillary left with after making the deposit?


        question = f'''{name} and Andrew had breakfast at a cafe. A slice of toast costs {a}, and eggs cost {b} each. 
        {name} had {c} slices of toast and {d} eggs. 
        Andrew had {e} slices of toast and {f} eggs. 
        How much did their breakfast cost?'''


        # The cost of Dale's toast is 2 × $1 = $<<2*1=2>>2.
        # The cost of Andrew's toast is 1 × $1 = $<<1*1=1>>1.
        # The cost of Dale's eggs is 2 × $3 = $<<2*3=6>>6.
        # The cost of Andrew's eggs is 2 × $3 = $<<2*3=6>>6.
        # Their breakfast cost $2 + $1 + $6 + $6 = $<<2+1+6+6=15>>15.
        # #### 15

        s1 = c*a
        s2 = e*a
        s3 = d*b
        s4 = f*b
        s5 = s1+s2+s3+s4

        answer = f'''The cost of {name}'s toast is {c} x ${a} = $<<{c}*{a}={s1}>>{s1}.
        The cost of Andrew's toast is {e} x ${a} = $<<{e}*{a}={s2}>>{s2}.
        The cost of {name}'s eggs is {d} x ${b} = $<<{d}*{b}={s3}>>{s3}.
        The cost of Andrew's eggs is {f} x ${b} = $<<{f}*{b}={s4}>>{s4}.
        Their breakfast cost ${s1} + ${s2} + ${s3} + ${s4} = $<<{s1}+{s2}+{s3}+{s4}={s5}>>{s5}.
        #### {s5}'''

        question_24_templates[f'question_{i}'] = question
        question_24_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

    return question_24_templates

def template_25(names, male_family, female_family):

    question_25_templates = {} 

    for i in range(1,51):

        name = random.choice(names)
        subject = random.choice(['Mathematics', 'English','Business'])

        a = random.randint(100, 250)
        b = random.randint(5, 100)
        c = random.randint(2, 10)
        d = random.randint(2, 10)
        e = random.randint(2, 10)
        f = random.randint(2, 10)

        # Applying Template

        # At a flea market, Hillary sells handmade crafts for 12 dollars per craft. 
        # Today, Hillary sells 3 crafts and is given an extra 7 dollars from an appreciative customer. 
        # Later on, Hillary deposits 18 dollars from today's profits into her bank account. 
        # How many dollars is Hillary left with after making the deposit?


        question = f'''A garden produced {a} potatoes, {b} fewer cucumbers and {c} times as many peppers than the cucumbers.
        How many vegetables did the garden produce?'''


        # The garden produced 237 potatoes - 60 = <<237-60=177>>177 cucumbers.
        # The garden produced 177 cucumbers * 2 peppers/cucumber = <<177*2=354>>354 peppers.
        # The garden produced 237 potatoes + 177 cucumbers + 354 peppers = <<237+177+354=768>>768 vegetables.
        # #### 768

        s1 = a-b
        s2 = s1*c
        s3 = a+s1+s2
    

        answer = f'''The garden produced {a} potatoes - {b} = <<{a}-{b}={s1}>>{s1} cucumbers.
        The garden produced {s1} cucumbers * {c} peppers/cucumber = <<{s1}*{c}={s2}>>{s2} peppers.
        The garden produced {a} potatoes + {s1} cucumbers + {s2} peppers = <<{a}+{s1}+{s2}={s3}>>{s3} vegetables.
        #### {s3}'''

        question_25_templates[f'question_{i}'] = question
        question_25_templates[f'answer_{i}'] = answer

        if i == 1:
            print(question)
            print(answer)

    return question_25_templates

import json
import os

class Template_Generator: 

    def __init__(self, names, gsm8k): 

        self.names = names 
        self.gsm8k = gsm8k 
        self.male_family = ["nephew", "cousin", "brother"]
        self.female_family = ["niece", "cousin", "sister"]

        self.templates = []

    def create_template(self, template: callable):
        '''Function for creating an individual template given the function'''

        template_dict = template(self.names, self.male_family, self.female_family)

        self.templates.append(template_dict)

    def generate_templates(self, template_funcs): 
        '''Function for generating all the templates given a list of template functions'''

        for i in template_funcs: 

            self.create_template(i)

    def store_templates(self, directory, output_file):
        '''Function for storing the list of templates'''

        os.chdir(directory)

        # Write the data to the JSON file
        with open(output_file, "w") as f:
            json.dump(self.templates, f, indent=2)

        print(f"Data successfully saved to {output_file}")

if __name__ == "__main__":

    GSM_SYM = Template_Generator(names, gsm8k)

    Templates = [template_1,template_2,template_3,template_4, template_5, template_6, template_7,template_8,template_9,template_10,template_11,
    template_12,template_13,template_14,template_15,template_16,template_17,template_18,template_19,template_20,template_21,template_22,template_23,
    template_24,template_25]

    GSM_SYM.generate_templates(Templates)

    print(f'Number of template: {len(GSM_SYM.templates)}')

    directory = os.getcwd()
    file_name = "Symbolic_Templates_26-50.json"
    GSM_SYM.store_templates(directory, file_name)

    with open(file_name, "r") as f:
        loaded_data = json.load(f)



