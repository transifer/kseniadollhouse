import urllib.request
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

images = {
    "profile.jpg": "https://instagram.fifo4-1.fna.fbcdn.net/v/t51.82787-19/671259811_18316474906262326_5180003256708232426_n.jpg?stp=dst-jpg_s240x240_tt6&efg=eyJ2ZW5jb2RlX3RhZyI6InByb2ZpbGVfcGljLmRqYW5nby4xMDgwLmMyIn0&_nc_ht=instagram.fifo4-1.fna.fbcdn.net&_nc_cat=110&_nc_oc=Q6cZ2gHXPKCvBEeNT0Zq-TdikVZW4CH3zP5zNPX6bpYZT8-Nee9h8AoaZhr22EtdEkYDf4E&_nc_ohc=xZFBRz3qxboQ7kNvwEATGAD&_nc_gid=D_pHanzNo2IdpZJV6n9veQ&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af2REX2gCkx4aDQmzI46gCKUtkXDsZaNsU98nhz6txmM_g&oe=69F11223&_nc_sid=10d13b",
    "post1_dollhouse_dream.jpg": "https://instagram.fifo4-1.fna.fbcdn.net/v/t51.82787-15/671795605_18316484704262326_6436021363484983450_n.jpg?stp=dst-jpg_e35_s1080x1080_sh0.08_tt6&_nc_ht=instagram.fifo4-1.fna.fbcdn.net&_nc_cat=110&_nc_oc=Q6cZ2gHXPKCvBEeNT0Zq-TdikVZW4CH3zP5zNPX6bpYZT8-Nee9h8AoaZhr22EtdEkYDf4E&_nc_ohc=xiggX0CTfvEQ7kNvwEtNGU_&_nc_gid=D_pHanzNo2IdpZJV6n9veQ&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af3uEZ8pF9x8zuYddsStsVzLevSU56vaTVJHD0iClb14bw&oe=69F0FCED&_nc_sid=10d13b",
    "post2_kitchen.jpg": "https://instagram.fifo4-1.fna.fbcdn.net/v/t51.82787-15/671748699_18316484659262326_3998698469012330908_n.jpg?stp=dst-jpg_e35_p1080x1080_sh0.08_tt6&_nc_ht=instagram.fifo4-1.fna.fbcdn.net&_nc_cat=110&_nc_oc=Q6cZ2gHXPKCvBEeNT0Zq-TdikVZW4CH3zP5zNPX6bpYZT8-Nee9h8AoaZhr22EtdEkYDf4E&_nc_ohc=u5sImTMv4ooQ7kNvwE1hSs1&_nc_gid=D_pHanzNo2IdpZJV6n9veQ&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af2NvWjrgolVnFbR77SlOBE_d1NX6EJTz1VycRxYE6KnWA&oe=69F120E6&_nc_sid=10d13b",
    "post3_dollhouse2.jpg": "https://instagram.fifo4-1.fna.fbcdn.net/v/t51.82787-15/672467221_18316484632262326_3923103377761262351_n.jpg?stp=dst-jpg_e35_p1080x1080_sh0.08_tt6&_nc_ht=instagram.fifo4-1.fna.fbcdn.net&_nc_cat=110&_nc_oc=Q6cZ2gHXPKCvBEeNT0Zq-TdikVZW4CH3zP5zNPX6bpYZT8-Nee9h8AoaZhr22EtdEkYDf4E&_nc_ohc=qE3yxAfcl8gQ7kNvwHZxl1M&_nc_gid=D_pHanzNo2IdpZJV6n9veQ&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af2_ZMnQid9JP8dVFIorvyPIBLqxr0yPpPgW5HztSYMnPw&oe=69F100CF&_nc_sid=10d13b",
    "post4_miniatures.jpg": "https://instagram.fifo4-1.fna.fbcdn.net/v/t51.82787-15/673822646_18316484542262326_3183793839260889777_n.jpg?stp=dst-jpg_e35_s1080x1080_sh0.08_tt6&_nc_ht=instagram.fifo4-1.fna.fbcdn.net&_nc_cat=110&_nc_oc=Q6cZ2gHXPKCvBEeNT0Zq-TdikVZW4CH3zP5zNPX6bpYZT8-Nee9h8AoaZhr22EtdEkYDf4E&_nc_ohc=gV6jd858TRsQ7kNvwEkLt4y&_nc_gid=D_pHanzNo2IdpZJV6n9veQ&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af2R9MjDqd3sKHlGNDtal5ZpdritaeaJIKxZhufeVlTczw&oe=69F0FFE9&_nc_sid=10d13b",
    "post5_dollhouse3.jpg": "https://instagram.fifo4-1.fna.fbcdn.net/v/t51.82787-15/672445625_18316484509262326_4588866317698433125_n.jpg?stp=dst-jpg_e35_s1080x1080_sh0.08_tt6&_nc_ht=instagram.fifo4-1.fna.fbcdn.net&_nc_cat=110&_nc_oc=Q6cZ2gHXPKCvBEeNT0Zq-TdikVZW4CH3zP5zNPX6bpYZT8-Nee9h8AoaZhr22EtdEkYDf4E&_nc_ohc=6mWukgAYhv0Q7kNvwE-93sa&_nc_gid=D_pHanzNo2IdpZJV6n9veQ&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af1IGiL_fxRgOBkKH2zCTVsN9Jo4MpKOLMctZ_O2Um1y2g&oe=69F10658&_nc_sid=10d13b",
    "post6_room.jpg": "https://instagram.fifo4-1.fna.fbcdn.net/v/t51.82787-15/673180730_18316484455262326_2287667429362444140_n.jpg?stp=dst-jpg_e35_p1080x1080_sh0.08_tt6&_nc_ht=instagram.fifo4-1.fna.fbcdn.net&_nc_cat=110&_nc_oc=Q6cZ2gHXPKCvBEeNT0Zq-TdikVZW4CH3zP5zNPX6bpYZT8-Nee9h8AoaZhr22EtdEkYDf4E&_nc_ohc=cdap6-5pdYcQ7kNvwHZpnot&_nc_gid=D_pHanzNo2IdpZJV6n9veQ&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af1_vnhUWHdnl0cVGcMON-tuuJPbDeN0UR2qFzUXkmyeXw&oe=69F0FB07&_nc_sid=10d13b",
    "post7_exterior.jpg": "https://instagram.fifo4-1.fna.fbcdn.net/v/t51.82787-15/673101189_18316483921262326_6221428007432965775_n.jpg?stp=dst-jpg_e35_p1080x1080_sh0.08_tt6&_nc_ht=instagram.fifo4-1.fna.fbcdn.net&_nc_cat=110&_nc_oc=Q6cZ2gFvBg0HiJV5uaj7XUV34x63Vyy9w2_92ixxeKkhxN0pHtOs4cPd-5esA0zFX8DHR1Y&_nc_ohc=aLuVmFNKUmAQ7kNvwHk8euH&_nc_gid=ypA_G8x-SZ5e51td7Xe2bg&edm=APs17CUBAAAA&ccb=7-5&oh=00_Af3YosVqCCKz7ns2A6fUltkc90691146JvyLltHhNQXq_g&oe=69F11C4C&_nc_sid=10d13b",
}

req_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'https://www.instagram.com/',
}

for fname, url in images.items():
    try:
        req = urllib.request.Request(url, headers=req_headers)
        with urllib.request.urlopen(req) as resp:
            data = resp.read()
            with open(f"img/{fname}", "wb") as f:
                f.write(data)
            print(f"OK: {fname} ({len(data)} bytes)")
    except Exception as e:
        print(f"FAIL: {fname} - {e}")
