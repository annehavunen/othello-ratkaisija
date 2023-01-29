# Viikkoraportti 2

Tällä viikolla syntyi paljon koodia, sillä kirjoitin othello-pelin, yksikkötestejä sekä minimax-tekoälyn.
Käytin pohjana aiemmassa periodissa aloittamaani koodia, mutta poistin siitä paljon toisteisuutta ja tein muita pienempiä muutoksia.
Koodi lyhenikin reilusti. Lisäksin kommentoin koodia ja konfiguroin pylintin sekä codecovin.

Opin monia asioita ja vastaan tuli myös paljon haasteita.
Opin uuden idean koodin lyhentämiseen funktiokutsussa annettavien parametrien avulla.
Ohjelmakoodin jakaminen funktioihin ja muihin osiin järkevästi tuntui paikoitellen yllättävän haastavalta.
Huomasin, että jotkin aiemmin tekemäni ratkaisut tuottivat päänvaivaa, kun yritin kirjoittaa tekoälyä.
Pelin riittävä yksikkötestaaminen mietityttää. Tutustuin minimax-algoritmiin.
En meinannut aluksi ymmärtää, miten saan GitHub Actionsin ja Codecovin konfiguroitua.

Käytin minimax-algoritmin toteutukseen paljon aikaa, ja sen toteutukseen kaipaisin nyt ehkä eniten apua.
Toteutukseni poikkeaa vähän kurssimateriaalista, sillä tutkin jo aiemmassa periodissa asiaa internetistä.
En mm. ymmärrä, mitä kurssimateriaalissa mainitussa valitseSiirto-funktiossa pitäisi käytännössä tehdä.
Return-lausekkeessani on sekä arvo että siirto, ja kurssimateriaalissa on vain arvo.
Minulla onkin vaikeuksia ymmärtää, miten kuljetan tarvittavia muuttujia oikeaoppisesti rekursiossa.
En ole varma, tarvitseeko minimaxissa aina luoda uusi pelilauta ennen minimaxin rekursiivista kutsua.

Ainakin minimax-algoritmini palauttaa jotain, enkä toistaiseksi ole saanut sitä kaatumaan.
Se ei pelaa hyvin, mutta en kyllä ole vielä edes yrittänyt panostaa heuristiseen arviointiin.
Omassa ratkaisussani pelilaudan heuristiseen arviointiin siirrytään jo siinä vaiheessa, 
kun yhdellä pelaajalla ei ole siirtoja eikä vasta suoranaisen pelin päättymisen jälkeen.
Sain tämän ratkaisun helpommin toimimaan edes jotenkuten.

Ensi viikon osalta en ole varma, miten edistän koodia, koska kysymyksiä on niin paljon. Yritänkö lisätä alfa-beeta-karsinnan?
Pitäisikö minun parannella ja/tai korjata minimax-algoritmia? Teenkö kenties jotain muuta?
Pitäisikö pylint-tarkistukset lisätä myös GitHub Actionsiin, jolloin ne suoritetaan aina, kun koodia pushataan?

Käytetty työaika: 17 h
