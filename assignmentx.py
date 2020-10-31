from PIL import Image, ImageDraw, ImageFont
import os
import os.path
import time
import string
import random
import shutil

class AssignmentX:
    directoryName = None
    name = None
    opacity = 255
    color1 = (0, 0, 0, 255)
    color2 = (255, 255, 255, 255)
    wtext = None
    opage = None
    sfont = None
    path = None
    path1 = None

    def __init__(self,opacity,color1,color2,wtext,opage,sfont):
        self.opacity = opacity
        self.color1 = color1
        self.color2 = color2
        self.opage = opage
        self.wtext = wtext.rstrip()
        self.sfont = sfont

    def initiateX(self,UPLOAD_FOLDER):
        N = 2
        # directoryName = time.strftime("%Y%m%d-%H%M%S")
        self.directoryName = time.strftime("%Y%m%d-%H%M%S").join(
            random.choices(string.ascii_uppercase + string.digits, k=N)
        )

        self.path = os.path.join(UPLOAD_FOLDER, self.directoryName)
        print(self.path)
        print(self.directoryName)
        os.mkdir(self.path)
        self.path1 = os.path.join(self.path, "output")
        os.mkdir(self.path1)
        
    def assignmentx(self):

        font = list()
        if self.opage == None or self.opage == "ucoePage":
            SheetImage = "D:/CODES/AssignmentX_All_Versions/Assignment_Assistant/AssignmentXAPI/essentials/ucoePage.jpg"
            fontSize = 100
        elif self.opage == "blankPage":
            SheetImage = "D:/CODES/AssignmentX_All_Versions/Assignment_Assistant/AssignmentXAPI/essentials/blankPage.jpg"
            fontSize = 130
        elif self.opage == "oldBlankPage":
            SheetImage = "D:/CODES/AssignmentX_All_Versions/Assignment_Assistant/AssignmentXAPI/essentials/oldBlankPage.jpg"
            fontSize = 130
        elif self.opage == "oldBlueRulePage":
            SheetImage = "D:/CODES/AssignmentX_All_Versions/Assignment_Assistant/AssignmentXAPI/essentials/oldBlueRulePage.jpg"
            fontSize = 100
        else:
            SheetImage = "D:/CODES/AssignmentX_All_Versions/Assignment_Assistant/AssignmentXAPI/essentials/normalPage.jpg"
            fontSize = 100

        if self.wtext == None or self.wtext == "":
            for files in os.listdir(self.path):
                if files.endswith(".txt"):
                    TextFile = os.path.join(self.path, files)
            fileopen = open(TextFile, encoding="utf8")
            text = fileopen.read()
            fileopen.close()
        else:
            text = self.wtext
        # print(self.sfont)
        if self.sfont == "no" or self.sfont == None:
            font.append(
                ImageFont.truetype(
                    "D:/CODES/AssignmentX_All_Versions/Assignment_Assistant/AssignmentXAPI/essentials/Utsav-1.ttf",
                    fontSize,
                )
            )
            font.append(
                ImageFont.truetype(
                    "D:/CODES/AssignmentX_All_Versions/Assignment_Assistant/AssignmentXAPI/essentials/Utsav-2.ttf",
                    fontSize,
                )
            )
            font.append(
                ImageFont.truetype(
                    "D:/CODES/AssignmentX_All_Versions/Assignment_Assistant/AssignmentXAPI/essentials/Utsav-3.ttf",
                    fontSize,
                )
            )
        else:
            for files in os.listdir(self.path):
                if files.endswith(".ttf"):
                    font.append(ImageFont.truetype(os.path.join(self.path, files), fontSize))

        images = list()
        color = self.color1
        pages = 0
        # from numpy import random
        # Opening the blank page
        def type_pages(pages, text, color):

            page = Image.open(SheetImage).convert("RGBA")
            width, height = page.size
            if self.opage == None or self.opage == "ucoePage":
                left_margin = 370
                top_margin = 340
                lineHeight = 95.85
                bottom_margin = 3310

            elif self.opage == "blankPage":
                left_margin = 80
                top_margin = 80
                lineHeight = 130
                bottom_margin = 3380

            elif self.opage == "oldBlankPage":
                left_margin = 100
                top_margin = 100
                lineHeight = 130
                bottom_margin = 3300
            
            elif self.opage == "oldBlueRulePage":
                left_margin = 385
                top_margin = 406
                lineHeight = 102
                bottom_margin = 3345

            else:
                left_margin = 385
                top_margin = 330
                lineHeight = 100.5
                bottom_margin = 3311

            txt = Image.new("RGBA", page.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(txt)
            lwidth = 0
            complete = True

            for index, letter in enumerate(text):
        
                human = random.randint(0, 5)
                fonts = random.choice(font)
                add_sub = random.randint(0, 1)


                tempWidth = draw.textsize(text[index:].split()[0], fonts)[0] + 10

                if (letter != " " and ((width - left_margin) < (lwidth + 50 + tempWidth)) and complete == True):
                    lwidth = 0
                    top_margin += lineHeight
                    complete = False
                    # print(draw.textsize(text[index:].split()[0], fonts)[0])
                    # print(text[index:].split()[0])
                else:
                    complete = True

                if top_margin + lineHeight > bottom_margin:
                    # txt.save("{}{}.png".format(name, pages))
                    txt = Image.alpha_composite(page, txt)
                    images.append(txt.convert("RGB"))
                    print("PRINTED PAGE {}".format(pages + 1))
                    pages += 1
                    text = text[index:]
                    type_pages(pages, text,color)
                    break




                if (letter == "\n") or (lwidth >= (width - left_margin - 30)):
                    lwidth = 0
                    top_margin += lineHeight
                if letter == "\t":
                    lwidth += 100

                if letter == '$' and color == self.color1:
                    color = self.color2
                elif letter == '$' and color == self.color2:
                    color = self.color1
                else:
                    if add_sub == 0:
                        draw.text(
                            (left_margin + lwidth, top_margin + human),
                            letter,
                            fill=color,
                            font=fonts,
                        )
                    else:
                        draw.text(
                            (left_margin + lwidth, top_margin - human),
                            letter,
                            fill=color,
                            font=fonts,
                        )
                    lwidth += draw.textsize(letter, fonts)[0]
                # print(draw.textsize(letter, fonts)[0])
                # print(index)
                if index == len(text) - 1:
                    print("DONE WRITING")
                    txt = Image.alpha_composite(page, txt)
                    images.append(txt.convert("RGB"))

                    images[0].save(
                            "{}.pdf".format(
                                os.path.join(self.path1, self.directoryName)
                            ),
                            save_all=True,
                            append_images=images[1:],
                        )
                    # time.sleep(5)
                    # shutil.rmtree(self.path, ignore_errors=True)
                    # txt.save("{}{}.png".format(name, pages))
                    exit()

            # txt.save("text{}.png".format(pages))


        type_pages(pages, text,color)
    
    def get_path(self):
        return self.path

    def get_path1(self):
        return self.path1

    def get_directoryName(self):
        return self.directoryName