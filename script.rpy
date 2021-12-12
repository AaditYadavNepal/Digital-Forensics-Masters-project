
default p = Character("Police", image="police")


# The game starts here.




label start:
    play music "audio/sg.ogg"

    scene bg hotel

    #p happy "lets go"
    p happy "My name is inspector X.."
    p happy "I am with police and I will need you help with investigation."
    p happy"The case we are going to dicuss today..."
    p happy"... is the craiglist murderer case"
    p angry"On April 10, 2009, 29-year-old Trisha Leffler, an escort, was gagged, bound and robbed at gunpoint at a Westin hotel by a man who had responded to an ad she placed on Craigslist."
    p angry"In April 2009, Boston police were investigating two separate attacks on women who had advertised erotic services online and had planned to meet their client at a luxury hotel."
    p sad  "Four days later,Julissa Brisman was found murdered in the doorway of her Marriott hotel room. It appeared that she had
     been trying to fight off her attacker, when she was shot multiple times. She had placed an ad on Craigslist offering erotic massage services"
    p sad "and had scheduled an appointment to meet a man named Andy at her hotel room Police believed the same attacker was linked to the attempted robbery of Cynthia Melton, an exotic dancer offering lap dance services"
    p happy" We need your help finding the culprit... lets go!"

label quiz:
    scene bg outside
    #Initialize score
    $ quiz_score = 0
    $ misclick = 0
################################################################################
    #1st question
    p happy" Their email show that they met in  craigslist hmmm...What should we do now?"
    menu:
        "Send a preservation Order to Craigslist":
            $quiz_score +=1
            p happy "That's a great idea, it is indeed very important to get a preservation order for the emails, we don't want our evidence to get tampared or damaged lets get into next step"
        " Request for warrent":
            $ misclick +=1
            p angry " Hmm, that comes after we get the preservation order, You lost a point, lets get into next step"
        "Request to search at the incident site":
            $ misclick +=1
            p angry "why incident site, we just went there,  play safe the misclicks are being counted, lets get into next step"
        "Look into network logs, time stamps":
            $ misclick +=1
            p angry " I think we need to reques for preservation order first, you lose a point, let get into next question"
#################################################################################
    #2nd question
    p happy "After sending the preservation order, what do we do next?"
    menu:
        "Get camera logs in Hotel":
            $ misclick +=1
            p angry " This is important but it will be done after some steps.It is very important to get the warrent first"
        "Request search warrant":
            $quiz_score +=1
            p happy " yes, that is correct remember if, you dont recieve the warrent with in 60 days you need to request for new preservation order"
        "Get IP address for Craigslist":
            $misclick +=1
            p angry " we need to get a warrent first, lets got to next question"
        "Retrive any device near the murder place":
            $misclick +=1
            p angry " This doesn't fall under our justriction, lets go into nextt question"
################################################################################

    #3rd question is fill in the blanks
    #
    # This till needs a little work
    p happy "Sweet, lets get into another question"
    $ fill_que = renpy.input("Can you explaing me the difference between IP and MAC address?")
    $ fill_que = fill_que.strip()
    p happy "Intresting!, in simple way MAC address is used to ensure the physical address of the computer..."
    p happy "while IP address are used to uniquely identifiy the connection of a network with that particular device. Let get back to case and to nect step:"
################################################################################
## extra comment
    #if  not fill_que:
        #fill_que = "internet service provider"
        #p happy "correct"
    #else:
        #p angry "practise more"
################################################################################
    #4th question
    p happy "This is going great..."
    p happy "After we got the warrent, we had the oppurtunity to check the email from craiglist and got an idea about Internet service provide, what should we do with this information"
    menu:
        "send the preservation order and then request for warrent to ISP":
            $ quiz_score +=1
            p happy " yes, that is correct"

        "Look for wifi logs and MAC address":
            $misclick +=1
            p angry " I dont think it is write, let get into next question"
        "Request search warrent to ISP":
            $misclick +=1
            p angry " That is after we send the preservation order to ISP"
        "Hire a white hacker to retirve data":
            $misclick +=1
            p angry " That is not a option we look into. you lost a point"
################################################################################
    #5th question
    p happy "After investigating ISP, we found out the IP address belong to boston university we send the PO and SW to BU, Now what should be done next"
    menu:
        " Look at the wifi/ network logs for the IP address":
            $ quiz_score +=1
            p happy " yes, that is correct"

        "Talk to BU to help them find the person":
            $misclick +=1
            p angry " I dont think it is right option, let get into next question"
        "Do a reconnaissance and creata profile for BU student":
            $misclick +=1
            p angry " That is not a option we look into. There are 1000 of student we need to narrow the suspect group. you lost a point"
################################################################################
    # 6th question
    p happy "I think we are getting near to the culprit, now we finally have the IP adress, my cologue told me after checking the network log, we can retive the time stamp and login information?"

    menu:
        "True":
            $ quiz_score +=1
            p happy " that is indeed true, this can help us get the username of that specific MAC adress"
        "False":
            $ misclick +=1
            p angry " that is not correct, lets continue"

    # Ending
    p happy "After we have the time stamp and login infomation, we cgot the user name and..."
    p happy "...we got the MAC address and it was connected to various devies we used that to compare the craiglist MAC address and found that user to be the culprit"

    #check the quiz score and mistake score
    if quiz_score == 5 :
        #Win
        p "you scored 5 correct answer:"
        $ win = True
    elif quiz_score == 4:
        p" you scored 4 correct and 1 incorrect answer"
        $win = True
    elif quiz_score == 3:
        p" you scored 3 correct and 2 incorrect answer"
        $win = True
    elif quiz_score == 2:
        p" you scored 2 correct and 3 incorrect answer"
        $win = True
    elif quiz_score == 1:
        p" you scored 1 correct and 4 incorrect answer"
        $win = True


    p happy " Make sure to go to history to check all your progress"
    ##elif misclick == 5:
    #    p "you failed, you had 5 mistakes"
    #    $win = False
    #elif misclick == 4:
    #    p" you faield, you had 4 mistake"
    #    $win = False
    #elif misclick == 3:
    #    p" you faield, you had 4 mistake"
    #    $win = False
    #elif misclick == 2:
    #    p" you faield, you had 4 mistake"
    #    $win = False









    return
