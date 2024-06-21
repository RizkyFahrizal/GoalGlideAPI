from typing import Union
from fastapi import FastAPI,Response,Request,HTTPException
from pydantic import BaseModel
import sqlite3
from typing import List, Dict
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
DB_NAME = "db_goalglide.db"

# Tambahkan CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ganti dengan URL aplikasi Flutter jika di-deploy
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class User(BaseModel):
    username: str
    email: str
    no_telpon: str
    alamat: str
    foto: str

class Player(BaseModel):
    nama_lengkap: str
    email: str
    no_telpon: str
    posisi: str
    tanggal_lahir: str
    tinggi_badan: int
    alamat: str
    foto: str

class Club(BaseModel):
    nama_club: str
    deskripsi_club: str
    alamat_club: str
    foto_club: str
    tahun_didirikan: int

class Registration(BaseModel):
    id_player: int
    id_club: int

class News(BaseModel):
    judul: str
    kategori_pertandingan: str
    foto: str
    tanggal: str
    biaya_pendaftaran: Union[float, None] = None
    total_prizepool: Union[float, None] = None

# @app.get("/alter_player_id/")
# def alter_player_id():
#     try:
#         con = sqlite3.connect(DB_NAME)
#         cur = con.cursor()
        
#         # Step 1: Rename the existing table
#         cur.execute("ALTER TABLE player RENAME TO player_old")
        
#         # Step 2: Create a new table with the correct schema
#         cur.execute("""
#             CREATE TABLE player(
#                 id_player INTEGER PRIMARY KEY AUTOINCREMENT,
#                 nama_lengkap TEXT NOT NULL,
#                 email TEXT NOT NULL,
#                 no_telpon TEXT NOT NULL,
#                 posisi TEXT NOT NULL,
#                 tanggal_lahir TEXT NOT NULL,
#                 tinggi_badan INTEGER,
#                 alamat TEXT NOT NULL,
#                 foto TEXT NOT NULL
#             )
#         """)
        
#         # Step 3: Copy the data from the old table to the new table
#         cur.execute("""
#             INSERT INTO player (id_player, nama_lengkap, email, no_telpon, posisi, tanggal_lahir, tinggi_badan, alamat, foto)
#             SELECT CAST(id_player AS INTEGER), nama_lengkap, email, no_telpon, posisi, tanggal_lahir, tinggi_badan, alamat, foto
#             FROM player_old
#         """)
        
#         # Step 4: Drop the old table
#         cur.execute("DROP TABLE player_old")
        
#         con.commit()
#     except Exception as e:
#         return {"status": "terjadi error", "detail": str(e)}
#     finally:
#         con.close()
    
#     return {"status": "ok, tipe data kolom id_player berhasil diubah"}

# @app.get("/init/")
# def init_db():
#     try:
#         con = sqlite3.connect(DB_NAME)
#         cur = con.cursor()

#         # Create user table
#         create_user_table = """CREATE TABLE IF NOT EXISTS user(
#             id_user INTEGER PRIMARY KEY AUTOINCREMENT,
#             username TEXT NOT NULL,
#             email TEXT NOT NULL,
#             no_telpon TEXT NOT NULL,
#             alamat TEXT NOT NULL,
#             foto TEXT NOT NULL
#         )"""
#         cur.execute(create_user_table)

#         # Create player table
#         create_player_table = """CREATE TABLE IF NOT EXISTS player(
#             id_player INTEGER PRIMARY KEY AUTOINCREMENT,
#             nama_lengkap TEXT NOT NULL,
#             email TEXT NOT NULL,
#             no_telpon TEXT NOT NULL,
#             posisi TEXT NOT NULL,
#             tanggal_lahir TEXT NOT NULL,
#             tinggi_badan INTEGER,
#             alamat TEXT NOT NULL,
#             foto TEXT NOT NULL
#         )"""
#         cur.execute(create_player_table)
        
#         # Create club table
#         create_club_table = """CREATE TABLE IF NOT EXISTS club(
#             id_club INTEGER PRIMARY KEY AUTOINCREMENT,
#             nama_club TEXT NOT NULL,
#             deskripsi_club TEXT NOT NULL,
#             alamat_club TEXT NOT NULL,
#             foto_club TEXT NOT NULL,
#             tahun_didirikan INTEGER
#         )"""
#         cur.execute(create_club_table)

#         # Create registration table
#         create_registration_table = """CREATE TABLE IF NOT EXISTS registration(
#             id_registration INTEGER PRIMARY KEY AUTOINCREMENT,
#             id_player INTEGER NOT NULL,
#             id_club INTEGER NOT NULL,
#             FOREIGN KEY (id_player) REFERENCES player(id_player),
#             FOREIGN KEY (id_club) REFERENCES club(id_club)
#         )"""
#         cur.execute(create_registration_table)

#          # Create news table
#         create_news_table = """CREATE TABLE IF NOT EXISTS news(
#             id_news INTEGER PRIMARY KEY AUTOINCREMENT,
#             judul TEXT NOT NULL,
#             konten TEXT NOT NULL,
#             foto TEXT NOT NULL,
#             tanggal DATE NOT NULL
#         )"""
#         cur.execute(create_news_table)

#         con.commit()
#     except Exception as e:
#         return {"status": "terjadi error", "detail": str(e)}
#     finally:
#         con.close()

#     return {"status": "ok, db dan tabel berhasil dicreate"}

# @app.get("/show_tables/")
# def show_tables():
#     try:
#         DB_NAME = "db_goalglide.db"
#         con = sqlite3.connect(DB_NAME)
#         cur = con.cursor()
        
#         # Query to get the list of all tables
#         cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
#         tables = cur.fetchall()

#         # Convert list of tuples to list of strings
#         table_list = [table[0] for table in tables]
#     except Exception as e:
#         return {"status": "terjadi error", "detail": str(e)}
#     finally:
#         con.close()

#     return {"tables": table_list}

# @app.get("/rename_table/")
# def rename_table(old_name: str, new_name: str):
#     try:
#         con = sqlite3.connect(DB_NAME)
#         cur = con.cursor()
#         cur.execute(f"ALTER TABLE {old_name} RENAME TO {new_name}")
#         con.commit()
#     except Exception as e:
#         return {"status": "terjadi error", "detail": str(e)}
#     finally:
#         con.close()

#     return {"status": f"Tabel {old_name} berhasil diubah namanya menjadi {new_name}"}

# @app.get("/table_info/{table_name}")
# def get_table_info(table_name: str):
#     try:
#         con = sqlite3.connect(DB_NAME)
#         cur = con.cursor()
#         cur.execute(f"PRAGMA table_info({table_name})")
#         columns = cur.fetchall()
#     except Exception as e:
#         return {"status": "terjadi error", "detail": str(e)}
#     finally:
#         con.close()

#     if not columns:
#         raise HTTPException(status_code=404, detail=f"Table {table_name} not found")

#     column_info = []
#     for column in columns:
#         column_info.append({
#             "cid": column[0],
#             "name": column[1],
#             "type": column[2],
#             "notnull": column[3],
#             "dflt_value": column[4],
#             "pk": column[5]
#         })

#     return column_info

# @app.delete("/delete_table/{table_name}")
# def delete_table(table_name: str):
#     try:
#         con = sqlite3.connect(DB_NAME)
#         cur = con.cursor()
#         cur.execute(f"DROP TABLE IF EXISTS {table_name}")
#         con.commit()
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Error: {str(e)}")
#     finally:
#         con.close()

#     return {"status": f"Table {table_name} has been deleted successfully"}

# CRUD for User
@app.post("/users/")
def create_user(user: User):
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("INSERT INTO user (username, email, no_telpon, alamat, foto) VALUES (?, ?, ?, ?, ?)",
                    (user.username, user.email, user.no_telpon, user.alamat, user.foto))
        con.commit()
        user_id = cur.lastrowid
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()
    return {"id_user": user_id}

@app.get("/users/")
def read_users():
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("SELECT * FROM user")
        users = cur.fetchall()
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()
    return users

@app.put("/users/{user_id}")
def update_user(user_id: int, user: User):
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("UPDATE user SET username = ?, email = ?, no_telpon = ?, alamat = ?, foto = ? WHERE id_user = ?",
                    (user.username, user.email, user.no_telpon, user.alamat, user.foto, user_id))
        con.commit()
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()
    return {"status": "User updated successfully"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("DELETE FROM user WHERE id_user = ?", (user_id,))
        con.commit()
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="User not found")
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()
    return {"status": "User deleted successfully"}

# CRUD for Player
@app.post("/players/")
def create_player(player: Player):
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("INSERT INTO player (nama_lengkap, email, no_telpon, posisi, tanggal_lahir, tinggi_badan, alamat, foto) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                    (player.nama_lengkap, player.email, player.no_telpon, player.posisi, player.tanggal_lahir, player.tinggi_badan, player.alamat, player.foto))
        con.commit()
        player_id = cur.lastrowid
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()
    return {"id_player": player_id}

@app.get("/players/", response_model=List[Dict[str, str]])
def read_players():
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("SELECT * FROM player")
        players = cur.fetchall()
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()

    player_list = []
    for player in players:
        player_list.append({
            "id_player": int(player[0]),
            "nama_lengkap": player[1],
            "email": player[2],
            "no_telpon": player[3],
            "posisi": player[4],
            "tanggal_lahir": player[5],
            "tinggi_badan": int(player[6]) if player[6] else None,
            "alamat": player[7],
            "foto": player[8]
        })
    
    return player_list

@app.put("/players/{player_id}")
def update_player(player_id: int, player: Player):
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("UPDATE player SET nama_lengkap = ?, email = ?, no_telpon = ?, posisi = ?, tanggal_lahir = ?, tinggi_badan = ?, alamat = ?, foto = ? WHERE id_player = ?",
                    (player.nama_lengkap, player.email, player.no_telpon, player.posisi, player.tanggal_lahir, player.tinggi_badan, player.alamat, player.foto, player_id))
        con.commit()
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Player not found")
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()
    return {"status": "Player updated successfully"}

@app.delete("/players/{player_id}")
def delete_player(player_id: int):
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("DELETE FROM player WHERE id_player = ?", (player_id,))
        con.commit()
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Player not found")
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()
    return {"status": "Player deleted successfully"}


# CRUD for Club
@app.post("/clubs/")
def create_club(club: Club):
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("INSERT INTO club (nama_club, deskripsi_club, alamat_club, foto_club, tahun_didirikan) VALUES (?, ?, ?, ?, ?)",
                    (club.nama_club, club.deskripsi_club, club.alamat_club, club.foto_club, club.tahun_didirikan))
        con.commit()
        club_id = cur.lastrowid
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()
    return {"id_club": club_id}

@app.get("/clubs/")
def read_clubs():
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("SELECT * FROM club")
        clubs = cur.fetchall()
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()
    return clubs

@app.put("/clubs/{club_id}")
def update_club(club_id: int, club: Club):
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("UPDATE club SET nama_club = ?, deskripsi_club = ?, alamat_club = ?, foto_club = ?, tahun_didirikan = ? WHERE id_club = ?",
                    (club.nama_club, club.deskripsi_club, club.alamat_club, club.foto_club, club.tahun_didirikan, club_id))
        con.commit()
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Club not found")
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()
    return {"status": "Club updated successfully"}

@app.delete("/clubs/{club_id}")
def delete_club(club_id: int):
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("DELETE FROM club WHERE id_club = ?", (club_id,))
        con.commit()
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Club not found")
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()
    return {"status": "Club deleted successfully"}

# CRUD for Registration
@app.post("/registrations/")
def create_registration(registration: Registration):
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("INSERT INTO registration (id_player, id_club) VALUES (?, ?)",
                    (registration.id_player, registration.id_club))
        con.commit()
        registration_id = cur.lastrowid
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()
    return {"id_registration": registration_id}

@app.get("/registrations/")
def read_registrations():
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("SELECT * FROM registration")
        registrations = cur.fetchall()
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()
    return registrations

@app.put("/registrations/{registration_id}")
def update_registration(registration_id: int, registration: Registration):
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("UPDATE registration SET id_player = ?, id_club = ? WHERE id_registration = ?",
                    (registration.id_player, registration.id_club, registration_id))
        con.commit()
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Registration not found")
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()
    return {"status": "Registration updated successfully"}

@app.delete("/registrations/{registration_id}")
def delete_registration(registration_id: int):
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("DELETE FROM registration WHERE id_registration = ?", (registration_id,))
        con.commit()
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="Registration not found")
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()
    return {"status": "Registration deleted successfully"}


# CRUD for News
@app.post("/news/")
def create_news(news: News):
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("""
            INSERT INTO news (judul, kategori_pertandingan, foto, tanggal, biaya_pendaftaran, total_prizepool) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (news.judul, news.kategori_pertandingan, news.foto, news.tanggal, news.biaya_pendaftaran, news.total_prizepool))
        con.commit()
        news_id = cur.lastrowid
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()
    return {"id_news": news_id}

@app.get("/news/")
def read_news():
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("SELECT * FROM news")
        news_list = cur.fetchall()
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()
    return news_list

@app.put("/news/{news_id}")
def update_news(news_id: int, news: News):
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("""
            UPDATE news 
            SET judul = ?, kategori_pertandingan = ?, foto = ?, tanggal = ?, biaya_pendaftaran = ?, total_prizepool = ? 
            WHERE id_news = ?
        """, (news.judul, news.kategori_pertandingan, news.foto, news.tanggal, news.biaya_pendaftaran, news.total_prizepool, news_id))
        con.commit()
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="News not found")
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()
    return {"status": "News updated successfully"}

@app.delete("/news/{news_id}")
def delete_news(news_id: int):
    try:
        con = sqlite3.connect(DB_NAME)
        cur = con.cursor()
        cur.execute("DELETE FROM news WHERE id_news = ?", (news_id,))
        con.commit()
        if cur.rowcount == 0:
            raise HTTPException(status_code=404, detail="News not found")
    except Exception as e:
        return {"status": "terjadi error", "detail": str(e)}
    finally:
        con.close()
    return {"status": "News deleted successfully"}