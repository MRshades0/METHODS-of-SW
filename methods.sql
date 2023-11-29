BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "INVENTORY" (
	"ISBN"	INT NOT NULL,
	"title"	text NOT NULL,
	"author"	text NOT NULL,
	"genre"	text NOT NULL,
	"pages"	int NOT NULL,
	"release_date"	int NOT NULL,
	"stock"	int NOT NULL,
	PRIMARY KEY("ISBN")
);
CREATE TABLE IF NOT EXISTS "CART" (
	"ISBN"	INT NOT NULL,
	"userID"	INT NOT NULL,
	"quantity"	INT NOT NULL,
	FOREIGN KEY("userID") REFERENCES "USER"("userID"),
	FOREIGN KEY("ISBN") REFERENCES "inventory"("ISBN")
);
CREATE TABLE IF NOT EXISTS "USER" (
	"last"	varchar(14) NOT NULL,
	"first"	varchar(14) DEFAULT NULL,
	"payment"	varchar(16) DEFAULT NULL,
	"email"	varchar(20) DEFAULT NULL,
	"address"	varchar(50) DEFAULT NULL,
	"zip"	varchar(5) DEFAULT NULL,
	"city"	varchar(12) DEFAULT NULL,
	"state"	varchar(12) DEFAULT NULL,
	"password"	varchar(15) DEFAULT NULL,
	"userID"	varchar(6) DEFAULT NULL,
	PRIMARY KEY("userID")
);
INSERT INTO "INVENTORY" ("ISBN","title","author","genre","pages","release_date","stock") VALUES (1,'abook','John','thriller',32,2003,19),
 (2,'Abook 2','John Doe','Mystery',201,2005,21),
 (3,'Abook 3','John Doe','Romance',203,2009,4);
INSERT INTO "CART" ("ISBN","userID","quantity") VALUES (1,22,13);
INSERT INTO "USER" ("last","first","payment","email","address","zip","city","state","password","userID") VALUES ('Dear','Cam','Paypal','abc123@gmail.com','123 Wallby Way','12345','Brandon','MS','12345','860846'),
 ('Dear','Camden','credit','12345@hotmail.com','202 Faraway Pl.','12345','Nunya','MS','12345','255674'),
 ('Dear','Cam','credit','123@gmail.com','12 Place Pl.','21313','Nunya','MS','12345','398352'),
 ('Dear','Cam','credit','12@gmail.com','2 Place St.','12345','Nunya','MS','11111','615652'),
 ('Dear','Cam','credit','1@gmail.com','2 place st','12345','Nun','MS','11111','475495'),
 ('D','Cam','credit','1@gmail.com','1 place st','12345','Nunya','MS','12345','254063');
COMMIT;
