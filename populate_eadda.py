import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mundial_project.settings')

import django
django.setup()
from eadda_app.models import SongInfo

# song_title = models.CharField(max_length=222, unique=True)
# song_lyrics = models.TextField(max_length=5000, unique=True)
# song_video_url = models.URLField(max_length=200, blank=True)

SONG_INFO = [
    {
        'song_title': 'El amor después del amor',
        'song_lyrics': '''
                        El amor después del amor, tal vez,
                        se parezca a este rayo de sol.
                        Y ahora que busqué
                        y ahora que encontré
                        el perfume que lleva al dolor
                        en la esencia de las almas.
                        En la ausencia del dolor.
                        Ahora sé que ya no
                        puedo vivir sin tu amor.

                        Mi hice fuerte ahí
                        donde nunca ví.
                        Nadie puede decirme quién soy
                        yo lo sé muy bien, te aprendí a querer
                        el perfume que lleva al dolor
                        en la esencia de las almas,
                        dice toda religión.
                        Para mí que es el amor
                        después del amor.

                        El amor después del amor, tal vez,
                        se parezca a este rayo de sol.
                        Y ahora que busqué
                        y ahora que encontré
                        el perfume que lleva al dolor
                        en la esencia de las almas.
                        Dice toda religión.
                        Para mí que es el amor
                        después del amor.

                        Nadie puede y nadie debe vivir, vivir sin amor.
                        Nadie puede y nadie debe vivir, vivir sin amor.

                        Una llave por una llave.
                        Y esa llave es mi amor.
                        Una llave por otra llave
                        y esa llave es tu amor.

                        El amor después del amor, tal vez.
                        Nadie puede y nadie debe vivir, vivir sin amor.
                        Y nadie puede, y nadie debe vivir, vivir sin amor.
                        Una llave por una llave.
                        Y esa llave es mi amor.
                        Una llave por otra llave
                        y esa llave es mi amor.

                        Nadie puede y nadie debe vivir, vivir sin amor.
                        Nadie puede y nadie debe vivir, vivir sin amor.''',
        'song_video_url': 'https://youtu.be/wFCpNO0o638'
    },
    {
        'song_title': 'Dos días en la vida',
        'song_lyrics': '''
                        Honey honey honey Babe
                        y ya dejemos de llorar
                        te veo ahí en media hora
                        no te olvides
                        nos largamos de aquí

                        Dos días en la vida
                        nunca vienen nada mal
                        de alguna forma de eso se trata vivir

                        Salieron en un coche
                        descansaron en un bar
                        con mejicanos margaritas
                        dos chicas: una sabe mentir
                        eligen una mesa un par de tragos
                        y a bailar
                        Thelma y su cowboy que
                        que ahora la saca de allí

                        Presa del mal
                        quise escapar
                        el tipo trata de violarla
                        cae Louise
                        -Qué te salgas de ahí!!
                        Vas a pedir, vas a pedir
                        piedad o te vuelo la cabeza puercoespín

                        La bala fue precisa, el mismo tipo
                        no hablo mas
                        tomaron una carretera
                        la botella y se marcharon de ahí
                        dormí con el ladrón
                        y me dio amor hasta llorar
                        me voy a México rápido
                        dijo Louise

                        Thelma entro y robo en el supermarket
                        sabias, tu chico vio MTV ?
                        los militares odian esas almas
                        y yo las quiero para mi

                        Debo decir, debo decir
                        las cosas se pusieron mas difíciles
                        y sabes que si
                        si lo soñé o lo viví
                        las chicas conmigo son Thelma y Louise.''',
        'song_video_url': 'https://youtu.be/flwzJmMnq8U'
    },
    {
        'song_title': 'La Verónica',
        'song_lyrics': '''
                        No se filmó en Portugal
                        eso no estaba en su plan
                        ella deshizo valijas
                        prendió un cigarrillo
                        y bajo a la ciudad
                        Roma no estaba tan mal
                        debo admitir nada mal
                        algo mantiene el hechizo penso
                        y se dejo llevar
                        por un tipo que bajaba solo por la
                        calle del calvario

                        plano secuencia real
                        solo debo caminar
                        si de algo estaba segura
                        era que su Verónica no iba a llorar
                        tarde de crucifixión
                        clavan al hijo de Dios
                        guarda el guión en un bolso amarillo
                        y se tira al sol a bailar

                        Todas las vidas cayeron al mar
                        es tan suave verlas
                        todas las vidas cayeron al mar
                        y se van, y se van, y se van
                        ella quiso hacerlo tan feliz
                        Exterior - día - toma 22
                        y el sudor de Cristo dibujado sobre un manto

                        Todas las vidas cayeron al mar
                        es tan suave verlas
                        todas las vidas cayeron al mar
                        y se van, y se van, y se van
                        ella quiso hacerlo tan feliz
                        el quiso un amor y no una actriz
                        ella quiso hacerlo tan feliz

                        El y su coraza de marfil
                        diseminada a resistir los encantos del jazmín
                        yo no se porque
                        eligió su dulce piel
                        fue quizás que la vio tan sola
                        yo no se ni porque
                        eligió aquella mujer
                        no hizo mas que volverse loca
                        y el sudor de Cristo dibujado sobre un manto
                        todas las vidas.

        ''',
        'song_video_url': 'https://youtu.be/seP1-aLGXOU'
    },
    {
        'song_title': 'Tráfico por Katmandú',
        'song_lyrics': '''
                        Y te digo :
                        que desde adentro yo me puedo mover
                        hice un agujero en una inmensa pared
                        prendí la radio y escuche y escuche
                        200 chicos mueren hoy sin su AZT
                        Dime Dios : Hay stop?
                        donde estés dímelo
                        si hablábamos de luz
                        del trafico por Katmandu

                        No todo el mundo va a dejarse caer
                        no todo el mundo va a arrastrarse a tus pies
                        lo que me falta no es la falta de fe
                        tendrías que pensarlo seriamente esta vez
                        ademan Art Deco
                        muéstrame quémalo
                        si hablábamos de luz
                        debajo de la Cruz del Sur

                        No tengo prisa no hay a donde llegar
                        este milagro es de un perfecto cristal
                        sabiduría pop me lo hizo entender
                        que siempre fue lo mismo el mono y Citizen Kane
                        yo también perdí quimeras
                        pero me hice buen voyeur

                        Y te digo :
                        que desde adentro nos podemos mover
                        hace un agujero en una inmensa pared
                        después sácate poco a poco la piel
                        la sangre es para siempre
                        nada puedes hacer
                        además, vos y yo
                        ámame por favor
                        si amábamos la luz
                        debajo de la Cruz del Sur

                        Siempre mas, never stop
                        te ofrecí mi corazón
                        si hablábamos de luz
                        del trafico por Katmandu.
        ''',
        'song_video_url': 'https://youtu.be/Zbpqt7Ztops'
    },
    {
        'song_title': 'Pétalo de sal',
        'song_lyrics': '''
                    Furioso pétalo de sal
                    la misma calle el mismo bar
                    nada te importa en la ciudad si nadie espera
                    ella se vuelve carmesí, no se si es Baires o Madrid
                    nada te importa en la ciudad si nadie espera
                    y no es tan trágico mi amor, es este sueño es este sol
                    que ayer pareció tan extraño
                    o al menos tus labios
                    yo te entiendo bien, es como hablarle a la pared
                    y tu podrías darme fe

                    ...y te imagino dando vueltas en el vecindario

                    algo tienen estos años que me hacen poner así
                    y decirte que te extraño
                    y voy a hacerte feliz
        ''',
        'song_video_url': 'https://youtu.be/NAcDZfLiwss'
    },
    {
        'song_title': 'Sasha, Sissí y el círculo de baba',
        'song_lyrics': '''
                        Pensar que no dijo nada
                        la mañana que lo vi
                        pensar que el amaba tanto a su divina Sissi
                        baje el callejón con calma
                        mas no pude resistir
                        entonces rece por Sasha por su
                        amada y por mi
                        Reptar, reptar
                        en horas de la siesta
                        cambiar, cambiar
                        las leyes del amar
                        Sissi lo volvió loco en una fiesta
                        y no volvió a tocarlo nunca mas
                        entonces penso en un arma
                        en matarla y en huir
                        lloro y escribió su réquiem
                        para Sasha y Sissi
                        no hizo mas que esperarla
                        la beso y durmió al llegar
                        y trazo un circulo de baba
                        con un medica style
                        y no dejo que nunca mas sufriera
                        Sissi murió hambre y vanidad
                        amar, amar y tuvo muerte lenta
                        así el meo tres veces mis zapatos
                        y llego hasta el bar...
                        simplemente fue lo que paso bajo esta luz
                        Sasha prendió un faso y se sentó
                        pito ese cigarrillo hasta explotar.
        ''',
        'song_video_url': 'https://youtu.be/_IXrszWjqis'
    },
    {
        'song_title': 'Un vestido y un amor',
        'song_lyrics': '''
                    Te vi
                    juntabas margaritas del mantel
                    ya sé que te traté bastante mal
                    no sé si eras un ángel o un rubí
                    o simplemente te vi
                    te vi
                    saliste entre la gente a saludar
                    los astros se rieron otra vez
                    la llave de Mandala se quebró
                    o simplemente te vi
                    todo lo que diga está de más
                    las luces siempre encienden en el alma
                    y cuando me pierdo en la ciudad
                    vos ya sabes comprender
                    es solo un rato no más
                    tendría que llorar o salir a matar
                    te vi, te vi, te vi
                    yo no buscaba a nadie y te vi
                    te vi
                    fumabas unos chinos en Madrid
                    hay cosas que te ayudan a vivir
                    no hacías otra cosa que escribir
                    y yo simplemente te vi
                    me fui
                    me voy de vez en cuando a algún lugar
                    ya sé, no te hace gracia este país
                    tenías un vestido y un amor
                    y yo simplemente te vi
        ''',
        'song_video_url': 'https://youtu.be/7aSsSf-e4zQ'
    },
    {
        'song_title': 'Tumbas de la gloria',
        'song_lyrics': '''
                    Tu amor abrió una herida
                    porque todo lo que te hace bien
                    siempre te hace mal
                    tu amor cambió mi vida como un rayo
                    para siempre, para lo que fue y ser.

                    La bola sobre el piano la mañana aquella
                    que dejamos de cantar.
                    Llegó la muerte un día y arrasó con todo,
                    todo, todo, todo un vendaval,
                    y fue un fuerte vendaval.

                    Algo de vos llega hasta mí
                    cae la lluvia sobre París
                    pero me escapé hacia otra ciudad
                    y no sirvió de nada,
                    porque todo el tiempo estabas dando vueltas
                    y más vueltas que pegué en la vida para tratar de reaccionar
                    un tango al mango revoleando la cabeza como un loco
                    de aquí para allá, de aquí para allá.

                    Después vinieron días de misterio y frío,
                    casi como todos los demás
                    lo bueno que tenemos dentro es un brillante,
                    es una luz que no dejar‚ escapar jamás.

                    Algo de vos llega hasta mí,
                    cuando era pibe tuve un jardín
                    pero me escapé hacia otra ciudad
                    y no sirvió de nada,
                    porque todo el tiempo estaba yo en un mismo lugar,
                    y bajo una misma piel y en la misma ceremonia
                    Yo te pido un favor, que no me dejes caer
                    en las tumbas de la gloria.
        ''',
        'song_video_url': 'https://youtu.be/2zMwG8HdNa4'
    },
    {
        'song_title': 'La rueda mágica',
        'song_lyrics': '''
                        Un recuerdo desde el Africa
                        un sueño con el Liverpool Bar
                        y ella que siempre se va
                        una foto de los Rolling Stones
                        mi vieja nunca los escuchó,
                        y no me puse a llorar.

                        Uh, los dias en cualquier lugar
                        perdido en un inmensa ciudad
                        en una rueda mágica,
                        y el, el ángel
                        de la soledad, protege,
                        lava y cura este mal
                        el no me abandonara.
                        Nuestra vida es un lecho de cristal
                        y esta vida esta hecha de cristal
                        nuestra vida es un lecho de cristal
                        un lecho de cristal para los dos.

                        Uh, yo extraño esa fascinación
                        un poster, y una Gibson Les Paul
                        que nuncas voy olvidar.
                        Recuerdo un día como hoy
                        me fui de casa a tocar rock & roll
                        y no vovlvi nunca más.

                        Nuestra vida es un lecho de cristal
                        y estas vida esta hecha de cristal
                        nuestra vida es un lecho de cristal
                        un lecho de cristal para los dos.

                        Podrías verlo así, sólo si supieras
                        que yo sin ti ya no podría vivir.

                        Todos ya nos fuimos de aquí
                        todos ya nos fuimos de casa
                        Para tocar rock & roll
                        todo lo que pude sentir
                        todo esta sellado en mi alma
                        para tocar rock & roll
                        un recuerdo desde Africa
                        un sueño con el Liverpool bar.
        ''',
        'song_video_url': 'https://youtu.be/3D0mF2JYk9k'
    },
    {
        'song_title': 'Creo',
        'song_lyrics': '''
                    Creo que aun tal vez piensas en mi
                    creo poder captarlo
                    creo que al fin nada tiene fin
                    creo desesperado
                    creo que morir es una sensación
                    creo que vivir podría serlo pero ahora es algo mucho mas real
                    creo que salí a ver un poco de sol
                    creo que te vi bailando Beatles en alguna vieja casa del lugar

                    Creo que aun tal vez piensas en mi
                    creo poder captarlo

                    y ya no quiero verte tan triste, triste así
                    creo que estas llorando
                    me acuerdo que abrí la puerta y eras vos
                    después me perdí mirándote desnuda y te reías de mi cara de maldad
                    entonces sentí la cima del amor
                    y si me caí no importa porque todo todo todo todo esto es de los dos

                    no quiero nada que nos haga mal
                    yo creo
                    yo creo y con eso basta
                    creo que aun tal vez piensas en mi
                    creo poder captarlo.
        ''',
        'song_video_url': 'https://youtu.be/7hiM7DggQVc'
    },
    {
        'song_title': 'Detrás del muro de los lamentos',
        'song_lyrics': '''
                        Gota que cae sobre el cielo, no besa el suelo,
                        lluvia que cae del cielo, y yo la bebo
                        Ah... tu corazón

                        desnudo mar abierto, no sopla el viento
                        todo resulto un juego, que quita el miedo

                        y cuando llega la cura
                        calma el a oro la luna
                        y yo que andaba ciego
                        cayo el cielo y no beso el suelo
                        y se detuvo el tiempo
                        detrás del Muro de los Lamentos

                        Todo lo que hicimos
                        la mentira y la verdad
                        todo lo que hicimos
                        sigue vivo en un lugar

                        Todo poco a poco
                        va dejando de importar
                        todo menos esos paraísos en el mar
                        y navegar y navegar y navegar.
        ''',
        'song_video_url': 'https://youtu.be/rXA5OX7G9CY'
    },
    {
        'song_title': 'La balada de Donna Helena',
        'song_lyrics': '''
                        Manejando por la ruta alguna noche sin mirar atrás
                        prendo un faso y en la radio siempre el mismo idiota de la música
                        Uh..., Helena
                        la petaca se quedo vacía y son los once en cualquier lugar
                        una Donna me hace señas sube al coche y empezó a falar
                        antes, debo confesar, no sentí placer igual
                        pero la verdad es que ya ven...

                        Uh..., Helena

                        empezó por recorrerme con su boca y no estaba mal
                        y su lengua parecía casi como loca, vamos a chocar...

                        hasta aquí pude hacerlo bien
                        después con su pocket me golpeo en la sien
                        y bajo mis pantalones sin apuro
                        y trago, trago, trago y había algo puro
                        me quemo con la luz de un superflash
                        y algo extraño comenzó a sudar
                        y tan pronto desapareció este mundo
                        y así fue como me fui del mundo

                        antes, debo confesar, no sentí placer igual
                        pero la verdad es que ya ven...

                        Donna Helena empezó a llorar,
                        sola en ese coche lamiendo su sal
                        por un momento se olvido de la verdad
                        que todo lo que toca se le esfuma, se le esfuma, se le esfuma...

                        hay un acuerdo de brujas en Gibraltar
                        que "todo amor perpetuo deberás matar
                        cuerpo sobre cuerpo y cuerpos sobre el mar
                        el mar de los caídos frente a Donna Helena.

        ''',
        'song_video_url': 'https://youtu.be/ntfCQI5Qz0g'
    },
    {
        'song_title': 'Brillante sobre el mic',
        'song_lyrics': '''
                        Hay recuerdos que no voy a borrar
                        personas que no voy a olvidar
                        silencios que prefiero callar

                        son dos, las caras de la luna son dos
                        prefiero que sigamos mi amor presos de este sol
                        dejar, amar, llorar
                        el tiempo nos ayuda a olvidar
                        allá, el tiempo que me lleva hacia allá
                        el tiempo es un efecto fugaz
                        y hay, hay cosas que no voy a olvidar
                        la noche que dejaste de actuar
                        solo, para darme amor

                        y yo vi tu corazón brillante sobre el mic en una mano
                        y ausente de las cosas pensaste en dejarlo
                        y tirarlo junto a mi
                        hay secretos en el fondo del mar
                        personas que me quiero llevar
                        aromas que no quiero olvidar
                        silencios que prefiero callar
                        mientras vos jugas.

        ''',
        'song_video_url': 'https://youtu.be/ROSqv1xzHqE'
    },
    {
        'song_title': 'A rodar mi vida',
        'song_lyrics': '''
                        Se me hacía tarde, ya me iba
                        siempre se hace tarde en la ciudad
                        cuando me di cuenta estaba vivo
                        vivo para siempre de verdad.

                        Hoy compré revistas en el metro
                        no pensaba en nada, nada más.
                        Y cai que al fin esto es un juego
                        todo empieza siempre una vez más.
                        Y a rodar, y a rodar, y a rodar
                        y a rodar mi vida.
                        Y a rodar, y a rodar, y a rodar
                        y a rodar mi amor.
                        Yo no se donde va
                        yo no se donde va mi vida
                        yo no se donde va,
                        pero tampoco creo que sepas vos.
                        Quiero salir, si, quiero vivir
                        quiero dejar una suerte de señal.
                        Si un corazón triste pudo ver la luz
                        si hice máss liviano el peso tu cruz
                        nada más me improta en esta vida,
                        chau, hasta mañana.

                        Y a rodar, y a rodar, y a rodar
                        y a rodar mi vida.
                        Y a rodar, y a rodar, y a rodar
                        y a rodar mi amor.
                        Yo no se donde va
                        yo no se donde va, mi vida
                        yo no se donde va,
                        pero tampoco creo que sepas vos.
                        Quiero salir, si, quiero vivir
                        quiero dejar una suerte de señal.
                        Si un corazón triste pudo ver la luz
                        si hice máss liviano el peso de tu cruz
                        nadie tiene a nadie
                        y yo te tengo aún
                        dentro de mi alma.
                        Siento que me amas
                        chau, hasta mañana.
        ''',
        'song_video_url': 'https://youtu.be/1DYUNaJ_rfU'
    },
]


def populate(song_info):
    for song in song_info:
        add_song(song_title=song['song_title'],song_lyrics=song['song_lyrics'], song_video_url=song['song_video_url'])


def add_song(song_title, song_lyrics, song_video_url):
    song_info = SongInfo.objects.get_or_create(song_title=song_title)[0]
    song_info.song_lyrics = song_lyrics
    song_info.song_video_url = song_video_url
    print("Canciones --->", song_info.song_title)
    song_info.save()
    return song_info


if __name__ == '__main__':
    print("Empezando...")
    populate(SONG_INFO)
