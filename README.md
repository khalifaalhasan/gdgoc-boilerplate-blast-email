# 📧 GDGoC Recruitment Mailer

Script otomatisasi berbasis Python untuk mengirim email pengumuman rekrutmen massal (Lolos/Tidak Lolos) bagi pendaftar GDG on Campus Universitas Sriwijaya.

Dibangun menggunakan **Python** dan **Gmail API**.

## 🚀 Fitur Utama

- **Pemilihan Template Cerdas:** Otomatis mengirim email yang berbeda berdasarkan status peserta (`selected` / `not selected`).
- **Gambar Inline (CID):** Desain email HTML profesional dengan gambar header dan logo footer yang menyatu (tidak pecah).
- **Dukungan Lampiran:** Otomatis melampirkan file PDF (Surat Komitmen) khusus bagi peserta yang lolos.
- **Anti-Spam (Rate Limiting):** Menggunakan jeda waktu acak (random delay) agar aman dari blokir spam Gmail.
- **Manajemen Token:** Login sekali via OAuth2, selanjutnya token disimpan otomatis.

## 📂 Struktur Folder

Pastikan struktur folder tim kalian seperti ini:

- `main.py` -> Script utama yang dijalankan (Eksekusi file ini).
- `config.py` -> Tempat atur link WA, nama file, dan subject email.
- `templates.py` -> Mengatur desain HTML & logika tampilan.
- `credentials.json` -> Kunci akses dari Google Cloud (Wajib ada).
- `assets/` -> (Opsional) Jika kalian mau merapikan gambar & PDF ke folder khusus.

## 🛠️ Prasyarat (Sebelum Jalanin)

1.  **Python 3.x** sudah terinstall.
2.  Punya file **`credentials.json`** dari Google Cloud Console (Tipe: Desktop App).
3.  File gambar (`header.png`, `logo.png`) dan PDF (`Commitment_Letter.pdf`) sudah ada di folder project.

## 📦 Instalasi

1.  **Clone repository ini:**

    ```bash
    git clone [https://github.com/USERNAME-LU/gdgoc-recruitment-mailer.git](https://github.com/USERNAME-LU/gdgoc-recruitment-mailer.git)
    cd gdgoc-recruitment-mailer
    ```

2.  **Install library yang dibutuhkan:**

    ```bash
    pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
    ```

3.  **Setup Credentials:**
    - Minta file `credentials.json` ke Admin/Lead.
    - Taruh file tersebut di folder utama project.
    - **Penting:** Pastikan email pengirim sudah didaftarkan di menu "Test Users" pada Google Cloud Console.

## ⚙️ Konfigurasi (`config.py`)

Edit file `config.py` untuk update link atau nama file:

```python
# Update Link Grup WhatsApp
LINK_COMMUNITY_GROUP = "[https://chat.whatsapp.com/LINK_BARU_DISINI](https://chat.whatsapp.com/LINK_BARU_DISINI)"
LINK_WA_CHANNEL = "[https://whatsapp.com/channel/LINK_BARU_DISINI](https://whatsapp.com/channel/LINK_BARU_DISINI)"

# Update Nama File (Jika ada perubahan aset)
IMG_HEADER = "header.png"
IMG_LOGO = "logo.png"
FILE_KOMITMEN = "Commitment_Letter.pdf"
```
