import requests

# ===== WAJIB GANTI =====
TOKEN = "7850336943:AAHaH_qc68s1x0ib7K9M41sA6MBUmgjUfS0"  
CHAT_ID = "5588684746"
# =======================

def cek_harga_ada():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=cardano&vs_currencies=usd,idr&include_24hr_vol=true&include_24hr_change=true"
    data = requests.get(url).json()['cardano']
    return {
        'harga_usd': data['usd'],
        'harga_idr': data['idr'],
        'volume': data['usd_24h_vol'],
        'change': data['usd_24h_change']
    }

def kirim_telegram(pesan):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    data = {"chat_id": CHAT_ID, "text": pesan, "parse_mode": "HTML"}
    res = requests.post(url, data=data)
    print("Respon Telegram:", res.json())

data = cek_harga_ada()
pesan = f"""<b>🐋 Radar ADA dari VS Code</b>

<b>Harga:</b> ${data['harga_usd']:.4f} 
<b>Rupiah:</b> Rp{data['harga_idr']:,.0f}
<b>24 Jam:</b> {data['change']:+.2f}%
<b>Volume:</b> ${data['volume']:,.0f}

Jalan dari laptop lu bro 🚀"""

kirim_telegram(pesan)
print("Kelarr bro, cek Telegram lu")
