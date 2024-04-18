SELECT price as max_price FROM product WHERE price = (SELECT MAX(price) FROM product);
