def test_yakit_ekle_tuzagi():
    # None kalıbı ile düzeltilmiş fonksiyon
    def yakit_ekle(miktar: int, depo: list = None) -> list:
        if depo is None:
            depo = []
        depo.append(miktar)
        return depo

    depo1 = yakit_ekle(10)
    depo2 = yakit_ekle(20)
    
    assert depo1 == [10]
    assert depo2 == [20]