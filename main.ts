namespace SpriteKind {
    export const boss = SpriteKind.create()
    export const Ice = SpriteKind.create()
    export const boss2 = SpriteKind.create()
    export const boss3 = SpriteKind.create()
    export const target = SpriteKind.create()
    export const ICEBOSS = SpriteKind.create()
    export const ICEBOSS2 = SpriteKind.create()
    export const ICEBOSS3 = SpriteKind.create()
    export const BOOM = SpriteKind.create()
    export const Mad_Scientist = SpriteKind.create()
    export const StatusBarSprite = SpriteKind.create()
    export const SCIENCE = SpriteKind.create()
}
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile1`, function (sprite, location) {
    tiles.setTileAt(tiles.getTileLocation(64, 21), assets.tile`tile4`)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.boss, function (sprite, otherSprite) {
    if (sprite.bottom < otherSprite.y) {
        sprite.vy = -100
        otherSprite.destroy(effects.fire, 500)
        for (let value of tiles.getTilesByType(assets.tile`boss2`)) {
            boss2 = sprites.create(assets.image`boss2`, SpriteKind.boss2)
            tiles.placeOnTile(boss2, value)
            boss2.follow(mySprite, 50)
        }
    } else {
        tiles.placeOnRandomTile(mySprite, assets.tile`tile3`)
        info.changeLifeBy(-1)
    }
})
controller.up.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(assets.image`breddd`)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.ICEBOSS, function (sprite, otherSprite) {
    tiles.placeOnRandomTile(mySprite, assets.tile`tile3`)
    info.changeLifeBy(-1)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`bottom0`, function (sprite, location) {
    tiles.placeOnRandomTile(mySprite, assets.tile`tile3`)
    info.changeLifeBy(-1)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`tile4`, function (sprite, location) {
    Startnextlevel()
})
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    if (b == 1) {
        if (LR == 1) {
            jamm = sprites.createProjectileFromSprite(assets.image`jammy`, mySprite, -125, 0)
        } else {
            jamm = sprites.createProjectileFromSprite(assets.image`jammy`, mySprite, 125, 0)
        }
    } else {
        game.showLongText("you haven't unlocked this yet", DialogLayout.Bottom)
        game.showLongText("get to world 2 to unlock this", DialogLayout.Bottom)
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile`, function (sprite, location) {
    mySprite.vy = -600
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`Orange0`, function (sprite, location) {
    tiles.placeOnRandomTile(mySprite, assets.tile`Blue`)
})
sprites.onOverlap(SpriteKind.Ice, SpriteKind.Projectile, function (sprite, otherSprite) {
    sprite.destroy(effects.spray, 500)
    otherSprite.destroy(effects.fire, 500)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.ICEBOSS, function (sprite, otherSprite) {
    sprite.destroy(effects.fire, 500)
    otherSprite.destroy(effects.spray, 500)
    for (let value of tiles.getTilesByType(assets.tile`fridge1`)) {
        BOOOOOOOOOS2 = sprites.create(assets.image`Temporary asset`, SpriteKind.ICEBOSS2)
        tiles.placeOnTile(BOOOOOOOOOS2, value)
        BOOOOOOOOOS2.follow(mySprite, 70)
    }
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.vy = -200
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile4`, function (sprite, location) {
    tiles.setTileAt(tiles.getTileLocation(0, 15), assets.tile`tile4`)
})
function Startnextlevel() {
    for (let value of sprites.allOfKind(SpriteKind.Enemy)) {
        value.destroy()
    }
    for (let value of sprites.allOfKind(SpriteKind.Ice)) {
        value.destroy()
    }
    for (let value of sprites.allOfKind(SpriteKind.SCIENCE)) {
        value.destroy()
    }
    currentlevel += 1
    deaths = 0
    if (currentlevel == 1) {
        tiles.setTilemap(tilemap`platformer1`)
    } else if (currentlevel == 2) {
        tiles.setTilemap(tilemap`Number 2`)
    } else if (currentlevel == 3) {
        tiles.setTilemap(tilemap`level7`)
    } else if (currentlevel == 4) {
        game.splash("So the bread got", "to the final level")
        game.splash("Of this world,", "and found the")
        game.splash("Guardian of the", "waffles,")
        game.splash("The microwave!")
        tiles.setTilemap(tilemap`level8`)
    } else if (currentlevel == 5) {
        b = 1
        scene.setBackgroundColor(4)
        info.setLife(3)
        tiles.setTilemap(tilemap`level9`)
    } else if (currentlevel == 6) {
        tiles.setTilemap(tilemap`level10`)
    } else if (currentlevel == 7) {
        tiles.setTilemap(tilemap`level11`)
    } else if (currentlevel == 8) {
        tiles.setTilemap(tilemap`level12`)
    } else if (currentlevel == 9) {
        scene.setBackgroundImage(img`
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
            `)
        tiles.setTilemap(tilemap`The Minefield`)
    } else if (currentlevel == 10) {
        tiles.setTilemap(tilemap`level14`)
    } else if (currentlevel == 11) {
        ITSMAD = 1
        tiles.setTilemap(tilemap`level15`)
    } else {
        game.over(true)
    }
    tiles.placeOnRandomTile(mySprite, assets.tile`tile3`)
    for (let value of tiles.getTilesByType(assets.tile`tile5`)) {
        myEnemy = sprites.create(assets.image`Toaster`, SpriteKind.Enemy)
        tiles.placeOnTile(myEnemy, value)
        myEnemy.follow(mySprite, 30)
    }
    for (let value of tiles.getTilesByType(assets.tile`tile2`)) {
        myboss = sprites.create(assets.image`BOSS`, SpriteKind.boss)
        tiles.placeOnTile(myboss, value)
        myboss.follow(mySprite, 30)
    }
    for (let value of tiles.getTilesByType(assets.tile`fridge`)) {
        ice = sprites.create(assets.image`ICEEEE`, SpriteKind.Ice)
        tiles.placeOnTile(ice, value)
        ice.follow(mySprite, 50)
    }
    for (let value of tiles.getTilesByType(assets.tile`fridge0`)) {
        BOOOOS = sprites.create(img`
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
            `, SpriteKind.ICEBOSS)
        tiles.placeOnTile(BOOOOS, value)
        BOOOOS.follow(mySprite, 50)
    }
    for (let value of tiles.getTilesByType(assets.tile`myTile15`)) {
        Madman = sprites.create(assets.image`Mad Scientist`, SpriteKind.Mad_Scientist)
        tiles.placeOnTile(Madman, value)
        Madman.follow(mySprite, 60)
        MadmanStage = 0
        statusbar = statusbars.create(50, 4, StatusBarKind.EnemyHealth)
        statusbar.positionDirection(CollisionDirection.Top)
        statusbar.setLabel("Boss HP")
        statusbar.value = 100
    }
}
controller.left.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(assets.image`Toasty1`)
    LR = 1
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Mad_Scientist, function (sprite, otherSprite) {
    if (MadmanStage == 1) {
        if (sprite.bottom > otherSprite.y) {
            statusbar.value += -20
            mySprite.setVelocity(-50, -50)
            if (statusbar.value < 50) {
                MadmanStage = 0
            } else {
                MadmanStage = 2
            }
        } else {
            info.changeLifeBy(-1)
        }
    } else {
        info.changeLifeBy(-1)
    }
})
sprites.onOverlap(SpriteKind.Enemy, SpriteKind.Projectile, function (sprite, otherSprite) {
    sprite.destroy(effects.fire, 500)
    otherSprite.destroy(effects.fire, 500)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`left`, function (sprite, location) {
    tiles.placeOnRandomTile(mySprite, assets.tile`tile3`)
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.ICEBOSS2, function (sprite, otherSprite) {
    tiles.placeOnRandomTile(mySprite, assets.tile`tile3`)
    info.changeLifeBy(-1)
})
statusbars.onZero(StatusBarKind.EnemyHealth, function (status) {
    Madman.destroy(effects.disintegrate, 2000)
    game.over(true, effects.confetti)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.ICEBOSS3, function (sprite, otherSprite) {
    sprite.destroy(effects.fire, 500)
    otherSprite.destroy(effects.spray, 500)
    tiles.setTileAt(tiles.getTileLocation(1, 10), assets.tile`tile4`)
})
controller.right.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(assets.image`Toasty`)
    LR = 2
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`left0`, function (sprite, location) {
    tiles.placeOnRandomTile(mySprite, assets.tile`tile3`)
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.Mad_Scientist, function (sprite, otherSprite) {
    sprite.destroy()
    if (MadmanStage != 1) {
        MadmanStage = 1
    } else {
        statusbar.value += -20
        if (statusbar.value < 50) {
            MadmanStage = 2
        } else {
            MadmanStage = 0
        }
    }
})
controller.down.onEvent(ControllerButtonEvent.Pressed, function () {
    mySprite.setImage(assets.image`Toasty0`)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile5`, function (sprite, location) {
    tiles.setTileAt(location, assets.tile`transparency16`)
    for (let value of tiles.getTilesByType(assets.tile`myTile5`)) {
        LANDMINE = sprites.create(assets.image`LANDMINE`, SpriteKind.BOOM)
        tiles.placeOnTile(LANDMINE, value)
    }
    LANDMINE.destroy(effects.fire, 500)
    music.bigCrash.play()
    info.changeLifeBy(-1)
    mySprite.setVelocity(-100, -100)
})
info.onLifeZero(function () {
    if (deaths == 0) {
        tiles.placeOnRandomTile(mySprite, assets.tile`tile3`)
        info.setLife(3)
        deaths += 1
    } else if (deaths == 1) {
        tiles.placeOnRandomTile(mySprite, assets.tile`tile3`)
        info.setLife(3)
        deaths += 1
    } else {
        game.over(false)
    }
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Ice, function (sprite, otherSprite) {
    tiles.placeOnRandomTile(mySprite, assets.tile`tile3`)
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.SCIENCE, function (sprite, otherSprite) {
    otherSprite.destroy(effects.spray, 500)
    info.changeLifeBy(-1)
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`top`, function (sprite, location) {
    tiles.placeOnRandomTile(mySprite, assets.tile`tile3`)
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.ICEBOSS3, function (sprite, otherSprite) {
    tiles.placeOnRandomTile(mySprite, assets.tile`tile3`)
    info.changeLifeBy(-1)
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.boss2, function (sprite, otherSprite) {
    if (sprite.bottom < otherSprite.y) {
        sprite.vy = -100
        otherSprite.destroy(effects.fire, 1000)
        for (let value of tiles.getTilesByType(assets.tile`boooos`)) {
            _3rdboss = sprites.create(assets.image`boss3`, SpriteKind.boss3)
            tiles.placeOnTile(_3rdboss, value)
            _3rdboss.follow(mySprite, 70)
        }
    } else {
        tiles.placeOnRandomTile(mySprite, assets.tile`tile3`)
        info.changeLifeBy(-1)
    }
})
scene.onOverlapTile(SpriteKind.Projectile, assets.tile`myTile5`, function (sprite, location) {
    tiles.setTileAt(location, assets.tile`transparency16`)
    for (let value of tiles.getTilesByType(assets.tile`myTile5`)) {
        LANDMINE = sprites.create(assets.image`LANDMINE`, SpriteKind.BOOM)
        tiles.placeOnTile(LANDMINE, value)
    }
    LANDMINE.destroy(effects.fire, 500)
    music.bigCrash.play()
    sprite.destroy()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.boss3, function (sprite, otherSprite) {
    if (sprite.bottom < otherSprite.y) {
        sprite.vy = -100
        otherSprite.destroy(effects.fire, 2000)
        tiles.setTileAt(tiles.getTileLocation(31, 6), assets.tile`tile4`)
    } else {
        tiles.placeOnRandomTile(mySprite, assets.tile`tile3`)
        info.changeLifeBy(-1)
    }
})
sprites.onOverlap(SpriteKind.Projectile, SpriteKind.ICEBOSS2, function (sprite, otherSprite) {
    sprite.destroy(effects.fire, 500)
    otherSprite.destroy(effects.spray, 500)
    for (let value of tiles.getTilesByType(assets.tile`fridge2`)) {
        BOOSSS3 = sprites.create(assets.image`Temporary asset0`, SpriteKind.ICEBOSS3)
        tiles.placeOnTile(BOOSSS3, value)
        BOOSSS3.follow(mySprite, 90)
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile14`, function (sprite, location) {
    Startnextlevel()
})
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite, otherSprite) {
    otherSprite.destroy()
    if (sprite.bottom < otherSprite.y) {
        sprite.vy = -100
    } else {
        info.changeLifeBy(-1)
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`Orange1`, function (sprite, location) {
    tiles.placeOnRandomTile(mySprite, assets.tile`Blue0`)
})
let Potion: Sprite = null
let FlameToaster: Sprite = null
let BOOSSS3: Sprite = null
let _3rdboss: Sprite = null
let LANDMINE: Sprite = null
let statusbar: StatusBarSprite = null
let MadmanStage = 0
let Madman: Sprite = null
let BOOOOS: Sprite = null
let ice: Sprite = null
let myboss: Sprite = null
let myEnemy: Sprite = null
let ITSMAD = 0
let deaths = 0
let BOOOOOOOOOS2: Sprite = null
let jamm: Sprite = null
let LR = 0
let b = 0
let boss2: Sprite = null
let mySprite: Sprite = null
let currentlevel = 0
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
scene.setBackgroundColor(9)
mySprite = sprites.create(assets.image`Toasty`, SpriteKind.Player)
mySprite.ay = 500
controller.moveSprite(mySprite, 100, 0)
scene.cameraFollowSprite(mySprite)
tiles.placeOnRandomTile(mySprite, assets.tile`tile3`)
info.setLife(3)
Startnextlevel()
game.onUpdate(function () {
    for (let value of sprites.allOfKind(SpriteKind.Enemy)) {
        if (value.isHittingTile(CollisionDirection.Bottom)) {
            if (value.vx < 0 && value.tileKindAt(TileDirection.Left, assets.tile`tile1`)) {
                value.vy = -150
            } else if (value.vx > 0 && value.tileKindAt(TileDirection.Right, assets.tile`tile1`)) {
                value.vy = -150
            }
        } else if (value.isHittingTile(CollisionDirection.Left)) {
            value.vx = 30
        } else if (value.isHittingTile(CollisionDirection.Right)) {
            value.vx = -30
        }
    }
})
game.onUpdateInterval(randint(4000, 7500), function () {
    if (ITSMAD == 1) {
        if (MadmanStage == 0) {
            for (let value of tiles.getTilesByType(assets.tile`tile5`)) {
                FlameToaster = sprites.create(assets.image`Toaster0`, SpriteKind.Enemy)
                tiles.placeOnTile(FlameToaster, value)
                FlameToaster.follow(mySprite, 60)
            }
        }
    }
})
game.onUpdateInterval(randint(4000, 7500), function () {
    if (ITSMAD == 1) {
        Potion = sprites.create(assets.image`shield pot`, SpriteKind.SCIENCE)
        Potion.follow(mySprite, 70)
    }
})

