from database import get_connection


def get_production_orders():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, product_name, quantity,
               production_line, status, due_date
        FROM production_orders
        ORDER BY id
    """)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def get_inventory():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, item_name, stock_quantity, reorder_level
        FROM inventory
        ORDER BY id
    """)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def get_resources():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, resource_name, utilization, availability
        FROM resources
        ORDER BY id
    """)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def get_workforce():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, employee_name, department, skill,
               availability, utilization
        FROM workforce
        ORDER BY id
    """)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def get_work_orders():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            wo.id,
            wo.order_id,
            po.product_name,
            wo.machine_id,
            r.resource_name,
            wo.worker_id,
            w.employee_name,
            wo.status,
            wo.progress,
            wo.start_date,
            wo.completion_date
        FROM work_orders wo
        LEFT JOIN production_orders po
            ON wo.order_id = po.id
        LEFT JOIN resources r
            ON wo.machine_id = r.id
        LEFT JOIN workforce w
            ON wo.worker_id = w.id
        ORDER BY wo.id
    """)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def get_bottlenecks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            bottleneck_type,
            description,
            severity,
            status,
            created_at
        FROM bottlenecks
        ORDER BY id DESC
    """)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data


def get_notifications():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            id,
            notification_type,
            message,
            severity,
            status,
            created_at
        FROM notifications
        ORDER BY id DESC
    """)

    data = cursor.fetchall()

    cursor.close()
    conn.close()

    return data