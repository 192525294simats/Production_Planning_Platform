CREATE TABLE IF NOT EXISTS production_orders (
    id SERIAL PRIMARY KEY,
    product_name VARCHAR(100) NOT NULL,
    quantity INTEGER NOT NULL,
    production_line VARCHAR(50) NOT NULL,
    status VARCHAR(30) NOT NULL,
    due_date DATE
);

CREATE TABLE IF NOT EXISTS inventory (
    id SERIAL PRIMARY KEY,
    item_name VARCHAR(100) NOT NULL,
    stock_quantity INTEGER NOT NULL,
    reorder_level INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS resources (
    id SERIAL PRIMARY KEY,
    resource_name VARCHAR(100) NOT NULL,
    utilization INTEGER NOT NULL,
    availability VARCHAR(30) NOT NULL
);

INSERT INTO production_orders
(product_name, quantity, production_line, status, due_date)
VALUES
('Smart Sensor', 500, 'Line A', 'In Progress', '2026-08-25'),
('Motor Controller', 300, 'Line B', 'Planned', '2026-08-28'),
('Control Panel', 150, 'Line C', 'Completed', '2026-08-20');

INSERT INTO inventory
(item_name, stock_quantity, reorder_level)
VALUES
('Sensor Module', 250, 100),
('PCB Board', 80, 100),
('Motor Unit', 180, 120),
('Cable Set', 50, 75);

INSERT INTO resources
(resource_name, utilization, availability)
VALUES
('Assembly Line A', 86, 'Available'),
('Assembly Line B', 72, 'Available'),
('Assembly Line C', 94, 'Maintenance'),
('Packaging Unit', 61, 'Available');
-- ============================================
-- WORKFORCE MANAGEMENT
-- ============================================

CREATE TABLE IF NOT EXISTS workforce (
    id SERIAL PRIMARY KEY,
    employee_name VARCHAR(100) NOT NULL,
    department VARCHAR(100) NOT NULL,
    skill VARCHAR(100),
    availability VARCHAR(30) NOT NULL,
    utilization INTEGER DEFAULT 0
);

-- ============================================
-- WORK ORDERS
-- ============================================

CREATE TABLE IF NOT EXISTS work_orders (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES production_orders(id),
    machine_id INTEGER REFERENCES resources(id),
    worker_id INTEGER REFERENCES workforce(id),
    status VARCHAR(30) NOT NULL DEFAULT 'Pending',
    progress INTEGER DEFAULT 0,
    start_date DATE,
    completion_date DATE
);

-- ============================================
-- BOTTLENECKS
-- ============================================

CREATE TABLE IF NOT EXISTS bottlenecks (
    id SERIAL PRIMARY KEY,
    bottleneck_type VARCHAR(50) NOT NULL,
    description VARCHAR(255) NOT NULL,
    severity VARCHAR(20) NOT NULL,
    status VARCHAR(30) DEFAULT 'ACTIVE',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- NOTIFICATIONS
-- ============================================

CREATE TABLE IF NOT EXISTS notifications (
    id SERIAL PRIMARY KEY,
    notification_type VARCHAR(50) NOT NULL,
    message VARCHAR(255) NOT NULL,
    severity VARCHAR(20) NOT NULL,
    status VARCHAR(30) DEFAULT 'UNREAD',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ============================================
-- WORKFORCE SAMPLE DATA
-- ============================================

INSERT INTO workforce
(employee_name, department, skill, availability, utilization)
VALUES
('Arun Kumar', 'Assembly', 'Machine Operation', 'Available', 75),
('Priya S', 'Assembly', 'Quality Control', 'Available', 82),
('Rahul M', 'Packaging', 'Packaging Operations', 'Busy', 95),
('Kaviya R', 'Maintenance', 'Equipment Maintenance', 'Available', 60),
('Vijay K', 'Assembly', 'Machine Operation', 'Available', 68);

-- ============================================
-- WORK ORDER SAMPLE DATA
-- ============================================

INSERT INTO work_orders
(order_id, machine_id, worker_id, status, progress, start_date)
VALUES
(1, 1, 1, 'In Progress', 75, '2026-08-21'),
(2, 2, 2, 'Scheduled', 30, '2026-08-22'),
(3, 3, 3, 'Completed', 100, '2026-08-19');

-- ============================================
-- BOTTLENECK SAMPLE DATA
-- ============================================

INSERT INTO bottlenecks
(bottleneck_type, description, severity)
VALUES
('Machine', 'Assembly Line C utilization is above 90%', 'HIGH'),
('Material', 'PCB Board stock is below reorder level', 'MEDIUM'),
('Workforce', 'Packaging department has high workforce utilization', 'MEDIUM');

-- ============================================
-- NOTIFICATION SAMPLE DATA
-- ============================================

INSERT INTO notifications
(notification_type, message, severity)
VALUES
('Machine Alert', 'Assembly Line C requires attention', 'HIGH'),
('Inventory Alert', 'PCB Board stock is below reorder level', 'MEDIUM'),
('Workforce Alert', 'Packaging workforce utilization is high', 'MEDIUM');