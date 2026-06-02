def formatRupiah(nominal: int | float):
    return f'Rp {nominal:,.0f}'.replace(',', '.') + ',00'

class Sales:
    _counter = 1
    def __init__(self, **kwargs):
        self.nama = kwargs.get('nama', f'K{Sales._counter:03d}')
        self.id_salesman = f'K{Sales._counter:03d}'
        Sales._counter += 1

        self.total_penjualan = kwargs.get('total_penjualan', 0)
        self.target_penjualan = kwargs.get('target_penjualan', 0)

    def _remuneration(self):
        pajak = 0.05
        if self.total_penjualan == self.target_penjualan:
            komisi = 0.05
            bonus = 0
        elif self.total_penjualan > self.target_penjualan:
            komisi = 1 
            bonus = 2000000
        else:
            komisi = 1
            bonus = 0
        
        return komisi, bonus, pajak
    
    def hitungPendapatan(self):
        return 0.0

    def __str__(self):
        return (
            f'Nama Salesman: {self.nama}\n'
            f'ID Salesman: {self.id_salesman}\n'
            f'Total Penjualan: {formatRupiah(self.total_penjualan)}\n'
            f'Target Penjualan: {formatRupiah(self.target_penjualan)}\n'
        )
    
class SalesJunior(Sales):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gaji_pokok = kwargs.get('gaji_pokok', 0)
        self.bonus_gaji = 0

    def hitungPendapatan(self):
        komisi, bonus, pajak = super()._remuneration()
        sub_total = (self.gaji_pokok + (1 + komisi) + bonus) * (1 - pajak)
        gaji_final = sub_total + self.bonus_gaji

        return f'{formatRupiah(gaji_final)}'


    def __str__(self):
        return (
            super().__str__() +
            f'Gaji Pokok: {formatRupiah(self.gaji_pokok)}\n'
        )

class SalesSenior(Sales):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gaji_pokok = kwargs.get('gaji_pokok', 0)
        self.bonus_gaji = kwargs.get('bonus_gaji', 0)

    def hitungPendapatan(self):
        komisi, bonus, pajak = super()._remuneration()
        sub_total = (self.gaji_pokok + (1 + komisi) + bonus) * (1 - pajak)
        gaji_final = sub_total + self.bonus_gaji

        return f'{formatRupiah(gaji_final)}'

    def __str__(self):
        return (
            super().__str__() +
            f'Gaji Pokok: {formatRupiah(self.gaji_pokok)}\n'
            f'Bonus Gaji: {self.bonus_gaji*100}%\n'
        )

class SalesManager(Sales):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.gaji_pokok = kwargs.get('gaji_pokok', 0)
        self.bonus_gaji = kwargs.get('bonus_gaji', 0)

    def hitungPendapatan(self):
        komisi, bonus, pajak = super()._remuneration()
        sub_total = (self.gaji_pokok + (1 + komisi) + bonus) * (1 - pajak)
        gaji_final = sub_total + self.bonus_gaji

        return f'{formatRupiah(gaji_final)}'

    def __str__(self):
        return (
            super().__str__() +
            f'Gaji Pokok: {formatRupiah(self.gaji_pokok)}\n'
            f'Bonus Gaji: {self.bonus_gaji*100}%\n'
        )   
    
