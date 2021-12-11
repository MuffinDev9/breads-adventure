@namespace
class SpriteKind:
    boss = SpriteKind.create()
    Ice = SpriteKind.create()
    boss2 = SpriteKind.create()
    boss3 = SpriteKind.create()
    target = SpriteKind.create()
    ICEBOSS = SpriteKind.create()
    ICEBOSS2 = SpriteKind.create()
    ICEBOSS3 = SpriteKind.create()
    BOOM = SpriteKind.create()
    Mad_Scientist = SpriteKind.create()
    SCIENCE = SpriteKind.create()

def on_overlap_tile(sprite, location):
    tiles.set_tile_at(tiles.get_tile_location(64, 21),
        assets.tile("""
            tile4
        """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
    """),
    on_overlap_tile)

def on_on_overlap(sprite2, otherSprite):
    global boss22
    if sprite2.bottom < otherSprite.y:
        sprite2.vy = -100
        otherSprite.destroy(effects.fire, 500)
        for value in tiles.get_tiles_by_type(assets.tile("""
            boss2
        """)):
            boss22 = sprites.create(assets.image("""
                boss2
            """), SpriteKind.boss2)
            tiles.place_on_tile(boss22, value)
            boss22.follow(mySprite, 50)
    else:
        tiles.place_on_random_tile(mySprite, assets.tile("""
            tile3
        """))
        info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.boss, on_on_overlap)

def on_up_pressed():
    mySprite.set_image(assets.image("""
        breddd
    """))
controller.up.on_event(ControllerButtonEvent.PRESSED, on_up_pressed)

def on_on_overlap2(sprite3, otherSprite2):
    tiles.place_on_random_tile(mySprite, assets.tile("""
        tile3
    """))
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.ICEBOSS, on_on_overlap2)

def on_overlap_tile2(sprite4, location2):
    tiles.place_on_random_tile(mySprite, assets.tile("""
        tile3
    """))
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        bottom0
    """),
    on_overlap_tile2)

def on_overlap_tile3(sprite5, location3):
    Startnextlevel()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        tile4
    """),
    on_overlap_tile3)

def on_b_pressed():
    global jamm
    if b == 1:
        if LR == 1:
            jamm = sprites.create_projectile_from_sprite(assets.image("""
                jammy
            """), mySprite, -125, 0)
        else:
            jamm = sprites.create_projectile_from_sprite(assets.image("""
                jammy
            """), mySprite, 125, 0)
    else:
        game.show_long_text("you haven't unlocked this yet", DialogLayout.BOTTOM)
        game.show_long_text("get to world 2 to unlock this", DialogLayout.BOTTOM)
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

def on_overlap_tile4(sprite6, location4):
    mySprite.vy = -600
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile
    """),
    on_overlap_tile4)

def on_overlap_tile5(sprite7, location5):
    tiles.place_on_random_tile(mySprite, assets.tile("""
        Blue
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        Orange0
    """),
    on_overlap_tile5)

def on_on_overlap3(sprite8, otherSprite3):
    sprite8.destroy(effects.spray, 500)
    otherSprite3.destroy(effects.fire, 500)
sprites.on_overlap(SpriteKind.Ice, SpriteKind.projectile, on_on_overlap3)

def on_on_overlap4(sprite9, otherSprite4):
    global BOOOOOOOOOS2
    sprite9.destroy(effects.fire, 500)
    otherSprite4.destroy(effects.spray, 500)
    for value2 in tiles.get_tiles_by_type(assets.tile("""
        fridge1
    """)):
        BOOOOOOOOOS2 = sprites.create(assets.image("""
                Temporary asset
            """),
            SpriteKind.ICEBOSS2)
        tiles.place_on_tile(BOOOOOOOOOS2, value2)
        BOOOOOOOOOS2.follow(mySprite, 70)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.ICEBOSS, on_on_overlap4)

def on_a_pressed():
    mySprite.vy = -200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_overlap_tile6(sprite10, location6):
    tiles.set_tile_at(tiles.get_tile_location(0, 15),
        assets.tile("""
            tile4
        """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile4
    """),
    on_overlap_tile6)

def Startnextlevel():
    global currentlevel, deaths, b, ITSMAD, myEnemy, myboss, ice, BOOOOS, Madman, MadmanStage, statusbar
    for value3 in sprites.all_of_kind(SpriteKind.enemy):
        value3.destroy()
    for value4 in sprites.all_of_kind(SpriteKind.Ice):
        value4.destroy()
    for value5 in sprites.all_of_kind(SpriteKind.SCIENCE):
        value5.destroy()
    currentlevel += 1
    deaths = 0
    if currentlevel == 1:
        tiles.set_tilemap(tilemap("""
            platformer1
        """))
    elif currentlevel == 2:
        tiles.set_tilemap(tilemap("""
            Number 2
        """))
    elif currentlevel == 3:
        tiles.set_tilemap(tilemap("""
            level7
        """))
    elif currentlevel == 4:
        game.splash("So the bread got", "to the final level")
        game.splash("Of this world,", "and found the")
        game.splash("Guardian of the", "waffles,")
        game.splash("The microwave!")
        tiles.set_tilemap(tilemap("""
            level8
        """))
    elif currentlevel == 5:
        b = 1
        scene.set_background_color(4)
        info.set_life(3)
        tiles.set_tilemap(tilemap("""
            level9
        """))
    elif currentlevel == 6:
        tiles.set_tilemap(tilemap("""
            level10
        """))
    elif currentlevel == 7:
        tiles.set_tilemap(tilemap("""
            level11
        """))
    elif currentlevel == 8:
        tiles.set_tilemap(tilemap("""
            level12
        """))
    elif currentlevel == 9:
        scene.set_background_image(img("""
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffff
                        fffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffff111ffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffff111fffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffff111fffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111fffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffff
                        ffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffff
                        ffffffff111ffffffffffffffffffffffffffffffffffffffff111fffffffffffffffff111fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffff
                        ffffffff111ffffffffffffffffffff111fffffffffffffffff111fffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffff111fffffffffffffffff111fffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffff
                        fffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff111ffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
        """))
        tiles.set_tilemap(tilemap("""
            The Minefield
        """))
    elif currentlevel == 10:
        tiles.set_tilemap(tilemap("""
            level14
        """))
    elif currentlevel == 11:
        ITSMAD = 1
        tiles.set_tilemap(tilemap("""
            level15
        """))
    else:
        game.over(True)
    tiles.place_on_random_tile(mySprite, assets.tile("""
        tile3
    """))
    for value6 in tiles.get_tiles_by_type(assets.tile("""
        tile5
    """)):
        myEnemy = sprites.create(assets.image("""
            Toaster
        """), SpriteKind.enemy)
        tiles.place_on_tile(myEnemy, value6)
        myEnemy.follow(mySprite, 30)
    for value7 in tiles.get_tiles_by_type(assets.tile("""
        tile2
    """)):
        myboss = sprites.create(assets.image("""
            BOSS
        """), SpriteKind.boss)
        tiles.place_on_tile(myboss, value7)
        myboss.follow(mySprite, 30)
    for value8 in tiles.get_tiles_by_type(assets.tile("""
        fridge
    """)):
        ice = sprites.create(assets.image("""
            ICEEEE
        """), SpriteKind.Ice)
        tiles.place_on_tile(ice, value8)
        ice.follow(mySprite, 50)
    for value9 in tiles.get_tiles_by_type(assets.tile("""
        fridge0
    """)):
        BOOOOS = sprites.create(img("""
                ....................
                            .........ee.........
                            ........eeee........
                            .......eeeeee.......
                            .......efeefe.......
                            ......eefeefee......
                            ......eeeeeeee......
                            .....4444444444.....
                            ....455555555554....
                            .....4555555554.....
                            ......45555554......
                            ......45555554......
                            ......45555554......
                            .......455554.......
                            .......455554.......
                            .......455554.......
                            .......455554.......
                            ........4554........
                            ........4554........
                            .........44.........
            """),
            SpriteKind.ICEBOSS)
        tiles.place_on_tile(BOOOOS, value9)
        BOOOOS.follow(mySprite, 50)
    for value10 in tiles.get_tiles_by_type(assets.tile("""
        myTile15
    """)):
        Madman = sprites.create(assets.image("""
                Mad Scientist
            """),
            SpriteKind.Mad_Scientist)
        tiles.place_on_tile(Madman, value10)
        Madman.follow(mySprite, 60)
        MadmanStage = 0
        statusbar = statusbars.create(50, 4, StatusBarKind.enemy_health)
        statusbar.position_direction(CollisionDirection.TOP)
        statusbar.set_label("Boss HP")
        statusbar.value = 100

def on_left_pressed():
    global LR
    mySprite.set_image(assets.image("""
        Toasty1
    """))
    LR = 1
controller.left.on_event(ControllerButtonEvent.PRESSED, on_left_pressed)

def on_on_overlap5(sprite11, otherSprite5):
    global MadmanStage
    if MadmanStage == 1:
        if sprite11.bottom > otherSprite5.y:
            statusbar.value += -20
            mySprite.set_velocity(-50, -50)
            if statusbar.value < 50:
                MadmanStage = 0
            else:
                MadmanStage = 2
        else:
            info.change_life_by(-1)
    else:
        info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.Mad_Scientist, on_on_overlap5)

def on_on_overlap6(sprite12, otherSprite6):
    sprite12.destroy(effects.fire, 500)
    otherSprite6.destroy(effects.fire, 500)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.projectile, on_on_overlap6)

def on_overlap_tile7(sprite13, location7):
    tiles.place_on_random_tile(mySprite, assets.tile("""
        tile3
    """))
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        left
    """),
    on_overlap_tile7)

def on_on_overlap7(sprite14, otherSprite7):
    tiles.place_on_random_tile(mySprite, assets.tile("""
        tile3
    """))
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.ICEBOSS2, on_on_overlap7)

def on_on_zero(status):
    Madman.destroy(effects.disintegrate, 2000)
    game.over(True, effects.confetti)
statusbars.on_zero(StatusBarKind.enemy_health, on_on_zero)

def on_on_overlap8(sprite15, otherSprite8):
    sprite15.destroy(effects.fire, 500)
    otherSprite8.destroy(effects.spray, 500)
    tiles.set_tile_at(tiles.get_tile_location(1, 10),
        assets.tile("""
            tile4
        """))
sprites.on_overlap(SpriteKind.projectile, SpriteKind.ICEBOSS3, on_on_overlap8)

def on_right_pressed():
    global LR
    mySprite.set_image(assets.image("""
        Toasty
    """))
    LR = 2
controller.right.on_event(ControllerButtonEvent.PRESSED, on_right_pressed)

def on_overlap_tile8(sprite16, location8):
    tiles.place_on_random_tile(mySprite, assets.tile("""
        tile3
    """))
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        left0
    """),
    on_overlap_tile8)

def on_on_overlap9(sprite17, otherSprite9):
    global MadmanStage
    sprite17.destroy()
    if MadmanStage != 1:
        MadmanStage = 1
    else:
        statusbar.value += -20
        if statusbar.value < 50:
            MadmanStage = 2
        else:
            MadmanStage = 0
sprites.on_overlap(SpriteKind.projectile,
    SpriteKind.Mad_Scientist,
    on_on_overlap9)

def on_down_pressed():
    mySprite.set_image(assets.image("""
        Toasty0
    """))
controller.down.on_event(ControllerButtonEvent.PRESSED, on_down_pressed)

def on_overlap_tile9(sprite18, location9):
    global LANDMINE
    tiles.set_tile_at(location9, assets.tile("""
        transparency16
    """))
    for value11 in tiles.get_tiles_by_type(assets.tile("""
        myTile5
    """)):
        LANDMINE = sprites.create(assets.image("""
            LANDMINE
        """), SpriteKind.BOOM)
        tiles.place_on_tile(LANDMINE, value11)
    LANDMINE.destroy(effects.fire, 500)
    music.big_crash.play()
    info.change_life_by(-1)
    mySprite.set_velocity(-100, -100)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile5
    """),
    on_overlap_tile9)

def on_life_zero():
    global deaths
    if deaths == 0:
        tiles.place_on_random_tile(mySprite, assets.tile("""
            tile3
        """))
        info.set_life(3)
        deaths += 1
    elif deaths == 1:
        tiles.place_on_random_tile(mySprite, assets.tile("""
            tile3
        """))
        info.set_life(3)
        deaths += 1
    else:
        game.over(False)
info.on_life_zero(on_life_zero)

def on_on_overlap10(sprite19, otherSprite10):
    tiles.place_on_random_tile(mySprite, assets.tile("""
        tile3
    """))
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.Ice, on_on_overlap10)

def on_on_overlap11(sprite20, otherSprite11):
    otherSprite11.destroy(effects.spray, 500)
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.SCIENCE, on_on_overlap11)

def on_overlap_tile10(sprite21, location10):
    tiles.place_on_random_tile(mySprite, assets.tile("""
        tile3
    """))
    info.change_life_by(-1)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        top
    """),
    on_overlap_tile10)

def on_on_overlap12(sprite22, otherSprite12):
    tiles.place_on_random_tile(mySprite, assets.tile("""
        tile3
    """))
    info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.ICEBOSS3, on_on_overlap12)

def on_on_overlap13(sprite23, otherSprite13):
    global _3rdboss
    if sprite23.bottom < otherSprite13.y:
        sprite23.vy = -100
        otherSprite13.destroy(effects.fire, 1000)
        for value12 in tiles.get_tiles_by_type(assets.tile("""
            boooos
        """)):
            _3rdboss = sprites.create(assets.image("""
                boss3
            """), SpriteKind.boss3)
            tiles.place_on_tile(_3rdboss, value12)
            _3rdboss.follow(mySprite, 70)
    else:
        tiles.place_on_random_tile(mySprite, assets.tile("""
            tile3
        """))
        info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.boss2, on_on_overlap13)

def on_overlap_tile11(sprite24, location11):
    global LANDMINE
    tiles.set_tile_at(location11, assets.tile("""
        transparency16
    """))
    for value13 in tiles.get_tiles_by_type(assets.tile("""
        myTile5
    """)):
        LANDMINE = sprites.create(assets.image("""
            LANDMINE
        """), SpriteKind.BOOM)
        tiles.place_on_tile(LANDMINE, value13)
    LANDMINE.destroy(effects.fire, 500)
    music.big_crash.play()
    sprite24.destroy()
scene.on_overlap_tile(SpriteKind.projectile,
    assets.tile("""
        myTile5
    """),
    on_overlap_tile11)

def on_on_overlap14(sprite25, otherSprite14):
    if sprite25.bottom < otherSprite14.y:
        sprite25.vy = -100
        otherSprite14.destroy(effects.fire, 2000)
        tiles.set_tile_at(tiles.get_tile_location(31, 6),
            assets.tile("""
                tile4
            """))
    else:
        tiles.place_on_random_tile(mySprite, assets.tile("""
            tile3
        """))
        info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.boss3, on_on_overlap14)

def on_on_overlap15(sprite26, otherSprite15):
    global BOOSSS3
    sprite26.destroy(effects.fire, 500)
    otherSprite15.destroy(effects.spray, 500)
    for value14 in tiles.get_tiles_by_type(assets.tile("""
        fridge2
    """)):
        BOOSSS3 = sprites.create(assets.image("""
                Temporary asset0
            """),
            SpriteKind.ICEBOSS3)
        tiles.place_on_tile(BOOSSS3, value14)
        BOOSSS3.follow(mySprite, 90)
sprites.on_overlap(SpriteKind.projectile, SpriteKind.ICEBOSS2, on_on_overlap15)

def on_overlap_tile12(sprite27, location12):
    Startnextlevel()
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile14
    """),
    on_overlap_tile12)

def on_on_overlap16(sprite28, otherSprite16):
    otherSprite16.destroy()
    if sprite28.bottom < otherSprite16.y:
        sprite28.vy = -100
    else:
        info.change_life_by(-1)
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap16)

def on_overlap_tile13(sprite29, location13):
    tiles.place_on_random_tile(mySprite, assets.tile("""
        Blue0
    """))
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        Orange1
    """),
    on_overlap_tile13)

Potion: Sprite = None
FlameToaster: Sprite = None
BOOSSS3: Sprite = None
_3rdboss: Sprite = None
LANDMINE: Sprite = None
statusbar: StatusBarSprite = None
MadmanStage = 0
Madman: Sprite = None
BOOOOS: Sprite = None
ice: Sprite = None
myboss: Sprite = None
myEnemy: Sprite = None
ITSMAD = 0
deaths = 0
BOOOOOOOOOS2: Sprite = None
jamm: Sprite = None
LR = 0
b = 0
boss22: Sprite = None
mySprite: Sprite = None
currentlevel = 0
game.splash("Once upon a time, ", "there was a piece of bread")
game.splash("Now, this bread was no", "ordinary piece of bread.")
game.splash("This bread was alive!")
game.splash("But one day,", "a mad scientist appeared ")
game.splash("And he brought the ", "appliances to life!")
game.splash("And he made the", "appliances chase after")
game.splash("The piece of bread", "so he could experiment")
game.splash("On the bread", "to learn how to bring")
game.splash("His dead friend ", "back to life.")
game.splash("So it was the bread's job", "to defeat the scientist")
game.splash("And save the world!")
currentlevel = 0
scene.set_background_color(9)
mySprite = sprites.create(assets.image("""
    Toasty
"""), SpriteKind.player)
mySprite.ay = 500
controller.move_sprite(mySprite, 100, 0)
scene.camera_follow_sprite(mySprite)
tiles.place_on_random_tile(mySprite, assets.tile("""
    tile3
"""))
info.set_life(3)
Startnextlevel()

def on_on_update():
    for value15 in sprites.all_of_kind(SpriteKind.enemy):
        if value15.is_hitting_tile(CollisionDirection.BOTTOM):
            if value15.vx < 0 and value15.tile_kind_at(TileDirection.LEFT, assets.tile("""
                tile1
            """)):
                value15.vy = -150
            elif value15.vx > 0 and value15.tile_kind_at(TileDirection.RIGHT, assets.tile("""
                tile1
            """)):
                value15.vy = -150
        elif value15.is_hitting_tile(CollisionDirection.LEFT):
            value15.vx = 30
        elif value15.is_hitting_tile(CollisionDirection.RIGHT):
            value15.vx = -30
game.on_update(on_on_update)

def on_update_interval():
    global FlameToaster
    if ITSMAD == 1:
        if MadmanStage == 0:
            for value16 in tiles.get_tiles_by_type(assets.tile("""
                tile5
            """)):
                FlameToaster = sprites.create(assets.image("""
                    Toaster0
                """), SpriteKind.enemy)
                tiles.place_on_tile(FlameToaster, value16)
                FlameToaster.follow(mySprite, 60)
game.on_update_interval(randint(4000, 7500), on_update_interval)

def on_update_interval2():
    global Potion
    if ITSMAD == 1:
        Potion = sprites.create(assets.image("""
            shield pot
        """), SpriteKind.SCIENCE)
        Potion.follow(mySprite, 70)
game.on_update_interval(randint(4000, 7500), on_update_interval2)
