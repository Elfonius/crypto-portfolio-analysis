# Örnek Portföy İncelemesi (Sentetik)

**Tarih:** 2026-10-30 14:00 UTC  
**Ana para birimi:** USD  
**Veri kapsamı:** %92 (5 pozisyonun 4'ü canlı; small-cap fiyatı 6 saat gecikmeli)  
**Benchmark:** BTC  
**Mod:** Tam inceleme

> Bu örnek sentetiktir. Gerçek bir cüzdan, kişi veya yatırım tavsiyesi değildir.

## 1. Yönetici Özeti

- **Ana bulgu:** Portföyün %65'i BTC ve ETH'de; ilk iki pozisyon kurumsal bir "beta" portföyü gibi davranıyor, ancak %8'lik small-cap pozisyonu likidite ve fiyat riskini artırıyor.
- **Neden önemli:** Getiri BTC'ye göre geride; bunun ne kadarı seçim, ne kadarı daha yüksek beta ve likidite riski, ayrıştırılmalı.
- **Doğrulanan:** Fiyatlar iki kaynaktan; cüzdan bakiyeleri ikinci kaynakla %0,4 farkla mutabık.
- **Doğrulanamayan:** Small-cap tokenın gerçek çıkış derinliği; cost basis yok.
- **Karar:** Small-cap pozisyonunu gözden geçir; BTC/ETH dışındaki riski ayrı bütçele. Bu bir işlem talimatı değildir.
- **Görüşü değiştirecek şey:** Small-cap likiditesinin 5 günün altına inmesi veya BTC beta'sının 1,4'ü aşması.

## 2. IPS-lite ve Kapsam

| Alan | Bilgi |
|---|---|
| Amaç | Büyüme; 3 yıllık ufuk |
| Getiri hedefi | BTC'yi geçmek değil, BTC'ye yakın riskle uzun vadeli büyüme |
| Risk toleransı | Maksimum %35 drawdown |
| Likidite | 12 ay içinde $20.000 |
| Vergi/hukuk | Vergi detayı bu örnekte kapsam dışıdır; bu bir vergi görüşü değildir |
| Karar verici | Portföy sahibi |
| İnceleme | Çeyreklik; %30 tek-pozisyon eşiği |

## 3. Portföy Anlık Görüntüsü

| Pozisyon | Değer | Ağırlık | Kaynak/tarih | Kanıt |
|---|---:|---:|---|---|
| BTC | $42.000 | %42,0 | İki borsa ortalaması, 14:00 UTC | VERIFIED |
| ETH | $23.000 | %23,0 | İki borsa ortalaması, 14:00 UTC | VERIFIED |
| SOL | $15.000 | %15,0 | Borsa + aggregator, 14:00 UTC | VERIFIED |
| USDC | $12.000 | %12,0 | İhraççı + piyasa, 14:00 UTC | VERIFIED |
| SMALL | $8.000 | %8,0 | Tek DEX, 08:00 UTC | ESTIMATED |
| **Toplam** | **$100.000** | **%100** | — | — |

**Top-1 / Top-2 / Top-3:** %42,0 / %65,0 / %80,0  
**HHI:** 0,2726; **efektif pozisyon:** 3,67  
**Küme haritası:** BTC %42; ETH %23; SOL %15; stablecoin %12; small-cap %8. İlk üç pozisyon “major crypto” kümesinde %80.

## 4. Performans ve Atıf

| Ölçü | Değer | Dönem | Benchmark | Kanıt |
|---|---:|---|---|---|
| TWR | +%18,4 | 2026-01-01 – 2026-10-30 | BTC +%24,1 | VERIFIED |
| MWR | +%16,9 | Aynı | — | ESTIMATED |
| Getiri katkısı | BTC +%9,8; ETH +%5,1; SOL +%4,2; diğer −%0,7 | Aynı | — | ESTIMATED |

Portföy BTC'ye göre **5,7 puan geride**. Bu, “seçim” mi yoksa “daha yüksek beta ve likidite riski” mi? Small-cap ve SOL katkısı bunu tek başına açıklamıyor; cost basis olmadığı için P&L değil, değer değişimi ölçülüyor.

## 5. Risk Panosu

| Ölçü | Değer | Dönem | Yöntem | Sınır |
|---|---:|---|---|---|
| Volatilite | %58 | 365g | Tarihsel | %50 |
| Maks. drawdown | −%34 | 2 yıl | Günlük | −%35 |
| VaR 95% 1g | %4,8 | 365g | Tarihsel | %4 |
| CVaR 95% 1g | %7,1 | 365g | Tarihsel | %6 |
| Beta (BTC) | 1,12 | 365g | OLS | 1,20 |
| En büyük risk katkısı | BTC %46 | 365g | Bileşen CVaR | — |

**Uyarı:** VaR “maksimum kayıp” değildir. Likidite ve kuyruk riski ayrıca test edilmelidir.

## 6. Likidite ve Çıkış

| Pozisyon | Değer | Günlük işlem hacmi | %1 gün | %5 gün | %10 gün | Kilit |
|---|---:|---:|---:|---:|---:|---|
| BTC | $42.000 | $8,0 mlr | 0,01 | 0,01 | 0,01 | Yok |
| ETH | $23.000 | $4,0 mlr | 0,01 | 0,01 | 0,01 | Yok |
| SOL | $15.000 | $600 mn | 0,03 | 0,01 | 0,01 | Yok |
| USDC | $12.000 | $2,0 mlr | 0,01 | 0,01 | 0,01 | İhraççı gate |
| SMALL | $8.000 | $180.000 | 4,4 | 0,9 | 0,4 | Yok |

**Stres likiditesi:** Small-cap hacmi %25'e düşerse çıkış **17,8 gün**.  
**İlk çıkamayan pozisyon:** Small-cap; 12 aylık likidite ihtiyacı için sorun değil, ancak ani çıkışta değil.

## 7. Varlık Bazlı Bulgular

### BTC

- **Tez:** Portföyün reserve asset'i; likidite ve kurumsal erişim güçlü.
- **Tokenomics:** Arz sabit; emisyon yok; madencilik ödülü ağ güvenliği.
- **Değer yakalama:** Doğrudan nakit akışı yok; değer, benimsenme ve likidite.
- **Risk:** Regülasyon, borsa/kendi kendine saklama, beta.
- **Kanıt:** Fiyat iki kaynak; hacim doğrulandı.

### ETH

- **Tez:** Akıllı sözleşme altyapısı; staking getirisi.
- **Tokenomics:** Emisyon + fee burn; net arz değişimi dönemsel.
- **Değer yakalama:** Staking getirisi ve burn; ancak validator/MEV bağımlılığı.
- **Risk:** L2'ye değer kayması, staking likiditesi, regülasyon.

### SOL

- **Tez:** Yüksek performanslı L1; tüketici uygulamaları.
- **Tokenomics:** Enflasyon + fee burn; gerçek net emisyon dönemsel.
- **Değer yakalama:** Staking ve ağ kullanımı; token holder nakit akışı sınırlı.
- **Risk:** Outage geçmişi, validator yoğunluğu, rekabet.

### USDC

- **Tez:** Likidite tamponu.
- **Risk:** İhraççı, rezerv, redemption gate; %12 ağırlık makul ama “cash” değil.

### SMALL

- **Tez:** Yüksek büyüme potansiyeli.
- **Tokenomics:** Düşük float; yakın unlock takvimi doğrulanmalı.
- **Değer yakalama:** Belirsiz; gelir paylaşımı yok.
- **Risk:** Likidite, fiyat manipülasyonu, akıllı sözleşme.
- **Kanıt:** Tek DEX fiyatı; bağımsız ikinci kaynak yok.

## 8. DeFi ve On-chain

Bu örnekte lending/LP pozisyonu yok. On-chain akış: BTC ve ETH borsa çıkışı son 7 günde hafif negatif; bu tek başına tez değiştirmez. Entity etiketleri olasılıksal; kesin yargı için kullanılmadı.

## 9. Piyasa Rejimi ve Senaryolar

| Senaryo | Şoklar | Portföy kaybı | En kötü pozisyon | İlk ihlal |
|---|---|---:|---|---|
| Risk-off | BTC −30%, ETH −40%, SOL −50%, SMALL −70% | $30.900 / %30,9 | SMALL | Drawdown limitine yakın |
| Stablecoin depeg | USDC −20% | $2.400 / %2,4 | USDC | Likidite gate |
| Likidite şoku | Small-cap hacmi −75% | Çıkış 17,8 gün | SMALL | 12 ay hedefi değil |
| Reverse stress | BTC −45%, ETH −55%, SOL −65%, SMALL −85% | $47.500 / %47,5 | SMALL | %35 drawdown ihlali |

## 10. Alternatifler ve Rebalans

| Alternatif | Risk | Likidite | Konsantrasyon | Maliyet/vergi | Ne zaman yanlış olur? |
|---|---|---|---|---|---|
| Mevcut | Yüksek beta | İyi (small-cap hariç) | Top-2 %65 | Düşük | BTC ralli yaparsa |
| Risk-azaltılmış | Daha düşük beta | Daha iyi | Top-2 %55 | Orta | Boğa kaçırılırsa |
| Tez içinde çeşitlendirilmiş | Benzer beta | Orta | Top-2 %50 | Orta | Korelasyon artarsa |

**Rebalans bandı:** ±5 puan; small-cap için ±3 puan.  
**Vergi/maliyet notu:** Cost basis yok; vergi etkisi hesaplanamadı.

## 11. Karar Kaydı

- **Karar:** Small-cap pozisyonunu gözden geçir; tek-pozisyon limitini %30'a çek; USDC'yi “cash” olarak değil, ihraççı riski taşıyan likidite tamponu olarak sınıflandır.
- **Gerekçe:** Top-2 %65, small-cap likiditesi zayıf, BTC'ye göre getiri geride.
- **Boyut/uygulama:** Kısıtlar netleşmeden işlem boyutu önerilmez.
- **Falsifier:** Small-cap likiditesi 5 günün altına inerse veya BTC beta 1,4'ü aşarsa.
- **İzleme:** 2027-01-30; aylık likidite ve beta kontrolü.

## 12. Kaynaklar ve Sınırlamalar

- Fiyat: iki bağımsız borsa/aggregator, 2026-10-30 14:00 UTC.
- Bakiye: cüzdan + ikinci kaynak; fark %0,4.
- Small-cap: tek DEX, 08:00 UTC; bağımsız doğrulama yok.
- Cost basis yok; P&L değil, değer değişimi.
- Bu rapor yatırım, vergi veya hukuk tavsiyesi değildir.

## 13. Görsel Paket

- [Allocation](charts/V1-allocation.png) — BTC %42; top-2 %65.
- [Concentration](charts/V2-concentration.png) — top-2 ve cluster limiti aşılıyor.
- [Risk-return](charts/V6-risk-return.png) — risk bütçesinin çoğu BTC/ETH'de.
- [Scenarios](charts/V9-scenarios.png) — reverse stress %35 loss floor'u aşıyor.

> Grafikler sentetiktir; her biri tek bir bulguyu gösterir.
