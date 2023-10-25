X   import time
import turtle
from turtle import *
import hashlib
import math
import os

class MediaTopic:
    _questions_answers = {"Media Language": [[
        "\nWhat is Levi Strauss Theory? \n A - Narrative Theory \n B - Structuralism \n C - Male Gaze \n D - Binary opposites\n",
        "\nWhat is a type of camera shot? \n A - Up - Down \n B - Mid Shot \n C - Bottom - Up \n D - Bird-eyes shot\n",
        "\nWhat is a linguistic code? \n A - Finding meaning from the language \n B - Finding meaning from the individual word \n C - Creating meaning through language \n D - Embeded meaning\n",
        "\nWhat is a lexical code?\n A - Finding meaning from the language \n B - Finding meaning from the individual word \n C - Creating meaning through language\n",
        "\nWhat is an indexical code? \n A - Something that has meaning \n B - No link to the meaning \n C - Direct link to meaning being signified \n D - Link we learn through life\n",
        "\nWhat is a mise-en-scene? \n A - What is put into the scene \n B -  What is out of the scene \n C - Props are left out to create meaning \n D - A picture\n",
        "\nWhich of these is not a typical convention of a website? \n A - Social Media Bar \n B - Logo \n C - Toolbar \n D - News Articles\n",
        "\nWhat is a digetic sound? \n A - Fake sound added \n B - Sound that comes from the setting \n C - A loud noise \n D - A noise that you can spell\n",
        "\nWhat is a non-digetic sound? \n A - Fake sound created \n B - Sound that comes from the setting \n C - A loud noise \n D - A noise that you can spell\n",
        "\nWhat is Todorov's theory? \n A - Genre theory \n B - Structuralism \n C - Equilibrium narrative \n D - Binary opposites\n"],
        ["d", "b", "a", "b", "a", "a", "d", "b", "a", "c"]],
        "Media Industries": [[
         "\nWhat is a conglomerate? \n A - A production company \n B - A company that buys other companies \n C - A large company in the media \n C - A company that has been bought \n",
         "\nWhat is a subsidary? \n A - A production company \n B - A company that buys other companies \n C - A large company \n D - A company that has been bought \n",
         "\nWhat is vertical integration? \n A - A company buying other company in the same level of industry \n B - A company buying the production stage \n",
         "\nWhat is horizontal integration? \n A - A company buying other company in the same level of industry \n B - A company buying the production stage \n",
         "\nWhat is a monopoly in media? \n A - A production company \n B - Few organisations control media \n C - One seller dominates the market \n D - Small number of companies that dominate the media \n",
         "\nWhat was Hesmonhalghs theory? \n A - Regulation of media \n B - Media is controlled by companies driven by power and profit \n C - Maximise profits and minimise risks \n",
         "\nHow do we maximise profits and minimise risks? \n A - Vertical and horizontal integration \n B - Representing an ethnic minority \n C - Buying companies in the media \n D - Encoding messages into the product \n",
         "\nWhich of these is an example of a large media conglomerate? \n A - Apple \n B - Samsung \n C - Walt Disney \n D - Adidas \n",
         "\nWho regulates the media \n A - PEGI \n B - GRA \n C - OFQUAL \n D - IWF \n",
         "\nMarxism believes that the bourgeoisie control the media. Is this true? \n Yes(Y) or No(N)"],
        ["c", "d", "a", "b", "c", "c", "a", "c", "c", "y"]],
        "Media Representation": [[
          "\nWhat is the male gaze? \n A - Black males are not represented \n B - Women are overlooked in the media \n C - Media is seen through the eyes of a man \n D - Men creating media products\n",
          "\nWhat is an ideology? \n A - Ideas and beliefs \n B - Ideas and beliefs held by media producers \n C - Message achieved by audience \n D - The way the producer encodes messages\n",
          "\nWhich of these is not a type of black person in the media(Alvarado)? \n A - Kind \n B - Pitied \n C - Dangerous \n D - Humorous\n",
          "\nWhat is a stereotype? \n A - Beliefs about a person \n B - Created ideologies by the media \n C - Basic characteristics which are exaggerated \n D - Describing a group \n",
          "\nWhat is Anchorage? \n A - Words that create meaning \n B - Words go along an image to create meaning \n C - Signs that create meaning \n D - Producers encoding messages \n",
          "\nWhat was Van Zoonen's theory? \n A - Women are there for sexual pleasure \n B - Media portrays image of stereoptypical women \n C - Gender is socially constructed \n D - Black people are under-represented \n",
          "\nWhat was Judith Butler's theory? \n A - Women are there for sexual pleasure \n B - Media portrays image of stereoptypical women \n C - Gender is socially constructed \n D - Social classifications are interconnected \n",
          "\nWhat was bell hooks theory? \n A - Women are in the media for sexual pleasure \n B - Media portrays image of stereoptypical women \n C - Gender is socially constructed \n D - Social classifications are interconnected \n",
          "\nWhat is a constructed identity? \n A - An identity created by the media \n B - Identity constructed by the group represented \n",
          "\nWhat is a hegemonic reading? \n A - Disagreeing with the desired message \n B - Agree with some of the desired message \n C - Agree completely with the desired message\n"],
        ["c", "a", "a", "c", "b", "b", "c", "d", "a", "b"]],
        "Media Audience": [[
            "\nWhat is the cultivation theory? \n A - Transformation from print to online \n B - Repetition of ideologies by the media \n C - Only exposed to one source of media \n D - Bias in the media \n",
            "\nWhat is a prosumer? \n A - A person who receives and creates their own media \n B - A person who only receives media\n",
            "\nWhat is a consumer? \n A - A person who receives and creates their own media \n B - A person who only receives media\n",
            "\nWhat is fandom? \n A - Group of fans \n B - People who buy the product \n C - Active participants \n D - Fans who do not create their own media\n",
            "\nWhat is a oppositional reading? \n A - Disagreeing with the desired message \n B - Agree with some of the desired message \n C - Agree completely with the desired message\n",
            "\nWhat has had a major effect on the relationship between media and individuals? \n A - Audience Interpretations \n B - Stereotypes \n C - NDM \n D - Mass Media\n",
            "\nName one strand of the U&G theory \n A - Homeostasis \n B - Acheivement by others \n C - Respect by others \n D - Surveillance \n",
            "\nWho proposed the U&G theory? \n A - Adorno \n B - Bulmer and Katz \n C - Jenkins \n D - Bandura \n",
            "\nWhat is an objectivist? \n A - Will not debate or argue with what they hear in the media \n B - Will question what they hear in the media \n",
            "\nWhat is a collectivist? \n A - Will not debate or argue with what they hear in the media \n B - Will question what they hear in the media \n"],
            ["b", "a", "b", "c", "a", "b", "d", "b", "d", "a"]]
        }

    def __init__(self, topic):
        self.topic = topic
        self.questions = self._questions_answers[topic]
        print("\n")
        print("It seems like last time, you struggled with " + topic)

    def run_test(self):
        weaknessscore = 0
        while weaknessscore != 5:
            for i, question in enumerate(self.questions[0]):
                answer = input(question).lower()
                if answer == self.questions[1][i]:
                    print("Correct")
                    weaknessscore = weaknessscore + 1
                    if weaknessscore == 5:
                        print("You have successfully learnt " + self.topic)
                        break
                else:
                    print("Incorrect")

def StartGame():
    # start identification
    print("Welcome to RevForYou!")
    time.sleep(1)
    print("This program has been designed to make Media revision enjoyable and educational!")
    time.sleep(1)
    print("But first, I need to find out if you are a new or returning user")
    time.sleep(0.5)
    Registered = False
    while not Registered:
        ReturningOrNot = input("Are you a new[n] or returning[r] user?")
        # new user
        if ReturningOrNot.upper() == "N":
            try:
                global NewUsername
                NewUsername = input("Please create a username!")
                if not NewUsername.isalpha():
                    raise TypeError
                else:
                    try:
                        filename = NewUsername + ".txt"
                        try:
                            NewPassword = input("Please create a Password!")
                            if not NewPassword.isalpha():
                                raise TypeError
                            try:
                                folder = "/Users/ymalek_/Desktop"
                                global myfile
                                myfile = open(os.path.join(folder, filename), "w")
                                md5 = hashlib.md5()
                                md5.update(NewPassword.encode())
                                myfile.write(md5.hexdigest())
                                myfile.write("\n")
                                Registered = True
                            except:
                                print("Could not hash password")
                        except TypeError:
                            print("No numbers or special characters")
                    except:
                        print("File already exists")
            except TypeError:
                print("Please do not enter any numbers or special characters")
        # returning user
        if ReturningOrNot.upper() == "R":
            try:
                ReturningUsername = input("Please enter your username!")
                if not ReturningUsername.isalpha():
                    raise TypeError
                else:
                    try:
                        file_name = ReturningUsername + ".txt"
                        try:
                            folder = "/Users/ymalek_/Desktop"
                            myfile = open(os.path.join(folder, file_name), "r")
                            try:
                                ReturningPassword = input("Please enter your password!")
                                if not ReturningPassword.isalpha():
                                    raise TypeError
                                md5 = hashlib.md5()
                                md5.update(ReturningPassword.encode())
                                first_line = myfile.readline()
                                if md5.hexdigest() in first_line:
                                    print("Password authorised, logging in")
                                    try:
                                        lines = myfile.readlines()
                                        GetTopic = lines[-1].strip()
                                        if GetTopic == "Language":
                                            MediaTopic("Media Language").run_test()
                                        if GetTopic == "Industries":
                                            MediaTopic("Media Industries").run_test()
                                        if GetTopic == "Representation":
                                            MediaTopic("Media Representation").run_test()
                                        if GetTopic == "Audience":
                                            MediaTopic("Media Audience").run_test()
                                        Registered = True
                                    except:
                                        print("Could not find what your last weakness was")
                                else:
                                    print("Wrong password")
                            except TypeError:
                                print("For your password, please do not enter numbers or special characters")
                        except:
                            print("Could not read from destination.")
                    except:
                        print("File does not exist in your username")
            except TypeError:
                print("For your username, please do not enter numbers or special characters")

StartGame()

class Screen():

    def __init__(self):
        self._initilise_screen()

    def _initilise_screen(self):
        screen = turtle.Screen()
        screen.bgcolor('lightblue')
        speed(200)
        penup()
        goto(-140, 140)
        for step in range(21):
            write(step, align='center')
            right(90)
            for num in range(8):
                penup()
                forward(10)
                pendown()
                forward(10)
            penup()
            backward(160)
            left(90)
            forward(20)

Screen()

class BaseCharacter:

    def __init__(self, name, topic):
        self.__name = name
        self.__topic = topic

    def recall(self):
        print("\n")
        print("Hey, I am " + self.__name)
        print("I am going to test you on " + self.__topic)






class QuestionNode:
    def __init__(self, question, answer, difficulty=0):
        self.__question = question
        self.__answer = answer
        self.__correct = difficulty

    def getDifficulty(self):
        return self.__correct

    def printQuestion(self):
        print(self.__question)

    def checkAnswer(self, answer):
        result = self.__answer == answer
        if result:
            self.__correct += 1
        else:
            self.__correct -= 1
        return result


class Character(BaseCharacter):

    def __init__(self, name, topic, question_bank):
        super(Character, self).__init__(name, topic)
        self.question_tree = self.buildQuestionTree(question_bank)
        self.sortTree()
        self.recall()

    def buildQuestionTree(self, question_bank):
        question_tree = []
        for q, a, d in zip(question_bank[0],question_bank[1],question_bank[2]):
            question_tree.append(QuestionNode(q,a,d))
        return question_tree

    def sortTree(self):
        swapped = True
        noofiterations = 0
        while (swapped):
            swapped = False
            for x in range(len(self.question_tree) - noofiterations - 1):
                if self.question_tree[x].getDifficulty() > self.question_tree[x + 1].getDifficulty():
                    self.question_tree[x], self.question_tree[x + 1] = self.question_tree[x + 1], self.question_tree[x]
                    swapped = True
            noofiterations += noofiterations


class Pikachu(Character):
    language_questions = [[
        "\nWhat is Levi Strauss Theory? \n A - Narrative Theory \n B - Structuralism \n C - Male Gaze \n D - Binary opposites\n",
        "\nWhat is a type of camera shot? \n A - Up - Down \n B - Mid Shot \n C - Bottom - Up \n D - Bird-eyes shot\n",
        "\nWhat is a linguistic code? \n A - Finding meaning from the language \n B - Finding meaning from the individual word \n C - Creating meaning through language \n D - Embeded meaning\n",
        "\nWhat is a lexical code?\n A - Finding meaning from the language \n B - Finding meaning from the individual word \n C - Creating meaning through language\n",
        "\nWhat is an indexical code? \n A - Something that has meaning \n B - No link to the meaning \n C - Direct link to meaning being signified \n D - Link we learn through life\n",
        "\nWhat is a mise-en-scene? \n A - What is put into the scene \n B -  What is out of the scene \n C - Props are left out to create meaning /n D - A picture\n",
        "\nWhich of these is not a typical convention of a website? \n A - Social Media Bar \n B - Logo \n C - Toolbar \n D - News Articles\n",
        "\nWhat is a digetic sound? \n A - Fake sound added \n B - Sound that comes from the setting \n C - A loud noise \n D - A noise that you can spell\n",
        "\nWhat is a non-digetic sound? \n A - Fake sound created \n B - Sound that comes from the setting \n C - A loud noise \n D - A noise that you can spell\n",
        "\nWhat is Todorov's theory? \n A - Genre theory \n B - Structuralism \n C - Equilibrium narrative \n D - Binary opposites\n",
        "\nWhat is a non-digetic sound? \n A - Fake sound created \n B - Sound that comes from the setting \n C - A loud noise \n D - A noise that you can spell\n",
        "\nWhat is Roland Barthes theory \n A - Binary opposites \n B - Semiotics \n C - Narrative theory \n D - Equilibrium",
        "\nWhat is Propp theory? \n A - Binary opposites \n B - Narrative theory \n C - Type of characters \n D - Post-coloniasm",
        "\nHow did media language create meaning in the score hair creamn advert? \n A - Through representation of women \n B - Through the industry \n C - Through the interpretation of the audience \n D - Through the use of media language \n",
        "\nWhat is Steve Neale theory? \n A - Narratology \n B - Structalism \n C - Instances of repetition and differences \n D - Postmodernism \n",
        "\nWhat is postmodernism? \n A - The real world is fake \n B - Boundaries of real-world and media have collapsed \n C - Simulation is preferred to reality \n D - Simulation replaces reality \n",
        "\nWhat is an extreme close up? \n A - Very close shot \n B - Cannot see anything \n C - Shows particular thing with extreme detail \n D - Back-up shot \n",
        "\nWhat is an antagonist? \n A - Villain \n B - Hero \n C - Someone who needs saving \n D - Helper \n",
        "\nWhat is a protagonist? \n A - Villain \n B - Hero \n C - Smeone who needs saving \n D - Helper \n",
        "\nWhich one of these is a typical convention of crime dramas? \n A - Eeery music \n B - Comedy \n C - Enigmas \n D - Romance \n",
        "\nWhat is a genre? \n A - Type of film \n B - Characterising stores, characters and plot structures \n C - RomCom \n D - Type of storyline \n",
        "\nWhat is a structuralist? \n A - How societies interpret different media languages \n B - Preferring a false reality \n C - Evolution of interpretations \n D - Evolution of ideologies \n",
        "\nWhat is the study of semiotics? \n A - Interpretations \n B - Binary opposites \n C - Sounds \n D - Signs and symbols \n",
        "\nWhat is a connotation? \n A - Literal meaning \n B - Implied meaning \n",
        "\nWhat is a denotation? \n A - Literal meaning \n B - Implied meaning \n",
        "\nWhat does it mean to encode? \n A - Put something in \n B - Trying to create meaning \n C - Messages placed within a product \n D - Reading of product \n",
        "\nWhat does it mean to decode? \n A - Put something in \n B - Trying to create meaning \n C - Messages placed wihin a product \n D - Audience interpretation \n",
        "\nWhat is an enigma? \n A - A cliffhanger \n B - Something that the audience question \n C - Unsolved crime \n D - Gap in series \n",
        "\nWhat is an equilibrium? \n A - Sense of normality \n B - Balance \n C - Start \n D - Ending \n",
        "\nWhat is a disequilibrium? \n A - Sense of normality \n B - Balance \n C - Start \n D - Challenging normality \n",
        "\nWhat does it mean to anchor something? \n A - Elements of text combining to create meaning \n B - Images alongside text create meaning \n C - An example \n D - Anchoring an image",
        "\nWhat is a myth? \n A - Fake story \n B - Dominant ideologies of time \n C - Mythical storyline \n D - Narrative based on moral panics\n",
        "\nAnother word for diegesis \n A - Diagnosis \n B - Equilibrium \n C - Narrative \n D - Plot \n",
        "\nWhat is genre hybridity? \n A - Combination of two genres \n B - Convergence of NDM \n C - Not liking a genre \n D - NDM combining with moral panics to create a new genre \n",
        "\nWhat is a signifier? \n A - Connotations \n B - Interpretations \n C - Language feature \n D - Form of a sign \n",
        "\nWhat is an action code? \n A - Something which suggests an action \n B - An action feature \n C - Aggressive action \n D - Connotation of a code \n",
        "\nWhy do we associate red with danger or stop? \n A - Society taught us \n B - Literal denotation \n C - Generational ideologies \n"],
        ["d", "b", "a", "b", "c", "a", "d", "b", "a", "a", "b", "c", "d", "c", "b", "c", "a", "b", "c", "b", "a", "d","b", "a", "c", "d", "b", "a", "d", "a", "b", "c", "a", "d", "a", "a"],
        [10, 12, 15, 18, 17, 32, 2, 34, 28, 6, 30, 16, 27, 22, 24, 7, 31, 35, 11, 25, 1, 3, 23, 8, 29, 4, 26, 13, 20, 19, 5, 21, 9, 14, 33, 36]]

    name = "Pikachu"
    topic = "Media Language"

    def __init__(self):
        super(Pikachu, self).__init__(self.name, self.topic, self.language_questions)
        self.runTree()


    # runs the tree traversal function on the question_tree array
    def runTree(self):
        global pikachucorrect
        pikachucorrect = 0
        Pikachuturtle = Turtle()
        Pikachuturtle.color("yellow")
        Pikachuturtle.shape("turtle")
        Pikachuturtle.penup()
        Pikachuturtle.goto(-160, 110)
        Pikachuturtle.pendown()
        for turn in range(10):
            Pikachuturtle.right(36)
        depth = int(math.log2(len(self.question_tree) + 1))
        current = int(len(self.question_tree) / 2)
        for i in range(depth):
            print(self.question_tree[current].printQuestion())
            answer = input("What is your answer?").lower()
            correct = self.question_tree[current].checkAnswer(answer)
            if correct:
                current += depth - i
                print("Correct")
                pikachucorrect = pikachucorrect + 1
                for turn in range(30):
                    Pikachuturtle.forward(3)
            else:
                print("Incorrect")
                current -= depth + i


class Thor(Character):
    industry_questions = [[
    "\nWhat is a conglomerate? \n A - A production company \n B - A company that buys other companies \n C - A large company in the media \n D - A company that has been bought \n",
    "\nWhat is a subsidary? \n A - A production company \n B - A company that buys other companies \n C - A large company \n D - A company that has been bought \n",
    "\nWhat is vertical integration? \n A - A company buying other company in the same level of industry \n B - A company buying the production stage \n",
    "\nWhat is horizontal integration? \n A - A company buying other company in the same level of industry \n B - A company buying the production stage \n",
    "\nWhat is a monopoly in media? \n A - A production company \n B - Few organisations control media \n C - One seller dominates the market \n D - Small number of companies that dominate the media \n",
    "\nWhat was Hesmonhalghs theory? \n A - Regulation of media \n B - Media is controlled by companies driven by power and profit \n C - Maximise profits and minimise risks \n",
    "\nHow do we maximise profits and minimise risks? \n A - Vertical and horizontal integration \n B - Representing an ethnic minority \n C - Buying companies in the media \n D - Encoding messages into the product \n",
    "\nWhich of these is an example of a large media conglomerate? \n A - Apple \n B - Samsung \n C - Walt Disney \n D - Adidas \n",
    "\nWho regulates the media \n A - PEGI \n B - GRA \n C - OFQUAL \n D - IWF \n",
    "\nMarxism believes that the bourgeoisie control the media. Is this true? \n Yes(Y) or No(N)",
    "\nWhat was Karl Marx's theory? \n A - Constructivism \n B - Control media \n C - Marxism \n D - Objectivism \n",
    "\nWhat is media regulation? \n A - Controlling the media \n B - Protection of the media \n C - Protection of the audience \n D - Circulation protection \n",
    "\nWhat is synergy? \n A - Cross-platform promotions \n B - NDM \n C - Multi-company promotions \n D - Promotion \n",
    "\nWhat is media convergence? \n A - Combination of platforms \n B - Audience using one platform to consume various types of media \n C - One company dominating the media \n D  - Limit on consumption \n",
    "\nWhat does PSB stand for? \n A - Person-service broadcast \n B - Public service broadcast \n C - Person survey broadcast \n D - Play service broadcast \n",
    "\nWhat are the three reithian values? \n A - Enjoy,Entertain,Play \n B - Entertain,Publicity,Fame \n C - BBC,Video,Radio \n D - Inform,Educate,Entertain \n",
    "\nWhat is an example of a PSB? \n A - BBC \n B - ITV \n C - Sky \n D - Netflix \n",
    "\nWhat is an independent film? \n A - Film about a social message \n B - Film that has no publicity \n C - Film that has a small budget due to a lack of funding \n D - Film that cannot be advertised \n",
    "\nWhat is an oligopoly? \n A - Market is dominated by big companies \n  B - Market is dominated by small companies \n",
    "\nWhat are the three types of media? \n A - Games,TV,Social Media \n B - Radio,TV,Print \n C - Phone,TV,Radio \n D - Print,Broadcast,NDM \n",
    "\nWhat is capitalism? \n A - Protection of media \n B - Limit of what is in the media \n C -  Control of media \n D - Private owners controlling trades for profit \n",
    "\nWhich of these can be a two-way interaction? \n A - Print \n Broadcast \n C - NDM",
    "\nWhat does PEGI stand for? \n A - Pro european grand information \n B - Pan european game information \n Pan ethnic game instituition \n Pan european game instituition \n",
    "\nWhat is Curran and Seaton's theory? \n A - Patterns of ownership \n B - Maximise profits and minimising risk \n C - Media regulation \n",
    "\nWhat is Livingstone and Lunt's theory? \n A - Patterns of ownership \n B - Maximise profits and minimising risk \n C - Media regulation \n",
    "\nHow has NDM impacted print? \n A - Increased circulation figures \n B - Decreased circulation figures \n C - Circulation figures stayed around the same \n",
    "\nWhat has NDM allowed people to do? \n A - Interact \n B - Read news \n C - Play games \n D - Be entertained \n",
    "\nHow to TV shows attempt to get a younger audience? \n A - Use known actors \n B - Set it somewhere nice \n C - Use social dillemas \n D - Put show on streaming sites \n",
    "\nHow did blinded by the light distribute their film? \n A - Film festival \n B - Social media \n C - Investment company \n D - Guerilla marketing \n",
    "\nHow is BBC radio funded? \n A - Tax \n B - Investors \n C - Hypothecated tax \n D - Funded by their own company \n",
    "\nWhy did Newsbeat go onto IPlayer? \n A - So people can catch up \n B - To appeal to younger audiences \n C - To earn more money \n D - Radio circulation figures were decreasing \n",
    "\nWhat emerged in the 1930/40s \n A - Newspapers \n B - Phones \n C - Coloured TVs \n D - Radio \n",
    "\nWhat did Iceberg press create? \n A - Newsbeat \n B - Men's Health \n C - Oh Comely \n D - Teen Vogue \n",
    "\nWhat is Iceberg press driven by? \n A - Profit \n B - Their audience \n",
    "\nWhat did Hearst Co-operations create? \n A - The Voice \n B - Teen Vogue \n C - Score hair cream \n D - Men's health \n",
    "\nWhat is Hearst Co-operations driven by? \n A - Profit \n B - Their audience \n"],
        ["c","d","b","a","c","c","a","c","c","y","c","c","a","b","b","d","a","b","b","d","d","c","b","a","c","b","a","d","b","c","b","a","c","b","d","a"],
        [13,16,9,24,22,8,2,18,7,5,6,23,34,33,12,27,15,21,11,1,30,25,19,10,29,14,28,35,20,31,32,26,36,4,3,17]]

    name = "Thor"
    topic = "Media Industries"

    def __init__(self):
        super(Thor, self).__init__(self.name, self.topic, self.industry_questions)
        self.runTree()

    def runTree(self):
        global thorcorrect
        thorcorrect = 0
        thorturtle = Turtle()
        thorturtle.color("blue")
        thorturtle.shape("turtle")
        thorturtle.penup()
        thorturtle.goto(-160, 80)
        thorturtle.pendown()
        for turn in range(10):
            thorturtle.right(36)
        depth = int(math.log2(len(self.question_tree) + 1))
        current = int(len(self.question_tree) / 2)
        for i in range(depth):
            print(self.question_tree[current].printQuestion())
            answer = input("What is your answer?").lower()
            correct = self.question_tree[current].checkAnswer(answer)
            if correct:
                current += depth - i
                print("Correct")
                thorcorrect = thorcorrect + 1
                for turn in range(30):
                    thorturtle.forward(3)
            else:
                print("Incorrect")
                current -= depth + i


class Luigi(Character):
    representation_questions = [[
    "\nWhat is the male gaze? \n A - Black males are not represented \n B - Women are overlooked in the media \n C - Media is seen through the eyes of a man \n D - Men creating media products\n",
    "\nWhat is an ideology? \n A - Ideas and beliefs \n B - Ideas and beliefs held by media producers \n C - Message achieved by audience \n D - The way the producer encodes messages\n",
    "\nWhich of these is not a type of black person in the media(Alvarado)? \n A - Kind \n B - Pitied \n C - Dangerous \n D - Humorous\n",
    "\nWhat is a stereotype? \n A - Beliefs about a person \n B - Created ideologies by the media \n C - Basic characteristics which are exaggerated \n D - Describing a group \n",
    "\nWhat is Anchorage? \n A - Words that create meaning \n B - Words go along an image to create meaning \n C - Signs that create meaning \n D - Producers encoding messages \n",
    "\nWhat was Van Zoonen's theory? \n A - Women are there for sexual pleasure \n B - Media portrays image of stereoptypical women \n C - Gender is socially constructed \n D - Black people are under-represented \n",
    "\nWhat was Judith Butler's theory? \n A - Women are there for sexual pleasure \n B - Media portrays image of stereoptypical women \n C - Gender is socially constructed \n D - Social classifications are interconnected \n",
    "\nWhat was bell hooks theory? \n A - Women are in the media for sexual pleasure \n B - Media portrays image of stereoptypical women \n C - Gender is socially constructed \n D - Social classifications are interconnected \n",
    "\nWhat is a constructed identity? \n A - An identity created by the media \n B - Identity constructed by the group represented \n",
    "\nWhat is a hegemonic reading? \n A - Disagreeing with the desired message \n B - Agree with some of the desired message \n C - Agree completely with the desired message\n",
    "\nWhat is a subverted stereotype? \n A - Supporting norms of society \n B - Support typical stereotypical ideologies \n C  - Protesting against dominant ideology \n",
    "\nWhat was Baudrillard's theory? \n A - Structalism \n B - Marxism \n C - Media reflecting stereotypcial gender roles \n D - Representation of black people \n",
    "\nWhat is a hyperreality? \n A - Representations replace reality \n B - Simulation is preferred to reality \n C - Postmodern concept \n D - Simulacra replaces reality \n",
    "\nWhat is a constructivist? \n A - Would accept everything they hear in the media \n B - Would challenge what they hear in the media \n",
    "\nWhat is an objectivist? \n A - Would accept everything they hear in the media \n B - Would challenge what they hear in the media \n",
    "\nIn the witnesses, how were muslim refugees represented as? \n A - Role-models \n B - Pitied \n C - Counter-stereotyped \n D - Ideological views \n",
    "\nWhat was Alvarado's theory? \n A - Gender in the media \n B - Gay people in the media \n C - Muslims in the media \n D - Black people in the media \n",
    "\nWhat is voyeurism? \n A - Mis-representations \n B - Gender \n C - Pleasure from observations \n D - Stereotypes \n",
    "\nDid the score cream hair advert subvert or conform gender stereotypes? \n A - Subvert \n B - Conform \n",
    "\nDid the maybelline advert subvert or conform gender stereotypes? \n A - Subvert \n B - Conform \n",
    "\nWhat was David Gauntlett's theory? \n A - Women are there for sexual pleasure \n B - Media portrays images of stereotypical women \n C - Identity is becoming more fluid \n D - Gender is socially constructed \n",
    "\nWhat would a preferred reading of the Score hair cream advert be? \n A - The roles are perfectly fine and reflect society \n B - Notices the problem but thinks nothing of it \n C - Disagreeing with the gender roles \n",
    "\nWhat reading would people in the time of score take? \n A - Preferred \n B - Negotiated \n C - Oppositional \n",
    "\nWhat reading would people in the current times take of score? \n A - Preferred \n B - Negotiated \n C - Oppositional \n",
    "\nWhat an oppositional reading of the Score hair cream advert be? \n A - The roles are perfectly fine and reflect society \n B - Notices the problem but thinks nothing of it \n C - Disagreeing with the gender roles \n",
    "\nWhat would a preferred reading of the maybelline advert be? \n A - The roles are perfectly fine and reflect society \n B - Notices the problem but thinks nothing of it \n C - Disagreeing with the gender roles \n",
    "\nWhat reading would people in the past take of maybelline? \n A - Preferred \n B - Negotiated \n C - Oppositional \n",
    "\nWhat reading would people now take of maybelline? \n A - Preferred \n B - Negotiated \n C - Oppositional \n",
    "\nWhat Netlix documentary was Letter to the free based off? \n A - 5 of us \n B - 13th \n C - Rosa Parks \n D - Central Park 5 \n",
    "\nWhat is Tajfel's theory? \n A - Consumers becoming prosumers \n B - Gender is performative \n C - Postmodernism \n D - Us vs them \n",
    "\nWhat is Gilroy's theory? \n A - Structuralism \n B - Postcolonialism \n C - Postmodernism \n D - Prosumerism \n",
    "\nHow were prisons represented in letter to the free? \n A - Conformed stereotypes of prisons \n B - Subverted stereotypes of prisons \n",
    "\nHow has the representations of gender changed over time? \n A - Gender has stayed the same \n B - Gender has evolved \n C - Gender has been fully subverted \n",
    "\nWhat reading would a prosumer take of a media product? \n A - Preferred \n B - Negotiated \n C - Oppositional \n",
    "\nWhat reading would a consumer take of a media product? \n A - Preferred \n B - Negotiated \n C - Oppositional \n"],
        ["c","b","a","b","d","d","c","b","a","c","c","c","b","a","b","b","d","c","b","a","c","a","a","c","c","c","c","a","b","d","b","b","c","a","c"],
        [10,36,7,15,33,34,21,29,2,27,8,16,25,20,11,28,23,22,12,6,17,13,30,5,3,32,18,1,4,26,14,31,9,24,19]]

    name = "Luigi"
    topic = "Media Representations"

    def __init__(self):
        super(Luigi, self).__init__(self.name, self.topic, self.representation_questions)
        self.runTree()

    def runTree(self):
        global luigicorrect
        luigicorrect = 0
        luigiturtle = Turtle()
        luigiturtle.color("red")
        luigiturtle.shape("turtle")
        luigiturtle.penup()
        luigiturtle.goto(-160, 50)
        luigiturtle.pendown()
        for turn in range(10):
            luigiturtle.right(36)
        depth = int(math.log2(len(self.question_tree) + 1))
        current = int(len(self.question_tree) / 2)
        for i in range(depth):
            print(self.question_tree[current].printQuestion())
            answer = input("What is your answer?").lower()
            correct = self.question_tree[current].checkAnswer(answer)
            if correct:
                current += depth - i
                print("Correct")
                luigicorrect = luigicorrect + 1
                for turn in range(30):
                    luigiturtle.forward(3)
            else:
                print("Incorrect")
                current -= depth + i




class Hulk(Character):
    audience_questions = [[
    "\nWhat is the cultivation theory? \n A - Transformation from print to online \n B - Repetition of ideologies by the media \n C - Only exposed to one source of media \n D - Bias in the media \n",
    "\nWhat is a prosumer? \n A - A person who receives and creates their own media \n B - A person who only receives media\n",
    "\nWhat is a consumer? \n A - A person who receives and creates their own media \n B - A person who only receives media\n",
    "\nWhat is fandom? \n A - Group of fans \n B - People who buy the product \n C - Active participants \n D - Fans who do not create their own media\n",
    "\nWhat is a oppositional reading? \n A - Disagreeing with the desired message \n B - Agree with some of the desired message \n C - Agree completely with the desired message\n",
    "\nWhat has had a major effect on the relationship between media and individuals? \n A - Audience Interpretations \n B - Stereotypes \n C - NDM \n D - Mass Media\n",
    "\nName one strand of the U&G theory \n A - Homeostasis \n B - Acheivement by others \n C - Respect by others \n D - Surveillance \n",
    "\nWho proposed the U&G theory? \n A - Adorno \n B - Bulmer and Katz \n C - Jenkins \n D - Bandura \n",
    "\nWhat is an objectivist? \n A - Will not debate or argue with what they hear in the media \n B - Will question what they hear in the media \n",
    "\nWhat is a collectivist? \n A - Will not debate or argue with what they hear in the media \n B - Will question what they hear in the media \n",
    "\nWhat is the diversion strand of U&G? \n A - Self-reflection in the media \n B - Using the media to know what is happening around you \n C - Media offers relationships \n D - Using media to escape from routine \n",
    "\nWhat is the surveillance strand of U&G? \n A - Self-reflection in the media \n B - Using the media to know what is happening around you \n C - Media offers relationships \n D - Using media to escape from routine \n",
    "\nWhat is the personal relationship strand of U&G? \n A - Self-reflection in the media \n B - Using the media to know what is happening around you \n C - Media offers relationships \n D - Using media to escape from routine \n",
    "\nWhat is the personal identity strand of U&G? \n A - Self-reflection in the media \n B - Using the media to know what is happening around you \n C - Media offers relationships \n D - Using media to escape from routine \n",
    "\nWhat is a passive audience? \n A - An audience that only consumes media \n B - An audience that consumes and creates their own media \n",
    "\nWhat is a active audience? \n A - An audience that only consumes media \n B - An audience that consumes and creates their own media \n",
    "\nWhat is the hypodermic needle theory? \n A - Ideologies are directly told to the audience \n B - Ideologies are told to the audience over time\n",
    "\nWhat is the cultivation theory? \n A - -Ideologies are directly told to the audience \n B - Ideologies are told to the audience \n",
    "\nWhat is a niche audience? \n A - Large Group \n B - Small group \n C - Specific demographic \n D - Large demographic \n",
    "\nWhat is a mass audience? \n A - Large Group \n B - Small group \n C - Specific demographic \n D - Large demographic \n",
    "\nWhat is a moral panic? \n A - Popular story in the media \n B - Story that has the audience frightened \n C - Strong negative audience reactions about a social behaviour \n D - Audience panic",
    "\nWhat was the moral panic in War of the worlds? \n A - War \n B - Germans bombing the US \n C - Halloween prank \n D - Alien Invasion \n",
    "\nWhy did the audience believe the 'prank'? \n A - Less forms of radio \n B - They took the preferred reading \n C - Time of prank was a time of worry \n D - It was halloween so they were already frightened \n",
    "\nWhat was Clay Shirky's theory? \n A - Hypodermic Needle theory \n B - Cultivation theory \n C - End of Audiences \n D - Fandom \n",
    "\nWhat is the 'End of Audienes'? \n A - Emergence of NDM \n B - Audience stopping print \n C - Audiences are no longer passive, they are now active \n",
    "\nWhy did Newsbeat purposely put their program on at midday? \n A - Most money to be made \n B - Strict schedule \n C - People have breaks or are off work \n D - Pre-recorded \n",
    "\nDuring the time of War of the worlds, were audiences passive or active? \n A - Passive \n B - Active \n",
    "\nDuring the time of Newsbeat, were audiences passive or active? \n A - Passive \n B - Active \n",
    "\nWhy was Blinded by the light successful? \n A - Used known actors \n B - Came with a presold audience \n C - Big budget \n D - Released on streaming sites \n",
    "\nHow did Blinded by the light target certain audiences? \n A - Social media \n B - Film Festival \n C - Guerilla Marketing \n",
    "\nWhat demographic did Blinded by the light target? \n A - A1 \n B - AB1 \n C - ABC1 \n D - All demographics \n",
    "\nWho did The Voice newspaper target? \n A - White people \n B - Asian people \n C - LGBT people \n D - Black people \n",
    "\nWhat demographic did Oh Comely target? \n A - A1 \n B - AB1 \n C - ABC1 \n D - All demographics \n",
    "\nWhat is a preferred reading? \n A - What the readers want you to decode \n B - Broadly accepting the preferred reading \n C - Interpreting the product in the complete wrong way \n",
    "\nWhat is a negotiated reading? \n A - What the readers want you to decode \n B - Broadly accepting the preferred reading \n C - Interpreting the product in the complete wrong way \n",
    "\nWhat is a oppositional reading? \n A - What the readers want you to decode \n B - Broadly accepting the preferred reading \n C - Interpreting the product in the complete wrong way \n"],
        ["b","a","b","c","a","c","d","b","b","a","d","b","c","a","a","b","a","b","b","a","c","d","a","c","c","c","a","b","b","a","d","d","b","a","b","c"],
        [30,15,21,12,32,11,18,2,9,6,26,10,1,20,31,8,24,13,5,34,3,28,17,35,23,33,7,19,14,25,29,22,4,16,27,36]]

    name = "Hulk"
    topic = "Media Audiences"

    def __init__(self):
        super(Hulk, self).__init__(self.name, self.topic, self.audience_questions)
        self.runTree()

    def runTree(self):
        global hulkcorrect
        hulkcorrect = 0
        hulkturtle = Turtle()
        hulkturtle.color("green")
        hulkturtle.shape("turtle")
        hulkturtle.penup()
        hulkturtle.goto(-160, 20)
        hulkturtle.pendown()
        for turn in range(10):
            hulkturtle.right(36)
        depth = int(math.log2(len(self.question_tree) + 1))
        current = int(len(self.question_tree) / 2)
        for i in range(depth):
            print(self.question_tree[current].printQuestion())
            answer = input("What is your answer?").lower()
            correct = self.question_tree[current].checkAnswer(answer)
            if correct:
                current += depth - i
                print("Correct")
                hulkcorrect = hulkcorrect + 1
                for turn in range(30):
                    hulkturtle.forward(3)
            else:
                print("Incorrect")
                current -= depth + i

if __name__ == "__main__":
    pikachu = Pikachu()
    thor = Thor()
    luigi = Luigi()
    hulk = Hulk()

class Game:

    def __init__(self):
        self.Scores = [pikachucorrect, thorcorrect, luigicorrect, hulkcorrect]

        if __name__ == '__main__':
            print("\n")
            print("Given array is", end="\n")
            self.printList(self.Scores)
            self.SortScores(self.Scores)
            print("\n")
            print("Sorted array is: ", end="\n")
            self.printList(self.Scores)

        self.EndGame()

    def FileWrite(self, x):
        myfile.write("\n")
        myfile.write(x)


    def EndGame(self):
        print("\n")
        print("Language Score =", pikachucorrect)
        print("Industry Score =", thorcorrect)
        print("Representation Score =", luigicorrect)
        print("Audience Score =", hulkcorrect)

        Scorespop0 = self.Scores.pop(0)
        if Scorespop0 == pikachucorrect:
            print("Media Language is your weakest!")
            MediaTopic("Media Language").run_test()
            try:
                self.FileWrite(x="Language")
            except:
                print("Could not write to file")
        if Scorespop0 == thorcorrect:
            print("Media Industries is your weakest!")
            MediaTopic("Media Industries").run_test()
            try:
                self.FileWrite(x="Industries")
            except:
                print("Could not write to file")
        if Scorespop0 == luigicorrect:
            print("Media Representation is your weakest!")
            MediaTopic("Media Representation").run_test()
            try:
                self.FileWrite(x="Representation")
            except:
                print("Could not write to file")

        if Scorespop0 == hulkcorrect:
            print("Media Audience is your weakest!")
            MediaTopic("Media Audience").run_test()
            try:
                self.FileWrite(x="Industries")
            except:
                print("Could not write to file")

    def SortScores(self, Scores):
        if len(Scores) > 1:

            mid = len(Scores) // 2

            L = Scores[:mid]

            R = Scores[mid:]

            self.SortScores(L)
            self.SortScores(R)

            i = j = k = 0

            while i < len(L) and j < len(R):
                if L[i] < R[j]:
                    Scores[k] = L[i]
                    i += 1
                else:
                    Scores[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                Scores[k] = L[i]
                i += 1
                k += 1

            while j < len(R):
                Scores[k] = R[j]
                j += 1
                k += 1

    def printList(self, Scores):
        for i in range(len(Scores)):
            print(Scores[i], end=" ")
        print()


Game()
