# Regex əsaslı Sistem Log Analizi

## Ümumi məlumat
Bu layihə, regex istifadə edərək `access_log.txt` faylından URL-ləri və status kodlarını çıxarır və qara siyahıdakı domenlərlə müqayisə edir. Eyni zamanda, 404 səhvlərini analiz edir və nəticələri müxtəlif formatlarda saxlayır.

## Lazım olan proqramlar
- Python 3.x
- `beautifulsoup4` kitabxanası
- `requests` kitabxanası

## Quraşdırma təlimatları
1. **GitHub-dan layihəni klonlayın:**
   ```bash
   git clone https://github.com/revan-aliyev/log-analysis.git
   ```

2. **Virtual mühitin yaradılması:**
   Layihənin qovluğunda virtual mühit yaratmaq üçün:
   ```bash
   python -m venv venv
   ```

3. **Virtual mühitin aktivləşdirilməsi:**
   - Windows-da:
     ```bash
       venv\Scripts\activate
     ```
   - macOS/Linux-da:
     ```bash
     source venv/bin/activate
     ```

4. **Tələb olunan kitabxanaların quraşdırılması:**
   Layihənin tələb etdiyi kitabxanaları quraşdırmaq üçün:
   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

5. **Proqramı işə salın:**
   Layihəni işə salmaq üçün aşağıdakı əmri daxil edin:
   ```bash
   python main.py
   ```

## Nəticələr
Proqramın işləyişi nəticəsində aşağıdakı fayllar yaradılacaq:
- `url_status_report.txt` – URL-ləri və onların status kodlarını sadalayır.
- `malware_candidates.csv` – 404 səhvli URL-ləri və onların saylarını ehtiva edir.
- `alert.json` – Qara siyahıya salınmış uyğun URL-ləri saxlayır.
- `summary_report.json` – Təhlilin nəticələrini xülasə edir.

**Qeyd:** Layihəni başladıqdan sonra, nəticə faylları yalnız işləmə zamanı yaradılacaq və onlara `.gitignore` səbəbi ilə GitHub-a yüklənməyəcək.

## Əlavə məlumat
Bu layihə təhlil və təhlükəsizlik məqsədləri üçün hazırlanmışdır. Qara siyahıya alınmış domenlərin tapılması və 404 səhvlərinin analizi əsas məqsəddir.

## Əlaqə:
Əgər hər hansı bir sualınız varsa, mənimlə əlaqə saxlaya bilərsiniz: aliyevrevan023@gmail.com
