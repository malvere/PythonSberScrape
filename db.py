import psycopg2


class ProductDatabase:
    def __init__(self, db_params):
        self.db_params = db_params
        self.conn = None
        self.cur = None

    def connect(self):
        try:
            self.conn = psycopg2.connect(**self.db_params)
            self.cur = self.conn.cursor()
            print("Connected to the database")
        except psycopg2.Error as e:
            print(f"Error connecting to the database: {e}")

    def create_table(self):
        if self.cur is not None:
            create_table_query = """
            CREATE TABLE IF NOT EXISTS product_data (
                id SERIAL PRIMARY KEY,
                title TEXT,
                price INT,
                bonuses INT,
                bonus_percent INT,
                discount INT,
                product_id BIGINT,
                link TEXT
            )
            """
            try:
                self.cur.execute(create_table_query)
                print("Table created or already exists")
            except psycopg2.Error as e:
                print(f"Error creating table: {e}")
        else:
            print("Database connection is not established. Call connect() first.")

    def add_product(self, data: dict):
        if self.cur is not None:
            insert_query = """
            INSERT INTO product_data (title, price, bonuses, bonus_percent, discount, product_id, link)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            try:
                self.cur.execute(insert_query, (
                    data["title"],
                    data["price"],
                    data["bonuses"],
                    data["bonus_percent"],
                    data["discount"],
                    data["product_id"],
                    data["link"],
                ))
                print("Data added successfully")
                # self.conn.commit()
            except psycopg2.Error as e:
                print(f"Error inserting data: {e}")
        else:
            print("Database connection is not established. Call connect() first.")

    def commit(self):
        if self.conn is not None:
            self.conn.commit()
            print("Changes committed to the database")
        else:
            print("Database connection is not established. Call connect() first.")

    def close(self):
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()
            print("Database connection closed")

