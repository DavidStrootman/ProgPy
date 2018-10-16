def seizoen(maand: int):
    if 2 < maand < 12:
        if maand > 5:
            if maand > 8 :
                print('herfst')
                return
            print('zomer')
            return
        print('lente')
        return
    print('winter')


seizoen(3)
