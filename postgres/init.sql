DO $$ BEGIN
  RAISE NOTICE 'Initializing database schema...';
END $$;

CREATE DATABASE whist_nginx;

\connect whist_nginx;

CREATE TABLE IF NOT EXISTS global_counter (
    hit_counter INTEGER NOT NULL
);

INSERT INTO global_counter (hit_counter) VALUES (0);

CREATE TABLE IF NOT EXISTS access_log (
    client_ip inet,
    date_time timestamp,
    replica_ip inet
);


DO $$ BEGIN
  RAISE NOTICE 'Database initialization complete.';
END $$;