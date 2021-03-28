-- Created by Vertabelo (http://vertabelo.com)
-- Last modification date: 2018-12-07 06:50:20.505





DROP TABLE IF EXISTS Banks CASCADE;
DROP TABLE IF EXISTS Bought CASCADE;
DROP TABLE IF EXISTS Business_Users CASCADE;
DROP TABLE IF EXISTS Comments CASCADE;
DROP TABLE IF EXISTS Connect_With CASCADE;
DROP TABLE IF EXISTS Employees CASCADE;
DROP TABLE IF EXISTS Feedbacks CASCADE;
DROP TABLE IF EXISTS Goods_Services CASCADE;
DROP TABLE IF EXISTS LikeS CASCADE;
DROP TABLE IF EXISTS P2B_Transactions CASCADE;
DROP TABLE IF EXISTS P2P_Transactions CASCADE;
DROP TABLE IF EXISTS Personal_Users CASCADE;
DROP TABLE IF EXISTS Review CASCADE;
DROP TABLE IF EXISTS Transactions CASCADE;
DROP TABLE IF EXISTS Users CASCADE;

-- tables
-- Table: Banks
CREATE TABLE Banks (
    bank_id serial  NOT NULL,
    name text  NOT NULL,
    CONSTRAINT Banks_pk PRIMARY KEY (bank_id)
);

-- Table: Bought
CREATE TABLE Bought (
    quantity int  NOT NULL,
    transaction_id serial  NOT NULL,
    item_id serial  NOT NULL,
    CONSTRAINT Bought_pk PRIMARY KEY (transaction_id,item_id)
);

-- Table: Business_Users
CREATE TABLE Business_Users (
    name text  NOT NULL,
    user_id text  NOT NULL,
    CONSTRAINT Business_Users_pk PRIMARY KEY (user_id)
);

-- Table: Comments
CREATE TABLE Comments (
    comment_id serial  NOT NULL,
    comment text  NOT NULL,
    timestamp timestamp  NOT NULL,
    user_id text  NOT NULL,
    transaction_id serial  NOT NULL,
    CONSTRAINT Comments_pk PRIMARY KEY (comment_id)
);

-- Table: Connect_With
CREATE TABLE Connect_With (
    user_id text  NOT NULL,
    bank_id serial  NOT NULL,
    CONSTRAINT Connect_With_pk PRIMARY KEY (user_id,bank_id)
);

-- Table: Employees
CREATE TABLE Employees (
    employee_id serial  NOT NULL,
    first_name text  NOT NULL,
    last_name text  NOT NULL,
    department text  NOT NULL,
    CONSTRAINT Employees_pk PRIMARY KEY (employee_id)
);

-- Table: Feedbacks
CREATE TABLE Feedbacks (
    feedback_id serial  NOT NULL,
    comment text  NOT NULL,
    timestamp timestamp  NOT NULL,
    user_id text  NOT NULL,
    CONSTRAINT Feedbacks_pk PRIMARY KEY (feedback_id)
);

-- Table: Goods_Services
CREATE TABLE Goods_Services (
    item_id serial  NOT NULL,
    price float  NOT NULL,
    name text  NOT NULL,
    CONSTRAINT Goods_Services_pk PRIMARY KEY (item_id)
);

-- Table: Likes
CREATE TABLE Likes (
    timestamp timestamp  NOT NULL,
    user_id text  NOT NULL,
    transaction_id serial  NOT NULL,
    CONSTRAINT Likes_pk PRIMARY KEY (user_id,transaction_id)
);

-- Table: P2B_Transactions
CREATE TABLE P2B_Transactions (
    transaction_id serial  NOT NULL,
    user_id_personal text  NOT NULL,
    user_id_business text  NOT NULL,
    CONSTRAINT P2B_Transactions_pk PRIMARY KEY (transaction_id)
);

-- Table: P2P_Transactions
CREATE TABLE P2P_Transactions (
    transaction_id serial  NOT NULL,
    user_id_sender text  NOT NULL,
    user_id_receiver text  NOT NULL,
    CONSTRAINT P2P_Transactions_pk PRIMARY KEY (transaction_id)
);

-- Table: Personal_Users
CREATE TABLE Personal_Users (
    first_name text  NOT NULL,
    last_name text  NOT NULL,
    gender text  NOT NULL,
    age int  NOT NULL,
    user_id text  NOT NULL,
    CONSTRAINT Personal_Users_pk PRIMARY KEY (user_id)
);

-- Table: Review
CREATE TABLE Review (
    feedback_id serial  NOT NULL,
    employee_id serial  NOT NULL,
    CONSTRAINT Review_pk PRIMARY KEY (feedback_id,employee_id)
);

-- Table: Transactions
CREATE TABLE Transactions (
    transaction_id serial  NOT NULL,
    amount float  NOT NULL,
    description text NOT NULL,
    privacy text  NOT NULL,
    timestamp timestamp  NOT NULL,
    CONSTRAINT Transactions_pk PRIMARY KEY (transaction_id)
);

-- Table: Users
CREATE TABLE Users (
    user_id text  NOT NULL,
    email text  NOT NULL,
    balance float  NOT NULL,
    CONSTRAINT Users_pk PRIMARY KEY (user_id)
);

-- foreign keys
-- Reference: Bought_Goods_Services (table: Bought)
ALTER TABLE Bought ADD CONSTRAINT Bought_Goods_Services
    FOREIGN KEY (item_id)
    REFERENCES Goods_Services (item_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Bought_P2B_Transactions (table: Bought)
ALTER TABLE Bought ADD CONSTRAINT Bought_P2B_Transactions
    FOREIGN KEY (transaction_id)
    REFERENCES P2B_Transactions (transaction_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Comments_P2B_Transactions (table: Comments)
ALTER TABLE Comments ADD CONSTRAINT Comments_P2B_Transactions
    FOREIGN KEY (transaction_id)
    REFERENCES P2B_Transactions (transaction_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Comments_Personal_Users (table: Comments)
ALTER TABLE Comments ADD CONSTRAINT Comments_Personal_Users
    FOREIGN KEY (user_id)
    REFERENCES Personal_Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Connect_With_Banks (table: Connect_With)
ALTER TABLE Connect_With ADD CONSTRAINT Connect_With_Banks
    FOREIGN KEY (bank_id)
    REFERENCES Banks (bank_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Connect_With_Users (table: Connect_With)
ALTER TABLE Connect_With ADD CONSTRAINT Connect_With_Users
    FOREIGN KEY (user_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Likes_P2B_Transactions (table: Likes)
ALTER TABLE Likes ADD CONSTRAINT Likes_P2B_Transactions
    FOREIGN KEY (transaction_id)
    REFERENCES P2B_Transactions (transaction_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Likes_Personal_Users (table: Likes)
ALTER TABLE Likes ADD CONSTRAINT Likes_Personal_Users
    FOREIGN KEY (user_id)
    REFERENCES Personal_Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: P2P_Transactions_Business_Users (table: P2B_Transactions)
ALTER TABLE P2B_Transactions ADD CONSTRAINT P2P_Transactions_Business_Users
    FOREIGN KEY (user_id_business)
    REFERENCES Business_Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: P2P_Transactions_Personal_Users (table: P2B_Transactions)
ALTER TABLE P2B_Transactions ADD CONSTRAINT P2P_Transactions_Personal_Users
    FOREIGN KEY (user_id_personal)
    REFERENCES Personal_Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: P2P_Transactions_Personal_Users_1 (table: P2P_Transactions)
ALTER TABLE P2P_Transactions ADD CONSTRAINT P2P_Transactions_Personal_Users_1
    FOREIGN KEY (user_id_sender)
    REFERENCES Personal_Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: P2P_Transactions_Personal_Users_2 (table: P2P_Transactions)
ALTER TABLE P2P_Transactions ADD CONSTRAINT P2P_Transactions_Personal_Users_2
    FOREIGN KEY (user_id_receiver)
    REFERENCES Personal_Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Review_Employees (table: Review)
ALTER TABLE Review ADD CONSTRAINT Review_Employees
    FOREIGN KEY (employee_id)
    REFERENCES Employees (employee_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Review_Feedbacks (table: Review)
ALTER TABLE Review ADD CONSTRAINT Review_Feedbacks
    FOREIGN KEY (feedback_id)
    REFERENCES Feedbacks (feedback_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Transactions_P2B_Transactions (table: P2B_Transactions)
ALTER TABLE P2B_Transactions ADD CONSTRAINT Transactions_P2B_Transactions
    FOREIGN KEY (transaction_id)
    REFERENCES Transactions (transaction_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Transactions_P2P_Transactions (table: P2P_Transactions)
ALTER TABLE P2P_Transactions ADD CONSTRAINT Transactions_P2P_Transactions
    FOREIGN KEY (transaction_id)
    REFERENCES Transactions (transaction_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Users_Business_Users (table: Business_Users)
ALTER TABLE Business_Users ADD CONSTRAINT Users_Business_Users
    FOREIGN KEY (user_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Users_Feedbacks (table: Feedback)
ALTER TABLE Feedbacks ADD CONSTRAINT Users_Feedbacks
    FOREIGN KEY (user_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- Reference: Users_Personal_Users (table: Personal_Users)
ALTER TABLE Personal_Users ADD CONSTRAINT Users_Personal_Users
    FOREIGN KEY (user_id)
    REFERENCES Users (user_id)  
    NOT DEFERRABLE 
    INITIALLY IMMEDIATE
;

-- End of file.

