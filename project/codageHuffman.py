from manim import *
import numpy as np


class CircleWithContent(VGroup):
    def __init__(self, content):
        super().__init__()
        self.circle = Circle()
        self.circle.set_fill(BLACK, opacity=1)
        self.content = content
        self.add(self.circle, content)
        content.move_to(self.circle.get_center())

    def clear_content(self):
        self.remove(self.content)
        self.content = None

    @override_animate(clear_content)
    def _clear_content_animation(self):
        anim = Uncreate(self.content)
        self.clear_content()
        return anim


#######################
#
# T I T R E
#
#######################

class Titre(Scene):
    def construct(self):
       
        l0 = Tex(r'Codage de Huffman',color=BLUE).scale(2).move_to(np.array([0,2,0]))
        l1 = Tex(r"Murièle Jacquier \& Simon Verdan").scale(1).next_to(l0, direction=3*DOWN)
        l2 = Tex(r"Algorithmes et structures de données - I").scale(.7).next_to(l1, direction=10*DOWN)
        l3 = Tex(r"GymInf 2021").scale(.7).next_to(l2, direction=DOWN)
       
       
        self.play(Write(l0))
        self.play(FadeIn(l1))
        self.play(FadeIn(l2))
        self.play(FadeIn(l3))

        self.wait(2)





#######################
#
# I N T R O
#
#######################

class Intro(Scene):
    def construct(self):
        
        ech = .6 # pour régler l'échelle
       
        
        l0 = Tex(r'Codage de Huffman ?').scale(2).move_to(np.array([0,3,0]))
        l0b = Tex(r'Compression de données').scale(2)

        l1 = Tex('H','e','l','l','o ','W','o','r','l','d',color=BLUE).scale(1).next_to(l0, direction=5*DOWN)
        
        # avec ! : listeAscii = ['1001000','1100101','1101100','1101100','1101111','0100000','1010111','1101111','1110010','1101100','1100100','0100000','0100001']

        listeAscii = ['01001000','01100101','01101100','01101100','01101111','00100000','01010111','01101111','01110010','01101100','01100100']
        
        code = ""
        for i in listeAscii :
           code = code + i + ' ' 

        l2 = Tex(code).scale(ech).next_to(l1, direction=2*DOWN)
        l3 = Tex('codage ASCII (mots de 8 bits) : 88 bits nécessaires').scale(ech).next_to(l2, direction=DOWN)
        
        self.play(Write(l0))
        self.wait(1)
        self.play(ReplacementTransform(l0,l0b))
        
        l0c= Tex('Utilisé pour PNG, JPEG, MPEG, MP3, ZIP, etc.').scale(ech).next_to(l0b, direction=DOWN)
        self.play(FadeIn(l0c))
        self.wait(2)
        self.play(FadeOut(l0c))
        self.play(l0b.animate.move_to(np.array([0,3,0])))

        self.wait(1)
        self.play(Write(l1))
        self.wait(1)
        self.play(FadeIn(l2))
        self.add(l3)
        
        self.wait(1)

        def switchColorForSmallTime(texte,couleur1,couleur2):
            l1.set_color_by_tex(texte, couleur1)
            self.wait(1.5)
            l1.set_color_by_tex(texte,couleur2)
            self.wait(1.5)

        switchColorForSmallTime('l',RED,BLUE)
        switchColorForSmallTime('o',RED,BLUE)
        
        l3b = Tex(r'$\leftarrow$ 8 symboles différents',color=RED).scale(.8).next_to(l1,direction=2*RIGHT)
        self.play(FadeIn(l3b))
        self.wait(2)
        self.play(FadeOut(l3b))
        
        l4 = Tex('Codage de Huffman :',color=BLUE).scale(ech).next_to(l3,direction=2*DOWN + .2*LEFT)
        l5 = Tex(r'$\circ$ codage adapté au nombre de symboles présents').scale(ech).next_to(l4,direction=RIGHT)
        l6 = Tex(r'$\circ$ mots plus courts pour les symboles plus fréquents').scale(ech).next_to(l5,direction=DOWN, aligned_edge=LEFT)

        self.play(Write(l4))
        self.play(FadeIn(l5))
        self.play(FadeIn(l6)) 
        
        listeHuffman = ['1111','010','10','10','00','1100','1101','00','1110','10','011']
        code = ""
        for i in listeHuffman :
           code = code + i + ' '

        l7 = Tex(code).scale(ech).next_to(l3, direction=7*DOWN)
        l8 = Tex('codage de Huffman (mots de taille variable) : 32 bits nécessaires').scale(ech).next_to(l7, direction=DOWN)

        self.play(FadeIn(l7))
        self.play(FadeIn(l8))
        
        l2b = Tex(r'ex : Hello World et image 10x10').scale(ech).next_to(l1, direction=DOWN, aligned_edge=LEFT)
        l3b = Tex(r'Domaine (où comment pourquoi) + exemple générique').scale(ech).next_to(l2, direction=DOWN, aligned_edge=LEFT)
        l4b = Tex(r'Partie historique ?').scale(ech).next_to(l3, direction=DOWN, aligned_edge=LEFT)
        l5b = Tex(r'Codage préfixe ? (exemple du livre ou exemple ci-dessus)').scale(ech).next_to(l4, direction=DOWN, aligned_edge=LEFT)

        
        
        self.wait(10)

#########################
#
# T E X T E    A R B R E
#
#########################

class TexteArbre(Scene):
    def construct(self):
        
        ech = .5 # pour régler l'échelle
        titre = Tex(r'Un exemple pour comprendre').scale(2).move_to(np.array([0,3,0]))
        self.play(Write(titre))
        self.wait(2)
        self.play(FadeOut(titre))
        self.wait(1)

        l0 = Tex(r'100 caractères $c$').scale(.7).move_to(np.array([-5, 3, 0]))
        l0b = Tex(r'avec $c \in C = \{A..F\}$').scale(.7).next_to(l0, direction=DOWN, aligned_edge=LEFT)
        
        
        l1 = Tex('D','B','A','E','E','C','C','A','A','A','D','A','A','D','B','A','C','A','A','B').scale(ech).move_to(np.array([0, 1, 0]))
        l2 = Tex('B','F','D','A','F','A','A','E','A','A','D','A','D','C','A','E','A','B','A','D').scale(ech).next_to(l1, direction=DOWN, aligned_edge=LEFT)
        l3 = Tex('C','C','C','A','A','D','A','F','F','A','A','B','A','A','E','A','D','D','C','F').scale(ech).next_to(l2, direction=DOWN, aligned_edge=LEFT)
        l4 = Tex('A','D','A','A','E','B','D','D','D','B','A','A','C','C','A','A','A','A','B','A').scale(ech).next_to(l3, direction=DOWN, aligned_edge=LEFT)
        l5 = Tex('B','B','D','E','E','C','A','A','A','B','B','A','A','A','C','A','A','D','A','E').scale(ech).next_to(l4, direction=DOWN, aligned_edge=LEFT)



        echA = .35
        as0 = Tex(r'100 caractères').scale(.7).move_to(np.array([-5, 3, 0]))
        as0b = Tex(r'ASCII (mots de 8 bits)').scale(.7).next_to(as0, direction=DOWN, aligned_edge=LEFT)
        as0c = Tex(r'800 bits').set_color(RED).scale(.8).next_to(as0b, direction=DOWN, aligned_edge=LEFT)
        as1 = Tex(r'10001001000010100000110001011000101100001110000111000001100000110000011000100100000110000011000100100001010000011000011100000110000011000010').scale(echA).move_to(np.array([0, 1, 0]))
        as2 = Tex(r'10000101000110100010010000011000110100000110000011000101100000110000011000100100000110001001000011100000110001011000001100001010000011000100').scale(echA).next_to(as1, direction=DOWN, aligned_edge=LEFT)
        as3 = Tex(r'10000111000011100001110000011000001100010010000011000110100011010000011000001100001010000011000001100010110000011000100100010010000111000110').scale(echA).next_to(as2, direction=DOWN, aligned_edge=LEFT)
        as4 = Tex(r'10000011000100100000110000011000101100001010001001000100100010010000101000001100000110000111000011100000110000011000001100000110000101000001').scale(echA).next_to(as3, direction=DOWN, aligned_edge=LEFT)
        as5 = Tex(r'10000101000010100010010001011000101100001110000011000001100000110000101000010100000110000011000001100001110000011000001100010010000011000101').scale(echA).next_to(as4, direction=DOWN, aligned_edge=LEFT)

        texteAscii = VGroup(as1,as2,as3,as4,as5)
        



        
        self.play(Write(l0))
        self.play(Write(l0b))

        listeCara=[l1,l2,l3,l4,l5]
        listeAscii=[as1,as2,as3,as4,as5]
        
        for i in listeCara :
            self.play(Write(i))
        self.wait(5)

        for i in range(len(listeCara)) :
            self.play(FadeOut(listeCara[i]))
            self.play(Write(listeAscii[i]))
        
        as6 = Tex(r'100 caractères en ASCII 8 bits soit 800 bits',color=BLUE).scale(.7).next_to(as5, direction=3*DOWN)
        self.play(Write(as6))

        self.wait(2)

        # on enlève le texte ascii
        self.play(FadeOut(texteAscii))
        self.play(FadeOut(as6))

        # et on remet le texte
        for i in listeCara :
            self.add(i)

        self.wait(2)

        

        

        echA = .35 
        margeBoite = .5 
        t6 = Text("A:45").set_color(WHITE).scale(echA).shift(np.array([-5, -2, 0]))
        t4 = Text("B:13").set_color(WHITE).scale(echA).next_to(t6, direction=3*RIGHT, aligned_edge=LEFT, buff=margeBoite)
        t3 = Text("C:12").set_color(WHITE).scale(echA).next_to(t4, direction=3*RIGHT, aligned_edge=LEFT, buff=margeBoite)
        t5 = Text("D:16").set_color(WHITE).scale(echA).next_to(t3, direction=3*RIGHT, aligned_edge=LEFT, buff=margeBoite)
        t2 = Text("E:9 ").set_color(WHITE).scale(echA).next_to(t5, direction=3*RIGHT, aligned_edge=LEFT, buff=margeBoite)
        t1 = Text("F:5").set_color(WHITE).scale(echA).next_to(t2, direction= 3*RIGHT, aligned_edge=LEFT, buff=margeBoite)

        bufferVal = .15
        f1 = SurroundingRectangle(t1, buff = bufferVal)
        b1 = BackgroundRectangle(f1,fill_color=BLACK,fill_opacity=1)
        f2 = SurroundingRectangle(t2, buff = bufferVal)
        b2 = BackgroundRectangle(f2,fill_color=BLACK,fill_opacity=1)
        f3 = SurroundingRectangle(t3, buff = bufferVal)
        b3 = BackgroundRectangle(f3,fill_color=BLACK,fill_opacity=1)
        f4 = SurroundingRectangle(t4, buff = bufferVal)
        b4 = BackgroundRectangle(f4,fill_color=BLACK,fill_opacity=1)
        f5 = SurroundingRectangle(t5, buff = bufferVal)
        b5 = BackgroundRectangle(f5,fill_color=BLACK,fill_opacity=1)
        f6 = SurroundingRectangle(t6, buff = bufferVal)
        b6 = BackgroundRectangle(f6,fill_color=BLACK,fill_opacity=1)
  
        x1 = VGroup(b1,f1,t1)
        x2 = VGroup(b2,f2,t2)
        x3 = VGroup(b3,t3,f3)
        x4 = VGroup(b4,t4,f4)
        x5 = VGroup(b5,t5,f5)
        x6 = VGroup(b6,t6,f6)
        
        def switchColor(texte,couleur):
            l1.set_color_by_tex(texte, couleur)
            l2.set_color_by_tex(texte, couleur)
            l3.set_color_by_tex(texte, couleur)
            l4.set_color_by_tex(texte, couleur)
            l5.set_color_by_tex(texte, couleur)

        # frequence A
        switchColor('A',RED)
        nbA = Tex(r'45\,\%',color=RED).scale(1.2).move_to(np.array([5, 0, 0]))
        self.play(Write(nbA))
        self.wait(1)
        self.play(ShowCreation(x6))
        self.play(FadeOut(nbA))
        self.wait(1)
        switchColor('A',WHITE)

        # frequence B
        switchColor('B',RED)
        nbB = Tex(r'13\,\%',color=RED).scale(1.2).move_to(np.array([5, 0, 0]))
        self.play(Write(nbB))
        self.wait(1)
        self.play(ShowCreation(x4))
        self.play(FadeOut(nbB))
        self.wait(1)
        switchColor('B',WHITE)

        # frequence C
        switchColor('C',RED)
        nbC = Tex(r'12\,\%',color=RED).scale(1.2).move_to(np.array([5, 0, 0]))
        self.play(Write(nbC))
        self.wait(1)
        self.play(ShowCreation(x3))
        self.play(FadeOut(nbC))
        self.wait(1)
        switchColor('C',WHITE)


        switchColor('D',RED)
        nbD = Tex(r'16\,\%',color=RED).scale(1.2).move_to(np.array([5, 0, 0]))
        self.play(Write(nbD))
        self.wait(1)
        self.play(ShowCreation(x5))
        self.play(FadeOut(nbD))
        self.wait(1)
        switchColor('D',WHITE)

        switchColor('E',RED)
        nbE = Tex(r'9\,\%',color=RED).scale(1.2).move_to(np.array([5, 0, 0]))
        self.play(Write(nbE))
        self.wait(1)
        self.play(ShowCreation(x2))
        self.play(FadeOut(nbE))
        self.wait(1)
        switchColor('E',WHITE)

        switchColor('F',RED)
        nbF = Tex(r'5\,\%',color=RED).scale(1.2).move_to(np.array([5, 0, 0]))
        self.play(Write(nbF))
        self.wait(1)
        self.play(ShowCreation(x1))
        self.play(FadeOut(nbF))
        self.wait(1)
        switchColor('F',WHITE)

        self.wait(5)

        self.play(ApplyMethod(x1.shift,DOWN))
        self.play(ApplyMethod(x1.shift,9*LEFT))
        self.wait(1)

        self.play(x2.animate.shift(DOWN))
        self.play(x2.animate.next_to(x1, direction= 3*RIGHT))
        self.wait(1)

        self.play(x3.animate.shift(DOWN))
        self.play(x3.animate.next_to(x2, direction= 3*RIGHT))
        self.wait(1)

        self.play(x5.animate.shift(RIGHT)) # on bouge un peu D
        self.play(x4.animate.shift(4*RIGHT)) # B
        self.play(x4.animate.shift(DOWN))
        self.play(x4.animate.next_to(x3, direction= 3*RIGHT))
        self.wait(1)

        #self.play(x5.animate.shift(RIGHT)) # D
        self.play(x5.animate.shift(DOWN))
        self.play(x5.animate.next_to(x4, direction= 3*RIGHT))
        self.wait(1)

        self.play(x6.animate.shift(9*RIGHT)) # A
        self.play(x6.animate.shift(DOWN))
        self.play(x6.animate.next_to(x5, direction= 3*RIGHT))
        self.wait(1)

        texte = Tex(r"File de priorité « min $F$ » dont les clés décrivent l'attribut $freq$ : ",color=BLUE).set_color(WHITE).scale(.7).shift(np.array([0, -2, 0]))
        self.play(Write(texte))
        self.wait(2)


#######################
#
# A R B R E
#
#######################

class Arbre(Scene):
    def construct(self):
        
        
        ### ALGO
        ech = .5 # pour régler l'échelle
        a0 = Tex(r'\textsc{Huffman}$(C)$').scale(ech).move_to(np.array([-5.75,3.5 ,0]))
        a1 = Tex(r'$1\quad n \leftarrow \vert C \vert$').scale(ech).next_to(a0, direction=DOWN, aligned_edge=LEFT)
        a2 = Tex(r'$2\quad Q \leftarrow C$').scale(ech).next_to(a1, direction=DOWN, aligned_edge=LEFT)
        a3 = Tex(r'$3\quad$\textbf{pour} $i \leftarrow 1$ \textbf{à} $n-1$').scale(ech).next_to(a2, direction=DOWN, aligned_edge=LEFT)
        a4 = Tex(r'$4\quad\quad$ \textbf{faire} allouer un nouveau n\oe ud $z$').scale(ech).next_to(a3, direction=DOWN, aligned_edge=LEFT)
        a5 = Tex(r'$5\quad\quad\quad z.gauche = x =$ \textsc{Extraire-Min}$(Q)$').scale(ech).next_to(a4, direction=DOWN, aligned_edge=LEFT)
        a6 = Tex(r'$6\quad\quad\quad z.droit = y =$ \textsc{Extraire-Min}$(Q)$').scale(ech).next_to(a5, direction=DOWN, aligned_edge=LEFT)
        a7 = Tex(r'$7\quad\quad\quad z.freq = x.freq + y.freq$').scale(ech).next_to(a6, direction=DOWN, aligned_edge=LEFT)
        a8 = Tex(r'$8\quad\quad\quad$\textsc{Insérer}$(Q,z)$').scale(ech).next_to(a7, direction=DOWN, aligned_edge=LEFT)
        a9 = Tex(r'$9$ \textbf{retourner} \textsc{Extraire-Min}$(Q)$').scale(ech).next_to(a8, direction=DOWN, aligned_edge=LEFT)
        boucleValue = Tex(r'Valeurs pour la boucle :').scale(ech).next_to(a9, direction=DOWN, aligned_edge=LEFT)
        nValue = Tex(r'$n = 6$').scale(ech).next_to(boucleValue, direction=DOWN, aligned_edge=LEFT)
        iValue = Tex(r'$i = $').scale(ech).next_to(nValue, direction=DOWN, aligned_edge=LEFT)
        boucleValue.set_color(ORANGE)
        nValue.set_color(ORANGE)
        iValue.set_color(ORANGE)

        
        self.add(a0,a1,a2,a3,a4,a5,a6,a7,a8,a9)
        
        
        self.wait(2)

        
        echA = .35 
        t1 = Text("f:5").set_color(WHITE).scale(echA).move_to(np.array([-1, 3, 0]))
        t2 = Text("e:9 ").set_color(WHITE).scale(echA).shift(np.array([0.2, 3, 0]))
        t3 = Text("c:12").set_color(WHITE).scale(echA).shift(np.array([1.5, 3, 0]))
        t4 = Text("b:13").set_color(WHITE).scale(echA).shift(np.array([2.9, 3, 0]))
        t5 = Text("d:16").set_color(WHITE).scale(echA).shift(np.array([4.3, 3, 0]))
        t6 = Text("a:45").set_color(WHITE).scale(echA).shift(np.array([5.7, 3, 0]))
        
        bufferVal = .15
        f1 = SurroundingRectangle(t1, buff = bufferVal)
        b1 = BackgroundRectangle(f1,fill_color=BLACK,fill_opacity=1)
        f2 = SurroundingRectangle(t2, buff = bufferVal)
        b2 = BackgroundRectangle(f2,fill_color=BLACK,fill_opacity=1)
        f3 = SurroundingRectangle(t3, buff = bufferVal)
        b3 = BackgroundRectangle(f3,fill_color=BLACK,fill_opacity=1)
        f4 = SurroundingRectangle(t4, buff = bufferVal)
        b4 = BackgroundRectangle(f4,fill_color=BLACK,fill_opacity=1)
        f5 = SurroundingRectangle(t5, buff = bufferVal)
        b5 = BackgroundRectangle(f5,fill_color=BLACK,fill_opacity=1)
        f6 = SurroundingRectangle(t6, buff = bufferVal)
        b6 = BackgroundRectangle(f6,fill_color=BLACK,fill_opacity=1)
  
        x1 = VGroup(b1,f1,t1)
        x2 = VGroup(b2,f2,t2)
        x3 = VGroup(b3,t3,f3)
        x4 = VGroup(b4,t4,f4)
        x5 = VGroup(b5,t5,f5)
        x6 = VGroup(b6,t6,f6)




# on affiche la valeur de n
        self.wait(.5)
        a1.set_color(RED)
        self.wait(.5)
        self.play(ShowCreation(boucleValue))
        self.play(ShowCreation(nValue))
        self.wait(1)
        a1.set_color(WHITE)
        self.wait(1)


# on affiche l'arbre Q 
        a2.set_color(RED)
        self.wait(.5)
        self.play(ShowCreation(x1))
        self.play(ShowCreation(x2))
        self.play(ShowCreation(x3))
        self.play(ShowCreation(x4))
        self.play(ShowCreation(x5))
        self.play(ShowCreation(x6))
        a2.set_color(WHITE)
        self.wait(1)

# on démarre la boucle, on affiche i
        i1 = Tex(r'$1$').scale(ech).move_to(np.array([-5.95,-2.22, 0]))
        i1.set_color(ORANGE)
        a3.set_color(RED)
        self.wait(.5)
        self.play(ShowCreation(iValue))
        self.play(ShowCreation(i1))
        self.wait(1)
        a3.set_color(WHITE)
        


#####  Étape (b)
        a4.set_color(RED)
        self.wait(.5)
        t00 = Text("00")
        x00 = CircleWithContent(t00).scale(echA).shift(np.array([2, 0, 0]))
        l21 = Line(np.array([1.75, -.25, 0]),np.array([1.4, -.75, 0]));
        l22 = Line(np.array([2.25, -0.25, 0]),np.array([2.6, -.75, 0]));
        self.add(x00)
        self.play(ShowCreation(l21))
        self.play(ShowCreation(l22))
        self.wait(1)
        a4.set_color(WHITE)
        
        a5.set_color(RED)
        self.wait(.5)
        self.play(x1.animate.move_to(np.array([1.2, -1, 0])))
        self.wait(1)
        a5.set_color(WHITE)

        a6.set_color(RED)
        self.wait(.5)
        self.play(x2.animate.move_to(np.array([2.8, -1, 0])))
        self.wait(1)
        a6.set_color(WHITE)

        t21 = Text("14")
        x21 = CircleWithContent(t21).scale(echA).shift(np.array([2, 0, 0]))
        a7.set_color(RED)
        self.wait(.5)
        self.play(ReplacementTransform(x00,x21))
        a7.set_color(WHITE)

        tl20 = Text("0").set_color(WHITE).scale(.3).move_to(np.array([1.4, -0.5, 0]))
        tl21 = Text("1").set_color(WHITE).scale(.3).move_to(np.array([2.6, -0.5, 0]))
        self.play(ShowCreation(tl20))
        self.play(ShowCreation(tl21))
       
        n14 = VGroup(l21,l22,x21,x1,x2,tl20,tl21)
        a8.set_color(RED)
        self.wait(.5)
        self.play(x3.animate.move_to(np.array([-1, 3, 0])))
        self.play(x4.animate.move_to(np.array([0.2, 3, 0])))
        self.play(n14.animate.move_to(np.array([2.2, 2.55, 0])))
        a8.set_color(WHITE)

        self.wait(1)


# on poursuit la boucle, on affiche i
        i2 = Tex(r'$2$').scale(ech).move_to(np.array([-5.95,-2.22, 0]))
        i2.set_color(ORANGE)
        a3.set_color(RED)
        self.wait(.5)
        self.play(ReplacementTransform(i1,i2))
        self.wait(1)
        a3.set_color(WHITE)
        
#####  Étape (c)
        a4.set_color(RED)
        self.wait(.5)
        t01 = Text("00")
        x01 = CircleWithContent(t01).scale(echA).shift(np.array([2, 0, 0]))
        l31 = Line(np.array([1.75, -.25, 0]),np.array([1.4, -.75, 0]));
        l32 = Line(np.array([2.25, -0.25, 0]),np.array([2.6, -.75, 0]));
        self.add(x01)
        self.play(ShowCreation(l31))
        self.play(ShowCreation(l32))
        self.wait(1)
        a4.set_color(WHITE)
  
            
        a5.set_color(RED)
        self.wait(.5)
        self.play(x3.animate.move_to(np.array([1.2, -1, 0])))
        self.wait(1)
        a5.set_color(WHITE)

        a6.set_color(RED)
        self.wait(.5)
        self.play(x4.animate.move_to(np.array([2.8, -1, 0])))
        self.wait(1)
        a6.set_color(WHITE)

        t31 = Text("25")
        x31 = CircleWithContent(t31).scale(echA).shift(np.array([2, 0, 0]))
        a7.set_color(RED)
        self.wait(.5)
        self.play(ReplacementTransform(x01,x31))
        a7.set_color(WHITE)

        tl30 = Text("0").set_color(WHITE).scale(.3).move_to(np.array([1.4, -0.5, 0]))
        tl31 = Text("1").set_color(WHITE).scale(.3).move_to(np.array([2.6, -0.5, 0]))
        self.play(ShowCreation(tl30))
        self.play(ShowCreation(tl31))
       
        n25 = VGroup(l31,l32,x31,x3,x4,tl30,tl31)
        a8.set_color(RED)
        self.wait(.5)
        self.play(n14.animate.move_to(np.array([1, 2.55, 0])))
        self.play(x5.animate.move_to(np.array([2.5, 3, 0])))
        self.play(n25.animate.move_to(np.array([4, 2.55, 0]))) # old : 4.2
        a8.set_color(WHITE)



# on poursuit la boucle, on affiche i
        i3 = Tex(r'$3$').scale(ech).move_to(np.array([-5.95,-2.22, 0]))
        i3.set_color(ORANGE)
        a3.set_color(RED)
        self.wait(.5)
        self.play(ReplacementTransform(i2,i3))
        self.wait(1)
        a3.set_color(WHITE)
       

#####  Étape (d)
        a4.set_color(RED)
        self.wait(.5)
        t02 = Text("00")
        x02 = CircleWithContent(t02).scale(echA).shift(np.array([2, 0, 0]))
        l41 = Line(np.array([1.75, -.25, 0]),np.array([1.4, -.75, 0]));
        l42 = Line(np.array([2.25, -0.25, 0]),np.array([2.6, -.75, 0]));
        self.add(x02)
        self.play(ShowCreation(l41))
        self.play(ShowCreation(l42))
        self.wait(1)
        a4.set_color(WHITE)
  
          
        a5.set_color(RED)
        self.wait(.5)
        self.play(n14.animate.move_to(np.array([1.2, -1.5, 0])))
        self.wait(1)
        a5.set_color(WHITE)
        
        a6.set_color(RED)
        self.wait(.5)
        self.play(x5.animate.move_to(np.array([2.8, -1, 0])))
        self.wait(1)
        a6.set_color(WHITE)

        t41 = Text("30")
        x41 = CircleWithContent(t41).scale(echA).shift(np.array([2, 0, 0]))
        a7.set_color(RED)
        self.wait(.5)
        self.play(ReplacementTransform(x02,x41))
        a7.set_color(WHITE)

        tl40 = Text("0").set_color(WHITE).scale(.3).move_to(np.array([1.4, -0.5, 0]))
        tl41 = Text("1").set_color(WHITE).scale(.3).move_to(np.array([2.6, -0.5, 0]))
        self.play(ShowCreation(tl40))
        self.play(ShowCreation(tl41))
       
        n30 = VGroup(l41,l42,x41,n14,x5,tl40,tl41)
        a8.set_color(RED)
        self.wait(.5)
        
        self.play(n25.animate.move_to(np.array([1, 2.55, 0])))
        self.play(n30.animate.move_to(np.array([4, 2, 0])))
        a8.set_color(WHITE)
        


# on poursuit la boucle, on affiche i
        i4 = Tex(r'$4$').scale(ech).move_to(np.array([-5.95,-2.22, 0]))
        i4.set_color(ORANGE)
        a3.set_color(RED)
        self.wait(.5)
        self.play(ReplacementTransform(i3,i4))
        self.wait(1)
        a3.set_color(WHITE)
       

#####  Étape (e)
        a4.set_color(RED)
        self.wait(.5)
        t03 = Text("00")
        x03 = CircleWithContent(t03).scale(echA).shift(np.array([2, 0, 0]))
        l51 = Line(np.array([1.75, -.25, 0]),np.array([.8, -.75, 0]));
        l52 = Line(np.array([2.25, -0.25, 0]),np.array([3.2, -.75, 0]));
        self.add(x03)
        self.play(ShowCreation(l51))
        self.play(ShowCreation(l52))
        self.wait(1)
        a4.set_color(WHITE)
  
          
        a5.set_color(RED)
        self.wait(.5)
        self.play(n25.animate.move_to(np.array([.6, -1.5, 0])))
        self.wait(1)
        a5.set_color(WHITE)
        
        a6.set_color(RED)
        self.wait(.5)
        self.play(n30.animate.move_to(np.array([3.02, -2.05, 0]))) # old y=-2 x=3.1 x=3.05
        self.wait(1)
        a6.set_color(WHITE)

        t51 = Text("55")
        x51 = CircleWithContent(t51).scale(echA).shift(np.array([2, 0, 0]))
        a7.set_color(RED)
        self.wait(.5)
        self.play(ReplacementTransform(x03,x51))
        a7.set_color(WHITE)

        tl50 = Text("0").set_color(WHITE).scale(.3).move_to(np.array([.8, -0.5, 0]))
        tl51 = Text("1").set_color(WHITE).scale(.3).move_to(np.array([3.2, -0.5, 0]))
        self.play(ShowCreation(tl50))
        self.play(ShowCreation(tl51))
       
        n55 = VGroup(l51,l52,x51,n25,n30,tl50,tl51)
        a8.set_color(RED)
        self.wait(.5)
        
        
        self.play(x6.animate.move_to(np.array([0, 3.5, 0]))) # old y=3
        self.play(n55.animate.move_to(np.array([4, 2, 0]))) # old y=1.5
        a8.set_color(WHITE)
        
# on poursuit la boucle, on affiche i
        i5 = Tex(r'$5$ (dernière itération)').scale(ech).move_to(np.array([-4.9,-2.22, 0])) # old x=-5.55 x=5
        i5.set_color(ORANGE)
        a3.set_color(RED)
        self.wait(.5)
        self.play(ReplacementTransform(i4,i5))
        self.wait(1)
        a3.set_color(WHITE)
       

#####  Étape (f)
        a4.set_color(RED)
        self.wait(.5)
        t04 = Text("00")
        x04 = CircleWithContent(t04).scale(echA).shift(np.array([2, 0, 0]))
        l61 = Line(np.array([1.75, -.25, 0]),np.array([.8, -.75, 0]));
        l62 = Line(np.array([2.25, -0.25, 0]),np.array([3.2, -.75, 0]));
        self.add(x04)
        self.play(ShowCreation(l61))
        self.play(ShowCreation(l62))
        self.wait(1)
        a4.set_color(WHITE)
  
          
        a5.set_color(RED)
        self.wait(.5)
        self.play(x6.animate.move_to(np.array([.6, -1, 0])))
        self.wait(1)
        a5.set_color(WHITE)
        
        a6.set_color(RED)
        self.wait(.5)
        self.play(n55.animate.move_to(np.array([3.5, -2.5, 0]))) # old : y=-2.1 x=3.1 x=3.35
        self.wait(1)
        a6.set_color(WHITE)

        t61 = Text("100")
        x61 = CircleWithContent(t61).scale(echA).shift(np.array([2, 0, 0]))
        a7.set_color(RED)
        self.wait(.5)
        self.play(ReplacementTransform(x04,x61))
        a7.set_color(WHITE)

        tl60 = Text("0").set_color(WHITE).scale(.3).move_to(np.array([.8, -0.5, 0]))
        tl61 = Text("1").set_color(WHITE).scale(.3).move_to(np.array([3.2, -0.5, 0]))
        self.play(ShowCreation(tl60))
        self.play(ShowCreation(tl61))
       
        n100 = VGroup(l61,l62,x61,x6,n55,tl60,tl61)
        a8.set_color(RED)
        self.wait(.5)
        
        self.play(n100.animate.move_to(np.array([3, 1, 0]))) # old y=2 y=1.5
        a8.set_color(WHITE)

        self.wait(2)

# dernière étape : l'extraction du min donne la racine de l'arborescence 
        a9.set_color(RED)
        self.wait(2)
        a9.set_color(WHITE)

        self.wait(3)



#######################
#
# LIMITATIONS
#
#######################

class Limitations(Scene):
    def construct(self):

        ech = .5 # pour régler l'échelle
        l0 = Tex(r'Limitations').scale(2).move_to(np.array([0,3 ,0]))
        l0b = Tex(r'du codage de Huffman').scale(1.5).next_to(l0, direction=DOWN)
        
        l1 = Tex(r"Le codage de Huffman impose d'utiliser un nombre entier de bits pour un symbole source").scale(.7).move_to(np.array([0,.5,0]))
        l2 = Tex(r"$\rightarrow$ codage Huffman sur des blocs de $n$ symboles",color=BLUE).scale(0.6).next_to(l1, direction=DOWN, aligned_edge=LEFT)
        l3 = Tex(r"Le codage de Huffman évalue les probabilités des symboles au début, donc il n'est pas adapté dans le cas d'une source dont les propriétés statistiques évoluent").scale(.7).next_to(l2, direction=DOWN, aligned_edge=LEFT)
        l4 = Tex(r"$\rightarrow$ codage de Huffman adaptatif",color=BLUE).scale(0.6).next_to(l3, direction=DOWN, aligned_edge=LEFT)
        
        
        self.play(Write(l0))
        self.play(Write(l0b))
        self.wait(1)
        self.play(FadeIn(l1))
        self.wait(1)
        self.play(Write(l2))
        self.wait(3)  
        self.play(FadeIn(l3))
        self.wait(1)
        self.play(Write(l4))
        self.wait(10)


class Caractéristiques(Scene):
    def construct(self):

        ech = .5 # pour régler l'échelle
        l0 = Tex(r'Caractéristiques').scale(2).move_to(np.array([0,3 ,0]))
        l0b = Tex(r'du codage de Huffman').scale(1.5).next_to(l0, direction=DOWN)
        l1 = Tex(r'Non-unicité',color=BLUE).scale(1).move_to(np.array([-4,1,0]))
        l2 = Tex(r'On peut produire des arbres différents pour un même alphabet :').scale(0.7).next_to(l1, direction=DOWN, aligned_edge=LEFT)
        l3 = Tex(r'$\circ$ choix pour les éléments de même fréquence').scale(0.7).next_to(l2, direction=DOWN+.5*RIGHT, aligned_edge=LEFT)
        l4 = Tex(r'$\circ$ choix gauche/droite pour chaque nœud').scale(0.7).next_to(l3, direction=DOWN, aligned_edge=LEFT)
        l5 = Tex(r'Conséquences',color=BLUE).scale(1).next_to(l4, direction=2*DOWN+.5*LEFT, aligned_edge=LEFT)
        l6 = Tex(r'Pour décoder, il faut fournir le code ou au moins donner les règles sur les choix').scale(0.7).next_to(l5, direction=DOWN, aligned_edge=LEFT)
        
        
        self.play(Write(l0))
        self.play(Write(l0b))
        self.wait(1)
        self.play(FadeIn(l1))
        self.wait(1)
        self.play(FadeIn(l2))
        self.wait(1)  
        self.play(FadeIn(l3))
        self.play(FadeIn(l4))
        self.wait(3)
        self.play(FadeIn(l5))
        self.play(FadeIn(l6))
        self.wait(10)
        


#######################
#
# P R E U V E
#
#######################

class Preuve(Scene):
    def construct(self):
        
        ech = .5 # pour régler l'échelle
        l0 = Tex(r'Preuve').scale(2).move_to(np.array([0,3,0]))
        l1 = Tex(r"Deux étapes pour démontrer que l'algorithme glouton de Huffman est correct").scale(0.7).next_to(l0, direction=DOWN)
        l2 = Tex(r'Étape 1 : Lemme des fréquences faibles',color=BLUE).scale(0.7).next_to(l1, direction=DOWN)  
        
        
        l6 = Tex(r"Étape 2 : Lemme de propagation de l'optimalité",color=BLUE).scale(0.7).next_to(l2, direction=9*DOWN)
        
        
       
        # On affiche les titres
        self.play(Write(l0))
        self.wait(1)
        self.play(Write(l1))
        self.wait(2)
        self.play(Write(l2))
        self.play(Write(l6))
        self.wait(2)
        # On efface les titres du haut
        Titre = VGroup(l0,l1)
        self.play(FadeOut(Titre))
        self.wait(1)
        # on déplace les titres des preuves
        ssTitre = VGroup(l2,l6) 
        self.play(ApplyMethod(ssTitre.shift,1.5*UP))

        # contenu des preuves
        l3 = Tex(r'Soit $C$ un alphabet dans lequel chaque caractère $c \in C$ a la fréquence $c.freq$').scale(0.5).next_to(l2, direction=DOWN)
        l4 = Tex(r'Soient $x$ et $y$ deux caractères de $C$ ayant les fréquences les plus basses').scale(0.5).next_to(l3, direction=DOWN)
        l5 = Tex(r'Alors il existe un codage préface optimal pour $C$ dans lequel les mots de code pour $x$ et $y$ ont la même longueur et ne diffèrent que par le dernier bit').scale(0.5).next_to(l4, direction=DOWN, aligned_edge=LEFT)
        l7 = Tex(r'Soit $C$ un alphabet dans lequel chaque caractère $c \in C$ a la fréquence $c.freq$').scale(0.5).next_to(l6, direction=DOWN)
        l8 = Tex(r'Soient $x$ et $y$ deux caractères de $C$ ayant la fréquence minimale').scale(0.5).next_to(l7, direction=DOWN)
        l9 = Tex(r"Soit $C'$ l'alphabet $C$ privé des caractères $x$ et $y$ et complété par un nouveau caractère, de sorte que $C'=C-(x,y)U(z)$").scale(0.5).next_to(l8, direction=DOWN)
        l10 = Tex(r"On définit $C'$ comme $C$ sauf que $z.freq=x.freq+y.freq$").scale(0.5).next_to(l9, direction=DOWN)
        l11 = Tex(r"Soit $T'$ un arbre  représentant un code préfixe optimal pour l'alphabet $C'$").scale(0.5).next_to(l10, direction=DOWN)
        l12 = Tex(r"Alors, l'arbre  $T$, obtenu à partir de $T'$ en remplaçant le nœud feuille associé à $z$ par un nœud interne ayant $x$ et $y$ comme enfants, représente un code optimal pour l'alphabet $C$").scale(0.5).next_to(l11, direction=DOWN)

        # affichage du contenu des preuves
        self.play(FadeIn(l3))
        self.play(FadeIn(l4))
        self.play(FadeIn(l5))
        self.wait(5)
        self.play(FadeIn(l7))
        self.play(FadeIn(l8))
        self.play(FadeIn(l9))
        self.wait(2)
        self.play(FadeIn(l10))
        self.play(FadeIn(l11))
        self.play(FadeIn(l12))
        self.wait(10)

class Complexite(Scene):
    def construct(self):
        
        ech = .5 # pour régler l'échelle
        l0 = Tex(r'Complexité').scale(2).move_to(np.array([0,3,0]))
        l1 = Tex(r"L'algorithme de Huffman est glouton").scale(1).next_to(l0, direction=2*DOWN)
        l2 = Tex(r"Tout nœud construit est définitif").scale(0.7).next_to(l1, direction=DOWN)
        l3 = Tex(r"Sous arbre - arbre optimal").scale(0.7).next_to(l2, direction=DOWN)
        l4 = Tex(r"Coûts pour un alphabet de $k$ symboles").scale(1).next_to(l3, direction=2*DOWN)
        l5 = Tex(r"$k-1$ itérations sur $E$").scale(0.7).next_to(l4, direction=DOWN)
        l6 = Tex(r"Coûts d'intégration et d'extraction sont en $\Theta(\log(k))$").scale(0.7).next_to(l5, direction=DOWN)
        l7 = Tex(r"L'algorithme est donc en $\Theta(k\,\log(k))$",color=BLUE).scale(1.0).next_to(l6, direction=2*DOWN)
        
        
        self.play(Write(l0))
        self.wait(1)
        self.play(Write(l1))
        self.wait(1)
        self.play(FadeIn(l2))
        self.play(FadeIn(l3))
        self.wait(3)  
        self.play(Write(l4))
        self.wait(1)
        self.play(FadeIn(l5))
        self.wait(1)
        self.play(FadeIn(l6))
        self.wait(3)
        self.play(Write(l7))
        self.wait(10)


##############################
#
# I M P L É M E N T A T I O N 
#
##############################

class Implementation(Scene):
    def construct(self):
        
        ech = 1 # pour régler l'échelle
        l0 = Tex(r'To do !').scale(2).move_to(np.array([0,3,0]))
        l1 = Tex(r"Montrer comment lire l'arbre pour en déduire le codage").scale(ech).next_to(l0, direction=3*DOWN)
        l2 = Tex(r"Montrer le codage obtenu sur le texte de 100 caractères").scale(ech).next_to(l1, direction=DOWN)
        l3 = Tex(r"Donner le taux de compression obtenu").scale(ech).next_to(l2, direction=DOWN)
                
        self.add(l0,l1,l2,l3)
        self.wait(10)

##############################
#
# C R É D I T 
#
##############################

class Credit(Scene):
    def construct(self):
        
        l0 = Tex(r'Crédits').scale(2).move_to(np.array([0,3,0]))
        l0b = Tex(r"Codage de Huffman",color=BLUE).scale(1.2).next_to(l0, direction=4*DOWN)
        l1 = Tex(r"Murièle Jacquier \& Simon Verdan").scale(.8).next_to(l0b, direction=DOWN)
        l1b = Tex(r"ASDI - GymInf 2021").scale(.8).next_to(l1, direction=3*DOWN)
        l2 = Tex(r"Une vidéo réalisée à l'aide de Python et de la bibliothèque Manim").scale(.7).next_to(l1b, direction=3*DOWN)

        self.play(Write(l0))
        self.play(FadeIn(l0b))
        self.play(FadeIn(l1))
        self.play(FadeIn(l1b))
        self.play(FadeIn(l2))

        self.wait(2)

        banner = ManimBanner().scale(0.25).to_corner(DR)
        self.play(FadeIn(banner))
        self.play(banner.expand())
        #self.play(FadeOut(banner))

        self.wait(1)
        
               
