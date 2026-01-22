# Weekly Journal
26 September 2025
Alex Hsiao

## Choose Your Own Adventure

> After spending an hour or two working on your CYOA, what has been your biggest challenge so far?

coming up with the story

> What's one thing you learned about variables, so far?

f{}

> What's one thing you learned about conditionals, so far?

how to use it

## Closing Questions

> What emoji best describes how you feel in this class this week? Explain why you chose this one.

🫠

```python
# Choose your own adventure
# Alex Hsiao
# 24 September 2025

import time
print("")
print("")
print("Make the Terminal Tab higher for better experience")
print('press "Enter" to continue')
pause = input()

print("Enter your name")
name = input("name: ")
print("loading......")
time.sleep(0.1)
print("loading.....")
time.sleep(0.1)
print("loading....")
time.sleep(0.1)
print("loading...")
time.sleep(0.1)
print("loading..")
time.sleep(0.1)
print("loading.")
time.sleep(2)

a = 3
while a >= 2:
    print("(´･ω･`)")
    time.sleep(0.05)
    print("( ´･ω･)")
    time.sleep(0.05)
    print("(　´･ω)")
    time.sleep(0.05)
    print("( 　´･)")
    time.sleep(0.05)
    print("( 　 ´)")
    time.sleep(0.05)
    print("(     )")
    time.sleep(0.05)
    print("(     )")
    time.sleep(0.05)
    print("(     )")
    time.sleep(0.05)
    print("(`　  )")
    time.sleep(0.05)
    print("(･`   )")
    time.sleep(0.05)
    print("(ω･`　)")
    time.sleep(0.05)
    print("(･ω･` )")
    time.sleep(0.05)
    a = a - 1
    if a == 1:
        print("(´･ω･`)")
        time.sleep(1.0)
        print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
        time.sleep(0.02)
        print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
        time.sleep(0.02)
        print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
        time.sleep(0.02)
        print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬛️⬛️⬛️⬛️⬜️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
        time.sleep(0.02)
        print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬛️⬛️⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
        time.sleep(0.02)
        print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
        time.sleep(0.02)
        print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
        time.sleep(0.02)
        print("⬜️⬜️⬛️⬛️⬛️⬜️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬛️⬛️⬜️⬜️⬛️⬛️⬛️⬛️⬛️⬜️⬛️⬛️⬛️⬛️⬜️⬛️⬛️⬛️⬜️⬜️")
        time.sleep(0.02)
        print("⬜️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬛️⬜️")
        time.sleep(0.02)
        print("⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬛️⬛️⬛️⬜️⬛️⬜️⬜️⬛️⬜️")
        time.sleep(0.02)
        print("⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬛️⬛️⬛️⬜️⬛️⬜️⬛️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬛️⬜️")
        time.sleep(0.02)
        print("⬜️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬛️⬛️⬛️⬜️⬛️⬛️⬛️⬜️⬜️")
        time.sleep(0.02)
        print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
time.sleep(2)
print("....")
time.sleep(0.5)
print("...")
time.sleep(0.5)
print("..")
time.sleep(0.5)
print(".")
time.sleep(0.5)
print("Alarm: Bibibi! Bibibi! Bibibi! Bibibi!")
time.sleep(0.5)
print(f"{name}: AUGHHHHHH! (smash the alarm clock)")
time.sleep(1)
print("YOU BROKE THE ALARM CLOCK")
time.sleep(0.5)
print(f"{name}: Noooo!!")
time.sleep(0.5)
print(f"{name}: I need dat shi to wake up!")
time.sleep(0.5)
print("(1) Go out earlier to buy a new alarm clock")
print("(2) Be late tomorrow anyway")
choose_1 = int(input(": "))
print('(Use number 1 to 9 to select options, and press "Enter" to confirm)')



# Introduction



# Problem



# Rising Action



# Climax



# Resolution



# python3 activity-cyoa-alex-hsiao.py




"""
🟥🟧🟨🟩🟦🟪⬛️⬜️🟫
r o y g b p bl w br

re = str("🟥")
on = str("🟧")
ye = str("🟨")
gr = str("🟩")
bu = str("🟦")
pu = str("🟪")
bl = str("⬛️")
wh = str("⬜️")
br = str("🟫")

print(bu, bu, bu, bu, bu, bu, bu, bu, bu, bu, bu, bu, bu, bu, bu, bu, bu, bu)
time.sleep(0.05)
print(bu, bl, bl, bl, bl, bl, bl, bl, bl, bl, bl, bl, bl, bl, bl, bl, bu, bu)
time.sleep(0.05)
print(bu, bl, ye, ye, ye, bl, bl, bl, ye, ye, ye, bl, ye, ye, ye, bl, bu, bu)
time.sleep(0.05)
print(bu, bl, ye, bl, ye, bl, ye, bl, ye, bl, ye, bl, ye, bl, ye, bl, bu, bu)
time.sleep(0.05)
print(bu, bl, ye, ye, ye, bl, bl, bl, ye, bl, ye, bl, ye, bl, ye, bl, bu, bu)
time.sleep(0.05)
print(bu, bl, ye, bl, ye, bl, ye, bl, ye, bl, ye, bl, ye, bl, ye, bl, bu, bu)
time.sleep(0.05)
print(bu, bl, ye, ye, ye, bl, bl, bl, ye, ye, ye, bl, ye, ye, ye, bl, bu, bu)
time.sleep(0.05)
print(bu, bl, bl, bl, bl, bl, bl, bl, bl, bl, bl, bl, bl, bl, bl, bl, bu, bu)
time.sleep(0.05)
print(bu, bu, bu, bu, bu, bu, bu, bu, bu, bu, bu, bu, bu, bu, bu, bu, bu, bu)

print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬜️⬛️⬛️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬛️⬛️⬛️⬛️⬜️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬛️⬛️⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬛️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
print("⬜️⬜️⬛️⬛️⬛️⬜️⬛️⬛️⬛️⬛️⬛️⬜️⬜️⬛️⬛️⬜️⬜️⬛️⬛️⬛️⬜️⬜️⬛️⬛️⬛️⬛️⬛️⬜️⬛️⬛️⬛️⬛️⬜️⬛️⬛️⬛️⬜️⬜️")
print("⬜️⬛️⬜️⬜️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬛️⬜️")
print("⬜️⬜️⬛️⬛️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬛️⬛️⬛️⬜️⬛️⬜️⬜️⬛️⬜️")
print("⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬛️⬛️⬛️⬜️⬛️⬜️⬛️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬛️⬜️")
print("⬜️⬛️⬛️⬛️⬜️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬛️⬜️⬛️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬜️⬜️⬜️⬛️⬛️⬛️⬛️⬜️⬛️⬛️⬛️⬜️⬜️")
print("⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️⬜️")
"""
```
