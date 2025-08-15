use sales_data;
CREATE TABLE sales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    product VARCHAR(50) NOT NULL,
    quantity INT NOT NULL,
    price DECIMAL(10,2) NOT NULL
);

INSERT INTO sales (product, quantity, price) VALUES
('Laptop', 3, 800.00),
('Laptop', 2, 850.00),
('Laptop', 5, 780.00),
('Phone', 5, 500.00),
('Phone', 3, 520.00),
('Phone', 7, 480.00),
('Headphones', 10, 50.00),
('Headphones', 8, 55.00),
('Headphones', 15, 45.00),
('Monitor', 2, 200.00),
('Monitor', 3, 210.00),
('Monitor', 1, 190.00),
('Keyboard', 4, 40.00),
('Keyboard', 6, 42.00),
('Keyboard', 5, 38.00),
('Mouse', 12, 25.00),
('Mouse', 8, 28.00),
('Mouse', 15, 22.00);
