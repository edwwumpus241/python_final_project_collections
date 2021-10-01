#Base codes
paidi = 10;
pesci = 12;
paket_paidi = paidi * 2;
paket_pesci = pesci * 7;
keranjang_paidi = paket_paidi * paket_paidi;
keranjang_pesci = paket_pesci * paket_pesci;
total_jeruk = keranjang_paidi + keranjang_pesci;
paino = 2;
bruno = 6;
jonathan = 5;
total_apel = paino + bruno + jonathan;
bus_sekolah_max = 150;
bus_sekolah_speed_now = 40;
coklat = 20;
chips  = 10;
total_snack_jonathan = coklat + chips;
jam_pr_start = 1321;
jam_pr_end = 1347;
time_spend = jam_pr_start - jam_pr_end;

#Result Codes
print("==========================================================================================================================================================================")
print("Pada suatu hari ada dua orang yang bersahabat membawa jeruk untuk piknik sekolah")
print("Paidi mempunyai " + str(paidi) + " paket jeruk " + str(paket_paidi) + " Dan teman Paidi pesci mempunyai " + str(pesci) + " jeruk dan pesci mempunyai  "  + str(paket_pesci) + " Paket jeruk")
print("Di keranjang Paidi ada " + str(keranjang_paidi) + " jeruk " + "Dan didalam keranjang pesci ada " + str(keranjang_pesci) + " jeruk " + "dan total jeruk di keranjang mereka adalah " + str(total_jeruk))
print("Saat mereka berjalan mereka bertemu beberapa teman yang bernama : Bruno,Jonathan dan Paino mereka membawa apel yang jumlah total apel yang dibawa mereka adalah = " + str(total_apel)) 
print("Setelah piknik sekolah Paidi,Pesci,Bruno,Jonathan, dan paino pulang menggunakan bus sekolah")
print("Saat mereka sedang perjalanan pulang sekolah Bruno mengetahui bahwa kecepatan bus sekolag sekarang adalah " + str(bus_sekolah_speed_now) + " lalu mereka pergi ketempat supir dan melihat bahwa kecepatan maksimal bus sekolah adalah " + str(bus_sekolah_max))
print("Lalu salah satu dari teman mereka, Jonathan mengundang teman-temannya ke rumahnya besok jam 13:00")
print("1 DAY LATER")
print("Mereka datang pada jam 12:58 dan mereka sedang menunggu jam 13:00 karena jonathan adalah anak yang harus tepat waktu lebih lambat atau cepat dia ingin tepat waktu")
print("Jonathan membuka pintu rumahnya dan mereka di sambut dengan " + str(coklat) + " coklat dan " + str(chips) + " snack kentang " + " dan total makanan yang dibawa oleh jonathan adalah " + str(total_snack_jonathan))
print("Dan mereka mempunyai ide untuk mengerjakan PR bersama-sama, pada jam " + str(jam_pr_start)+ " mereka mulai mengerjakan " + "pada jam " + str(jam_pr_end) + " dan mereka menghitung berapa menit yang mereka habis kan untuk mengerjakan PR ")
print("Mereka menghabiskan " + str(time_spend) + " menit")
print("Saat pada jam 14:32 mereka pulang dari rumah Jonathan")
print("The end")
print("==========================================================================================================================================================================")

