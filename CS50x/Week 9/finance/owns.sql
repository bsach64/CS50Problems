CREATE TABLE owns(
    user_id INTEGER,
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    symbol TEXT NOT NULL,
    stock_name TEXT NOT NULL,
    share_count TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id)
)