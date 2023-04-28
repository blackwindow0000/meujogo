# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Kara")
define b = Character("Nevra")
define k = Character("Erika")
define t = Character("Garam")
define r = Character("Evan")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene floresta

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    e "Eu estava com meus amigos em um acampamento, distante da cidade em uma floresta, combinamos de todo mundo estar juntos."

    e "Mas... Onde eu estou agora?" 

    show nevra

    t "..."

    e "..."

    with fade

    scene entradaf

    show garam

    t "Oi, como vai Kara?"

    e "Oi Garam, estou tão cansada com todos esses trabalhos da faculdade, finalmente está chegando as férias"

    t "Sei como se sente, eu tava pensando da gente ir para um acampamento"

    e "Acampamento...?"

    t "Sim, nós poderiamos ter mais contato com a natureza, imagina como deve ser acordar e ouvir os sons dos passáros, da cachoeira. Isso não soa bom para você?"

    e "Pelo jeito você ja tem um lugar em mente, não é mesmo?"

    t "Você me conhece bem, em. Conversaremos sobre isso depois então quando irmos para casa, ok?"

    e "Ok"

    
menu:

    "It's a videogame.":
        jump choco1

    "It's an interactive book.":
        jump choco2

label choco1:

    show nevra

    b "It's a kind of videogame you can play on your computer or a console."

    jump nevra

label choco2:
 
    show nevra

    b "It's like an interactive book that you can read on a computer or a console."

    jump nevra

label nevra:
 

   "And so, we become a visual novel creating duo."


    # This ends the game.
return