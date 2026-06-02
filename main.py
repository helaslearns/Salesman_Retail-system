from Sales.Sales import Sales, SalesJunior, SalesSenior, SalesManager

def main():
    salesman1 = SalesJunior(
                                nama="Helas", 
                                total_penjualan=500000, 
                                target_penjualan=250000, 
                                gaji_pokok=1000000
                            )
    
    salesman2 = SalesSenior(
                                nama="Danis", 
                                total_penjualan=1000000, 
                                target_penjualan=100000, 
                                gaji_pokok=2000000,
                                bonus_gaji=0.02
                            )
    
    salesman3 = SalesManager(
                                nama="Maul", 
                                total_penjualan=2000000, 
                                target_penjualan=4000000, 
                                gaji_pokok=5000000,
                                bonus_gaji=0.03
                            )
    print(salesman1)
    print(salesman2)
    print(salesman3)

    print(f'Gaji {salesman1.nama} adalah {salesman1.hitungPendapatan()}')
    print(f'Gaji {salesman2.nama} adalah {salesman2.hitungPendapatan()}')
    print(f'Gaji {salesman3.nama} adalah {salesman3.hitungPendapatan()}')


if __name__ == "__main__":
    main()