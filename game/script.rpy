

define Somira = Character("Somira")

image HalfEyes:
    "HalfEyes1.png"
    alpha 1.0
    pause 0.2
    "HalfEyes2.png"
    alpha 1.0
    pause 0.2
    repeat
image Arms:
    "Arms1.png"
    alpha 1.0
    pause 0.2
    "Arms2.png"
    alpha 1.0
    pause 0.2
    repeat
image Smile:
    "Smile1.png"
    alpha 1.0
    pause 0.2
    "Smile2.png"
    alpha 1.0
    pause 0.2
    repeat
image Angry:
    "Angry1.png"
    alpha 1.0
    pause 0.2
    "Angry2.png"
    alpha 1.0
    pause 0.2
    repeat
image Stare:
    "Stare1.png"
    alpha 1.0
    pause 0.2
    "Stare2.png"
    alpha 1.0
    pause 0.2
    repeat
image Run:
    "Run1.png"
    alpha 1.0
    pause 0.2
    "Run2.png"
    alpha 1.0
    pause 0.2
    "Run3.png"
    alpha 1.0
    pause 0.2
    "Run4.png"
    alpha 1.0
    pause 0.2
    "Run3.png"
    alpha 1.0
    pause 0.2
    "Run2.png"
    alpha 1.0
    pause 0.2
    repeat
image Trees:
    "Trees1.png"
    alpha 1.0
    pause 0.2
    "Trees2.png"
    alpha 1.0
    pause 0.2
    repeat
image Shave1:
    "shave1.png"
    alpha 1.0
    pause 1.0
    "shave2.png"
    alpha 1.0
    pause 1.0
    repeat
image Shave2:
    "shave3.png"
    alpha 1.0
    pause 0.7
    "shave4.png"
    alpha 1.0
    pause 0.7
    repeat
image Shave3:
    "shave5.png"
    alpha 1.0
    pause 0.2
    "shave6.png"
    alpha 1.0
    pause 0.2
    repeat
image ShaveEnd:
    "shave7.png"
    alpha 1.0
    pause 0.1
    "shave8.png"
    alpha 1.0
    pause 0.1
    repeat

label start:
    stop music
    scene bg black
    "Hola,{w} soy Gabi y esto es Somira,{w} una novela visual sobre una chica y sus vivencias e inquietudes,{w} basada en mis propios miedos."
    "Este juego contiene escenas explicitas de Disfória y Sangre,{w} y trata temas sensibles como la ansiedad social, la depresión, la reclusión, y por supuesto, la identidad."
    "Si eres sensible a estos temas,{w} te recomiendo cerrar el juego."
    "Recuerda que esta build es tán solo una demo.{w} Por lo tanto tiene un a corta duración por el momento,{w} sigue el proyecto en mi pagina de Itch.io para estar al dia."
    "Disfruta del juego :)"
    pause
    play music "1.wav"
    show text "DIA 0" with dissolve
    pause 0.5
    scene bg black with dissolve
    "Ugh.{w} Donde estoy...{w} no veo una mierda."
    "Oh,{w} creo que me he quedado dormida encima del teclado{w}.{w}.{w}.{w} otra vez," 
    "tengo el shift clavado en el ojo,{w} joder como duele,{w} igual deberia levantarme de aqui."
    scene bg room with dissolve
    "Se me han vuelto a hacer las tantas como siempre,{w} y al final no ha venido nadie."
    "No puedo evitar pensar que igual soy una molestia siempre que me quedo sola esperando en llamada,"
    "jaja,{w} soy penosa,{w} calentandome la cabeza otra vez por esto."
    "En fín,{w} creo que sera mejor irse a la cama,{w} o si no me voy a volver aún más loca"
    stop music fadeout 2.0
    scene bg black with dissolve
    pause
    play music "4.wav"
    show Trees
    show Run
    show text "En el seno de un bosque, yace el árbol erguído"

    with dissolve
    pause
    show text "La neblina danzante, simula el mas inmenso vacío"
    with dissolve
    pause
    show text "Ramas que acarician, susurran al oído,"
    with dissolve
    pause
    show text "Ten cuidado, hijo mio."
    with dissolve
    pause

    scene bg black with dissolve
    
    show Trees
    show Run
    show text "Colosales figuras, en masa se inclinan"
    with dissolve
    pause
    show text "Cuales notas de una triste melodía,"
    with dissolve
    pause
    show text "La ola de Madera, hacia mí ser Camina,"
    with dissolve
    pause
    show text "Ten cuidado, hija mia."
    with dissolve
    pause

    scene bg black with dissolve
    show Trees
    show text "En un instante se para todo,"
    with dissolve
    pause
    show text "Mi espiritu, se desvanece con rudeza,"
    with dissolve
    pause
    show text "Del mundo de los vivos, mi exodo,"
    with dissolve
    pause
    show text "El arbol acaba conmigo con firmeza."
    with dissolve
    pause
    stop music
    scene bg room
    "Hostia puta."
    "Me duele todo el cuerpo,{w} es como si me hubiese caido un árbol encima,{w} raro... {w}Bueno, supongo que ya debe ser de dia,{w} a ver que hora es!"
    ".{w}.{w}."
    show HalfEyes with dissolve
    "Las 9 de la mañana..."
    "De verdad me voy a levantar a las nueve de la mañana?{w} Con lo agustito que estoy..."

    menu:
            "Levantate, vaga":
                
                scene bg room
            "Seguir durmiendo":
                hide HalfEyes
                show Arms
                "Bah, paso,{w} no me apetece ser responsable hoy,{w} aún menos que de costumbre."

                scene bg black with dissolve
                pause
                "Enserio?{w} Acabamos de empezar y ya te estas echando atrás?{w} Vamos no me jodas."
                "Pues sabes que,{w} dí adiós a tu progreso,{w} tú lo has querido."
                pause
                play sound "3.wav" loop fadein 1.0
                show text "Game Over - Narcolepsia"
                with dissolve
                pause
                scene bg black with dissolve
                pause
                return
    play music "1.wav"
    show Smile

    "Venga va,{w} voy a intentar ser un ser humano funcional por una vez."
    "Voy a subir la persiana,{w} que entre un poco de luz me vendra bien."

    show bg roomlight with dissolve
    pause
    hide Smile
    show Stare


    "Grave Error,{w} que dolor en los ojos joder,{w} como se nota que no estoy acostumbrada,"
    hide Stare
    show HalfEyes
    "en fin,{w} debería hacer una visita al purgatorio para despejarme de cara a este nuevo día,"
    hide HalfEyes
    show Angry
    "o como a mi me gusta llamarlo,{w} el cuarto de baño."

    scene bg bathroom with dissolve
    stop music
    pause
    #play sound wc
    pause
    show Arms with dissolve
    "Bueno,{w} llegó el momento, ya lleva varios dias creciendo,"
    hide Arms
    show Angry
    "tú puedes con esto Somi"

    scene bg shave with dissolve
    "Cada día crecen más y más rapidamente,{w} estoy segura,"
    "seguro que el mamonazo que haya ahí arriba se divierte mazo con mi desdicha,{w} en fín,{w} al lío."

    show Shave1
    "Qué harta estoy de tener que hacer esto constantemente,{w} a ver cuando me busco un curro y me pago la láser de una vez."
    "Joder,{w} que dificl es hacer la puta barbilla."
    hide Shave1
    "Bueno ya esta bastante bien,{w} aunque aún lo noto en ciertas zonas, que molesto{w}.{w}.{w}."
    "Sigo o lo dejo por hoy?"
    menu:
            "Apura un poco más.":
                "Nah, sido notandolo mucho a contrapelo,{w} total ya estoy perdiendo el tiempo desde el momento en que me he puesto,{w} que menos que acabar el trabajo."
                show Shave1
                play music "2.wav"
                "Odio mis putas manías,{w} podria simplemente no tocarme tanto la cara y no lo notaría,"
                "Que se le va a hacer,{w} ahora que se que eso esta ahí no puedo dejarlo como si nada."
                show shave4
                "Auch!"
                "Joder!!!"
                "Ya me he cortado como siempre,{w} creo que igual debería parar ya."
                menu:
                        "Ya Basta.":
                            stop music
                            "Casi no se nota,{w} me aguanto con esto y ya."

                        "No pasa nada por un poquito de sangre.":
                            "Tampoco es la primera vez,{w} no va a pasarme nada por unas cuantas heridas."
                            show Shave2
                            "Aún hay pelos en la barbilla,{w} y en el lado,{w} y en el puto cuello,{w} en todas partes,"
                            show Shave3
                            "Tengo que hacerlo mas rápido,{w} con más fuerza,{w} hasta que no quede nada,"
                            "tengo que arrancar todo hombre de mí,{w} sea como sea."
                            show ShaveEnd
                            "Jaja,{w} mira cuanta sangre,{w} mira como gotea en la pila,"
                            "jajajajajaja,{w} ja,{w} ja,{w} ja,"
                            "me he cortado tanto ya que no duele,"
                            "mira que lisa se queda mi piel de tanto frotar la cuchilla,{w} esto es genial,"
                            "frota,{w} frota,{w} frota,{w} jajajajaja"
                            menu:
                                    "CORTACORTACORTACORTACORTACORTACORTACORTACORTACORTA":
                                        "Oh oh,{w} creo que me estoy pasando,"
                                        "me estoy mareando mucho, creo que voy a perder el conocimiento{w}.{w}.{w}."
                                        stop music fadeout 1.0
                                        scene bg red with dissolve
                                        pause
                                        play music "3.wav" fadein 1.0
                                        show text "Game Over - Sangría"
                                        with dissolve
                                        pause
                                        scene bg black with dissolve
                                        pause
                                        return
                                    "CORTACORTACORTACORTACORTACORTACORTACORTACORTACORTA":
                                        "Oh oh,{w} creo que me estoy pasando,"
                                        "me estoy mareando mucho, creo que voy a perder el conocimiento{w}.{w}.{w}."
                                        stop music fadeout 1.0
                                        scene bg red with dissolve
                                        pause
                                        play music "3.wav" fadein 1.0
                                        show text "Game Over - Sangría"
                                        with dissolve
                                        pause
                                        scene bg black with dissolve
                                        pause
                                        return
                                    "Para":
                                        stop music
                                        show shave5
                                        "Ya basta,{w} ya me he vuelto a pasar otra vez,{w} voy a limpiar este desastre y irme de aqui ya."

                                    "CORTACORTACORTACORTACORTACORTACORTACORTACORTACORTA":
                                        "Oh oh,{w} creo que me estoy pasando,"
                                        "me estoy mareando mucho, creo que voy a perder el conocimiento{w}.{w}.{w}."
                                        stop music fadeout 1.0
                                        scene bg red with dissolve
                                        pause
                                        play music "3.wav" fadein 1.0
                                        show text "Game Over - Sangría"
                                        with dissolve
                                        pause
                                        scene bg black with dissolve
                                        pause
                                        return

                                    "CORTACORTACORTACORTACORTACORTACORTACORTACORTACORTA":
                                        "Oh oh,{w} creo que me estoy pasando,"
                                        "me estoy mareando mucho, creo que voy a perder el conocimiento{w}.{w}.{w}."
                                        stop music fadeout 1.0
                                        scene bg red with dissolve
                                        pause
                                        play music "3.wav" fadein 1.0
                                        show text "Game Over - Sangría"
                                        with dissolve
                                        pause
                                        scene bg black with dissolve
                                        pause
                                        return



            
            "Ya está bien.":
                "Casi no se nota, me aguanto con esto y ya."

    "Voy a lavarme un poco y a irme de aqui,{w} no aguanto más estar tanto rato delante del espejo..."
    show bg bathroomwat with dissolve
    #play water
    pause

    scene bg black with dissolve
    pause
    "Aún me queda un buen rato hasta la hora de comer,{w} que podria hacer?"
    play music "1.wav"
    menu:
            "Pasar el rato en el ordenador":
                "Voy a echarme alguna partidilla y ya veré lo que hay por la nevera"
                show escrit1 with dissolve
                "Que podría jugar hoy, tengo muchos juegos pendientes,{w} o podría jugar a lo mismo de siempre,{w} que pereza empezar algo nuevo."
                "Un LOL va a ser, no me voy a complicar mucho, y me vendrá bien la serotonina de ganar."
                show face1 with dissolve
                "Joder macho, porque tarda tanto en encontrar partida..."
                show face5
                "No me creo que sea la unica jugando de buena mañana a esto,{w} verdad?"
                "Pues vaya, voy a esperar un poco más,"
                show face4
                "y si no pues a otra cosa mariposa"


            "Salir y que me dé el aire":
                "Hoy ha empezado raro el dia,{w} creo que necesito despejarme de verdad,"
                "Voy a bajar un rato al parque,{w} seguro que puedo comer en algun tenderete de por ahí,"
                pause
                scene bg park1 with dissolve
                "Realmente no estoy acostumbrada a la luz del sol,{w} debeía haber traido una gorra..."
                show bg park2 with dissolve
                "Ojalá fuese una vampira ancestral,{w} de esas que no sufren con el sol en vez de una común,{w} o al menos eso decía ese libro japonés que leí hace tiempo."
                "Me falta espabilar cosa mala,{w} bueno,{w} voy a sentarme un poco y recapacitar."

                show parkface8 with dissolve
                "Se esta agusto en este banquito, no pega mucho porque tapan los{w}.{w}.{w}.{w} Arboles,"
                show parkface5
                "por que he sentido como escalofríos al decir eso?{w} Que raro..."
                show parkface9
                "La verdad es que es muy tranquilizadora esta brisa,{w} estoy parquemaxxing ahora mismo,{w} bancopilleada y dando vibras de poseer una calma impenetrable,"
                show parkface4
                "espero que nadie me haya oido decir eso en voz alta,{w} que bochorno..."
                "A veces me cuesta darme cuenta de que estoy en la calle,{w} no hablando con otra rarita en discord..."
                show parkface3
                "Aunque bueno supongo que es casi lo mismo si estoy hablando conmigo misma,{w} lo cual es lo mas normal del mundo!!!"
                "Tal vez ahora sería un buen momento para pensar en mi Videojuego,{w} la verdad es que no he sido capaz de imaginar una historia interesante hasta ahora,"
                show parkface6
                "Quizá podria venirme bien utilizar el lienzo como Desahogo personal,{w} No hace falta que sea autobiográfico,"
                "pero explorar algunas de mis inquietudes mediante la propia historia del juego podría ser un buen ejercicio."
                "Tengo que darle una vuelta,{w} pero es algo por donde podría tirar,"
                show parkface9
                "bueno, voy a pillar algo de comer y de vuelta a casa, ese puestecito italiano tiene muy buena pinta!"

    scene bg black with dissolve
    show Smile with dissolve
    pause
    "Eso es todo por ahora,{w} espero que hayas disfrutado la demo,{w} sigue el proyecto en Itch.io para enterarte de las ulltimas actualizaciónes,{w} y no dudes en compartir tus impresiones. ^^"
    hide Smile with dissolve

