SELECT seller_id,
        sum(price) AS totalRevenue,
        count(DISTINCT t1.order_id) AS qtdSalles
FROM tb_order_items AS t1

LEFT JOIN tb_orders AS t2
ON t1.order_id = t2.order_id

GROUP BY seller_id

