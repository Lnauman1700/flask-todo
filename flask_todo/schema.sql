DROP TABLE IF EXISTS todo_list;

CREATE TABLE todo_list (
  id bigserial,
  task text,
  tstamp timestamp,
  is_completed bool
);
