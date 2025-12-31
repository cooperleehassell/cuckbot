import discord
from discord.ext import commands
import random
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

PHRASES = [
    "You don’t know what real paint is. Ok. I ask my girl to fuck a dude in front of me so I can get off. She does sometime and I like it. I get of. Tho sometime she doesn’t fuck the dude in front me and sometimes she does when im not their to get of. That’s where reel pain comes into. Does feel good no does it",
    "Can. You bring a guy to fuck in from of me. I piss right now. Chiefs loss. Fuck the jaguars. Fuck the @nflnetwork and fuck live",
    "U fuck a guy. Find. I’m not there. So what. Doesn’t matter to you. U just car about getting of when I’m not there but i can’t get of. U know that hurts and you don’t care but I care. That’s what makes me different. Very. Single. Time. Maybe nice guts do Finnish last.",
    "Hello their. The angle from my nightmare. The shadow in the background of the morg. The unsuspecting vision of darkness in the valley we can life like jack and salley if we want. Where you can always fine me. And well have Halloween on Christmas and well wish this never ends. Well wish this ever ends.Were are you. And I’m so sorry. I cannot sleep I cannot dreamt tonite. I kneed somebody and also this sick strange, darkness comes creepy on so haughty every. time. And as a starred I counter, the webs from all the spiders catching thins and either they’re insides. Like a decision to call you and here youre voice of treason will you come home and stop this pain tonite. Stop this pain tonite. Dont wait your time on me I’m already a voice in side youre head",
    "u fuck a guy. great. i fuck u guy. now olivia sudden its a problem. u think u know what u want but reality u need me to do it for u. and i will bc thats the kind of men i am. u woudlnt know that if u ever paid attendence.",
    "U can only fuck guy when I’m they’re. U cant fuck the guy when I’m not there. I can get of only when another guy is involved. It’s that simple. Thanks for coming to my tent talk.",
    "lol. listen up dum dum. i can go to the super bowel if i start shaving now. i just got a promise at cd tradepost and now i make $8.50 in our. just because your team isnt there doesnt mean u get too take shit 😂",
    "Missouri loves company huh. I ask my girl not to fuck a guy unless I’m they’re. They do anyway. Then I fine out that I’m being laid off because cd tradepost its going out of business. Why cant a nice guy like me catch a break. The only of I get is from my job 😞",
    "Listen up dum dum. This is the last time I explain it to you. I don’t fuck the guy. My wife does in from of me. That’s how I get of. lol how are you this dumb. Seriously. The left claims education is imported but can’t even read property. Giid gid man.",
    "Nope. My girl fuck the guy not me. I watch. Usual in a chair. U wouldn’t now about it because you fuck your own girl. But the of is better watching. But I digest.",
    "Lol. U think u gay. Ur the gay one dum dum. I watch my girl fuck Guy, u don’t even have u girl. Who’s the gay one now. Lol. Good thing I’m not homonymphic",
    "No. I’m not gay just because I can’t of without a guy in the room. Ur gay because u don’t have girl. I have girl and not gay. Good red herring tho.",
    "So I’m gay. Lol. That’s rick coming from u. I get a girlfriend and olive a sudden I’m gay. Lol. U can’t even get lays. Stop protracting ur in securities onto me. Just because I can’t get of without my girlfriend fucking a guy in front of me doesn’t mean you got the oral high ground.",
    "Lmfao. We didn’t evolve from monkey dum dum. I go to zoo and see monkeys fucks each other. But never do I see a monkey watch two other monkeys fuck each other in from of him to get of. But if I do that where that come from. Huh. Must not come from monkey. Gid made me this way.",
    "Lmfoa. We got hut back ya. I watch the games after I watch the dud fuck my wife. He stay after to watch the game with me. We are just one big happy family. Karen hut didn’t beat up that women lmfoa. He genuinely pushed her with his leg. I mean sure. She fell and hurt herself against a wall. But that’s what she gets for provocation him. I watched the footage with the dude who fucks my wife and he agreed with me. Kareem hut getting canceled is just another example of wsj and the left ruining our county.",
    "U dont car. u fuck the dude when im not theyre to get of. whatever. ill get oven it. maybe then youll see that im a nice guy and not like those fucking assholes you like to fuck. nice guys always finnish last.",
    "Ok. So I meat a guy on tinder. He says he’s down to fuck u. U agree. Next thing I know income home to find u fucking another dude. What. The. F. Uck. U say u thought it was the same dude. Lol. That’s Richard coming from u. Guess u expect me to be leave u thought I was in the room the hole time? #makeitmakesins",
    "Just unloaded a new episode of my podcast, move moron. Special guess is the dude who fucked my girl while i watch. Accept when i go to get some beer for the pod i accidentally left the record on. The dude and my girl fuck without me theyre. Like wtf. I found this guy and they fuck so i cant get of. they suppose to fuck in from of me. any way, new episode is up if you want to check it out!",
    "you come home width a. guy and u are surprise to see me home. Ok. I ask if you were surprising me with the dude you are going to fuck. I have not got of in a while. I ask and you say yes. But something tell me you lie right to my face. Idk. Maybe you just aren't honestly with me no more. it’s hard to be in a relationship when one person keeps lieing.",
    "Try something new in the bedroom last night at the suggesting of Naruto girl. She had me fuck her while nick and nick 2 watch. Didn’t really like it. Hard to get of. Even nick 2 tried and he just started crying. Real wish she wouldn’t try new things in the bedroom. If it’s not broken don’t fix it.",
    "Funny. When we first meet. I try to eat you out while your own your period. You didn’t want that. Now I come home from cd tradepost and nick is gettin’ his red winks while nick 2 watch. Nice. Don’t want to sound cyclical but I can’t get of because of the hypocritical.",
    "U fuck u Guy. I watch. U peg me. The other guy watches. Funny. U never peg the other guy when its his turn. U only let me watch u fuck him. Witch dont get my wrong.  I love. I get of with that. But I thought by now u wouldve seen thru the lions and let me fuck u to. But no. U only peg me. Seems hypothetical.",
    "Their was even on time when you had the dude fuck me. That was weird. I didn’t get of then even thought you said I would. Tired of lines.",
    "I fuck a dude for u. U get of. U fuck a dude for me. I got of. We have a symbiological relation ship. My question to u is. How am I supposed to get of when u fuck the dude when I’m not their. How would u like it if I fuck the dude while ur not they’re. Wouldn’t be so funny now wood it 😂",
    "Let me get this strate. U tell me u dont want too shit on my chest. I say ok. Fine. Thats reason able. Than I come home too take a shit. Our toilet looks clean as it ever have. The dude u fuck walks into the kitchen. He has a huge brown spot on his chest. What. The. What. If u were going to shit on his chest, the leest u could do was to tell me so I could get of. But no. U do it behind my back. Why do I even brother.",
    "the dud who fucked my girl is on the einstein files. who new.",
    "Asked a dude over twitter to fuck my wife. He hasn’t respond yet. The suspenders is killing me.",
    "You don’t car. No one fuck king cars anymore.  I ask you to fuck nick 2 in from me now instead of nick 1. Nick 1 is mad at me for not prompting him to manger. Ok. He can’t fuck my girl now. See how he likes it. But you can’t respect me decision and you fuck him anyway. Nick 2 still watch to. It fucking sucks not having really friends.",
    "Illegal immigrations can only come here if they fuck my wife. At lease they’ll add something to society.",
    "No one card about me till I watch a dude fuck my wife",
    "You don’t car. Good. That make to of us. Have fun having only nick 2 watch u fuck.",
    "Gid work in intersecting way. I was trying to find another dude to fuck my girl and I meant this guy who mangers a restaurant. His names also Nick. How funny. He fucks ok. He make me where assless chips thought.",
    "Me and nick are friends again and he fucks my girl. All is well that ends good. I gave him the assistance manager position and nick 2 is store clerk. We listen to the justatem Christmas album. But now the other nick won’t leave us alone. He keeps asking when its his turn to fuck. Like buddy. You had your chance. Go way.",
    "He thinks just because he fucks ok he gets to fuck Olive the time. What. The. What. It doesn’t work like that. U have to earn ur roll. Everyone is looking for a handbag. I’m going to defense whats mine",
    "Nick and my girl has been fuck king to that new Charlie Kirk song. It really good. I like the bet. Nick 2 and I hum it while we watch. ",
    "The Nicks were over and Nick 1 was doing his thing. Fucking my girl in from of me and Nick 2. I notice Nick 2 not watching the fuck king but was watching me instead. It was wired. I still got of and I think he did to but not to them but me. I think he mighty be gay. Maybe we take a break from invitation him for now on",
    "Just found out that my girl has other livers that she doesn’t fuck in front of me. This is devastated. It’s just hard to find loyalty people any more. We make promise to each other. She would fuck guys in from of me and I would get of. That’s what real love is. Not lieing to your partner about how many dudes you fuck. ",
    "Decided to do dirt Santa this year with the nick’s and my girl. Nick 2 accident got my girl and he wants to give her a 10 percent coupon to cd trade post as the present. Idk if that’s cool as the head manger. That wound hurt our profit. Maybe he can get her a couple use dvd or blu rays from the store. She can even pick them out. I think that would save Christmas. ",
    "Lmfao. Dude. Your the loser. Every day is a three way when your a cuck 😂. Watching my girl get fuck by another dude is all the excitement I need. It even an ogre when Nick 2 comes and watched with me. ",
    "Lmfoa. AO will never replace my lifestyle. I like to see a robot try to fuck my girl like Nick 1 does. I’m mean. Sure. It can maybe watch with me like Nick 2 does. But it can’t fuck the same way humanity do. ",
    "Bro. U can’t make fun of me for being in the poly cube but never fucking. That’s. What. I. Does. U don’t understand. I don’t get of from fucking. I get of from watching my girl fuck dudes. I’m getting of day and nighttime. U only get of every couple. Of days when u fuck ur girl 😂",
    "Nick has a stomach arch and Nick 2 is busy picking up chicks a bingo. My girl wanted to Bring over a new guy. I said. Sure. Why not. Turn out he was a muslim. I was like babe. Don’t you now they are evil. They will beheld you if you don’t wear a turbine on your head. I told her I won’t get of if she has sex with him. I will go to OC and watch football. Well guess what. She fucks him anyway and I don’t get of. Glad I stood the morale high ground. ",
    "Both Nick’s call in sick today. I think. Huh. That’s weird. Wander where they might be. I come home from cd trade post and I see Nick fucking my girl and Nick 2 watching. Apprentice they have been doing this all day. Real Hard to believe theirs good people in this word when shit like this Happen. If like dont ever treat u like shit. Just wait to weeks. Then you’ll see different. ",
    "I just dont get it. Your the only girl who i watch get fuck by guys. Accept that one time I went to a ogre to get of. We had are hiccups. Sure. But I’ve stay loyal to you. Guest you havent done the same. Loyalty and respect is a to way street. ",
    "Ok. Sure. I was in a polygon. They fucked in my bed. Kylor gave me moneys to buy us snacks. We had a good think going. But none of that matter until I meet u. The polycube only let me watch sometimes. And I had to clean up after words. But u let me watch most of the times. That means so much too me. Its why when I tweet about how woman deserve less, I say “accept my girl” in my head. U changed what love look like for me.  I want to watch u fuck other dudes in from of me for ever. Good night sweet prince S",
    "Couldnt performance last night. Had a hard Tim getting hard last night (no pun intense). It was real sad because Nick 2 wanted to fuck since it was his birthday. No raisin for me not to get of when every one else is. ",
    "Try some thing new in the bed room tonight. Want Nick to “soke” with Naruto girl. It’ll He’lp me get of. Tire of getting of to my girl getting fuck so might try this and see what happens",
    "There is no benefit to being the nice cuck. My girl didn’t want to fuck the nicks. Find. But then she brings a new guy. And guess what. He’s a Muslim. I still get of but didn’t liked it. Tire of bull shit that happen daily. ",
]

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def cuckbot(ctx):
    await ctx.send(random.choice(PHRASES))



bot.run(os.getenv("DISCORD_TOKEN"))




