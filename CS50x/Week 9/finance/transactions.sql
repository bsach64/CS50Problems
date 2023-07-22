CREATE TABLE transactions(
    user_id INTEGER,
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    symbol TEXT NOT NULL,
    stock_name TEXT NOT NULL,
    price FLOAT NOT NULL,
    share_count INTEGER NOT NULL,
    transaction_type TEXT NOT NULL,
    transaction_date TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id)
)