CREATE USER tourism_developer WITH LOGIN CREATEROLE PASSWORD 'developer';
CREATE USER tourism_director WITH LOGIN CREATEROLE PASSWORD 'director';
CREATE USER tourism_staff WITH LOGIN  PASSWORD 'staff';
CREATE USER tourism_client WITH LOGIN  PASSWORD 'client';
CREATE USER tourism_guest WITH LOGIN  PASSWORD 'guest';


REVOKE ALL on DATABASE farm FROM tourism_developer;m, 
REVOKE ALL ON SCHEMA public FROM tourism_developer;

REVOKE CREATE ON SCHEMA public FROM public;
REVOKE ALL ON DATABASE farm FROM public;

grant all PRIVILEGES on schema public to tourism_developer;
grant all PRIVILEGES on schema public to tourism_director;


GRANT CREATE ON SCHEMA public to tourism_developer;

GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES, TRIGGER ON ALL TABLES IN SCHEMA public
TO tourism_developer;
GRANT SELECT, INSERT, UPDATE, DELETE, REFERENCES, TRIGGER ON ALL TABLES IN SCHEMA public
TO tourism_director;

GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO tourism_director;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO tourism_developer;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO tourism_staff;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO tourism_client;

GRANT CONNECT ON DATABASE farm to tourism_director;
GRANT CONNECT ON DATABASE farm to tourism_developer;
GRANT CONNECT ON DATABASE farm to tourism_staff;
GRANT CONNECT ON DATABASE farm to tourism_client;
GRANT CONNECT ON DATABASE farm to tourism_guest;

grant SELECT(login, passw, role_) ON TABLE staff
to tourism_guest;

grant select on client_info to tourism_staff;

grant SELECT(client_id, login, passw) ON TABLE client
to tourism_guest;


GRANT SELECT, REFERENCES ON TABLE
	public.subdivision, 
	public.client,
	public.order_,
	public.supply,
	public.product
	TO tourism_client;

GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE 
	public.client,
	public.order_,
	public.supply,
	public.product,
	public.order_resource
	TO tourism_staff;

GRANT SELECT ON TABLE
	public.subdivision, 
	public.order_resource,
	public.staff
	TO tourism_staff; 
grant insert on table 
	public.order_,
	public.supply
	to tourism_client;
--To use
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO tourism_staff;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA public TO tourism_client;
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE 
	public.client,
	public.order_,
	public.supply,
	public.proffesion,
	public.product,
	public.order_resource
	TO tourism_staff;

revoke SELECT, INSERT, UPDATE, DELETE ON TABLE staff
FROM tourism_guest;

grant select on client_info to tourism_staff;

revoke SELECT ON TABLE client
from tourism_guest;

grant SELECT(login, passw, role_) ON TABLE staff
to tourism_guest;

grant select on client_info to tourism_staff;

grant SELECT(client_id, login, passw) ON TABLE client
to tourism_guest;

grant insert on table 
	public.order_,
	public.supply
	to tourism_client;
