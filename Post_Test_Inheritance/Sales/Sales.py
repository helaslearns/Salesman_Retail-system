from __future__ import annotations

def formatRupiah(nominal: int | float):
    return f'Rp {nominal:,.0f}'.replace(',', '.') + ',00'

def hitungEkstra(sales: Sales | SalesJunior | SalesManager | SalesManager):
    pajak = 0.05
    if isinstance(sales, Sales | SalesJunior | SalesManager | SalesManager):
        if sales.total_penjualan == sales.target_penjualan:
            komisi = 0.05
            bonus = 0
        elif sales.total_penjualan >= sales.target_penjualan:
            bonus = 2000000
            komisi = 1
        else:
            komisi = 1
            bonus = 0
    
    return (bonus, komisi, pajak)

class Sales:
    _counter = 1
    def __init__(self, **kwargs):
        self.nama = kwargs.get('nama', f'K{Sales._counter:03d}')
        self.id_salesman = f'K{Sales._counter:03d}'
        Sales._counter += 1

        self.total_penjualan = kwargs.get('total_penjualan', 0)
        self.target_penjualan = kwargs.get('target_penjualan', 0)

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

    def hitungPendapatan(self):
        tambahan = hitungEkstra(self)
        gaji_final = ((self.gaji_pokok*tambahan[1]) + tambahan[0]) * (1 - tambahan[2])

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
        tambahan = hitungEkstra(self)
        sub_total = ((self.gaji_pokok*tambahan[1]) + tambahan[0]) * (1 - tambahan[2])
        gaji_final = sub_total * (1 + self.bonus_gaji)

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
        tambahan = hitungEkstra(self)
        sub_total = ((self.gaji_pokok*tambahan[1]) + tambahan[0]) * (1 - tambahan[2])
        gaji_final = sub_total * (1 + self.bonus_gaji)
        
        return f'{formatRupiah(gaji_final)}'

    def __str__(self):
        return (
            super().__str__() +
            f'Gaji Pokok: {formatRupiah(self.gaji_pokok)}\n'
            f'Bonus Gaji: {self.bonus_gaji*100}%\n'
        )   
    