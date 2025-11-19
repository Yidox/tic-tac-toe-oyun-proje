Tic-Tac-Toe (X-O Oyunu)

Bu proje Python ile geliştirilmiş basit bir konsol tabanlı Tic-Tac-Toe (X-O) oyunudur. Oyuncu O, bilgisayar ise X ile oynar. Bilgisayar oyuna her zaman merkeze X koyarak başlar.

Özellikler

3x3 standart Tic-Tac-Toe tahtası

Kullanıcı girdi doğrulama (geçersiz veya dolu kare seçme engellenir)

Bilgisayarın rastgele hamle yapması

Kazanma, kaybetme ve berabere durumunun kontrol edilmesi

Açıklayıcı ve düzenli kod yapısı

Nasıl Çalışır?

Oyun başlar ve bilgisayar merkeze X koyar.

Kullanıcı 1-9 arasında bir sayı girerek hamle yapar.

Her hamleden sonra:

Oyuncunun kazanıp kazanmadığı kontrol edilir.

Tahtada boş yer kalmazsa oyun berabere biter.

Bilgisayar boş karelerden rastgele birine X koyar.

Oyuncu veya bilgisayar kazanırsa oyun sona erer.

Kullanılan Fonksiyonlar

display_board(board): Tahtayı ekrana biçimli şekilde yazdırır.

enter_move(board): Kullanıcıdan geçerli hamle alır.

make_list_of_free_fields(board): Boş kareleri listeler.

victory_for(board, sign): Belirtilen işaretin kazanıp kazanmadığını kontrol eder.

draw_move(board): Bilgisayarın rastgele hamle yapmasını sağlar.

Ana oyun döngüsü.
