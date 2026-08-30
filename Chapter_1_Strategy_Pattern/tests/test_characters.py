from characters.characters import Character,WeaponBehaviour,King,Bandit,KnifeBehaviour,GunBehaviour

def test_king_has_gun_and_bandit_has_knife():
    king=King()
    bandit=Bandit()
    assert king.fight()=='use gun'
    assert bandit.fight()=='use knife'

def test_dynamically_change_weapon_behaviour():
    king=King()
    king.set_weapon_behaviour(KnifeBehaviour())

    assert king.fight()=='use knife'