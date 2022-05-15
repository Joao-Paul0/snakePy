# importando bibliotecas
import turtle
import random
import time


# criando turtle screen
screen = turtle.Screen()
screen.title('Joao-Paul0')
screen.setup(width = 700, height = 700)
screen.tracer(0)
turtle.bgcolor('#FFF')



# criando um border para o nosso game

turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# ponto
pontos = 0
delay = 0.1


# cobra
cobra = turtle.Turtle()
cobra.speed(0)
cobra.shape('square')
cobra.color("black")
cobra.penup()
cobra.goto(0,0)
cobra.direcao = 'stop'


# comida
fruta = turtle.Turtle()
fruta.speed(0)
fruta.shape('circle')
fruta.color('green')
fruta.penup()
fruta.goto(30,30)

velha_fruta=[]

# pontuação
pontuacao = turtle.Turtle()
pontuacao.speed(0)
pontuacao.color("black")
pontuacao.penup()
pontuacao.hideturtle()
pontuacao.goto(0,300)
pontuacao.write("Score :",align="center",font=("Courier",24,"bold"))


####### definindo os movimentos
def cobra_indo_pra_cima():
  if cobra.direcao != "down":
    cobra.direcao = "up"

def cobra_indo_pra_baixo():
  if cobra.direcao != "up":
    cobra.direcao = "down"

def cobra_indo_pra_esquerda():
  if cobra.direcao != "right":
    cobra.direcao = "left"

def cobra_indo_pra_direita():
  if cobra.direcao != "left":
    cobra.direcao = "right"

def cobra_move():
  if cobra.direcao == "up":
    y = cobra.ycor()
    cobra.sety(y + 20)

  if cobra.direcao == "down":
    y = cobra.ycor()
    cobra.sety(y - 20)

  if cobra.direcao == "left":
    x = cobra.xcor()
    cobra.setx(x - 20)

  if cobra.direcao == "right":
    x = cobra.xcor()
    cobra.setx(x + 20)

# mapeando as teclas
screen.listen()
screen.onkeypress(cobra_indo_pra_cima, "Up")
screen.onkeypress(cobra_indo_pra_baixo, "Down")
screen.onkeypress(cobra_indo_pra_esquerda, "Left")
screen.onkeypress(cobra_indo_pra_direita, "Right")

# main loop

while True:
  screen.update()
      #colisão da cobra e as frutas
  if cobra.distance(fruta)< 20:
    x = random.randint(-290,270)
    y = random.randint(-240,240)
    fruta.goto(x,y)
    pontuacao.clear()
    pontos+=1
    pontuacao.write("Score:{}".format(pontos),align="center",font=("Courier",24,"bold"))
    delay-=0.001
    
    ## criando uma nova bola
    nova_fruta = turtle.Turtle()
    nova_fruta.speed(0)
    nova_fruta.shape('square')
    nova_fruta.color('green')
    nova_fruta.penup()
    velha_fruta.append(nova_fruta)
    

  # adicionando a bola a cobra
  
  for index in range(len(velha_fruta)-1,0,-1):
    a = velha_fruta[index-1].xcor()
    b = velha_fruta[index-1].ycor()

    velha_fruta[index].goto(a,b)
                                
  if len(velha_fruta)>0:
    a= cobra.xcor()
    b = cobra.ycor()
    velha_fruta[0].goto(a,b)
  cobra_move()

  ##cobra e a colisão da border   
  if cobra.xcor()>280 or cobra.xcor()< -300 or cobra.ycor()>240 or cobra.ycor()<-240:
    time.sleep(1)
    screen.clear()
    screen.bgcolor('turquoise')
    pontuacao.goto(0,0)
    pontuacao.write("   GAME OVER \n Sua pontuação foi {}".format(pontos),align="center",font=("Courier",30,"bold"))


  ## colisão da cobra
  for comida in velha_fruta:
    if comida.distance(cobra) < 20:
      time.sleep(1)
      screen.clear()
      screen.bgcolor('turquoise')
      pontuacao.goto(0,0)
      pontuacao.write("    GAME OVER \n Sua pontuação foi {}".format(pontos),align="center",font=("Courier",30,"bold"))


          
  time.sleep(delay)

turtle.Terminator()





