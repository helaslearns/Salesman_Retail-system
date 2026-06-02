def formatRupiah(nominal: int | float):
    return f'Rp {nominal:,.0f}'.replace(',', '.') + ',00'

class Sales:
    _counter = 1
    
    def __init__(self, nama, total_penjualan, target_penjualan):
        self.nama = nama
        self.id_salesman = f'K{Sales._counter:03d}'
        Sales._counter += 1
        self.total_penjualan = total_penjualan
        self.target_penjualan = target_penjualan

    def _hitung_komisi_dasar(self):
        return self.total_penjualan * 0.05

    def _hitung_bonus_target(self):
        if self.total_penjualan >= self.target_penjualan:
            return 2000000
        return 0

    def hitungPendapatan(self):
        raise NotImplementedError

    def get_rincian(self):
        raise NotImplementedError

    def __str__(self):
        return (
            f'--- Rincian Pendapatan ---\n'
            f'Nama Salesman    : {self.nama}\n'
            f'ID Salesman      : {self.id_salesman}\n'
            f'Total Penjualan  : {formatRupiah(self.total_penjualan)}\n'
            f'Target Penjualan : {formatRupiah(self.target_penjualan)}\n'
            + self.get_rincian()
        )

class SalesJunior(Sales):
    def __init__(self, nama, total_penjualan, target_penjualan):
        super().__init__(nama, total_penjualan, target_penjualan)
        self.gaji_pokok = 3000000

    def hitungPendapatan(self):
        komisi = self._hitung_komisi_dasar()

        bonus_target = self._hitung_bonus_target()

        pendapatan_kotor = self.gaji_pokok + komisi + bonus_target

        pajak = pendapatan_kotor * 0.05

        return pendapatan_kotor - pajak

    def get_rincian(self):
        komisi = self._hitung_komisi_dasar()
        bonus_target = self._hitung_bonus_target()

        pendapatan_kotor = self.gaji_pokok + komisi + bonus_target

        pajak = pendapatan_kotor * 0.05
        pendapatan_bersih = pendapatan_kotor - pajak
        
        return (
            f'Jenjang          : Junior\n'
            f'Gaji Pokok       : {formatRupiah(self.gaji_pokok)}\n'
            f'Komisi Penjualan : {formatRupiah(komisi)}\n'
            f'Bonus Target     : {formatRupiah(bonus_target)}\n'
            f'Potongan Pajak   : {formatRupiah(pajak)}\n'
            f'Pendapatan Bersih: {formatRupiah(pendapatan_bersih)}\n'
        )

class SalesSenior(Sales):
    def __init__(self, nama, total_penjualan, target_penjualan):
        super().__init__(nama, total_penjualan, target_penjualan)
        self.gaji_pokok = 5000000

    def hitungPendapatan(self):
        komisi_dasar = self._hitung_komisi_dasar()
        tambahan_komisi = self.total_penjualan * 0.02
        total_komisi = komisi_dasar + tambahan_komisi

        bonus_target = self._hitung_bonus_target()

        pendapatan_kotor = self.gaji_pokok + total_komisi + bonus_target
        pajak = pendapatan_kotor * 0.05

        return pendapatan_kotor - pajak

    def get_rincian(self):
        komisi_dasar = self._hitung_komisi_dasar()
        tambahan_komisi = self.total_penjualan * 0.02
        total_komisi = komisi_dasar + tambahan_komisi

        bonus_target = self._hitung_bonus_target()

        pendapatan_kotor = self.gaji_pokok + total_komisi + bonus_target
        pajak = pendapatan_kotor * 0.05

        pendapatan_bersih = pendapatan_kotor - pajak
        
        return (
            f'Jenjang          : Senior\n'
            f'Gaji Pokok       : {formatRupiah(self.gaji_pokok)}\n'
            f'Total Komisi (7%): {formatRupiah(total_komisi)}\n'
            f'Bonus Target     : {formatRupiah(bonus_target)}\n'
            f'Potongan Pajak   : {formatRupiah(pajak)}\n'
            f'Pendapatan Bersih: {formatRupiah(pendapatan_bersih)}\n'
        )

class SalesManager(Sales):
    def __init__(self, nama, total_penjualan, target_penjualan):
        super().__init__(nama, total_penjualan, target_penjualan)
        self.gaji_pokok = 8000000

    def hitungPendapatan(self):
        komisi_dasar = self._hitung_komisi_dasar()
        tambahan_komisi = self.total_penjualan * 0.03
        total_komisi = komisi_dasar + tambahan_komisi

        bonus_tambahan = total_komisi * 0.01
        bonus_target = self._hitung_bonus_target()

        pendapatan_kotor = self.gaji_pokok + total_komisi + bonus_tambahan + bonus_target

        pajak = pendapatan_kotor * 0.05
        
        return pendapatan_kotor - pajak

    def get_rincian(self):
        komisi_dasar = self._hitung_komisi_dasar()
        tambahan_komisi = self.total_penjualan * 0.03
        total_komisi = komisi_dasar + tambahan_komisi

        bonus_tambahan = total_komisi * 0.01
        bonus_target = self._hitung_bonus_target()
        pendapatan_kotor = self.gaji_pokok + total_komisi + bonus_tambahan + bonus_target
        
        pajak = pendapatan_kotor * 0.05
        pendapatan_bersih = pendapatan_kotor - pajak
        
        return (
            f'Jenjang          : Manager\n'
            f'Gaji Pokok       : {formatRupiah(self.gaji_pokok)}\n'
            f'Total Komisi (8%): {formatRupiah(total_komisi)}\n'
            f'Bonus Tmbh (1%)  : {formatRupiah(bonus_tambahan)}\n'
            f'Bonus Target     : {formatRupiah(bonus_target)}\n'
            f'Potongan Pajak   : {formatRupiah(pajak)}\n'
            f'Pendapatan Bersih: {formatRupiah(pendapatan_bersih)}\n'
        )