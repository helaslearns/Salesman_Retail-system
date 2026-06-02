from Sales.Sales import SalesJunior, SalesSenior, SalesManager

def main():
    salesman1 = SalesJunior(
        nama="Helas", 
        total_penjualan=5000000, 
        target_penjualan=5000000
    )
    
    salesman2 = SalesSenior(
        nama="Danis", 
        total_penjualan=15000000, 
        target_penjualan=10000000
    )
    
    salesman3 = SalesManager(
        nama="Maul", 
        total_penjualan=8000000, 
        target_penjualan=10000000
    )

    print(salesman1)
    print(salesman2)
    print(salesman3)

if __name__ == "__main__":
    main()