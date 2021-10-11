def add_to_queue(func, args):
    # The SQL statement that will add the work to the queue.
    update = '''
        INSERT INTO work_queue (function, arguments)
        VALUES (func, args)
        RETURNING id
    '''

    # Use SQLAlchemy to run the SQL statement.
    with engine.begin() as conn:
        queue_id = conn.execute(update)

    # Return the ID of the new work added to the queue.
    return queue_id