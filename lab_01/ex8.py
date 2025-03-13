def chia_cho_5(so_nhi_phan):
    so_thap_phan = int(so_nhi_phan, 2)
    if so_thap_phan % 5 == 0:
        return True 
    else:
        return False
chuoi_nhi_phan = input("nhap so nhi phan: ")
so_nhi_phan_list = chuoi_nhi_phan.split(',')
chia_cho_5 = [so for so in so_nhi_phan_list if chia_cho_5(so)]
if len(chia_cho_5) > 0:
    ket_qua = ",".join(chia_cho_5)
    print("cac so chia het cho 5: ", ",".ket_qua)
else:
    print("khong co so nao chia het cho 5")