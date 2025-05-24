use scratch_pad

CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(255) NOT NULL
) COMMENT = 'This table stores product categories.';

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(255) NOT NULL,
    description TEXT,
    price DECIMAL(10, 2) NOT NULL,
    category_id INT,
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
) COMMENT = 'This table stores information about the products sold in our store.  It is related to the categories table.';

use scratch_pad
INSERT INTO categories (category_name) VALUES
('Electronics'),
('Clothing'),
('Home & Kitchen'),
('Books'),
('Sports & Outdoors');

INSERT INTO products (product_name, description, price, category_id) VALUES
('4K Smart TV', '55-inch Ultra HD Smart LED TV with HDR', 499.99, 1),
('Cotton T-Shirt', 'Men\'s classic fit cotton t-shirt', 19.99, 2),
('Stainless Steel Cookware Set', '12-piece stainless steel cookware set with non-stick coating', 149.50, 3),
('The Lord of the Rings', 'J.R.R. Tolkien\'s epic fantasy trilogy', 29.99, 4),
('Basketball', 'Official size and weight basketball', 24.75, 5),
('Noise Cancelling Headphones', 'Over-ear wireless headphones with active noise cancellation', 199.00, 1),
('Denim Jeans', 'Women\'s slim fit denim jeans', 39.50, 2),
('Blender', 'High-performance blender for smoothies and shakes', 79.99, 3),
('Pride and Prejudice', 'Jane Austen\'s classic novel', 9.99, 4),
('Yoga Mat', 'Non-slip yoga mat for exercise and fitness', 14.99, 5);
